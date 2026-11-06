# CONN-CAMUNDA-MCP — Connector identity, engine surface and business-process content

**Owner:** this repository. **Delivery:** SPECIFIED. **Acceptance:** NOT_AUDITED.

See [`requirements.md`](requirements.md) for the definition of every requirement ID this spec owns and [`status.json`](status.json) for their current delivery and acceptance state.

## Outcome

The version the `camunda_mcp` package reports at runtime (`camunda_mcp.__version__`) is the version that was released, so a deployed digest-only image identifies itself correctly in the fleet ledger and in acceptance runs. The business's processes live on the Operaton (Camunda 7) engine as BPMN and DMN: the connector serves the whole engine REST API as typed tools, sends values the way the engine parses them, and ships the ontology, tool-use contracts, skills and agent prompts that let the platform run those processes and generate agent workflow graphs from them.

## Requirements

| ID | Requirement | Evidence |
| --- | --- | --- |
| `CONN-CAMUNDA-MCP-R001` | Connector reports its released version: `__version__` equals the `pyproject.toml` version, and the version bump tool updates both together. | `tests/test_version.py` |
| `CONN-CAMUNDA-MCP-R002` | One tool per engine REST operation. | `tests/test_tool_surface.py` |
| `CONN-CAMUNDA-MCP-R003` | No condensed or routed tools. | `tests/test_tool_surface.py` |
| `CONN-CAMUNDA-MCP-R004` | Engine wire values. | `tests/test_wire_values.py` |
| `CONN-CAMUNDA-MCP-R005` | Tool-use contracts, links, data locations and roles. | `tests/test_surface_contracts.py` |
| `CONN-CAMUNDA-MCP-R006` | Prompts are agent definitions; task skills. | `tests/test_surface_contracts.py` |
| `CONN-CAMUNDA-MCP-R007` | BPMN ontology rolls up to core. | `tests/test_ontology.py` |

## Tool surface

The server exposes each engine REST operation once: 386 `camunda7_*` tools cover the whole Operaton 1.0.3 engine REST API (the operation id names the tool), 24 `camunda8_*` tools wrap the Camunda 8 client, and `camunda_ingest_processes` mirrors processes into the knowledge graph. Its content tier serves the BPMN ontology, the tool-use contracts, four task skills plus the operations catalog, and three agent prompts.

## Boundaries

The connector contract, certification and transport rules belong to scion-sdk. Generating agent workflow graphs from the BPMN model is owned by medulla and arbora; this connector supplies the model, the contracts and the tools. Release publication belongs to the repository pipeline.

## Why a new spec

The specs of this repository were read; none owns this capability. This spec states it for this connector only.

## Scope and interfaces

In scope: the rows of [requirements.md](requirements.md). Out of scope: the SDK modules and the engine, which own the shared capabilities.

## User Scenarios & Testing

### User Story 1 - Connector identity and release metadata (Priority: P1)

The version the `camunda_mcp` package reports at runtime (`camunda_mcp.__version__`) is the version that was released, so a deployed digest-only image identifies itself correctly in the fleet ledger and in acceptance runs.

**Acceptance Scenarios**:

1. **Given** the connector is configured, **When** the behaviour of row `CONN-CAMUNDA-MCP-R001` (connector reports its released version) is exercised, **Then** `tests/test_version.py::test_reported_version_matches_the_released_package`.
2. **Given** the connector is configured, **When** the behaviour of row `CONN-CAMUNDA-MCP-R002` (one tool per engine rest operation) is exercised, **Then** `tests/test_tool_surface.py::test_surface_is_one_tool_per_engine_operation`.
3. **Given** the connector is configured, **When** the behaviour of row `CONN-CAMUNDA-MCP-R003` (no condensed or routed tools) is exercised, **Then** `tests/test_tool_surface.py::test_no_action_routed_or_untyped_tools`.
4. **Given** the connector is configured, **When** the behaviour of row `CONN-CAMUNDA-MCP-R004` (engine wire values) is exercised, **Then** `tests/test_wire_values.py::test_booleans_are_lowercase_and_unset_filters_dropped`.
5. **Given** the connector is configured, **When** the behaviour of row `CONN-CAMUNDA-MCP-R005` (tool-use contracts, links, data locations and roles) is exercised, **Then** `tests/test_surface_contracts.py::test_every_tool_is_called_by_a_contract_and_named_by_a_link`.
6. **Given** the connector is configured, **When** the behaviour of row `CONN-CAMUNDA-MCP-R006` (prompts are agent definitions; task skills) is exercised, **Then** `tests/test_surface_contracts.py::test_prompts_are_complete_agent_definitions`.
7. **Given** the connector is configured, **When** the behaviour of row `CONN-CAMUNDA-MCP-R007` (bpmn ontology rolls up to core) is exercised, **Then** `tests/test_ontology.py::test_every_class_reaches_a_core_class`.

### User Story 2 - The engine syncs this system as a federated secondary (Priority: P2)

The engine reads this system's documents through the connector and sends governed changes back.

**Acceptance Scenarios**:

1. **Given** the connector is configured, **When** the behaviour of row `CONN-CAMUNDA-MCP-R008` is exercised, **Then** its rollup test passes.

### Edge Cases

- If `CONN-CAMUNDA-MCP-R001` is not met, its proving test fails: connector reports its released version.
- If `CONN-CAMUNDA-MCP-R002` is not met, its proving test fails: one tool per engine rest operation.
- If `CONN-CAMUNDA-MCP-R003` is not met, its proving test fails: no condensed or routed tools.
- If `CONN-CAMUNDA-MCP-R004` is not met, its proving test fails: engine wire values.
- If `CONN-CAMUNDA-MCP-R005` is not met, its proving test fails: tool-use contracts, links, data locations and roles.
- If `CONN-CAMUNDA-MCP-R006` is not met, its proving test fails: prompts are agent definitions; task skills.
- If `CONN-CAMUNDA-MCP-R007` is not met, its proving test fails: bpmn ontology rolls up to core.

## Requirements

- **FR-001**: Connector reports its released version. Rows: `CONN-CAMUNDA-MCP-R001`.
- **FR-002**: One tool per engine REST operation. Rows: `CONN-CAMUNDA-MCP-R002`.
- **FR-003**: No condensed or routed tools. Rows: `CONN-CAMUNDA-MCP-R003`.
- **FR-004**: Engine wire values. Rows: `CONN-CAMUNDA-MCP-R004`.
- **FR-005**: Tool-use contracts, links, data locations and roles. Rows: `CONN-CAMUNDA-MCP-R005`.
- **FR-006**: Prompts are agent definitions; task skills. Rows: `CONN-CAMUNDA-MCP-R006`.
- **FR-007**: BPMN ontology rolls up to core. Rows: `CONN-CAMUNDA-MCP-R007`.
- **FR-008**: Governed deploy sink for released process models. Rows: `CONN-CAMUNDA-MCP-R008`.
- **FR-009**: Process instance and user task lifecycles are explicit state machines (rollup). Rows: `CONN-CAMUNDA-MCP-R009`, `CONN-CAMUNDA-MCP-R009.1`, `CONN-CAMUNDA-MCP-R009.2`, `CONN-CAMUNDA-MCP-R009.3`, `CONN-CAMUNDA-MCP-R009.4`, `CONN-CAMUNDA-MCP-R009.5`, `CONN-CAMUNDA-MCP-R009.6`, `CONN-CAMUNDA-MCP-R009.7`.

## Success Criteria

- **SC-001**: `tests/test_version.py::test_reported_version_matches_the_released_package`. Rows: `CONN-CAMUNDA-MCP-R001`.
- **SC-002**: `tests/test_tool_surface.py::test_surface_is_one_tool_per_engine_operation`. Rows: `CONN-CAMUNDA-MCP-R002`.
- **SC-003**: `tests/test_tool_surface.py::test_no_action_routed_or_untyped_tools`. Rows: `CONN-CAMUNDA-MCP-R003`.
- **SC-004**: `tests/test_wire_values.py::test_booleans_are_lowercase_and_unset_filters_dropped`. Rows: `CONN-CAMUNDA-MCP-R004`.
- **SC-005**: `tests/test_surface_contracts.py::test_every_tool_is_called_by_a_contract_and_named_by_a_link`. Rows: `CONN-CAMUNDA-MCP-R005`.
- **SC-006**: `tests/test_surface_contracts.py::test_prompts_are_complete_agent_definitions`. Rows: `CONN-CAMUNDA-MCP-R006`.
- **SC-007**: `tests/test_ontology.py::test_every_class_reaches_a_core_class`. Rows: `CONN-CAMUNDA-MCP-R007`.

## Assumptions

- The external system is reachable with operator-supplied credentials.
- The SDK and engine contracts the rows cite are at the floors declared in `pyproject.toml`.

## Traceability

| Label | Rows | Design section | Test ID | Evidence |
|---|---|---|---|---|
| FR-001 | `CONN-CAMUNDA-MCP-R001` | [plan.md](plan.md) | T-001 | [test-spec.md](test-spec.md) |
| FR-002 | `CONN-CAMUNDA-MCP-R002` | [plan.md](plan.md) | T-002 | [test-spec.md](test-spec.md) |
| FR-003 | `CONN-CAMUNDA-MCP-R003` | [plan.md](plan.md) | T-003 | [test-spec.md](test-spec.md) |
| FR-004 | `CONN-CAMUNDA-MCP-R004` | [plan.md](plan.md) | T-004 | [test-spec.md](test-spec.md) |
| FR-005 | `CONN-CAMUNDA-MCP-R005` | [plan.md](plan.md) | T-005 | [test-spec.md](test-spec.md) |
| FR-006 | `CONN-CAMUNDA-MCP-R006` | [plan.md](plan.md) | T-006 | [test-spec.md](test-spec.md) |
| FR-007 | `CONN-CAMUNDA-MCP-R007` | [plan.md](plan.md) | T-007 | [test-spec.md](test-spec.md) |
| FR-009 | `CONN-CAMUNDA-MCP-R009`, `CONN-CAMUNDA-MCP-R009.1`, `CONN-CAMUNDA-MCP-R009.2`, `CONN-CAMUNDA-MCP-R009.3`, `CONN-CAMUNDA-MCP-R009.4`, `CONN-CAMUNDA-MCP-R009.5`, `CONN-CAMUNDA-MCP-R009.6`, `CONN-CAMUNDA-MCP-R009.7` | [plan.md](plan.md) | T-009 | [test-spec.md](test-spec.md) |
