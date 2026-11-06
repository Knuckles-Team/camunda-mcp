---
name: camunda-run-and-monitor-instance
skill_type: skill
description: >-
  Run and monitor business process instances on the Operaton / Camunda 7 engine
  through camunda-mcp: start an instance with a business key and typed variables,
  read and change its variables, see where it is and what it already did, work
  its service tasks as an external-task worker, deliver messages and signals, and
  read its history. Use when the agent must kick off a business process, push it
  forward or report on it. Do NOT use to deploy models (use
  camunda-deploy-business-process), for human approvals (use
  camunda-work-human-task-queue) or to repair a failed instance (use
  camunda-incident-recovery).
license: MIT
tags: [camunda, operaton, bpmn, process-instance, external-task, monitoring]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# Run and monitor an instance

Contracts: `start-process-instance`, `set-instance-variables`,
`monitor-process-instance`, `work-external-tasks`, `correlate-message`,
`broadcast-signal`. Data locations: `process-runtime`, `process-history`.

## Variables

Every variable is typed: `{"amount": {"value": 250.0, "type": "Double"}}`. Types:
String, Integer, Long, Double, Boolean, Date (`2026-11-06T10:00:00.000+0000`),
Json (value is a JSON string, `"valueInfo": {"serializationDataFormat":
"application/json"}`). Query filters take plain values; booleans may be passed
as true/false, the connector sends them as the engine expects.

## Start

1. `camunda7_get_process_definition_by_key(key=...)`: exists and not suspended.
2. `camunda7_start_process_instance_by_key(key=..., body={"businessKey":
   "<business record id>", "variables": {...}})`. Use the business record's id
   (invoice number, order id) as the business key: it is how the instance is
   found again and joined to the record in other systems.

## Change variables

- `camunda7_get_process_instance_variables(id=...)`
- `camunda7_modify_process_instance_variables(id=..., body={"modifications": {...},
  "deletions": ["name"]})` or `camunda7_set_process_instance_variable(id=...,
  var_name=..., body={"value": ..., "type": ...})`.

## Monitor

- Running: `camunda7_get_process_instances(business_key=...)`,
  `camunda7_get_process_instance(id=...)`.
- Where it waits: `camunda7_get_activity_instance_tree(id=...)` (the active
  activity ids), plus open work: `camunda7_get_tasks(process_instance_id=...)`,
  `camunda7_get_external_tasks(process_instance_id=...)`,
  `camunda7_get_jobs(process_instance_id=...)` (timers).
- Stuck: `camunda7_get_incidents(process_instance_id=...)`; if any, switch to
  camunda-incident-recovery.
- Finished or not: `camunda7_get_historic_process_instance(id=...)` gives `state`
  (ACTIVE, COMPLETED, EXTERNALLY_TERMINATED, INTERNALLY_TERMINATED) and duration.
- Path taken: `camunda7_get_historic_activity_instances(process_instance_id=...,
  sort_by="startTime", sort_order="asc")`; values over time:
  `camunda7_get_historic_variable_instances(process_instance_id=...)`.
- Portfolio view: `camunda7_get_process_definition_statistics(incidents=true)`.

## Work service tasks (agent worker)

A service task with `operaton:type="external" operaton:topic="T"` waits for a worker.

1. `camunda7_fetch_and_lock(body={"workerId": "<agent id>", "maxTasks": 1,
   "topics": [{"topicName": "T", "lockDuration": 300000}]})` returns the locked
   tasks with their variables and business key.
2. Do the work. Longer than the lock? `camunda7_extend_lock(id=..., body={"workerId":
   ..., "newDuration": 300000})`.
3. Then exactly one of:
   - success: `camunda7_complete_external_task_resource(id=..., body={"workerId":
     ..., "variables": {...}})`;
   - technical failure: `camunda7_handle_failure(id=..., body={"workerId": ...,
     "errorMessage": ..., "retries": <left>, "retryTimeout": 60000})` (at 0 retries
     the engine raises an incident);
   - business outcome the model handles: `camunda7_handle_external_task_bpmn_error(
     id=..., body={"workerId": ..., "errorCode": ...})`.

## Messages and signals

- `camunda7_deliver_message(body={"messageName": ..., "businessKey": ...,
  "processVariables": {...}, "resultEnabled": true})`: exactly one waiting
  instance must match, else HTTP 400.
- `camunda7_throw_signal(body={"name": ..., "variables": {...}})` reaches every
  waiting instance.

## Guardrails

- Cancelling an instance (`camunda7_delete_process_instance`) or modifying its
  token position (`camunda7_modify_process_instance`) needs approval.
- Report the instance id and business key with every result.
