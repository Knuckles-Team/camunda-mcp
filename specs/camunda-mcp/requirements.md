# CONN-CAMUNDA-MCP requirements

Every requirement this specification owns, with the proof that closes it. Delivery state and
public evidence for each ID are recorded in [`status.json`](status.json); this file defines what
each ID means. The design is in [`spec.md`](spec.md) and [`plan.md`](plan.md), the test contract
in [`test-spec.md`](test-spec.md), and the work order in [`tasks.md`](tasks.md).

| ID | Requirement | Verification |
|---|---|---|
| `CONN-CAMUNDA-MCP-R001` | **Connector reports its released version.** `camunda_mcp.__version__` equals the released `pyproject.toml` version and the bump configuration updates both. | `tests/test_version.py::test_reported_version_matches_the_released_package` |
| `CONN-CAMUNDA-MCP-R002` | **One tool per API operation.** The server lists 65 tools: one `camunda7_<operation>` per Camunda 7 client method (39), one `camunda8_<operation>` per Camunda 8 client method (24), plus `camunda_deploy` and `camunda_ingest_processes`. | `tests/test_tool_surface.py::test_surface_is_one_tool_per_operation_plus_two` |
| `CONN-CAMUNDA-MCP-R003` | **No condensed action facades.** No tool is tagged `split-action`, and no `camunda_*` tool routes an `action` string to an operation a `camunda7_*` or `camunda8_*` tool already serves. | `tests/test_tool_surface.py::test_no_split_action_facade_tools` |
