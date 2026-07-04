"""Native epistemic-graph ingestion for Camunda records (typed graph nodes).

CONCEPT:AU-KG.ingest.enterprise-source-extractor. camunda-mcp natively pushes its
process-automation data into the ONE epistemic-graph knowledge graph as **typed OWL
nodes** (``:BusinessProcess``, ``:ProcessInstance``, ``:Task``, ``:Deployment``,
``:Incident`` …) + links, matching the classes federated by ``camunda_mcp.ontology``.

The write path is the shared fleet primitive
``agent_utilities.knowledge_graph.memory.native_ingest`` (the ONE txn implementation).
It is imported **guarded**: if the KG stack is absent (the primitive is not yet in the
installed agent_utilities), this module falls back to a small self-contained txn writer
over the lightweight engine client (``GraphComputeEngine()._client`` + ``txn``) — the
same fast client the blob ``MediaStore`` uses, NOT the heavy ingestion engine.

Everything is best-effort and dependency-/engine-guarded: with no KG stack or no
reachable engine, every entry point **no-ops** (returns ``None``), so the connector
keeps working with zero KG infrastructure. Node ids follow ``camunda:<class>:<extId>``;
each ``type`` matches a class in ``camunda_mcp/ontology/camunda.ttl``.
"""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger("camunda_mcp.kg")

_SOURCE = "camunda-mcp"
_DOMAIN = "camunda"
_DEFAULT_GRAPH = "__commons__"

# --- shared primitive (preferred), imported guarded ------------------------- #
try:
    from agent_utilities.knowledge_graph.memory.native_ingest import (
        ingest_documents as _shared_ingest_documents,
    )
    from agent_utilities.knowledge_graph.memory.native_ingest import (
        ingest_entities as _shared_ingest_entities,
    )
except Exception as e:  # noqa: BLE001 — KG stack absent; self-contained fallback used
    logger.debug("native_ingest primitive unavailable (%s); using local fallback", e)
    _shared_ingest_entities = None
    _shared_ingest_documents = None


# --- self-contained fallback (used when the primitive or an injected client is present) #
def _fallback_client() -> tuple[Any | None, str]:
    """Return ``(engine_client, graph_name)`` or ``(None, "")`` when unavailable."""
    try:
        from agent_utilities.knowledge_graph.core.graph_compute import (
            GraphComputeEngine,
        )
    except Exception as e:  # noqa: BLE001 — KG stack absent
        logger.debug("KG ingest unavailable (import): %s", e)
        return None, ""
    try:
        engine = GraphComputeEngine()
        client = getattr(engine, "_client", None)
        if client is None:
            return None, ""
        return client, (getattr(engine, "graph_name", None) or _DEFAULT_GRAPH)
    except Exception as e:  # noqa: BLE001 — engine unreachable
        logger.debug("KG ingest: engine unreachable: %s", e)
        return None, ""


def _fallback_write(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None,
    *,
    source: str,
    domain: str,
    client: Any | None,
    graph: str | None,
) -> dict[str, int] | None:
    entities = [e for e in (entities or []) if e.get("id")]
    if not entities:
        return None
    if client is None:
        client, graph = _fallback_client()
    if client is None:
        return None
    graph = graph or _DEFAULT_GRAPH
    try:
        txn = client.txn.begin(graph=graph)
        for ent in entities:
            props = {k: v for k, v in ent.items() if k != "id" and v is not None}
            props.setdefault("source", source)
            props.setdefault("domain", domain)
            client.txn.add_node(txn, ent["id"], props)
        committed = client.txn.commit(txn)
    except Exception as e:  # noqa: BLE001 — engine/txn failure is non-fatal
        logger.warning("KG ingest: txn failed: %s", e)
        return None
    if not committed:
        logger.warning("KG ingest: txn not committed (conflict)")
        return None
    edges = 0
    for rel in relationships or []:
        try:
            client.edges.add(
                rel["source"], rel["target"], {"type": rel.get("type", "RELATED")}
            )
            edges += 1
        except Exception as e:  # noqa: BLE001 — pure edge link, best-effort
            logger.debug("KG ingest: edge skipped: %s", e)
    logger.info("KG ingest[%s]: wrote %d nodes, %d edges", domain, len(entities), edges)
    return {"nodes": len(entities), "edges": edges}


# --- public thin wrappers --------------------------------------------------- #
def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Write typed OWL nodes (+ edges) into epistemic-graph.

    Delegates to the shared ``native_ingest`` primitive when it is importable and no
    explicit ``client`` is injected; otherwise uses the self-contained fallback (also
    the path tests exercise with a fake client). Returns ``{"nodes":n,"edges":m}`` or
    ``None`` (never raises).
    """
    if not entities:
        return None
    if client is None and _shared_ingest_entities is not None:
        return _shared_ingest_entities(
            entities, relationships, source=source, domain=domain
        )
    return _fallback_write(
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
) -> dict[str, int] | None:
    """Write text records (e.g. BPMN XML) as ``:Document`` nodes for semantic search."""
    if not documents:
        return None
    if client is None and _shared_ingest_documents is not None:
        return _shared_ingest_documents(documents, source=source, domain=domain)
    # Fallback: shape docs as :Document typed nodes and reuse the txn writer.
    nodes: list[dict[str, Any]] = []
    for doc in documents:
        did = doc.get("id")
        text = doc.get("text") or doc.get("content")
        if not did or not text:
            continue
        node = {k: v for k, v in doc.items() if k != "content" and v is not None}
        node["id"] = did
        node["type"] = "Document"
        node["text"] = text
        nodes.append(node)
    return _fallback_write(
        nodes, None, source=source, domain=domain, client=client, graph=graph
    )


# --- domain mappers (records -> typed entity/relationship dicts) ------------ #
def ingest_process_definitions(
    definitions: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
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
                "type": "BusinessProcess",
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
                    "type": "Deployment",
                    "externalToolId": str(dep),
                }
            )
            relationships.append(
                {
                    "source": f"camunda:process:{did}",
                    "target": f"camunda:deployment:{dep}",
                    "type": "deployedIn",
                }
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_process_instances(
    instances: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
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
                "type": "ProcessInstance",
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
                    "type": "instanceOf",
                }
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_tasks(
    tasks: list[dict[str, Any]],
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
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
                "type": "Task",
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
                    "type": "partOfInstance",
                }
            )
        assignee = t.get("assignee")
        if assignee:
            entities.append(
                {
                    "id": f"camunda:person:{assignee}",
                    "type": "Person",
                    "name": assignee,
                }
            )
            relationships.append(
                {
                    "source": f"camunda:task:{tid}",
                    "target": f"camunda:person:{assignee}",
                    "type": "assignedTo",
                }
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)
