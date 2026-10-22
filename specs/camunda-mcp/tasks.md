# CONN-CAMUNDA-MCP — Delivery tasks

- [ ] `CONN-CAMUNDA-MCP-R002` — Register only the per-operation tools plus `camunda_deploy` and `camunda_ingest_processes`; test the count of 65.
- [ ] `CONN-CAMUNDA-MCP-R003` — Remove the action-routing `camunda_*` tools; test that no tool carries the `split-action` tag.
- [x] `CONN-CAMUNDA-MCP-R001` — Track `__version__` in the bump configuration and test it against `pyproject.toml`.
