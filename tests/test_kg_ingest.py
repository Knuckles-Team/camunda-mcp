"""Epistemic-graph typed-node ingestion — Wire-First coverage.

Exercises the real ``ingest_entities`` / ``ingest_process_definitions`` /
``ingest_process_instances`` / ``ingest_tasks`` seam against a fake
``agent_connector_sdk.ingest`` transport (no engine required). The real SDK
request builder (``agent_connector_sdk.ingest.request.build_request``) still
runs, so a malformed change set is still caught by the SDK's own contract, not
re-derived here; only the final network commit is faked.
CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

from types import SimpleNamespace
from typing import Any

import pytest
from agent_connector_sdk.ingest import IngestError, KnowledgeIngest
from epistemic_graph.generated.source_ingestion import SourceIngestionRequest

from camunda_mcp.kg_ingest import (
    ingest_entities,
    ingest_process_definitions,
    ingest_process_instances,
    ingest_tasks,
)


class _FakeTransport:
    """Records every submitted request; no epistemic-graph engine required."""

    def __init__(self) -> None:
        self.requests: list[SourceIngestionRequest] = []

    async def source_status(self, _connector: str, _stream: str) -> Any:
        return SimpleNamespace(accepted_checkpoint=None)

    async def submit(self, request: SourceIngestionRequest) -> Any:
        self.requests.append(request)
        return SimpleNamespace(
            affected_count=len(request.records),
            relationship_count=len(request.relationships),
        )

    async def store_blob(self, _data: bytes) -> str:
        raise AssertionError("camunda-mcp topology ingestion carries no media")


@pytest.fixture
def ingest() -> tuple[KnowledgeIngest, _FakeTransport]:
    transport = _FakeTransport()
    return KnowledgeIngest(transport, loop=None), transport


@pytest.mark.asyncio
async def test_ingest_entities_writes_nodes_and_edges(ingest):
    service, transport = ingest
    res = await ingest_entities(
        [
            {"id": "a", "node_type": "BusinessProcess", "name": "p"},
            {"id": "b", "node_type": "Deployment"},
        ],
        [{"source": "a", "target": "b", "relationship": "deployedIn"}],
        ingest=service,
    )
    assert res == {"nodes": 2, "edges": 1}
    assert len(transport.requests) == 1
    request = transport.requests[0]
    record_ids = {record.record_id for record in request.records}
    assert record_ids == {"a", "b"}
    a_record = next(r for r in request.records if r.record_id == "a")
    assert a_record.payload["name"] == "p"
    assert request.relationships[0].relation_reference.endswith(
        "resources/BusinessProcess/relations/deployedIn"
    )


@pytest.mark.asyncio
async def test_ingest_process_definitions_maps_process_and_deployment(ingest):
    service, transport = ingest
    res = await ingest_process_definitions(
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
        ingest=service,
    )
    assert res == {"nodes": 2, "edges": 1}
    request = transport.requests[0]
    proc = next(
        r for r in request.records if r.record_id == "camunda:process:invoice:1:abc"
    )
    assert proc.payload["processDefinitionKey"] == "invoice"
    assert proc.payload["bpmnVersion"] == 1
    assert proc.payload["externalToolId"] == "invoice:1:abc"
    assert any(
        r.record_id == "camunda:deployment:dep-9" for r in request.records
    )
    assert request.relationships[0].relation_reference.endswith(
        "resources/BusinessProcess/relations/deployedIn"
    )


@pytest.mark.asyncio
async def test_ingest_process_instances_links_definition(ingest):
    service, transport = ingest
    res = await ingest_process_instances(
        [
            {
                "id": "pi-1",
                "definitionId": "invoice:1:abc",
                "businessKey": "INV-42",
                "suspended": False,
            }
        ],
        ingest=service,
    )
    assert res == {"nodes": 1, "edges": 1}
    request = transport.requests[0]
    inst = next(r for r in request.records if r.record_id == "camunda:instance:pi-1")
    assert inst.payload["businessKey"] == "INV-42"
    assert request.relationships[0].relation_reference.endswith(
        "resources/ProcessInstance/relations/instanceOf"
    )


@pytest.mark.asyncio
async def test_ingest_tasks_maps_task_instance_and_assignee(ingest):
    service, transport = ingest
    res = await ingest_tasks(
        [
            {
                "id": "task-1",
                "name": "Approve invoice",
                "assignee": "jdoe",
                "taskDefinitionKey": "approve",
                "processInstanceId": "pi-1",
            }
        ],
        ingest=service,
    )
    # 2 nodes (task + person), 2 edges (partOfInstance + assignedTo)
    assert res == {"nodes": 2, "edges": 2}
    request = transport.requests[0]
    task = next(r for r in request.records if r.record_id == "camunda:task:task-1")
    # the SDK's PersistencePrivacyGuard redacts assignee-shaped values.
    assert task.payload["assignee"] == "[REDACTED_PERSON]"
    assert task.payload["activityId"] == "approve"
    assert any(r.record_id == "camunda:person:jdoe" for r in request.records)
    relation_refs = {r.relation_reference for r in request.relationships}
    assert any(ref.endswith("relations/partOfInstance") for ref in relation_refs)
    assert any(ref.endswith("relations/assignedTo") for ref in relation_refs)


@pytest.mark.asyncio
async def test_ingest_rejects_missing_node_type(ingest):
    service, _ = ingest
    with pytest.raises(IngestError):
        await ingest_entities([{"id": "legacy"}], ingest=service)


@pytest.mark.asyncio
async def test_ingest_empty_is_rejected(ingest):
    service, _ = ingest
    with pytest.raises(IngestError, match="at least one entity"):
        await ingest_entities([], ingest=service)
