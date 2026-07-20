# Camunda Process Orchestration

Orchestrate BPMN processes on Camunda 7 (Engine REST) and Camunda 8 (Zeebe/Operate) via the camunda-mcp MCP server — deploy BPMN/DMN resources, list and inspect process definitions, start process instances with variables, and query/suspend/cancel running instances with the domain-typed tools. Use when the agent must deploy a process, kick off a workflow, or inspect the state of definitions and running instances. Do NOT use for human user-task work (claim/assign/complete) — use camunda-task-operations; or for failed jobs and incidents — use camunda-incident-recovery.

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
- External-task worker fetch/complete → the `camunda_external_task` tool directly.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`camunda-mcp`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `CAMUNDA_PLATFORM` | optional | `7` or `8` (default `7`) |
| `CAMUNDA7_URL` | for v7 | Engine REST base (default `[configured-endpoint]`) |
| `CAMUNDA7_TOKEN` / `CAMUNDA7_USERNAME` / `CAMUNDA7_PASSWORD` | optional | bearer or basic auth |
| `CAMUNDA8_ZEEBE_REST_URL` | for v8 | Zeebe REST base |
| `CAMUNDA8_OPERATE_URL` / `CAMUNDA8_CLIENT_ID` / `CAMUNDA8_CLIENT_SECRET` / `CAMUNDA8_OAUTH_URL` | for v8 | Operate + client-credentials |
| `CAMUNDA_TLS_PROFILE` | optional | Named outbound TLS policy from AgentConfig |

`MCP_TOOL_MODE` (`condensed`|`verbose`|`both`) selects the condensed action-based
surface (used below) vs. one-to-one verbose tools.

## Tools & actions
Each tool takes an `action`, a `platform` (`7`/`8`), and a `params_json` **JSON string**.

| Tool | Actions |
|------|---------|
| `camunda_process` | v7: `list`, `get`, `xml`, `start`, `statistics`, `suspend`; v8: `list` |
| `camunda_instance` | v7: `list`, `get`, `delete`, `variables`, `set_variables`, `suspend`; v8: `list`, `get`, `statistics`, `cancel` |
| `camunda_deploy` | (takes `resource_name` + `resource_content`) deploy BPMN/DMN/form |
| `camunda_deployment` | v7: `list`, `get`, `delete` |
| `camunda_ingest_processes` | native KG ingest of definitions (+instances) |

## Recipes (`params_json`)
List the latest version of each definition (v7):
```json
{"latestVersion": true}
```
Start an instance by key with variables + business key (v7 `camunda_process` action `start`):
```json
{"key":"invoice","body":{"businessKey":"INV-42","variables":{"amount":{"value":1200,"type":"Double"}}}}
```
Fetch the BPMN XML of a definition (v7 action `xml`):
```json
{"key":"invoice"}
```
Cancel a running Camunda 8 instance (`camunda_instance` action `cancel`, platform `8`):
```json
{"key":"[REDACTED_CREDIT_CARD]"}
```
Deploy a BPMN file (`camunda_deploy`): pass `resource_name="invoice.bpmn"` and the
XML as `resource_content`; v7 also takes `{"deployment_name":"invoice"}` in `params_json`.

## Gotchas
- `params_json` is a **string** of JSON, not an object — serialize it.
- v7 `get`/`xml`/`start` accept **either** `{"id":..}` (a specific version) **or**
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
  (`:BusinessProcess` / `:ProcessInstance`, `agent-utilities-source-integration`).
