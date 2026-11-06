# CONN-CAMUNDA-MCP — Quickstart

The shortest path that shows the served behaviour working.

- `CONN-CAMUNDA-MCP-R002`, `CONN-CAMUNDA-MCP-R003`: run `pytest tests/test_tool_surface.py`.
- `CONN-CAMUNDA-MCP-R004`: run `pytest tests/test_wire_values.py`.
- `CONN-CAMUNDA-MCP-R005`, `CONN-CAMUNDA-MCP-R006`: run `pytest tests/test_surface_contracts.py`; read `ontology://camunda-mcp/contracts.ttl` and the prompt `camunda-process-operator` from the running server.
- `CONN-CAMUNDA-MCP-R007`: run `pytest tests/test_ontology.py`.
- Live scenario against an engine: deploy a BPMN with a user task and an external service task plus a DMN decision with `camunda7_create_deployment`, start it with `camunda7_start_process_instance_by_key`, set variables, `camunda7_claim` and `camunda7_complete` the user task, `camunda7_fetch_and_lock` and `camunda7_complete_external_task_resource` the service task, read `camunda7_get_historic_activity_instances`, evaluate with `camunda7_evaluate_decision_by_key`, then `camunda7_delete_deployment` with `cascade=true`.
