"""CONN-CAMUNDA-MCP-R007: the BPMN/engine ontology rolls up to core by subclassing."""

import asyncio
import re
from pathlib import Path

from scion_sdk.connector import build_server

TTL = (
    Path(__file__).resolve().parents[1] / "camunda_mcp" / "ontology" / "camunda.ttl"
).read_text()
BLOCKS = {
    m.group(1): m.group(2)
    for m in re.finditer(r"^:(\w+) a owl:Class\b(.*?)\s\.\s*$", TTL, re.M | re.S)
}


def _parents(body: str) -> list[str]:
    match = re.search(r"rdfs:subClassOf ([^;]+?)\s*(;|$)", body, re.S)
    return re.findall(r":(\w+)", match.group(1)) if match else []


def test_every_class_reaches_a_core_class():
    for name in BLOCKS:
        seen, todo = set(), [name]
        reached = False
        while todo:
            cls = todo.pop()
            if cls in seen:
                continue
            seen.add(cls)
            if cls not in BLOCKS:
                reached = True  # a core class (https://knuckles-team.github.io/ontology/core#)
                continue
            parents = _parents(BLOCKS[cls])
            assert parents, f"{cls} has no rdfs:subClassOf"
            todo += parents
        assert reached, name


def test_no_import_of_core_and_bpmn_constructs_modelled():
    assert "owl:imports" not in TTL
    for cls in (
        "BpmnProcess",
        "BpmnUserTask",
        "BpmnServiceTask",
        "BpmnBusinessRuleTask",
        "BpmnExclusiveGateway",
        "BpmnParallelGateway",
        "BpmnStartEvent",
        "BpmnBoundaryEvent",
        "BpmnTimerEventDefinition",
        "BpmnSequenceFlow",
        "BpmnLane",
        "BpmnParticipant",
        "DmnDecision",
        "CamundaEngine",
    ):
        assert cls in BLOCKS, cls


def test_flow_nodes_carry_graph_kind_and_tools_exist():
    _, mcp = build_server("camunda_mcp", command_args=[])
    tools = {t.name for t in asyncio.run(mcp.list_tools())}
    for tool in re.findall(r'"(camunda7_\w+)"', TTL):
        assert tool in tools, tool
    for name, body in BLOCKS.items():
        if (
            "bpmnElement" in body
            and name.startswith("Bpmn")
            and "EventDefinition" not in name
        ):
            if name not in (
                "BpmnDefinitions",
                "BpmnSequenceFlow",
                "BpmnMessageFlow",
                "BpmnParticipant",
                "BpmnLaneSet",
                "BpmnLane",
                "BpmnDataObject",
                "BpmnDataStoreReference",
            ):
                assert ":dagNodeKind" in body, name


# --- CONNECTOR-CONTENT-R004: lifecycle machines ---------------------------------

import pytest  # noqa: E402

from camunda_mcp.lifecycle import (  # noqa: E402
    INSTANCE_TABLE,
    TASK_TABLE,
    InstanceEvent,
    InstanceState,
    Reason,
    TaskEvent,
    TaskState,
)


def _ancestors(name: str) -> set[str]:
    seen, todo = set(), [name]
    while todo:
        cls = todo.pop()
        if cls in seen:
            continue
        seen.add(cls)
        todo += _parents(BLOCKS[cls]) if cls in BLOCKS else []
    return seen


def _camel(value: str) -> str:
    return "".join(p.capitalize() for p in value.split("_"))


@pytest.mark.parametrize(
    "kind,pattern,core",
    [
        ("machine", r"(ProcessInstanceLifecycle|UserTaskLifecycle)$", "StateMachine"),
        ("state", r"(Instance|Task)(?!TransitionRefused)\w+State$", "State"),
        ("transition", r"(Instance|Task)\w+Transition$", "Transition"),
        ("event", r"(Instance|Task)\w+Event$", "Event"),
        ("guard", r"TaskCompleteGuard$", "TransitionGuard"),
        ("refusal", r"(Instance|Task)TransitionRefused\w*$", "RefusalCode"),
    ],
)
def test_lifecycle_classes_extend_core_state_machine_classes(kind, pattern, core):
    names = [n for n in BLOCKS if re.match(pattern, n)]
    assert names, kind
    for name in names:
        assert core in _ancestors(name), name


def test_ontology_states_and_transitions_equal_the_code_machines():
    states = {
        n
        for n in BLOCKS
        if re.match(r"(Instance|Task)(?!TransitionRefused)\w+State$", n)
    }
    assert states == {f"Instance{m.name.capitalize()}State" for m in InstanceState} | {
        f"Task{m.name.capitalize()}State" for m in TaskState
    }
    expected = {}
    for pre, table in (("Instance", INSTANCE_TABLE), ("Task", TASK_TABLE)):
        for (a, e), b in table.items():
            expected[f"{pre}{a.name.capitalize()}{_camel(e.value)}Transition"] = (
                f"{pre}{a.name.capitalize()}State",
                f"{pre}{b.name.capitalize()}State",
                f"{pre}{_camel(e.value)}Event",
            )
    found = {}
    for name, body in BLOCKS.items():
        if re.match(r"(Instance|Task)\w+Transition$", name):
            found[name] = tuple(
                re.search(rf":{prop} :(\w+)", body).group(1)
                for prop in ("transitionSource", "transitionTarget", "transitionEvent")
            )
    assert found == expected
    reasons = {m.group(1) for m in re.finditer(r':refusalReason "(\w+)"', TTL)}
    assert reasons == {r.value for r in Reason}
    events = {n for n in BLOCKS if re.match(r"(Instance|Task)\w+Event$", n)}
    assert events == {f"Instance{_camel(e.value)}Event" for e in InstanceEvent} | {
        f"Task{_camel(e.value)}Event" for e in TaskEvent
    }
    assert ":processState" not in TTL and ":suspended " not in TTL
    assert ":lifecycleState a owl:ObjectProperty" in TTL


def test_ontology_definition_machine_equals_the_code_machine():
    from camunda_mcp.lifecycle import DEFINITION_TABLE, DefinitionState

    states = {
        n for n in BLOCKS if re.match(r"Definition(?!TransitionRefused)\w+State$", n)
    }
    assert states == {f"Definition{m.name.capitalize()}State" for m in DefinitionState}
    found = {}
    for name, body in BLOCKS.items():
        if re.match(r"Definition\w+Transition$", name):
            found[name] = tuple(
                re.search(rf":{prop} :(\w+)", body).group(1)
                for prop in ("transitionSource", "transitionTarget", "transitionEvent")
            )
    expected = {
        f"Definition{a.name.capitalize()}{_camel(e.value)}Transition": (
            f"Definition{a.name.capitalize()}State",
            f"Definition{b.name.capitalize()}State",
            f"Definition{_camel(e.value)}Event",
        )
        for (a, e), b in DEFINITION_TABLE.items()
    }
    assert found == expected
    assert "StateMachine" in _ancestors("ProcessDefinitionLifecycle")
