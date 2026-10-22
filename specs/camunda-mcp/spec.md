# CONN-CAMUNDA-MCP — Connector identity and release metadata

**Owner:** this repository. **Delivery:** SPECIFIED. **Acceptance:** NOT_AUDITED.

See [`requirements.md`](requirements.md) for the definition of every requirement ID this spec owns and [`status.json`](status.json) for their current delivery and acceptance state.

## Outcome

The version the `camunda_mcp` package reports at runtime (`camunda_mcp.__version__`) is the version that was released, so a deployed digest-only image identifies itself correctly in the fleet ledger and in acceptance runs.

## Requirements

| ID | Requirement | Evidence |
| --- | --- | --- |
| `CONN-CAMUNDA-MCP-R001` | Connector reports its released version: `__version__` equals the `pyproject.toml` version, and the version bump tool updates both together. | `tests/test_version.py` |
| `CONN-CAMUNDA-MCP-R002` | One tool per API operation: 39 `camunda7_*`, 24 `camunda8_*`, `camunda_deploy` and `camunda_ingest_processes`; 65 tools. | `tests/test_tool_surface.py` |
| `CONN-CAMUNDA-MCP-R003` | No condensed action facades: no `split-action` tools. | `tests/test_tool_surface.py` |

## Tool surface

The server exposes each Camunda API operation once. `camunda7_*` tools wrap the Camunda 7 Engine REST client, `camunda8_*` tools wrap the Camunda 8 client; `camunda_deploy` (deploy a BPMN, DMN or form resource to either platform) and `camunda_ingest_processes` (ingest definitions and instances into the knowledge graph) are the two tools that are not single client operations. The server lists 65 tools in all.

## Boundaries

The connector contract, certification and transport rules belong to agent-connector-sdk. Release publication belongs to the repository pipeline.
