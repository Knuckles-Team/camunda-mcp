"""Epistemic-graph ingestion for Camunda records (typed graph nodes).

CONCEPT:AU-KG.ingest.enterprise-source-extractor. camunda-mcp pushes its
process-automation data into the ONE medulla knowledge graph as **typed
OWL nodes** (``:BusinessProcess``, ``:ProcessInstance``, ``:CamundaUserTask``,
``:CamundaDeployment``, ``:CamundaIncident`` …) + links, matching the classes federated by
``camunda_mcp.ontology``.

The write path is ``scion_sdk.ingest`` -- the generated ``SourceIngest``
client, not a local ingestion helper. Node ids follow ``camunda:<class>:<extId>``;
each ``node_type`` matches a class in ``camunda_mcp/ontology/camunda.ttl``.
"""

from __future__ import annotations

from typing import Any

from scion_sdk.ingest import (
    ChangeSet,
    Document,
    Entity,
    IngestBinding,
    IngestError,
    KnowledgeIngest,
    Relationship,
    current_ingest,
)

from camunda_mcp.lifecycle import (
    definition_state_of,
    instance_state_of,
    task_state_of,
)

_BINDING = IngestBinding(connector="camunda-mcp", stream="camunda")

_ENTITY_RESERVED_KEYS = frozenset({"id", "node_type"})
_RELATIONSHIP_RESERVED_KEYS = frozenset({"source", "target", "relationship"})


def _to_entity(record: dict[str, Any]) -> Entity:
    return Entity(
        id=record.get("id"),
        node_type=record.get("node_type"),
        properties={
            key: value
            for key, value in record.items()
            if key not in _ENTITY_RESERVED_KEYS
        },
    )


def _to_relationship(record: dict[str, Any]) -> Relationship:
    properties = {
        key: value
        for key, value in record.items()
        if key not in _RELATIONSHIP_RESERVED_KEYS
    }
    return Relationship(
        source=record["source"],
        target=record["target"],
        relationship=record["relationship"],
        properties=properties or None,
    )


# --- public thin wrappers --------------------------------------------------- #
async def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Write typed OWL nodes (+ edges) into medulla.

    A malformed change set or a refused commit raises ``IngestError``.
    """
    if not entities:
        raise IngestError("ingest_entities needs at least one entity")
    change_set = ChangeSet(
        entities=tuple(_to_entity(entity) for entity in entities),
        relationships=tuple(
            _to_relationship(relationship) for relationship in relationships or ()
        ),
    )
    service = ingest or current_ingest()
    receipt = await service.submit(_BINDING, change_set)
    return {"nodes": receipt.affected_count, "edges": receipt.relationship_count}


async def ingest_documents(
    documents: list[dict[str, Any]],
    *,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Write text records (e.g. BPMN XML) as ``:Document`` nodes for semantic search."""
    if not documents:
        raise IngestError("ingest_documents needs at least one document")
    change_set = ChangeSet(
        documents=tuple(
            Document(
                id=doc["id"],
                text=doc["text"],
                title=doc.get("title"),
                source_uri=doc.get("source_uri"),
                properties={
                    key: value
                    for key, value in doc.items()
                    if key not in {"id", "text", "title", "source_uri"}
                },
            )
            for doc in documents
        )
    )
    service = ingest or current_ingest()
    receipt = await service.submit(_BINDING, change_set)
    return {"nodes": receipt.affected_count, "edges": receipt.relationship_count}


# --- domain mappers (records -> typed entity/relationship dicts) ------------ #
async def ingest_process_definitions(
    definitions: list[dict[str, Any]],
    *,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Map Camunda process-definition records → ``:BusinessProcess`` (+ ``:CamundaDeployment``).

    Accepts Camunda 7 Engine-REST ``process-definition`` records (fields ``id``,
    ``key``, ``name``, ``version``, ``deploymentId``, ``suspended`` …). Emits the
    ``:deployedIn`` link when a ``deploymentId`` is present.
    """
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for d in definitions or []:
        did = d.get("id") or d.get("key")
        if did is None:
            continue
        entities.append(
            {
                "id": f"camunda:process:{did}",
                "node_type": "BusinessProcess",
                "name": d.get("name") or d.get("key"),
                "processDefinitionKey": d.get("key"),
                "bpmnVersion": d.get("version"),
                "category": d.get("category"),
                "tenantId": d.get("tenantId"),
                "lifecycleState": (
                    definition_state_of(d).value
                    if isinstance(d.get("suspended"), bool)
                    else None
                ),
                "externalToolId": str(did),
            }
        )
        dep = d.get("deploymentId")
        if dep is not None:
            entities.append(
                {
                    "id": f"camunda:deployment:{dep}",
                    "node_type": "CamundaDeployment",
                    "externalToolId": str(dep),
                }
            )
            relationships.append(
                {
                    "source": f"camunda:process:{did}",
                    "target": f"camunda:deployment:{dep}",
                    "relationship": "deployedIn",
                }
            )
    return await ingest_entities(entities, relationships, ingest=ingest)


def _generation(record: dict[str, Any]) -> int:
    """Generation 8 records are keyed by ``key`` and carry no ``id``."""
    return 8 if record.get("key") is not None and record.get("id") is None else 7


async def ingest_process_instances(
    instances: list[dict[str, Any]],
    *,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Map process-instance records → ``:ProcessInstance`` (+ ``:instanceOf`` link)."""
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for i in instances or []:
        iid = i.get("id") or i.get("key")
        if iid is None:
            continue
        entities.append(
            {
                "id": f"camunda:instance:{iid}",
                "node_type": "ProcessInstance",
                "businessKey": i.get("businessKey"),
                "lifecycleState": instance_state_of(_generation(i), i).value,
                "ended": i.get("ended"),
                "tenantId": i.get("tenantId"),
                "externalToolId": str(iid),
            }
        )
        pdid = i.get("definitionId") or i.get("processDefinitionId")
        if pdid is not None:
            relationships.append(
                {
                    "source": f"camunda:instance:{iid}",
                    "target": f"camunda:process:{pdid}",
                    "relationship": "instanceOf",
                }
            )
    return await ingest_entities(entities, relationships, ingest=ingest)


async def ingest_tasks(
    tasks: list[dict[str, Any]],
    *,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Map user-task records → ``:CamundaUserTask`` (+ ``:partOfInstance`` / ``:assignedTo``)."""
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for t in tasks or []:
        tid = t.get("id")
        if tid is None:
            continue
        entities.append(
            {
                "id": f"camunda:task:{tid}",
                "node_type": "CamundaUserTask",
                "name": t.get("name"),
                "assignee": t.get("assignee"),
                "lifecycleState": task_state_of(8 if "taskState" in t else 7, t).value,
                "activityId": t.get("taskDefinitionKey"),
                "priority": t.get("priority"),
                "created": t.get("created"),
                "due": t.get("due"),
                "externalToolId": str(tid),
            }
        )
        piid = t.get("processInstanceId")
        if piid is not None:
            relationships.append(
                {
                    "source": f"camunda:task:{tid}",
                    "target": f"camunda:instance:{piid}",
                    "relationship": "partOfInstance",
                }
            )
        assignee = t.get("assignee")
        if assignee:
            entities.append(
                {
                    "id": f"camunda:person:{assignee}",
                    "node_type": "Person",
                    "name": assignee,
                }
            )
            relationships.append(
                {
                    "source": f"camunda:task:{tid}",
                    "target": f"camunda:person:{assignee}",
                    "relationship": "assignedTo",
                }
            )
    return await ingest_entities(entities, relationships, ingest=ingest)
