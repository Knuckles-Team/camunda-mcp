# CONN-CAMUNDA-MCP-CONNECTOR-CONTENT — Implementation plan

Governing spec: [spec.md](spec.md). Rows: [requirements.md](requirements.md).

## Summary

`pyproject.toml` declares `camunda-mcp` as the connector identity. `create_mcp_server` resolves the packaged content of `camunda_mcp` from it.

## Technical Context

- **Language/Version**: Python 3.14 (floor 3.12)
- **Primary Dependencies**: scion-sdk, fastmcp
- **Storage**: N/A; the connector stores nothing
- **Testing**: pytest; the proof level each row names
- **Target Platform**: Linux containers
- **Project Type**: connector (MCP server)
- **Performance Goals**: N/A
- **Constraints**: one tool per API operation; shared capabilities come from the SDK
- **Scale/Scope**: 2 rows

## Constitution Check

- One owner per concept: pass. The connector owns one external system's calls, mappings and tools only.
- Connectors depend on the SDK and are called through arbora: pass.
- No ratchets: pass. The rows add no suppression.

## Project Structure

```text
pyproject.toml  existing
camunda_mcp/connector_sources.py  existing
```

## Phase 0: Research

No unknowns. Each row names the code it touches.

## Phase 1: Design

The rows are delivered in place; the design is the caller chain below.

### Definition documents as pack sources (R003)

The engine treats Camunda as a federated secondary for process and decision models. The connector serves each definition's BPMN 2.0 or DMN document through an access contract, so arbora's source executor reads it at sync time. The data location and the class roll-up already exist (`CONN-CAMUNDA-MCP-R005`, `CONN-CAMUNDA-MCP-R007`).

### Lifecycle ontology (CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R004)

`camunda_mcp/ontology/camunda.ttl` describes the machines of `CONN-CAMUNDA-MCP-R009`. Every class extends a medulla core state-machine class; the file never imports the core ontology. The test compares the ontology with the code tables, so a state added in code without a class fails the build.

## Phase 2: Task approach

`tasks.md` holds one task line per row, producer first.

## Complexity Tracking

None. The constitution check passed.

## Build contract

The repository pre-commit hooks apply: `ruff-format`, `connector-standard`, `secrets`, `tests-fast`. Each row names its proving test. No suppression and no duplicate implementation.

## Production caller chain

1. `CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R001`: the `camunda-mcp` console script (`scion_sdk.cli:serve`) loads the `scion_sdk.connector` entry point `camunda_mcp:connector` (`camunda_mcp/__init__.py:85`), which the SDK `build_server` turns into the served MCP server and its resources and prompts.
2. `CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R002`: arbora calls `fleet.call` for the existing read tool `camunda7_list_process_definitions and camunda7_list_incidents` (`Camunda7Api.list_process_definitions` at `camunda_mcp/api/api_client_camunda7.py:19` and `list_incidents` at line 337) -> the connector source in `camunda_mcp/connector_sources.py` -> the packaged `camunda_mcp/ontology/access_contracts.ttl` (planned, not yet present).
4. `CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R004`: the `scion_sdk.ontology_providers` entry point serves `camunda_mcp/ontology/camunda.ttl`, whose lifecycle classes are checked against `camunda_mcp/lifecycle.py`.

## Cross-repo seams

none. The cited owner rows are library capabilities the connector calls in process; spec.md names them.

### Amendments

- 2026-11-06: lifecycle ontology (organization constitution Article XXXI). Row `CONN-CAMUNDA-MCP-CONNECTOR-CONTENT-R004` and children R004.1 to R004.3 describe the machines of `CONN-CAMUNDA-MCP-R009`.
