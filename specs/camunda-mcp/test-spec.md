# CONN-CAMUNDA-MCP — Test specification

| Case | Fixture/action | Expected result |
| --- | --- | --- |
| VER-T1 | Read `camunda_mcp.__version__` and the `pyproject.toml` project version | They are equal |
| SURF-T1 | List the tools of the server built by `build_server("camunda_mcp")` | 386 `camunda7_*`, 24 `camunda8_*` and `camunda_ingest_processes` |
| SURF-T2 | Read every listed tool | None is tagged `split-action`, takes `action` or is untyped; the retired tools are absent |
| WIRE-T1 | Call `get_process_definitions(latest_version=True, suspended=False)` against a captured session | The URL carries `latestVersion=true&suspended=false` |
| WIRE-T2 | Call `create_deployment(resources=...)` and a failing call | Multipart parts are sent; the error carries the engine message |
| CONTRACT-T1 | Compare served tools with contract steps and links | Every tool is called by a step and named by a link; step parameters exist on the tool |
| PROMPT-T1 | Read every packaged prompt | Each is a full agent definition naming served tools, packaged skills and declared locations |
| ONTO-T1 | Walk the `rdfs:subClassOf` chain of every class in `camunda.ttl` | Each reaches a core class; no `owl:imports` |

Proof: `tests/test_version.py::test_reported_version_matches_the_released_package` (`CONN-CAMUNDA-MCP-R001`).

Proof: `tests/test_tool_surface.py` (`CONN-CAMUNDA-MCP-R002`, `CONN-CAMUNDA-MCP-R003`).

Proof: `tests/test_wire_values.py` (`CONN-CAMUNDA-MCP-R004`).

Proof: `tests/test_surface_contracts.py` (`CONN-CAMUNDA-MCP-R005`, `CONN-CAMUNDA-MCP-R006`).

Proof: `tests/test_ontology.py` (`CONN-CAMUNDA-MCP-R007`).
