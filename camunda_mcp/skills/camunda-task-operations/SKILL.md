---
name: camunda-task-operations
skill_type: skill
description: >-
  Human user-task lifecycle on Camunda 7 (Engine REST) and Camunda 8 (Tasklist)
  via the camunda-mcp MCP server — list/filter the task inbox, claim/unclaim,
  assign, read/set task variables, and complete tasks with the domain-typed
  camunda_task tool. Use when the agent must work an approval queue, assign work
  to a user, or complete a user task with output variables. Do NOT use for
  deploying or starting processes (use camunda-process-orchestration) or for
  external-task workers, jobs, and incidents (use camunda-incident-recovery).
license: MIT
tags: [camunda, user-task, tasklist, workflow, mcp]
metadata:
  author: Genius
  version: '0.1.0'
---
# Camunda Task Operations

Domain-typed access to Camunda **user tasks** — the human work items in a running
process — across Camunda 7 (Engine REST `task`) and Camunda 8 (Tasklist). Prefer
this tool over raw calls; it maps to `:Task` nodes assigned to a `:Person`.

## When to use
- List / filter the task inbox (by `assignee`, `processInstanceId`, `candidateGroup`…).
- Claim or unclaim a task for a user.
- Assign a task to a specific user.
- Read the variables visible from a task; set/modify task variables.
- Complete a task, passing the output variables that drive the next step.

## When NOT to use
- Deploying, starting, suspending, or cancelling processes/instances →
  `camunda-process-orchestration`.
- External-task worker fetch-and-lock/complete, jobs, retries, incidents →
  `camunda-incident-recovery`.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`camunda-mcp`** MCP server. Same
`CAMUNDA7_*` / `CAMUNDA8_*` variables as `camunda-process-orchestration`; for v8 the
Tasklist surface needs `CAMUNDA8_TASKLIST_URL` (+ client-credentials). `MCP_TOOL_MODE`
selects the condensed vs. verbose surface.

## Tools & actions
| Tool | Platform | Actions |
|------|----------|---------|
| `camunda_task` | v7 | `list`, `get`, `claim`, `unclaim`, `assign`, `complete`, `variables`, `set_variables` |
| `camunda_task` | v8 | `list`, `get`, `assign`, `unassign`, `complete`, `variables` |

### Key parameters (`params_json`)
- `task_id` — required for everything except `list`.
- `user_id` — required for v7 `claim` / `assign`.
- `variables` — object (v7) or list `[{"name":..,"value":..}]` (v8) for `complete`.
- v7 `list` accepts engine task-filter fields (`assignee`, `candidateGroup`,
  `processDefinitionKey`, `processInstanceId`, `sortBy`, `maxResults`).

## Recipes (`params_json`)
List the inbox for one assignee (v7):
```json
{"assignee":"jdoe","sortBy":"created","sortOrder":"desc","maxResults":25}
```
Claim a task (v7 action `claim`):
```json
{"task_id":"<task_id>","user_id":"jdoe"}
```
Complete a task with output variables (v7 action `complete`):
```json
{"task_id":"<task_id>","variables":{"approved":{"value":true,"type":"Boolean"}}}
```
Complete a Camunda 8 task (platform `8`, action `complete`):
```json
{"task_id":"<task_id>","variables":[{"name":"approved","value":true}]}
```

## Gotchas
- `params_json` is a **string** of JSON — serialize it.
- v7 vs v8 differ: v7 `complete` variables are a **typed object**
  (`{"value":..,"type":..}`); v8 wants a **list** of `{"name":..,"value":..}`.
- Claiming a task that is already assigned fails on v7 — `unclaim` first, or use
  `assign` to reassign.
- A task only completes if all **required** variables/forms are satisfied; the engine
  rejects otherwise.
- `list` with no filter can return a large inbox — always scope by assignee/group
  and cap `maxResults`.

## Related
- `camunda-process-orchestration` — the definitions/instances these tasks live in.
- `camunda-incident-recovery` — when a task's downstream service job fails.
- User tasks map to `:Task` nodes (`:assignedTo` a `:Person`, `:partOfInstance`) in
  the knowledge graph.
