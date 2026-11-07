---
name: camunda-incident-recovery
skill_type: skill
description: >-
  Diagnose and recover stuck process instances on the Operaton / Camunda 7 engine
  through camunda-mcp: find incidents, read the failing job's stack trace or the
  external task's error details, fix the cause, give the job or external task new
  retries, annotate the incident, and confirm the instance moves on. Use when an
  instance is blocked by a failed job, a failed external task or an incident. Do
  NOT use for deploying (camunda-deploy-business-process), starting or monitoring
  (camunda-run-and-monitor-instance) or human tasks (camunda-work-human-task-queue).
license: MIT
tags: [camunda, operaton, incident, jobs, external-task, recovery]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# Incident recovery

Contract: `recover-incident`. Data location: `process-runtime`. Incidents are
`:CamundaIncident` nodes linked to their `:ProcessInstance` by `:hasIncident`.

## 1. Find

- `camunda7_get_incidents(process_instance_id=...)`, or by type:
  `incident_type="failedJob"` / `"failedExternalTask"`. Unfiltered lists are large
  on a busy engine; scope by instance, definition (`process_definition_key_in`) or
  activity (`activity_id`).
- Portfolio: `camunda7_get_process_definition_statistics(incidents=true)`.

Each incident has `incidentType`, `activityId`, `incidentMessage` and
`configuration` (the failed job id, or the external task id).

## 2. Read the cause

- failedJob: `camunda7_get_stacktrace(id=<configuration>)`;
  `camunda7_get_job(id=...)` shows retries and due date.
- failedExternalTask: `camunda7_get_external_task_error_details(id=<configuration>)`;
  `camunda7_get_external_task(id=...)` shows the worker and topic.
- Context: `camunda7_get_process_instance_variables(id=<processInstanceId>)`.

## 3. Fix, then retry

Fix the cause first (wrong variable: `camunda7_modify_process_instance_variables`;
a down dependency: wait for it). Then:

- failedJob: `camunda7_set_job_retries(id=<job>, body={"retries": 1})`; the job
  executor runs it again, or run it now with `camunda7_execute_job(id=<job>)`.
- failedExternalTask: `camunda7_set_external_task_resource_retries(id=<task>,
  body={"retries": 1})`; the worker fetches it again.
- Many at once: `camunda7_set_job_retries_async_operation` /
  `camunda7_set_external_task_retries` with a filter (needs approval).

Raising retries above 0 is what clears the incident; `camunda7_resolve_incident`
only works for custom incident types and does not re-run anything.

## 4. Record and confirm

- `camunda7_set_incident_annotation(id=<incident>, body={"annotation": "<cause and fix>"})`.
- Confirm: `camunda7_get_incidents(process_instance_id=...)` is empty and
  `camunda7_get_activity_instance_tree(id=...)` has moved past the failed activity.
- History: `camunda7_get_historic_incidents(process_instance_id=...)`.

## Lifecycle moves and refusals

Read the state with `camunda7_get_process_instance` (or `camunda7_get_historic_process_instance`)
and `camunda7_get_tasks` before you act. A process instance is Created, Active,
Suspended, Incident (a sub-state of Active), Completed, Canceled or Terminated;
the last three are terminal. Legal moves: suspend from Active or Incident,
activate from Suspended, cancel or terminate (`camunda7_delete_process_instance`)
from Active, Suspended or Incident. A user task is Created, Claimed, Completed,
Canceled or Deleted: claim from Created, unclaim or complete from Claimed, and
only the assignee completes. An illegal move is refused with `ILLEGAL_TRANSITION`
before any engine call, carrying the reason: `IllegalEdge`, `TerminalState`,
`AlreadyClaimed`, `NotClaimed`, `ClaimedByOther`, `NoActingIdentity` or
`UnknownEngineState`. Read the reason, fix the state, do not retry the same call.

## Guardrails

- Never cancel an instance, delete a job or skip an activity
  (`camunda7_modify_process_instance`) to clear an incident without approval.
- Do not set retries again on a failure whose cause is not fixed; it fails again
  and raises a new incident.
