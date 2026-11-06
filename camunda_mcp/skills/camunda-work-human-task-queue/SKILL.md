---
name: camunda-work-human-task-queue
skill_type: skill
description: >-
  Work the human task queue of the Operaton / Camunda 7 engine through
  camunda-mcp: list the open approvals, reviews and data-entry tasks for a user or
  group, claim one, read its context, record a comment, complete it with typed
  outputs, or hand it over (unclaim, reassign, delegate). Use when a process waits
  on a person or an agent acting for one. Do NOT use to start processes (use
  camunda-run-and-monitor-instance) or for automated service-task work (external
  tasks, same skill).
license: MIT
tags: [camunda, operaton, user-task, approval, tasklist, human-in-the-loop]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# Work the human task queue

Contracts: `work-human-task-queue`, `hand-over-human-task`. Data location:
`human-task-queue`.

## 1. Read the queue

- My open tasks: `camunda7_get_tasks(assignee=<user>)`.
- Tasks I may take: `camunda7_get_tasks(candidate_user=<user>)` or
  `camunda7_get_tasks(candidate_group=<group>)`; add `unassigned=true` for the
  unclaimed ones.
- Urgent first: `sort_by="dueDate", sort_order="asc"` (or `"priority"`, `"desc"`);
  `due_before=<date>` finds overdue ones.
- For one process: `process_instance_business_key=<business record id>`.

Each task has `id`, `name`, `taskDefinitionKey` (the BPMN user task id),
`processInstanceId`, `assignee`, `due`, `priority`.

## 2. Take and decide

1. `camunda7_claim(id=<task>, body={"userId": <user>})`. Fails (HTTP 500,
   "already claimed") when someone else holds it: pick another.
2. Context: `camunda7_get_task_variables(id=<task>)` (process data the task can see),
   `camunda7_get_form_variables(id=<task>)` (the fields the task's form expects).
3. Record why: `camunda7_create_comment(id=<task>, body={"message": "<reason>"})`.
4. `camunda7_complete(id=<task>, body={"variables": {"approved": {"value": true,
   "type": "Boolean"}}})`. The output variable names are those the process model's
   gateway conditions read (for example `approved`); check the model with
   `camunda7_get_process_definition_bpmn20_xml(id=<processDefinitionId>)` if unsure.

## 3. Hand over

- Give back: `camunda7_unclaim(id=...)`.
- Reassign: `camunda7_set_assignee(id=..., body={"userId": ...})`.
- Ask someone else and get it back: `camunda7_delegate_task(id=..., body={"userId":
  ...})`; the delegate finishes with `camunda7_resolve(id=..., body={"variables": ...})`.
- Who may work it: `camunda7_get_identity_links(id=...)`.

## Audit

`camunda7_get_historic_task_instances(process_instance_id=...)` shows who worked
each task, when, and how it ended (`deleteReason` = completed).

## Guardrails

- Complete only tasks assigned to the user you act for; never complete an
  approval without the decision of the person or rule that owns it.
- Never delete a task (`camunda7_delete_task`) that a process created.
