# CONN-CAMUNDA-MCP — Design and architecture

`camunda_mcp/mcp/mcp_camunda.py` registers only `camunda_deploy` and `camunda_ingest_processes`; the SDK `register_tool_surface` adds the 39 `camunda7_*` and 24 `camunda8_*` operation tools from the two API clients.

`camunda_mcp/__init__.py` carries `__version__`. `.bumpversion.cfg` lists that file next to `pyproject.toml` and the Dockerfile pin, so one bump updates all of them. A stale `__version__` is the failure this prevents: the released image identified itself with an old number although the package metadata was correct.
