---
name: camunda-process-orchestration
skill_type: skill
description: >-
  Orchestrate BPMN processes on Camunda 7 (Engine REST) and Camunda 8
  (Zeebe/Operate) via the camunda-mcp MCP server — deploy BPMN/DMN resources,
  list and inspect process definitions, start process instances with variables,
  and query/suspend/cancel running instances with the domain-typed tools. Use
  when the agent must deploy a process, kick off a workflow, or inspect the state
  of definitions and running instances. Do NOT use for human user-task work
  (claim/assign/complete) — use camunda-task-operations; or for failed jobs and
  incidents — use camunda-incident-recovery.
license: MIT
tags: [camunda, bpmn, process, workflow, zeebe, mcp]
metadata:
  author: Genius
  version: '0.1.0'
---
# Camunda Process Orchestration

Domain-typed access to Camunda **process definitions**, **instances**, and
**deployments** across Camunda 7 (Engine REST) and Camunda 8 (Zeebe/Operate).
Prefer these tools over raw HTTP — they select the platform client and return
process-shaped records.

## When to use
- Deploy a BPMN/DMN/form resource to the engine.
- List / read process definitions (by `id` or shared `key`), or fetch their BPMN XML.
- Start a process instance (with `variables` / `businessKey`).
- List, inspect, suspend, or cancel/delete running instances; read/modify instance variables.
- Mirror definitions & instances into the knowledge graph as `:BusinessProcess` / `:ProcessInstance`.

## When NOT to use
- Human user-task lifecycle (claim/assign/complete) → `camunda-task-operations`.
- Failed jobs, retries, and incidents → `camunda-incident-recovery`.
- External-task worker fetch/complete → the `camunda7_fetch_and_lock` / `camunda7_complete_external_task` tools directly.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`camunda-mcp`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `CAMUNDA_PLATFORM` | optional | `7` or `8` (default `7`) |
| `CAMUNDA7_URL` | for v7 | Engine REST base (default `http://localhost:8080/engine-rest`) |
| `CAMUNDA7_TOKEN` / `CAMUNDA7_USERNAME` / `CAMUNDA7_PASSWORD` | optional | bearer or basic auth |
| `CAMUNDA8_ZEEBE_REST_URL` | for v8 | Zeebe REST base |
| `CAMUNDA8_OPERATE_URL` / `CAMUNDA8_CLIENT_ID` / `CAMUNDA8_CLIENT_SECRET` / `CAMUNDA8_OAUTH_URL` | for v8 | Operate + client-credentials |
| `CAMUNDA_SSL_VERIFY` | optional | TLS verification toggle |

## Tools & actions
One tool per API operation, named `camunda7_<operation>` (Engine REST) or
`camunda8_<operation>` (Zeebe/Operate REST); arguments are the operation's typed
parameters (query filters as a `params` object, request bodies as `body`).

| Tool | Purpose |
|------|---------|
| `camunda7_list_process_definitions`, `camunda7_get_process_definition`, `camunda7_get_process_definition_xml`, `camunda7_get_process_definition_statistics`, `camunda7_suspend_process_definition` | v7 process definitions |
| `camunda7_start_process_instance` | v7: start an instance (by `id` or `key`, with `body`) |
| `camunda7_list_process_instances`, `camunda7_get_process_instance`, `camunda7_delete_process_instance`, `camunda7_suspend_process_instance` | v7 instances |
| `camunda7_get_process_instance_variables`, `camunda7_modify_process_instance_variables` | v7 instance variables |
| `camunda7_list_deployments`, `camunda7_get_deployment`, `camunda7_delete_deployment` | v7 deployments |
| `camunda8_search_process_definitions`, `camunda8_search_process_instances`, `camunda8_get_process_instance`, `camunda8_get_process_instance_statistics` | v8 definitions and instances |
| `camunda8_create_process_instance`, `camunda8_create_process_instance_with_result`, `camunda8_cancel_process_instance` | v8: start and cancel |
| `camunda_deploy` | (takes `resource_name` + `resource_content`) deploy BPMN/DMN/form |
| `camunda_ingest_processes` | native KG ingest of definitions (+instances) |

## Recipes (arguments)
List the latest version of each definition (`camunda7_list_process_definitions`):
```json
{"params":{"latestVersion": true}}
```
Start an instance by key with variables + business key (`camunda7_start_process_instance`):
```json
{"key":"invoice","body":{"businessKey":"INV-42","variables":{"amount":{"value":1200,"type":"Double"}}}}
```
Fetch the BPMN XML of a definition (`camunda7_get_process_definition_xml`):
```json
{"key":"invoice"}
```
Cancel a running Camunda 8 instance (`camunda8_cancel_process_instance`):
```json
{"key":"2251799813685249"}
```
Deploy a BPMN file (`camunda_deploy`): pass `resource_name="invoice.bpmn"` and the
XML as `resource_content`; v7 also takes `{"deployment_name":"invoice"}` in `params_json`.

## Gotchas
- Query filters are a `params` object; request bodies are a `body` object.
- v7 `get_process_definition`, `get_process_definition_xml` and `start_process_instance` accept **either** `{"id":..}` (a specific version) **or**
  `{"key":..}` (the latest version) — id wins if both are given.
- Camunda 7 process-definition **ids** look like `invoice:1:abc-def` (`key:version:deployId`);
  the stable cross-version handle is the `key`.
- v7 start variables are **typed**: `{"value":.., "type":"String|Double|Boolean|Json"}`.
- v8 keys are large numeric strings — keep them as strings, never coerce to int.
- Suspending a definition can optionally suspend all its instances (`include_instances`).

## Related
- `camunda-task-operations` — the human user-task half of the same processes.
- `camunda-incident-recovery` — jobs/incidents blocking these instances.
- `camunda_ingest_processes` natively mirrors definitions/instances into the KG
  (`:BusinessProcess` / `:ProcessInstance`, `agent-connector-sdk-source-integration`).
