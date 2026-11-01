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

The connector contract, certification and transport rules belong to scion-sdk. Release publication belongs to the repository pipeline.

## Why a new spec

The specs of this repository were read; none owns this capability. This spec states it for this connector only.

## Scope and interfaces

In scope: the rows of [requirements.md](requirements.md). Out of scope: the SDK modules and the engine, which own the shared capabilities.

## User Scenarios & Testing

### User Story 1 - Connector identity and release metadata (Priority: P1)

The version the `camunda_mcp` package reports at runtime (`camunda_mcp.__version__`) is the version that was released, so a deployed digest-only image identifies itself correctly in the fleet ledger and in acceptance runs.

**Acceptance Scenarios**:

1. **Given** the connector is configured, **When** the behaviour of row `CONN-CAMUNDA-MCP-R001` (connector reports its released version) is exercised, **Then** `tests/test_version.py::test_reported_version_matches_the_released_package`.
2. **Given** the connector is configured, **When** the behaviour of row `CONN-CAMUNDA-MCP-R002` (one tool per api operation) is exercised, **Then** `tests/test_tool_surface.py::test_surface_is_one_tool_per_operation_plus_two`.
3. **Given** the connector is configured, **When** the behaviour of row `CONN-CAMUNDA-MCP-R003` (no condensed action facades) is exercised, **Then** `tests/test_tool_surface.py::test_no_split_action_facade_tools`.

### Edge Cases

- If `CONN-CAMUNDA-MCP-R001` is not met, its proving test fails: connector reports its released version.
- If `CONN-CAMUNDA-MCP-R002` is not met, its proving test fails: one tool per api operation.
- If `CONN-CAMUNDA-MCP-R003` is not met, its proving test fails: no condensed action facades.

## Requirements

- **FR-001**: Connector reports its released version. Rows: `CONN-CAMUNDA-MCP-R001`.
- **FR-002**: One tool per API operation. Rows: `CONN-CAMUNDA-MCP-R002`.
- **FR-003**: No condensed action facades. Rows: `CONN-CAMUNDA-MCP-R003`.

## Success Criteria

- **SC-001**: `tests/test_version.py::test_reported_version_matches_the_released_package`. Rows: `CONN-CAMUNDA-MCP-R001`.
- **SC-002**: `tests/test_tool_surface.py::test_surface_is_one_tool_per_operation_plus_two`. Rows: `CONN-CAMUNDA-MCP-R002`.
- **SC-003**: `tests/test_tool_surface.py::test_no_split_action_facade_tools`. Rows: `CONN-CAMUNDA-MCP-R003`.

## Assumptions

- The external system is reachable with operator-supplied credentials.
- The SDK and engine contracts the rows cite are at the floors declared in `pyproject.toml`.

## Traceability

| Label | Rows | Design section | Test ID | Evidence |
|---|---|---|---|---|
| FR-001 | `CONN-CAMUNDA-MCP-R001` | [plan.md](plan.md) | T-001 | [test-spec.md](test-spec.md) |
| FR-002 | `CONN-CAMUNDA-MCP-R002` | [plan.md](plan.md) | T-002 | [test-spec.md](test-spec.md) |
| FR-003 | `CONN-CAMUNDA-MCP-R003` | [plan.md](plan.md) | T-003 | [test-spec.md](test-spec.md) |
