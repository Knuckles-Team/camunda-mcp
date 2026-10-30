---
name: camunda-incident-recovery
skill_type: skill
description: >-
  Diagnose and recover stuck Camunda processes on Camunda 7 (Engine REST) and
  Camunda 8 (Operate) via the camunda-mcp MCP server — list jobs and incidents,
  set job retries, execute jobs, resolve incidents, and drive external-task
  workers (fetch-and-lock / complete / failure / bpmn_error) with the per-operation
  camunda7_*/camunda8_* job, incident and external-task tools. Use when a process instance is
  blocked by a failed job, an incident, or a stalled external task. Do NOT use for
  starting/deploying processes (use camunda-process-orchestration) or human
  user-task work (use camunda-task-operations).
license: MIT
tags: [camunda, incident, jobs, external-task, operate, mcp]
metadata:
  author: Knuckles-Team
  version: '0.1.0'
---
# Camunda Incident Recovery

Domain-typed access to Camunda **jobs**, **incidents**, and **external tasks** —
the failure and async-execution surface that blocks running instances. Prefer these
tools over raw calls; incidents map to `:Incident` nodes on a `:ProcessInstance`.

## When to use
- List/inspect jobs and incidents; find why an instance is stuck.
- Bump a failed job's retries (`set_retries`) or force-execute a job.
- Resolve an incident once its root cause is fixed.
- Run an external-task worker loop: `fetch_and_lock`, then `complete` / report
  `failure` (with retries) / throw a `bpmn_error`.

## When NOT to use
- Deploying, starting, suspending processes/instances → `camunda-process-orchestration`.
- Human user-task claim/assign/complete → `camunda-task-operations`.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`camunda-mcp`** MCP server. Same
`CAMUNDA7_*` / `CAMUNDA8_*` variables as the other camunda skills; incident search on
v8 uses the Operate surface (`CAMUNDA8_OPERATE_URL`).

## Tools & actions
| Tool | Platform | Operation |
|------|----------|-----------|
| `camunda7_list_jobs`, `camunda7_execute_job`, `camunda7_set_job_retries` | v7 | list jobs, run a job, set retries |
| `camunda7_list_incidents`, `camunda7_get_incident`, `camunda7_resolve_incident` | v7 | incidents |
| `camunda7_fetch_and_lock`, `camunda7_complete_external_task`, `camunda7_handle_external_task_failure`, `camunda7_handle_external_task_bpmn_error` | v7 | external-task worker |
| `camunda8_activate_jobs`, `camunda8_complete_job`, `camunda8_fail_job`, `camunda8_update_job` | v8 | jobs |
| `camunda8_resolve_incident` | v8 | resolve an incident |
| `camunda8_search_incidents`, `camunda8_search_flownode_instances`, `camunda8_search_variables` | v8 | Operate search |

### Key parameters
- v7: `job_id`, `retries`, `incident_id`; filter bodies for `list_*`.
- v8: `job_key`, `incident_key`, `body`.
- external task: `fetch_and_lock` takes a full request body; others take
  `{"task_id":..,"body":{...}}`.

## Recipes (arguments)
Find incidents for a process instance (`camunda7_list_incidents`):
```json
{"params":{"processInstanceId":"<instance_id>"}}
```
Reset retries on a failed job so it runs again (`camunda7_set_job_retries`):
```json
{"job_id":"<job_id>","retries":3}
```
Resolve an incident after the fix (`camunda7_resolve_incident`):
```json
{"incident_id":"<incident_id>"}
```
Fetch-and-lock external tasks for a worker (`camunda7_fetch_and_lock`):
```json
{"body":{"workerId":"worker-1","maxTasks":10,"topics":[{"topicName":"charge-card","lockDuration":30000}]}}
```
Report an external-task failure with retries (`camunda7_handle_external_task_failure`):
```json
{"task_id":"<task_id>","body":{"workerId":"worker-1","errorMessage":"gateway timeout","retries":2,"retryTimeout":60000}}
```

## Gotchas
- Query filters are a `params` object; request bodies are a `body` object.
- Setting retries back above 0 is what makes a failed job **retryable**; resolving the
  incident alone does not re-run the job.
- External-task failure (`camunda7_handle_external_task_failure`) with `retries: 0` creates an **incident** (no more automatic
  retries) — usually intentional as a dead-letter.
- v8 uses **keys** (`job_key`, `incident_key`) — large numeric strings, keep as strings.
- Always scope `camunda7_list_jobs` / `camunda7_list_incidents` by process instance or definition; an
  unfiltered list on a busy engine is large.

## Related
- `camunda-process-orchestration` / `camunda-task-operations` — the rest of the process
  lifecycle these failures interrupt.
- Incidents map to `:Incident` (`:hasIncident` from `:ProcessInstance`) in the KG.
