---
name: camunda-incident-recovery
skill_type: skill
description: >-
  Diagnose and recover stuck Camunda processes on Camunda 7 (Engine REST) and
  Camunda 8 (Operate) via the camunda-mcp MCP server — list jobs and incidents,
  set job retries, execute jobs, resolve incidents, and drive external-task
  workers (fetch-and-lock / complete / failure / bpmn_error) with the domain-typed
  camunda_job and camunda_external_task tools. Use when a process instance is
  blocked by a failed job, an incident, or a stalled external task. Do NOT use for
  starting/deploying processes (use camunda-process-orchestration) or human
  user-task work (use camunda-task-operations).
license: MIT
tags: [camunda, incident, jobs, external-task, operate, mcp]
metadata:
  author: Genius
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
v8 uses the Operate surface (`CAMUNDA8_OPERATE_URL`). `MCP_TOOL_MODE` selects the
condensed vs. verbose surface.

## Tools & actions
| Tool | Platform | Actions |
|------|----------|---------|
| `camunda_job` | v7 | `list_jobs`, `execute_job`, `set_retries`, `list_incidents`, `get_incident`, `resolve_incident` |
| `camunda_job` | v8 | `activate`, `complete`, `fail`, `update`, `resolve_incident` |
| `camunda_external_task` | v7 | `fetch_and_lock`, `complete`, `failure`, `bpmn_error` |
| `camunda_ops` | v8 | search `incidents` (Operate), `flownode_instances`, `variables` |

### Key parameters (`params_json`)
- v7: `job_id`, `retries`, `incident_id`; filter bodies for `list_*`.
- v8: `job_key`, `incident_key`, `body`.
- external task: `fetch_and_lock` takes a full request body; others take
  `{"task_id":..,"body":{...}}`.

## Recipes (`params_json`)
Find incidents for a process instance (v7 `list_incidents`):
```json
{"processInstanceId":"<instance_id>"}
```
Reset retries on a failed job so it runs again (v7 `set_retries`):
```json
{"job_id":"<job_id>","retries":3}
```
Resolve an incident after the fix (v7 `resolve_incident`):
```json
{"incident_id":"<incident_id>"}
```
Fetch-and-lock external tasks for a worker (v7 `camunda_external_task` `fetch_and_lock`):
```json
{"body":{"workerId":"worker-1","maxTasks":10,"topics":[{"topicName":"charge-card","lockDuration":30000}]}}
```
Report an external-task failure with retries (v7 `failure`):
```json
{"task_id":"<task_id>","body":{"workerId":"worker-1","errorMessage":"gateway timeout","retries":2,"retryTimeout":60000}}
```

## Gotchas
- `params_json` is a **string** of JSON — serialize it.
- Setting retries back above 0 is what makes a failed job **retryable**; resolving the
  incident alone does not re-run the job.
- External-task `failure` with `retries: 0` creates an **incident** (no more automatic
  retries) — usually intentional as a dead-letter.
- v8 uses **keys** (`job_key`, `incident_key`) — large numeric strings, keep as strings.
- Always scope `list_jobs` / `list_incidents` by process instance or definition; an
  unfiltered list on a busy engine is large.

## Related
- `camunda-process-orchestration` / `camunda-task-operations` — the rest of the process
  lifecycle these failures interrupt.
- Incidents map to `:Incident` (`:hasIncident` from `:ProcessInstance`) in the KG.
