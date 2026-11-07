"""Process instance and user task lifecycles as explicit state machines.

CONN-CAMUNDA-MCP-R009 (organization constitution Article XXXI). Two closed
machines, one transition function each, and one typed refusal. The engine holds
the authoritative state; this module maps an engine record onto a machine state,
decides a move, and the ``guarded`` wrapper refuses an illegal move before any
engine write. No other module branches on a raw engine state string.
"""

from __future__ import annotations

import functools
import inspect
import xml.etree.ElementTree as ET
from collections.abc import Callable, Mapping
from enum import StrEnum
from typing import Any

MACHINE_INSTANCE = "process_instance"
MACHINE_TASK = "user_task"
ILLEGAL_TRANSITION = "ILLEGAL_TRANSITION"


class InstanceState(StrEnum):
    CREATED = "Created"
    ACTIVE = "Active"
    SUSPENDED = "Suspended"
    INCIDENT = "Incident"
    COMPLETED = "Completed"
    CANCELED = "Canceled"
    TERMINATED = "Terminated"


class InstanceEvent(StrEnum):
    START = "start"
    SUSPEND = "suspend"
    ACTIVATE = "activate"
    RAISE_INCIDENT = "raise_incident"
    RESOLVE_INCIDENT = "resolve_incident"
    COMPLETE = "complete"
    CANCEL = "cancel"
    TERMINATE = "terminate"


class TaskState(StrEnum):
    CREATED = "Created"
    CLAIMED = "Claimed"
    COMPLETED = "Completed"
    CANCELED = "Canceled"
    DELETED = "Deleted"


class TaskEvent(StrEnum):
    CLAIM = "claim"
    UNCLAIM = "unclaim"
    COMPLETE = "complete"
    CANCEL = "cancel"
    DELETE = "delete"


class Reason(StrEnum):
    ILLEGAL_EDGE = "IllegalEdge"
    TERMINAL_STATE = "TerminalState"
    ALREADY_CLAIMED = "AlreadyClaimed"
    NOT_CLAIMED = "NotClaimed"
    CLAIMED_BY_OTHER = "ClaimedByOther"
    NO_ACTING_IDENTITY = "NoActingIdentity"
    UNKNOWN_ENGINE_STATE = "UnknownEngineState"


class IllegalTransition(Exception):
    """The typed refusal of an illegal move (code ``ILLEGAL_TRANSITION``)."""

    code = ILLEGAL_TRANSITION

    def __init__(
        self,
        machine: str,
        from_state: str | None,
        event: str,
        reason: Reason,
        entity: str = "",
        id: str = "",
    ):
        self.machine = machine
        self.from_state = from_state
        self.event = event
        self.reason = reason
        self.entity = entity
        self.id = id
        super().__init__(
            f"{ILLEGAL_TRANSITION}: {machine} {entity} {id} in state "
            f"{from_state} refuses {event} ({reason})"
        )

    def as_dict(self) -> dict[str, Any]:
        return {
            "code": self.code,
            "machine": self.machine,
            "from_state": self.from_state,
            "event": str(self.event),
            "reason": str(self.reason),
            "entity": self.entity,
            "id": self.id,
        }


_I, _E = InstanceState, InstanceEvent
INSTANCE_TABLE: dict[tuple[InstanceState, InstanceEvent], InstanceState] = {
    (_I.CREATED, _E.START): _I.ACTIVE,
    (_I.ACTIVE, _E.SUSPEND): _I.SUSPENDED,
    (_I.SUSPENDED, _E.ACTIVATE): _I.ACTIVE,
    (_I.ACTIVE, _E.RAISE_INCIDENT): _I.INCIDENT,
    (_I.INCIDENT, _E.RESOLVE_INCIDENT): _I.ACTIVE,
    (_I.INCIDENT, _E.SUSPEND): _I.SUSPENDED,
    (_I.ACTIVE, _E.COMPLETE): _I.COMPLETED,
    (_I.INCIDENT, _E.COMPLETE): _I.COMPLETED,
    (_I.ACTIVE, _E.CANCEL): _I.CANCELED,
    (_I.SUSPENDED, _E.CANCEL): _I.CANCELED,
    (_I.INCIDENT, _E.CANCEL): _I.CANCELED,
    (_I.ACTIVE, _E.TERMINATE): _I.TERMINATED,
    (_I.SUSPENDED, _E.TERMINATE): _I.TERMINATED,
    (_I.INCIDENT, _E.TERMINATE): _I.TERMINATED,
}
INSTANCE_TERMINAL = frozenset({_I.COMPLETED, _I.CANCELED, _I.TERMINATED})
#: Incident is a sub-state of Active: Active's parent role, same events but one.
INSTANCE_PARENT = {_I.INCIDENT: _I.ACTIVE}

_T, _V = TaskState, TaskEvent
TASK_TABLE: dict[tuple[TaskState, TaskEvent], TaskState] = {
    (_T.CREATED, _V.CLAIM): _T.CLAIMED,
    (_T.CLAIMED, _V.UNCLAIM): _T.CREATED,
    (_T.CLAIMED, _V.COMPLETE): _T.COMPLETED,
    (_T.CREATED, _V.CANCEL): _T.CANCELED,
    (_T.CLAIMED, _V.CANCEL): _T.CANCELED,
    (_T.CREATED, _V.DELETE): _T.DELETED,
    (_T.CLAIMED, _V.DELETE): _T.DELETED,
}
TASK_TERMINAL = frozenset({_T.COMPLETED, _T.CANCELED, _T.DELETED})


def instance_transition(
    state: InstanceState,
    event: InstanceEvent,
    *,
    entity: str = "ProcessInstance",
    id: str = "",
) -> InstanceState:
    """The only transition function of the instance machine."""
    nxt = INSTANCE_TABLE.get((state, event))
    if nxt is not None:
        return nxt
    reason = (
        Reason.TERMINAL_STATE if state in INSTANCE_TERMINAL else Reason.ILLEGAL_EDGE
    )
    raise IllegalTransition(MACHINE_INSTANCE, state, event, reason, entity, id)


def task_transition(
    state: TaskState,
    event: TaskEvent,
    guards: Mapping[str, Any] | None = None,
    *,
    entity: str = "UserTask",
    id: str = "",
) -> TaskState:
    """The only transition function of the task machine.

    ``guards`` carries ``assignee`` (data of the Claimed state) and ``identity``
    (the acting identity, see :func:`acting_identity`).
    """
    guards = guards or {}

    def refuse(reason: Reason) -> IllegalTransition:
        return IllegalTransition(MACHINE_TASK, state, event, reason, entity, id)

    if state in TASK_TERMINAL:
        raise refuse(Reason.TERMINAL_STATE)
    nxt = TASK_TABLE.get((state, event))
    if nxt is None:
        if event is _V.CLAIM:
            raise refuse(Reason.ALREADY_CLAIMED)
        if event in (_V.UNCLAIM, _V.COMPLETE):
            raise refuse(Reason.NOT_CLAIMED)
        raise refuse(Reason.ILLEGAL_EDGE)
    if event is _V.COMPLETE:
        identity = guards.get("identity")
        if not identity:
            raise refuse(Reason.NO_ACTING_IDENTITY)
        if identity != guards.get("assignee"):
            raise refuse(Reason.CLAIMED_BY_OTHER)
    return nxt


# --- engine record -> machine state ---------------------------------------

_G7_INSTANCE = {
    "SUSPENDED": _I.SUSPENDED,
    "COMPLETED": _I.COMPLETED,
    "EXTERNALLY_TERMINATED": _I.TERMINATED,
    "INTERNALLY_TERMINATED": _I.TERMINATED,
}
_G8_INSTANCE = {"COMPLETED": _I.COMPLETED, "CANCELED": _I.CANCELED}
_G8_TASK = {"CREATED": _T.CREATED, "COMPLETED": _T.COMPLETED, "CANCELED": _T.CANCELED}


def _unknown(machine: str, value: Any, entity: str, id: str) -> IllegalTransition:
    return IllegalTransition(
        machine, str(value), "read", Reason.UNKNOWN_ENGINE_STATE, entity, id
    )


def instance_state_of(
    generation: int | str, record: Mapping[str, Any]
) -> InstanceState:
    """Map a generation 7 or 8 instance record onto the one instance machine.

    Generation 7 reads ``state`` and ``openIncidents`` (count); generation 8
    reads ``state`` and ``incident``. A runtime record without ``state`` (the
    generation 7 runtime list) is read from its ``suspended`` flag.
    """
    gen = str(generation)
    rid = str(record.get("id") or record.get("key") or "")
    state = record.get("state")
    if gen == "7":
        if state is None and isinstance(record.get("suspended"), bool):
            state = "SUSPENDED" if record["suspended"] else "ACTIVE"
        incident = bool(record.get("openIncidents"))
        if state == "ACTIVE":
            return _I.INCIDENT if incident else _I.ACTIVE
        if state in _G7_INSTANCE:
            return _G7_INSTANCE[state]
    elif gen == "8":
        incident = bool(record.get("incident"))
        if state == "ACTIVE":
            return _I.INCIDENT if incident else _I.ACTIVE
        if state in _G8_INSTANCE:
            return _G8_INSTANCE[state]
    raise _unknown(MACHINE_INSTANCE, state, "ProcessInstance", rid)


def task_state_of(generation: int | str, record: Mapping[str, Any]) -> TaskState:
    """Map a task record onto the task machine.

    Generation 7: a runtime task is Created or Claimed (by ``assignee``); a
    finished one comes from history (``endTime`` plus ``deleteReason``).
    Generation 8: ``taskState`` plus ``assignee``.
    """
    gen = str(generation)
    rid = str(record.get("id") or "")
    if gen == "7":
        if record.get("endTime"):
            reason = record.get("deleteReason")
            if reason == "completed":
                return _T.COMPLETED
            if reason == "deleted":
                return _T.DELETED
            return _T.CANCELED
        return _T.CLAIMED if record.get("assignee") else _T.CREATED
    state = record.get("taskState")
    if gen == "8" and state in _G8_TASK:
        if _G8_TASK[state] is _T.CREATED and record.get("assignee"):
            return _T.CLAIMED
        return _G8_TASK[state]
    raise _unknown(MACHINE_TASK, state, "UserTask", rid)


# --- acting identity --------------------------------------------------------


def is_automated(definition_xml: str | None, task_definition_key: str | None) -> bool:
    """True when the user task's definition carries property ``automated=true``."""
    if not definition_xml or not task_definition_key:
        return False
    try:
        root = ET.fromstring(definition_xml)
    except ET.ParseError:
        return False
    for node in root.iter():
        if (
            node.tag.rsplit("}", 1)[-1] != "userTask"
            or node.get("id") != task_definition_key
        ):
            continue
        for prop in node.iter():
            if (
                prop.tag.rsplit("}", 1)[-1] == "property"
                and prop.get("name") == "automated"
                and str(prop.get("value", "")).strip().lower() == "true"
            ):
                return True
    return False


def acting_identity(
    automated: bool,
    signed_in_user: str | None,
    agent_account: str | None,
    *,
    id: str = "",
    state: TaskState | None = None,
) -> str:
    """Human tasks complete as the signed-in user, automated ones as the agent
    account. Neither falls back to the other. Raises ``NoActingIdentity``."""
    identity = agent_account if automated else signed_in_user
    if not identity:
        raise IllegalTransition(
            MACHINE_TASK,
            state,
            TaskEvent.COMPLETE,
            Reason.NO_ACTING_IDENTITY,
            "UserTask",
            id,
        )
    return identity


def signed_in_user() -> str | None:
    """The authenticated human principal of the tool call, if any."""
    from scion_sdk.identity import ActorType, current_actor

    actor = current_actor()
    if not actor.authenticated or actor.actor_type in (
        ActorType.SYSTEM,
        ActorType.ANONYMOUS,
    ):
        return None
    return actor.actor_id


def agent_account() -> str | None:
    from scion_sdk.config import setting

    return setting("CAMUNDA_AGENT_ACCOUNT", None) or None


# --- engine readers (one per generation) -----------------------------------


def _not_found(exc: Exception) -> bool:
    return "HTTP 404" in str(exc)


def read_instance_state(client: Any, generation: int | str, id: str) -> InstanceState:
    if str(generation) == "8":
        return instance_state_of(8, client.get_process_instance(id))
    record = dict(
        client._call("GET", "/history/process-instance/{id}", path={"id": id})
    )
    count = client._call("GET", "/incident/count", params={"processInstanceId": id})
    record["openIncidents"] = (count or {}).get("count", 0)
    return instance_state_of(7, record)


def read_task(client: Any, generation: int | str, id: str) -> tuple[TaskState, dict]:
    if str(generation) == "8":
        record = client._call("GET", f"{client.tasklist_url}/v1/tasks/{id}")
        return task_state_of(8, record), record
    try:
        record = client._call("GET", "/task/{id}", path={"id": id})
    except RuntimeError as exc:
        if not _not_found(exc):
            raise
        found = client._call("GET", "/history/task", params={"taskId": id})
        if not found:
            raise _unknown(MACHINE_TASK, "missing", "UserTask", id) from exc
        record = found[0]
    return task_state_of(7, record), record


def read_automated(
    client: Any, generation: int | str, record: Mapping[str, Any]
) -> bool:
    if str(generation) == "8":
        key = record.get("processDefinitionKey")
        if not (key and getattr(client, "operate_url", "")):
            return False
        doc = client._call(
            "GET", f"{client.operate_url}/v1/process-definitions/{key}/xml"
        )
        xml = doc.get("text") if isinstance(doc, dict) else None
        return is_automated(
            xml, record.get("taskDefinitionId") or record.get("taskDefinitionKey")
        )
    definition = record.get("processDefinitionId")
    if not definition:
        return False
    doc = client._call("GET", "/process-definition/{id}/xml", path={"id": definition})
    return is_automated(doc.get("bpmn20Xml"), record.get("taskDefinitionKey"))


# --- the guard -----------------------------------------------------------------


def guarded(kind: str, generation: int | str, event: Any) -> Callable:
    """Refuse an illegal move before the engine write.

    Wraps one generated client method. The first argument after ``self`` is the
    entity id. For the suspension tools ``event`` is ``None`` and is chosen from
    the request (``suspended`` true is Suspend, false is Activate).
    """

    def decorate(method: Callable) -> Callable:
        sig = inspect.signature(method)

        @functools.wraps(method)
        def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
            bound = sig.bind(self, *args, **kwargs).arguments
            ev = event
            if kind == "instance_suspension":
                ev, ids = _suspension_targets(bound)
                for pid in ids:
                    instance_transition(
                        read_instance_state(self, generation, pid), ev, id=pid
                    )
            elif kind == "instance":
                pid = str(bound["id" if "id" in bound else "process_instance_key"])
                instance_transition(
                    read_instance_state(self, generation, pid), ev, id=pid
                )
            else:
                tid = str(bound.get("id") or bound.get("task_id"))
                state, record = read_task(self, generation, tid)
                guards: dict[str, Any] = {"assignee": record.get("assignee")}
                if ev is TaskEvent.COMPLETE and state is TaskState.CLAIMED:
                    guards["identity"] = acting_identity(
                        read_automated(self, generation, record),
                        signed_in_user(),
                        agent_account(),
                        id=tid,
                        state=state,
                    )
                task_transition(state, ev, guards, id=tid)
            return method(self, *args, **kwargs)

        return wrapper

    return decorate


def _suspension_targets(bound: Mapping[str, Any]) -> tuple[InstanceEvent, list[str]]:
    """Event and instance ids of a suspension request (by id, or by id list).

    A request addressed by definition id or key has no single instance state and
    passes through to the engine, which applies it idempotently.
    """
    body = bound.get("body")
    if body is None:
        body = {"suspended": bound.get("suspended")}
    suspended = body.get("suspended") if isinstance(body, Mapping) else None
    if not isinstance(suspended, bool):
        suspended = bool(suspended)
    event = InstanceEvent.SUSPEND if suspended else InstanceEvent.ACTIVATE
    if "id" in bound:
        return event, [str(bound["id"])]
    ids = body.get("processInstanceIds") if isinstance(body, Mapping) else None
    return event, [str(i) for i in (ids or [])]
