"""CONN-CAMUNDA-MCP-R009: process instance and user task lifecycle machines."""

import asyncio
import json
import re
from pathlib import Path

import pytest
import requests
from scion_sdk.connector import build_server

from camunda_mcp import lifecycle as lc
from camunda_mcp.lifecycle import (
    IllegalTransition,
    Reason,
    acting_identity,
    instance_state_of,
    instance_transition,
    task_state_of,
    task_transition,
)
from camunda_mcp.lifecycle import (
    InstanceEvent as IE,
)
from camunda_mcp.lifecycle import (
    InstanceState as IS,
)
from camunda_mcp.lifecycle import (
    TaskEvent as TE,
)
from camunda_mcp.lifecycle import (
    TaskState as TS,
)

INSTANCE_EDGES = {
    "created-start": (IS.CREATED, IE.START, IS.ACTIVE),
    "active-suspend": (IS.ACTIVE, IE.SUSPEND, IS.SUSPENDED),
    "suspended-activate": (IS.SUSPENDED, IE.ACTIVATE, IS.ACTIVE),
    "active-raise_incident": (IS.ACTIVE, IE.RAISE_INCIDENT, IS.INCIDENT),
    "incident-resolve_incident": (IS.INCIDENT, IE.RESOLVE_INCIDENT, IS.ACTIVE),
    "incident-suspend": (IS.INCIDENT, IE.SUSPEND, IS.SUSPENDED),
    "active-complete": (IS.ACTIVE, IE.COMPLETE, IS.COMPLETED),
    "incident-complete": (IS.INCIDENT, IE.COMPLETE, IS.COMPLETED),
    "active-cancel": (IS.ACTIVE, IE.CANCEL, IS.CANCELED),
    "suspended-cancel": (IS.SUSPENDED, IE.CANCEL, IS.CANCELED),
    "incident-cancel": (IS.INCIDENT, IE.CANCEL, IS.CANCELED),
    "active-terminate": (IS.ACTIVE, IE.TERMINATE, IS.TERMINATED),
    "suspended-terminate": (IS.SUSPENDED, IE.TERMINATE, IS.TERMINATED),
    "incident-terminate": (IS.INCIDENT, IE.TERMINATE, IS.TERMINATED),
}
LEGAL_INSTANCE = {(a, e) for a, e, _ in INSTANCE_EDGES.values()}
OTHER_INSTANCE = [
    pytest.param(s, e, id=f"{s.name.lower()}-{e.value}")
    for s in IS
    for e in IE
    if (s, e) not in LEGAL_INSTANCE
]

TASK_EDGES = {
    "claim": (TS.CREATED, TE.CLAIM, TS.CLAIMED),
    "unclaim": (TS.CLAIMED, TE.UNCLAIM, TS.CREATED),
    "complete": (TS.CLAIMED, TE.COMPLETE, TS.COMPLETED),
    "cancel_from_created": (TS.CREATED, TE.CANCEL, TS.CANCELED),
    "cancel_from_claimed": (TS.CLAIMED, TE.CANCEL, TS.CANCELED),
    "delete_from_created": (TS.CREATED, TE.DELETE, TS.DELETED),
    "delete_from_claimed": (TS.CLAIMED, TE.DELETE, TS.DELETED),
}
LEGAL_TASK = {(a, e) for a, e, _ in TASK_EDGES.values()}
OTHER_TASK = [
    pytest.param(s, e, id=f"{s.name.lower()}-{e.value}")
    for s in TS
    for e in TE
    if (s, e) not in LEGAL_TASK
]
GUARDS = {"assignee": "alice", "identity": "alice"}


@pytest.mark.parametrize("edge", INSTANCE_EDGES, ids=list(INSTANCE_EDGES))
def test_every_legal_instance_transition_reaches_its_state(edge):
    state, event, target = INSTANCE_EDGES[edge]
    assert instance_transition(state, event) is target


@pytest.mark.parametrize("state,event", OTHER_INSTANCE)
def test_every_other_instance_pair_is_refused_with_a_typed_error(state, event):
    with pytest.raises(IllegalTransition) as err:
        instance_transition(state, event, id="pi-1")
    assert err.value.code == "ILLEGAL_TRANSITION"
    assert err.value.machine == "process_instance"
    assert err.value.from_state == state
    assert err.value.event == event
    expected = (
        Reason.TERMINAL_STATE if state in lc.INSTANCE_TERMINAL else Reason.ILLEGAL_EDGE
    )
    assert err.value.reason == expected


def test_incident_is_a_sub_state_of_active():
    assert lc.INSTANCE_PARENT[IS.INCIDENT] is IS.ACTIVE
    for event in IE:
        if event is IE.RAISE_INCIDENT:
            with pytest.raises(IllegalTransition):
                instance_transition(IS.INCIDENT, event)
        elif (IS.ACTIVE, event) in lc.INSTANCE_TABLE and event is not IE.SUSPEND:
            assert (
                instance_transition(IS.INCIDENT, event)
                is lc.INSTANCE_TABLE[(IS.ACTIVE, event)]
            )
    assert instance_transition(IS.INCIDENT, IE.RESOLVE_INCIDENT) is IS.ACTIVE


@pytest.mark.parametrize(
    "gen,record,expected",
    [
        pytest.param(7, {"state": "ACTIVE"}, IS.ACTIVE, id="g7-active"),
        pytest.param(
            7,
            {"state": "ACTIVE", "openIncidents": 1},
            IS.INCIDENT,
            id="g7-active-incident",
        ),
        pytest.param(7, {"state": "SUSPENDED"}, IS.SUSPENDED, id="g7-suspended"),
        pytest.param(7, {"state": "COMPLETED"}, IS.COMPLETED, id="g7-completed"),
        pytest.param(
            7,
            {"state": "EXTERNALLY_TERMINATED"},
            IS.TERMINATED,
            id="g7-externally_terminated",
        ),
        pytest.param(
            7,
            {"state": "INTERNALLY_TERMINATED"},
            IS.TERMINATED,
            id="g7-internally_terminated",
        ),
        pytest.param(8, {"state": "ACTIVE"}, IS.ACTIVE, id="g8-active"),
        pytest.param(
            8,
            {"state": "ACTIVE", "incident": True},
            IS.INCIDENT,
            id="g8-active-incident",
        ),
        pytest.param(8, {"state": "COMPLETED"}, IS.COMPLETED, id="g8-completed"),
        pytest.param(8, {"state": "CANCELED"}, IS.CANCELED, id="g8-canceled"),
    ],
)
def test_generation_7_and_8_records_map_to_one_machine(gen, record, expected):
    assert instance_state_of(gen, record) is expected


def test_unknown_engine_state_is_refused():
    for gen, record in ((7, {"state": "BOGUS"}), (8, {"state": "SUSPENDED"}), (8, {})):
        with pytest.raises(IllegalTransition) as err:
            instance_state_of(gen, record)
        assert err.value.reason == Reason.UNKNOWN_ENGINE_STATE


@pytest.mark.parametrize("edge", TASK_EDGES, ids=list(TASK_EDGES))
def test_every_legal_task_transition_reaches_its_state(edge):
    state, event, target = TASK_EDGES[edge]
    assert task_transition(state, event, GUARDS) is target


@pytest.mark.parametrize("state,event", OTHER_TASK)
def test_every_other_task_pair_is_refused_with_a_typed_error(state, event):
    with pytest.raises(IllegalTransition) as err:
        task_transition(state, event, GUARDS, id="t-1")
    assert err.value.machine == "user_task"
    assert err.value.from_state == state
    assert err.value.event == event


def test_complete_needs_claimed_by_the_same_assignee():
    with pytest.raises(IllegalTransition) as err:
        task_transition(TS.CREATED, TE.COMPLETE, {"identity": "alice"})
    assert err.value.reason == Reason.NOT_CLAIMED
    with pytest.raises(IllegalTransition) as err:
        task_transition(
            TS.CLAIMED, TE.COMPLETE, {"assignee": "bob", "identity": "alice"}
        )
    assert err.value.reason == Reason.CLAIMED_BY_OTHER
    assert task_transition(TS.CLAIMED, TE.COMPLETE, GUARDS) is TS.COMPLETED


@pytest.mark.parametrize(
    "state,event", [p for p in OTHER_TASK if p.values[1] in (TE.CLAIM, TE.UNCLAIM)]
)
def test_claim_and_unclaim_are_refused_from_wrong_states_without_a_write(
    served, state, event
):
    record = {TS.CREATED: None, TS.CLAIMED: "alice"}.get(state, "alice")
    routes = {"/task/t1": {"id": "t1", "assignee": record}}
    if state in (TS.COMPLETED, TS.CANCELED, TS.DELETED):
        reason = {TS.COMPLETED: "completed", TS.DELETED: "deleted"}.get(state, "x")
        routes = {
            "/task/t1": None,
            "/history/task": [{"id": "t1", "endTime": "t", "deleteReason": reason}],
        }
    engine = _Engine({k: v for k, v in routes.items() if v is not None})
    tool = "camunda7_claim" if event is TE.CLAIM else "camunda7_unclaim"
    with pytest.raises(Exception, match="ILLEGAL_TRANSITION"):
        served(engine, tool, {"id": "t1"})
    assert engine.writes == []


def test_task_state_mapping():
    assert task_state_of(7, {"id": "t"}) is TS.CREATED
    assert task_state_of(7, {"id": "t", "assignee": "a"}) is TS.CLAIMED
    done = {"id": "t", "endTime": "x", "deleteReason": "completed"}
    assert task_state_of(7, done) is TS.COMPLETED
    assert task_state_of(7, {**done, "deleteReason": "deleted"}) is TS.DELETED
    assert task_state_of(8, {"taskState": "CREATED", "assignee": "a"}) is TS.CLAIMED
    assert task_state_of(8, {"taskState": "CANCELED"}) is TS.CANCELED
    with pytest.raises(IllegalTransition):
        task_state_of(8, {"taskState": "WEIRD"})


# --- acting identity --------------------------------------------------------

_XML = """<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
 xmlns:camunda="http://camunda.org/schema/1.0/bpmn"><process id="p">
 <userTask id="auto"><extensionElements><camunda:properties>
 <camunda:property name="automated" value="true"/></camunda:properties>
 </extensionElements></userTask><userTask id="human"/></process></definitions>"""


def test_human_task_completes_as_the_signed_in_user():
    assert lc.is_automated(_XML, "human") is False
    assert acting_identity(False, "alice", "arbora-agent") == "alice"


def test_automated_task_completes_as_the_arbora_agent_account():
    assert lc.is_automated(_XML, "auto") is True
    assert acting_identity(True, "alice", "arbora-agent") == "arbora-agent"


def test_no_resolvable_identity_is_refused_with_no_acting_identity():
    for automated, user, agent in ((False, None, "agent"), (True, "alice", None)):
        with pytest.raises(IllegalTransition) as err:
            acting_identity(automated, user, agent)
        assert err.value.reason == Reason.NO_ACTING_IDENTITY


def test_human_task_never_falls_back_to_the_agent_account():
    with pytest.raises(IllegalTransition):
        acting_identity(False, None, "arbora-agent")
    assert acting_identity(True, "alice", "agent") != "alice"


# --- ingest field ------------------------------------------------------------


def test_ingested_nodes_carry_lifecycle_state_only():
    src = Path(lc.__file__).parent
    ingest = (src / "kg_ingest.py").read_text()
    assert '"lifecycleState"' in ingest
    assert '"processState"' not in ingest
    assert '"suspended": i.get' not in ingest
    sources = (src / "connector_sources.py").read_text()
    assert "lifecycleState" in sources
    assert "processState" not in sources and '"suspended"' not in sources


def test_no_module_outside_lifecycle_branches_on_engine_state_strings():
    src = Path(lc.__file__).parent
    pattern = re.compile(
        r"""['"](ACTIVE|SUSPENDED|COMPLETED|CANCELED|EXTERNALLY_TERMINATED|INTERNALLY_TERMINATED)['"]"""
    )
    for path in src.rglob("*.py"):
        if path.name in {"lifecycle.py", "connector_contracts.py"}:
            continue
        for line in path.read_text().splitlines():
            if pattern.search(line) and not line.lstrip().startswith(("#", '"""')):
                raise AssertionError(f"{path.name}: {line.strip()}")


# --- hot path: a refusal never reaches the engine ------------------------------


class _Engine:
    """A recorded engine: GET answers from fixtures, writes are recorded."""

    def __init__(self, routes):
        self.routes = routes
        self.writes = []

    def __call__(self, session, method, url, **kwargs):
        path = (
            url.split("/engine-rest", 1)[-1]
            if "/engine-rest" in url
            else "/" + url.split("/", 3)[-1]
        )
        if method != "GET":
            self.writes.append((method, path))
            return _Resp({})
        for key, body in self.routes.items():
            if path.startswith(key):
                return _Resp(body)
        return _Resp({"type": "X", "message": "nope"}, 404)


class _Resp:
    headers = {"Content-Type": "application/json"}
    encoding = "utf-8"

    def __init__(self, body, status=200):
        self.status_code = status
        self._body = json.dumps(body).encode()

    def iter_content(self, chunk_size):
        yield self._body

    def close(self):
        pass


@pytest.fixture
def served(monkeypatch):
    monkeypatch.setenv("CAMUNDA7_URL", "http://engine.test/engine-rest")
    monkeypatch.setenv("CAMUNDA8_ZEEBE_REST_URL", "http://zeebe.test")
    monkeypatch.setenv("CAMUNDA8_OPERATE_URL", "http://operate.test")
    monkeypatch.setenv("CAMUNDA8_TASKLIST_URL", "http://tasklist.test")
    monkeypatch.setenv("CAMUNDA_AGENT_ACCOUNT", "arbora-agent")
    _, mcp = build_server("camunda_mcp", command_args=[])

    def call(engine, tool, args):
        monkeypatch.setattr(
            requests.Session,
            "request",
            lambda s, **k: engine(s, k.pop("method"), k.pop("url"), **k),
        )

        async def run():
            return await mcp.call_tool(tool, args)

        return asyncio.run(run())

    return call


def _instance_engine(state, incidents=0):
    return _Engine(
        {
            "/history/process-instance/pi": {"id": "pi", "state": state},
            "/incident/count": {"count": incidents},
        }
    )


INSTANCE_CALLS = {
    "cancel": (
        "camunda7_delete_process_instance",
        {"id": "pi", "confirm": True},
        "DELETE",
    ),
    "suspend": (
        "camunda7_update_suspension_state_by_id",
        {"id": "pi", "body": {"suspended": True}},
        "PUT",
    ),
    "activate": (
        "camunda7_update_suspension_state_by_id",
        {"id": "pi", "body": {"suspended": False}},
        "PUT",
    ),
}
_STATE_RECORD = {
    IS.ACTIVE: ("ACTIVE", 0),
    IS.INCIDENT: ("ACTIVE", 1),
    IS.SUSPENDED: ("SUSPENDED", 0),
    IS.COMPLETED: ("COMPLETED", 0),
    IS.TERMINATED: ("EXTERNALLY_TERMINATED", 0),
}
_CALL_EVENT = {"cancel": IE.TERMINATE, "suspend": IE.SUSPEND, "activate": IE.ACTIVATE}


@pytest.mark.parametrize(
    "state,call",
    [
        pytest.param(s, c, id=f"{s.name.lower()}-{c}")
        for s in _STATE_RECORD
        for c in INSTANCE_CALLS
    ],
)
def test_cancel_suspend_and_activate_are_refused_from_wrong_states_without_a_write(
    served, state, call
):
    tool, args, verb = INSTANCE_CALLS[call]
    engine = _instance_engine(*_STATE_RECORD[state])
    if (state, _CALL_EVENT[call]) in lc.INSTANCE_TABLE:
        served(engine, tool, args)
        assert [w[0] for w in engine.writes] == [verb]
    else:
        with pytest.raises(Exception, match="ILLEGAL_TRANSITION"):
            served(engine, tool, args)
        assert engine.writes == []


def _task_engine(assignee=None, definition=""):
    routes = {
        "/task/t1": {
            "id": "t1",
            "assignee": assignee,
            "processDefinitionId": "d1",
            "taskDefinitionKey": "auto" if definition else "human",
        },
        "/process-definition/d1/xml": {"bpmn20Xml": definition or _XML},
    }
    return _Engine(routes)


def test_instance_and_task_machines_refuse_before_any_engine_call(served):
    # unclaimed task: complete is refused before the write (the live-check case)
    engine = _task_engine(assignee=None)
    with pytest.raises(Exception, match="ILLEGAL_TRANSITION.*NotClaimed"):
        served(engine, "camunda7_complete", {"id": "t1"})
    assert engine.writes == []
    # claimed task: claim again is refused
    engine = _task_engine(assignee="alice")
    with pytest.raises(Exception, match="AlreadyClaimed"):
        served(engine, "camunda7_claim", {"id": "t1", "body": {"userId": "bob"}})
    assert engine.writes == []
    # terminal instance refuses cancel
    engine = _instance_engine("COMPLETED")
    with pytest.raises(Exception, match="TerminalState"):
        served(
            engine, "camunda7_delete_process_instance", {"id": "pi", "confirm": True}
        )
    assert engine.writes == []
    # generation 8: cancel of a completed instance is refused
    engine = _Engine({"/v1/process-instances/9": {"key": 9, "state": "COMPLETED"}})
    with pytest.raises(Exception, match="TerminalState"):
        served(
            engine, "camunda8_cancel_process_instance", {"process_instance_key": "9"}
        )
    assert engine.writes == []


def test_complete_writes_only_for_the_assignee(served, monkeypatch):
    monkeypatch.setattr(lc, "signed_in_user", lambda: "alice")
    engine = _task_engine(assignee="alice")
    served(engine, "camunda7_complete", {"id": "t1"})
    assert engine.writes == [("POST", "/task/t1/complete")]
    engine = _task_engine(assignee="bob")
    with pytest.raises(Exception, match="ClaimedByOther"):
        served(engine, "camunda7_complete", {"id": "t1"})
    assert engine.writes == []
    monkeypatch.setattr(lc, "signed_in_user", lambda: None)
    engine = _task_engine(assignee="alice")
    with pytest.raises(Exception, match="NoActingIdentity"):
        served(engine, "camunda7_complete", {"id": "t1"})
    assert engine.writes == []
    # an automated task completes as the agent account, not the signed-in user
    monkeypatch.setattr(lc, "signed_in_user", lambda: "alice")
    engine = _task_engine(assignee="arbora-agent", definition=_XML)
    served(engine, "camunda7_complete", {"id": "t1"})
    assert engine.writes == [("POST", "/task/t1/complete")]


# --- process definition suspension (CONN-CAMUNDA-MCP-R009.9) ---------------

DefState, DefEvent = lc.DefinitionState, lc.DefinitionEvent
DEFINITION_EDGES = {
    "active-suspend": (DefState.ACTIVE, DefEvent.SUSPEND, DefState.SUSPENDED),
    "suspended-activate": (DefState.SUSPENDED, DefEvent.ACTIVATE, DefState.ACTIVE),
}
OTHER_DEFINITION = [
    pytest.param(s, e, id=f"{s.name.lower()}-{e.value}")
    for s in DefState
    for e in DefEvent
    if (s, e) not in {(a, b) for a, b, _ in DEFINITION_EDGES.values()}
]


@pytest.mark.parametrize("edge", DEFINITION_EDGES.values(), ids=DEFINITION_EDGES)
def test_every_legal_definition_transition_reaches_its_state(edge):
    state, event, expected = edge
    assert lc.definition_transition(state, event) is expected


@pytest.mark.parametrize("state,event", OTHER_DEFINITION)
def test_every_other_definition_pair_is_refused_with_a_typed_error(state, event):
    with pytest.raises(IllegalTransition) as err:
        lc.definition_transition(state, event, id="d1")
    assert err.value.machine == "process_definition"
    assert err.value.from_state == state and err.value.event == event


def test_definition_state_is_read_from_the_suspended_flag():
    assert lc.definition_state_of({"suspended": False}) is DefState.ACTIVE
    assert lc.definition_state_of({"suspended": True}) is DefState.SUSPENDED
    with pytest.raises(IllegalTransition, match="UnknownEngineState"):
        lc.definition_state_of({"id": "d1"})


@pytest.mark.parametrize(
    "suspended,request_suspend",
    [
        pytest.param(False, True, id="active-suspend"),
        pytest.param(True, False, id="suspended-activate"),
        pytest.param(True, True, id="suspended-suspend"),
        pytest.param(False, False, id="active-activate"),
    ],
)
def test_definition_suspension_is_guarded_without_a_write_on_refusal(
    served, suspended, request_suspend
):
    engine = _Engine({"/process-definition/d1": {"id": "d1", "suspended": suspended}})
    args = {"id": "d1", "body": {"suspended": request_suspend}}
    if suspended != request_suspend:
        served(
            engine, "camunda7_update_process_definition_suspension_state_by_id", args
        )
        assert [w[0] for w in engine.writes] == ["PUT"]
    else:
        with pytest.raises(Exception, match="ILLEGAL_TRANSITION"):
            served(
                engine,
                "camunda7_update_process_definition_suspension_state_by_id",
                args,
            )
        assert engine.writes == []


def test_definition_node_carries_lifecycle_state():
    src = (Path(lc.__file__).parent / "kg_ingest.py").read_text()
    assert "definition_state_of(d)" in src
