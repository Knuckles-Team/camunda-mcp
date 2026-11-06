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
                reached = True  # a core class (http://knuckles.team/kg#)
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
