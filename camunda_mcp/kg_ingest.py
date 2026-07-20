"""Native epistemic-graph ingestion for Camunda records (typed graph nodes).

CONCEPT:AU-KG.ingest.enterprise-source-extractor. camunda-mcp natively pushes its
process-automation data into the ONE epistemic-graph knowledge graph as **typed OWL
nodes** (``:BusinessProcess``, ``:ProcessInstance``, ``:Task``, ``:Deployment``,
``:Incident`` …) + links, matching the classes federated by ``camunda_mcp.ontology``.

The write path is the required
``agent_utilities.knowledge_graph.memory.native_ingest`` authority. Node ids follow
``camunda:<class>:<extId>``; each ``node_type`` matches a class in
``camunda_mcp/ontology/camunda.ttl``.
"""

from __future__ import annotations

from typing import Any

from agent_utilities.knowledge_graph.memory.native_ingest import (
    ingest_documents as _native_ingest_documents,
)
from agent_utilities.knowledge_graph.memory.native_ingest import (
    ingest_entities as _native_ingest_entities,
)

_SOURCE = "camunda-mcp"
_DOMAIN = "camunda"
# --- public thin wrappers --------------------------------------------------- #
def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Write typed OWL nodes (+ edges) into epistemic-graph.

    Validation and engine failures are surfaced as ``NativeIngestError``.
    """
    return _native_ingest_entities(
        entities,
        relationships,
        source=source,
        domain=domain,
        client=client,
        graph=graph,
    )


def ingest_documents(
    documents: list[dict[str, Any]],
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Write text records (e.g. BPMN XML) as ``:Document`` nodes for semantic search."""
    return _native_ingest_documents(
        documents, source=source, domain=domain, client=client, graph=graph
    )


# --- domain mappers (records -> typed entity/relationship dicts) ------------ #
def ingest_process_definitions(
    definitions: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map Camunda process-definition records → ``:BusinessProcess`` (+ ``:Deployment``).

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
                "suspended": d.get("suspended"),
                "category": d.get("category"),
                "tenantId": d.get("tenantId"),
                "externalToolId": str(did),
            }
        )
        dep = d.get("deploymentId")
        if dep is not None:
            entities.append(
                {
                    "id": f"camunda:deployment:{dep}",
                    "node_type": "Deployment",
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
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_process_instances(
    instances: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
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
                "suspended": i.get("suspended"),
                "processState": i.get("state"),
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
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_tasks(
    tasks: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map user-task records → ``:Task`` (+ ``:partOfInstance`` / ``:assignedTo``)."""
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for t in tasks or []:
        tid = t.get("id")
        if tid is None:
            continue
        entities.append(
            {
                "id": f"camunda:task:{tid}",
                "node_type": "Task",
                "name": t.get("name"),
                "assignee": t.get("assignee"),
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
    return ingest_entities(entities, relationships, client=client, graph=graph)
