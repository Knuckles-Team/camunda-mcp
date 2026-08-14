"""Native epistemic-graph typed-node ingestion — Wire-First coverage.

Exercises the real ``ingest_entities`` / ``ingest_process_definitions`` /
``ingest_process_instances`` / ``ingest_tasks`` seam with a fake engine client (no
engine required), asserting the txn add_node/commit + edge calls and the Camunda
record → :BusinessProcess / :ProcessInstance / :Task mappings.
CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

from typing import Any

import msgpack
import pytest
from agent_utilities.knowledge_graph.memory.native_ingest import NativeIngestError
from agent_utilities.security.brain_context import ActorContext, use_actor
from agent_utilities.models.company_brain import ActorType
from agent_utilities.knowledge_graph.core.session import GraphSession, use_session

from camunda_mcp.kg_ingest import (
    ingest_entities,
    ingest_process_definitions,
    ingest_process_instances,
    ingest_tasks,
)


@pytest.fixture(autouse=True)
def _governed_session():
    actor = ActorContext(
        actor_id="subject:opaque:synthetic",
        actor_type=ActorType.AUTOMATED_SERVICE,
        roles=(),
        tenant_id="tenant:opaque:synthetic",
        authenticated=True,
    )
    session = GraphSession(
        actor=actor,
        tenant=actor.tenant_id,
        scopes=frozenset({"kg:write"}),
        graph="graph:opaque:synthetic",
        policy_version="policy:opaque:synthetic",
        audience="epistemic-graph",
    )
    with use_actor(actor), use_session(session):
        yield


class _FakeNodes:
    def __init__(self) -> None:
        self.values: dict[str, dict[str, Any]] = {}

    def properties(self, node_id: str) -> dict[str, Any] | None:
        return self.values.get(node_id)

    def list(self) -> list[tuple[str, dict[str, Any]]]:
        return list(self.values.items())


class _FakeChanges:
    def __init__(self, nodes: _FakeNodes) -> None:
        self.nodes = nodes
        self.edges: list[tuple[str, str, dict[str, Any]]] = []
        self.applied: list[dict[str, Any]] = []
        self.records: dict[str, dict[str, Any]] = {}
        self.versions: dict[str, dict[str, Any]] = {}

    def get(self, envelope_id: str) -> dict[str, Any] | None:
        return self.records.get(envelope_id)

    def content_version(self, object_id: str) -> dict[str, Any] | None:
        return self.versions.get(object_id)

    def cursor(self, _source: str, _partition: str = "") -> None:
        return None

    def apply(self, envelope: dict[str, Any]) -> dict[str, Any]:
        self.applied.append(envelope)
        mutation = envelope["mutation"]
        for operation in mutation["operations"]:
            method = operation["method"]
            params = method["params"]
            properties = msgpack.unpackb(params["properties_msgpack"], raw=False)
            if method["method"] == "AddNode":
                self.nodes.values[params["node_id"]] = properties
            elif method["method"] == "AddEdge":
                self.edges.append(
                    (params["source_id"], params["target_id"], properties)
                )
        version = envelope["content_version"]
        self.versions[version["object_id"]] = version
        self.records[envelope["envelope_id"]] = envelope
        return {
            "batch_id": mutation["batch_id"],
            "replayed": False,
            "projection_pending": False,
        }


class _FakeRdf:
    def validate_shacl(self, _shapes: str, _data_graph: str) -> dict[str, Any]:
        return {"conforms": True, "results": []}


class _FakeClient:
    def __init__(self) -> None:
        self.nodes = _FakeNodes()
        self.changes = _FakeChanges(self.nodes)
        self.rdf = _FakeRdf()

    @staticmethod
    def supports(operation: str) -> bool:
        return operation == "ApplyChangeEnvelope"


def test_ingest_entities_writes_nodes_and_edges():
    c = _FakeClient()
    res = ingest_entities(
        [
            {"id": "a", "node_type": "BusinessProcess", "name": "p"},
            {"id": "b", "node_type": "Deployment"},
        ],
        [{"source": "a", "target": "b", "relationship": "deployedIn"}],
        client=c,
    )
    assert res == {"nodes": 2, "edges": 1}
    assert len(c.changes.applied) == 1
    assert set(c.nodes.values) == {"a", "b"}
    # provenance is stamped
    assert c.nodes.values["a"]["source"] == "camunda-mcp"
    assert c.nodes.values["a"]["domain"] == "camunda"
    assert c.changes.edges == [("a", "b", {"relationship": "deployedIn"})]


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
    )
    assert res == {"nodes": 2, "edges": 1}
    proc = c.nodes.values["camunda:process:invoice:1:abc"]
    assert proc["node_type"] == "BusinessProcess"
    assert proc["processDefinitionKey"] == "invoice"
    assert proc["bpmnVersion"] == 1
    assert proc["externalToolId"] == "invoice:1:abc"
    assert c.nodes.values["camunda:deployment:dep-9"]["node_type"] == "Deployment"
    assert c.changes.edges == [
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
    )
    assert res == {"nodes": 1, "edges": 1}
    inst = c.nodes.values["camunda:instance:pi-1"]
    assert inst["node_type"] == "ProcessInstance"
    assert inst["businessKey"] == "INV-42"
    assert c.changes.edges == [
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
    )
    # 2 nodes (task + person), 2 edges (partOfInstance + assignedTo)
    assert res == {"nodes": 2, "edges": 2}
    task = c.nodes.values["camunda:task:task-1"]
    assert task["node_type"] == "Task"
    # native_ingest's governed PII scrubber redacts assignee-shaped values.
    assert task["assignee"] == "[REDACTED_PERSON]"
    assert task["activityId"] == "approve"
    assert c.nodes.values["camunda:person:jdoe"]["node_type"] == "Person"
    assert (
        "camunda:task:task-1",
        "camunda:instance:pi-1",
        {"relationship": "partOfInstance"},
    ) in c.changes.edges
    assert (
        "camunda:task:task-1",
        "camunda:person:jdoe",
        {"relationship": "assignedTo"},
    ) in c.changes.edges


def test_ingest_rejects_legacy_structural_fields():
    with pytest.raises(NativeIngestError, match="canonical node_type"):
        ingest_entities([{"id": "legacy", "type": "Legacy"}], client=_FakeClient())

def test_ingest_empty_is_rejected():
    with pytest.raises(NativeIngestError, match="at least one entity"):
        ingest_entities([], client=_FakeClient())
