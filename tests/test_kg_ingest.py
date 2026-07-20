"""Native epistemic-graph typed-node ingestion — Wire-First coverage.

Exercises the real ``ingest_entities`` / ``ingest_process_definitions`` /
``ingest_process_instances`` / ``ingest_tasks`` seam with a fake engine client (no
engine required), asserting the txn add_node/commit + edge calls and the Camunda
record → :BusinessProcess / :ProcessInstance / :Task mappings.
CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

import pytest
from agent_utilities.knowledge_graph.memory.native_ingest import NativeIngestError

from camunda_mcp.kg_ingest import (
    ingest_entities,
    ingest_process_definitions,
    ingest_process_instances,
    ingest_tasks,
)


class _FakeTxn:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.committed = False

    def begin(self, graph=None):
        self.graph = graph
        return "txn-1"

    def add_node(self, txn, node_id, props):
        self.nodes[node_id] = props

    def add_edge(self, txn, src, dst, props):
        self.edges.append((src, dst, props))

    def commit(self, txn):
        self.committed = True
        return True



class _FakeClient:
    def __init__(self):
        self.txn = _FakeTxn()


def test_ingest_entities_writes_nodes_and_edges():
    c = _FakeClient()
    res = ingest_entities(
        [
            {"id": "a", "node_type": "BusinessProcess", "name": "p"},
            {"id": "b", "node_type": "Deployment"},
        ],
        [{"source": "a", "target": "b", "relationship": "deployedIn"}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 2, "edges": 1}
    assert c.txn.committed is True
    assert set(c.txn.nodes) == {"a", "b"}
    # provenance is stamped
    assert c.txn.nodes["a"]["source"] == "camunda-mcp"
    assert c.txn.nodes["a"]["domain"] == "camunda"
    assert c.txn.edges == [("a", "b", {"relationship": "deployedIn"})]


def test_ingest_process_definitions_maps_process_and_deployment():
    c = _FakeClient()
    res = ingest_process_definitions(
        [
            {
                "id": "invoice:1:abc",
                "key": "invoice",
                "name": "Invoice Receipt",
                "version": 1,
                "suspended": False,
                "deploymentId": "dep-9",
            }
        ],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 2, "edges": 1}
    proc = c.txn.nodes["camunda:process:invoice:1:abc"]
    assert proc["node_type"] == "BusinessProcess"
    assert proc["processDefinitionKey"] == "invoice"
    assert proc["bpmnVersion"] == 1
    assert proc["externalToolId"] == "invoice:1:abc"
    assert c.txn.nodes["camunda:deployment:dep-9"]["node_type"] == "Deployment"
    assert c.txn.edges == [
        (
            "camunda:process:invoice:1:abc",
            "camunda:deployment:dep-9",
            {"relationship": "deployedIn"},
        )
    ]


def test_ingest_process_instances_links_definition():
    c = _FakeClient()
    res = ingest_process_instances(
        [
            {
                "id": "pi-1",
                "definitionId": "invoice:1:abc",
                "businessKey": "INV-42",
                "suspended": False,
            }
        ],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 1}
    inst = c.txn.nodes["camunda:instance:pi-1"]
    assert inst["node_type"] == "ProcessInstance"
    assert inst["businessKey"] == "INV-42"
    assert c.txn.edges == [
        (
            "camunda:instance:pi-1",
            "camunda:process:invoice:1:abc",
            {"relationship": "instanceOf"},
        )
    ]


def test_ingest_tasks_maps_task_instance_and_assignee():
    c = _FakeClient()
    res = ingest_tasks(
        [
            {
                "id": "task-1",
                "name": "Approve invoice",
                "assignee": "jdoe",
                "taskDefinitionKey": "approve",
                "processInstanceId": "pi-1",
            }
        ],
        client=c,
        graph="__commons__",
    )
    # 2 nodes (task + person), 2 edges (partOfInstance + assignedTo)
    assert res == {"nodes": 2, "edges": 2}
    task = c.txn.nodes["camunda:task:task-1"]
    assert task["node_type"] == "Task"
    assert task["assignee"] == "jdoe"
    assert task["activityId"] == "approve"
    assert c.txn.nodes["camunda:person:jdoe"]["node_type"] == "Person"
    assert (
        "camunda:task:task-1",
        "camunda:instance:pi-1",
        {"relationship": "partOfInstance"},
    ) in c.txn.edges
    assert (
        "camunda:task:task-1",
        "camunda:person:jdoe",
        {"relationship": "assignedTo"},
    ) in c.txn.edges


def test_ingest_rejects_legacy_structural_fields():
    with pytest.raises(NativeIngestError, match="canonical node_type"):
        ingest_entities([{"id": "legacy", "type": "Legacy"}], client=_FakeClient())

def test_ingest_empty_is_rejected():
    with pytest.raises(NativeIngestError, match="at least one entity"):
        ingest_entities([], client=_FakeClient())
