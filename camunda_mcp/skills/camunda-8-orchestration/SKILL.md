---
name: camunda-8-orchestration
skill_type: skill
description: >-
  Run processes on a Camunda 8 cluster through camunda-mcp: deploy resources, create and cancel process instances, work jobs, publish messages, broadcast signals, resolve incidents and work user tasks over the Zeebe, Operate and Tasklist REST APIs. Use only when the target engine is Camunda 8; for the Operaton / Camunda 7 engine use the camunda7 skills.
license: MIT
tags: [camunda, camunda8, zeebe, operate, tasklist]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# Camunda 8 orchestration

- `camunda8_deploy_resources`
- `camunda8_create_process_instance`
- `camunda8_create_process_instance_with_result`
- `camunda8_cancel_process_instance`
- `camunda8_publish_message`
- `camunda8_broadcast_signal`
- `camunda8_activate_jobs`
- `camunda8_complete_job`
- `camunda8_fail_job`
- `camunda8_update_job`
- `camunda8_resolve_incident`
- `camunda8_search_process_definitions`
- `camunda8_search_process_instances`
- `camunda8_get_process_instance`
- `camunda8_get_process_instance_statistics`
- `camunda8_search_flownode_instances`
- `camunda8_search_variables`
- `camunda8_search_incidents`
- `camunda8_search_tasks`
- `camunda8_get_task`
- `camunda8_assign_task`
- `camunda8_unassign_task`
- `camunda8_complete_task`
- `camunda8_get_task_variables`

## Workflow

1. Deploy BPMN, DMN or forms with `camunda8_deploy_resources`, then start with `camunda8_create_process_instance` (or `camunda8_create_process_instance_with_result` to wait for the outcome).
2. Monitor with `camunda8_get_process_instance`, `camunda8_get_process_instance_statistics`, `camunda8_search_flownode_instances` and `camunda8_search_incidents`.
3. Work automated steps with `camunda8_activate_jobs`, `camunda8_complete_job` and `camunda8_fail_job`; deliver events with `camunda8_publish_message` and `camunda8_broadcast_signal`.
4. Work human steps with `camunda8_get_task`, `camunda8_get_task_variables`, `camunda8_assign_task` and `camunda8_complete_task`.
5. Recover with `camunda8_resolve_incident` once the cause is fixed; ask for approval before `camunda8_cancel_process_instance`.
