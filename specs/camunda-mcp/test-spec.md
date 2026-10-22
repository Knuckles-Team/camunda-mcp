# CONN-CAMUNDA-MCP — Test specification

| Case | Fixture/action | Expected result |
| --- | --- | --- |
| VER-T1 | Read `camunda_mcp.__version__` and the `pyproject.toml` project version | They are equal |
| SURF-T1 | List the tools of the server built by `get_mcp_instance()` | 39 `camunda7_*`, 24 `camunda8_*`, `camunda_deploy`, `camunda_ingest_processes`; 65 in all |
| SURF-T2 | Read the tags of every listed tool | None is tagged `split-action` |

Proof: `tests/test_tool_surface.py` (`CONN-CAMUNDA-MCP-R002`, `CONN-CAMUNDA-MCP-R003`).

Proof: `tests/test_version.py::test_reported_version_matches_the_released_package` (`CONN-CAMUNDA-MCP-R001`).
