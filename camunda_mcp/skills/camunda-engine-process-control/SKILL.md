---
name: camunda-engine-process-control
skill_type: skill
description: >-
  Process definitions, instances, executions, messages, signals, migration and modification. Use when the request is about controlling running processes beyond the basic start and monitor skills: suspend and activate, migrate or modify instances, correlate messages, throw signals, evaluate conditions, run batches. Do NOT use for the business workflows covered by camunda-deploy-business-process, camunda-run-and-monitor-instance, camunda-work-human-task-queue and camunda-incident-recovery.
license: MIT
tags: [camunda, operaton, engine-rest]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# Process definitions, instances, executions, messages, signals, migration and modification

Every operation here is its own typed `camunda7_<operation>` tool; arguments follow the engine REST API
(path parameters are required, query filters are snake_case optional arguments, a JSON request body is the
`body` argument). Read first (get, query, count), change second, and ask for approval before any delete,
suspend, migration or modification: those tools take `confirm=true` once the approval was given.


## Batch

| Tool | Call | Summary |
|---|---|---|
| `camunda7_delete_batch` | `DELETE /batch/{id}` | Delete |
| `camunda7_get_batch` | `GET /batch/{id}` | Get |
| `camunda7_get_batch_statistics` | `GET /batch/statistics` | Get Statistics |
| `camunda7_get_batch_statistics_count` | `GET /batch/statistics/count` | Get Statistics Count |
| `camunda7_get_batches` | `GET /batch` | Get List |
| `camunda7_get_batches_count` | `GET /batch/count` | Get List Count |
| `camunda7_update_batch_suspension_state` | `PUT /batch/{id}/suspended` | Activate/Suspend |

## Condition

| Tool | Call | Summary |
|---|---|---|
| `camunda7_evaluate_condition` | `POST /condition` | Evaluate |

## Event Subscription

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_event_subscriptions` | `GET /event-subscription` | Get List |
| `camunda7_get_event_subscriptions_count` | `GET /event-subscription/count` | Get List Count |

## Execution

| Tool | Call | Summary |
|---|---|---|
| `camunda7_create_incident` | `POST /execution/{id}/create-incident` | Create Incident |
| `camunda7_delete_local_execution_variable` | `DELETE /execution/{id}/localVariables/{varName}` | Delete Local Execution Variable |
| `camunda7_get_execution` | `GET /execution/{id}` | Get Execution |
| `camunda7_get_executions` | `GET /execution` | Get Executions |
| `camunda7_get_executions_count` | `GET /execution/count` | Get Execution Count |
| `camunda7_get_local_execution_variable` | `GET /execution/{id}/localVariables/{varName}` | Get Local Execution Variable |
| `camunda7_get_local_execution_variable_binary` | `GET /execution/{id}/localVariables/{varName}/data` | Get Local Execution Variable (Binary) |
| `camunda7_get_local_execution_variables` | `GET /execution/{id}/localVariables` | Get Local Execution Variables |
| `camunda7_get_message_event_subscription` | `GET /execution/{id}/messageSubscriptions/{messageName}` | Get Message Event Subscription |
| `camunda7_modify_local_execution_variables` | `POST /execution/{id}/localVariables` | Update/Delete Local Execution Variables |
| `camunda7_put_local_execution_variable` | `PUT /execution/{id}/localVariables/{varName}` | Put Local Execution Variable |
| `camunda7_query_executions` | `POST /execution` | Get Executions (POST) |
| `camunda7_query_executions_count` | `POST /execution/count` | Get Execution Count (POST) |
| `camunda7_set_local_execution_variable_binary` | `POST /execution/{id}/localVariables/{varName}/data` | Post Local Execution Variable (Binary) |
| `camunda7_signal_execution` | `POST /execution/{id}/signal` | Trigger Execution |
| `camunda7_trigger_event` | `POST /execution/{id}/messageSubscriptions/{messageName}/trigger` | Trigger Message Event Subscription |

## Message

| Tool | Call | Summary |
|---|---|---|
| `camunda7_deliver_message` | `POST /message` | Correlate |

## Migration

| Tool | Call | Summary |
|---|---|---|
| `camunda7_execute_migration_plan` | `POST /migration/execute` | Execute Migration Plan |
| `camunda7_execute_migration_plan_async` | `POST /migration/executeAsync` | Execute Migration Plan Async (Batch) |
| `camunda7_generate_migration_plan` | `POST /migration/generate` | Generate Migration Plan |
| `camunda7_validate_migration_plan` | `POST /migration/validate` | Validate Migration Plan |

## Modification

| Tool | Call | Summary |
|---|---|---|
| `camunda7_execute_modification` | `POST /modification/execute` | Execute Modification |
| `camunda7_execute_modification_async` | `POST /modification/executeAsync` | Execute Modification Async (Batch) |

## Process Definition

| Tool | Call | Summary |
|---|---|---|
| `camunda7_delete_process_definition` | `DELETE /process-definition/{id}` | Delete |
| `camunda7_delete_process_definitions_by_key` | `DELETE /process-definition/key/{key}` | Delete By Key |
| `camunda7_delete_process_definitions_by_key_and_tenant_id` | `DELETE /process-definition/key/{key}/tenant-id/{tenant-id}` | Delete By Key |
| `camunda7_get_activity_statistics` | `GET /process-definition/{id}/statistics` | Get Activity Instance Statistics |
| `camunda7_get_activity_statistics_by_process_definition_key` | `GET /process-definition/key/{key}/statistics` | Get Activity Instance Statistics |
| `camunda7_get_activity_statistics_by_process_definition_key_and_tenant_id` | `GET /process-definition/key/{key}/tenant-id/{tenant-id}/statistics` | Get Activity Instance Statistics |
| `camunda7_get_deployed_start_form` | `GET /process-definition/{id}/deployed-start-form` | Get Deployed Start Form |
| `camunda7_get_deployed_start_form_by_key` | `GET /process-definition/key/{key}/deployed-start-form` | Get Deployed Start Form |
| `camunda7_get_deployed_start_form_by_key_and_tenant_id` | `GET /process-definition/key/{key}/tenant-id/{tenant-id}/deployed-start-form` | Get Deployed Start Form |
| `camunda7_get_latest_process_definition_by_tenant_id` | `GET /process-definition/key/{key}/tenant-id/{tenant-id}` | Get |
| `camunda7_get_process_definition` | `GET /process-definition/{id}` | Get |
| `camunda7_get_process_definition_bpmn20_xml` | `GET /process-definition/{id}/xml` | Get XML |
| `camunda7_get_process_definition_bpmn20_xml_by_key` | `GET /process-definition/key/{key}/xml` | Get XML |
| `camunda7_get_process_definition_bpmn20_xml_by_key_and_tenant_id` | `GET /process-definition/key/{key}/tenant-id/{tenant-id}/xml` | Get XML |
| `camunda7_get_process_definition_by_key` | `GET /process-definition/key/{key}` | Get |
| `camunda7_get_process_definition_diagram` | `GET /process-definition/{id}/diagram` | Get Diagram |
| `camunda7_get_process_definition_diagram_by_key` | `GET /process-definition/key/{key}/diagram` | Get Diagram |
| `camunda7_get_process_definition_diagram_by_key_and_tenant_id` | `GET /process-definition/key/{key}/tenant-id/{tenant-id}/diagram` | Get Diagram |
| `camunda7_get_process_definition_statistics` | `GET /process-definition/statistics` | Get Process Instance Statistics |
| `camunda7_get_process_definitions` | `GET /process-definition` | Get List |
| `camunda7_get_process_definitions_count` | `GET /process-definition/count` | Get List Count |
| `camunda7_get_rendered_start_form` | `GET /process-definition/{id}/rendered-form` | Get Rendered Start Form |
| `camunda7_get_rendered_start_form_by_key` | `GET /process-definition/key/{key}/rendered-form` | Get Rendered Start Form |
| `camunda7_get_rendered_start_form_by_key_and_tenant_id` | `GET /process-definition/key/{key}/tenant-id/{tenant-id}/rendered-form` | Get Rendered Start Form |
| `camunda7_get_start_form` | `GET /process-definition/{id}/startForm` | Get Start Form Key |
| `camunda7_get_start_form_by_key` | `GET /process-definition/key/{key}/startForm` | Get Start Form Key |
| `camunda7_get_start_form_by_key_and_tenant_id` | `GET /process-definition/key/{key}/tenant-id/{tenant-id}/startForm` | Get Start Form Key |
| `camunda7_get_start_form_variables` | `GET /process-definition/{id}/form-variables` | Get Start Form Variables |
| `camunda7_get_start_form_variables_by_key` | `GET /process-definition/key/{key}/form-variables` | Get Start Form Variables |
| `camunda7_get_start_form_variables_by_key_and_tenant_id` | `GET /process-definition/key/{key}/tenant-id/{tenant-id}/form-variables` | Get Start Form Variables |
| `camunda7_get_static_called_process_definitions` | `GET /process-definition/{id}/static-called-process-definitions` | Get Static Called Process Definitions |
| `camunda7_restart_process_instance` | `POST /process-definition/{id}/restart` | Restart Process Instance |
| `camunda7_restart_process_instance_async_operation` | `POST /process-definition/{id}/restart-async` | Restart Process Instance Async |
| `camunda7_start_process_instance` | `POST /process-definition/{id}/start` | Start Instance |
| `camunda7_start_process_instance_by_key` | `POST /process-definition/key/{key}/start` | Start Instance |
| `camunda7_start_process_instance_by_key_and_tenant_id` | `POST /process-definition/key/{key}/tenant-id/{tenant-id}/start` | Start Instance |
| `camunda7_submit_form` | `POST /process-definition/{id}/submit-form` | Submit Start Form |
| `camunda7_submit_form_by_key` | `POST /process-definition/key/{key}/submit-form` | Submit Start Form |
| `camunda7_submit_form_by_key_and_tenant_id` | `POST /process-definition/key/{key}/tenant-id/{tenant-id}/submit-form` | Submit Start Form |
| `camunda7_update_history_time_to_live_by_process_definition_id` | `PUT /process-definition/{id}/history-time-to-live` | Update History Time to Live |
| `camunda7_update_history_time_to_live_by_process_definition_key` | `PUT /process-definition/key/{key}/history-time-to-live` | Update History Time to Live |
| `camunda7_update_history_time_to_live_by_process_definition_key_and_tenant_id` | `PUT /process-definition/key/{key}/tenant-id/{tenant-id}/history-time-to-live` | Update History Time to Live |
| `camunda7_update_process_definition_suspension_state` | `PUT /process-definition/suspended` | Activate/Suspend By Key |
| `camunda7_update_process_definition_suspension_state_by_id` | `PUT /process-definition/{id}/suspended` | Activate/Suspend By Id |
| `camunda7_update_process_definition_suspension_state_by_key` | `PUT /process-definition/key/{key}/suspended` | Activate/Suspend by Id |
| `camunda7_update_process_definition_suspension_state_by_key_and_tenant_id` | `PUT /process-definition/key/{key}/tenant-id/{tenant-id}/suspended` | Activate/Suspend by Id |

## Process Instance

| Tool | Call | Summary |
|---|---|---|
| `camunda7_correlate_message_async_operation` | `POST /process-instance/message-async` | Correlate Message Async (POST) |
| `camunda7_delete_async_historic_query_based` | `POST /process-instance/delete-historic-query-based` | Delete Async Historic Query Based (POST) |
| `camunda7_delete_process_instance` | `DELETE /process-instance/{id}` | Delete |
| `camunda7_delete_process_instance_variable` | `DELETE /process-instance/{id}/variables/{varName}` | Delete Process Variable |
| `camunda7_delete_process_instances_async_operation` | `POST /process-instance/delete` | Delete Async (POST) |
| `camunda7_get_activity_instance_tree` | `GET /process-instance/{id}/activity-instances` | Get Activity Instance |
| `camunda7_get_process_instance` | `GET /process-instance/{id}` | Get Process Instance |
| `camunda7_get_process_instance_variable` | `GET /process-instance/{id}/variables/{varName}` | Get Process Variable |
| `camunda7_get_process_instance_variable_binary` | `GET /process-instance/{id}/variables/{varName}/data` | Get Process Variable (Binary) |
| `camunda7_get_process_instance_variables` | `GET /process-instance/{id}/variables` | Get Process Variables |
| `camunda7_get_process_instances` | `GET /process-instance` | Get List |
| `camunda7_get_process_instances_count` | `GET /process-instance/count` | Get List Count |
| `camunda7_modify_process_instance` | `POST /process-instance/{id}/modification` | Modify Process Instance Execution State |
| `camunda7_modify_process_instance_async_operation` | `POST /process-instance/{id}/modification-async` | Modify Process Instance Execution State Async |
| `camunda7_modify_process_instance_variables` | `POST /process-instance/{id}/variables` | Update/Delete Process Variables |
| `camunda7_query_process_instances` | `POST /process-instance` | Get List (POST) |
| `camunda7_query_process_instances_count` | `POST /process-instance/count` | Get List Count (POST) |
| `camunda7_set_process_instance_variable` | `PUT /process-instance/{id}/variables/{varName}` | Update Process Variable |
| `camunda7_set_process_instance_variable_binary` | `POST /process-instance/{id}/variables/{varName}/data` | Update Process Variable (Binary) |
| `camunda7_set_retries_by_process` | `POST /process-instance/job-retries` | Set Job Retries Async (POST) |
| `camunda7_set_retries_by_process_historic_query_based` | `POST /process-instance/job-retries-historic-query-based` | Set Job Retries Async Historic Query Based (POST) |
| `camunda7_set_variables_async_operation` | `POST /process-instance/variables-async` | Set Variables Async (POST) |
| `camunda7_update_suspension_state` | `PUT /process-instance/suspended` | Activate/Suspend In Group |
| `camunda7_update_suspension_state_async_operation` | `POST /process-instance/suspended-async` | Activate/Suspend In Batch |
| `camunda7_update_suspension_state_by_id` | `PUT /process-instance/{id}/suspended` | Activate/Suspend Process Instance By Id |

## Process Instance Comment

| Tool | Call | Summary |
|---|---|---|
| `camunda7_delete_process_instance_comment` | `DELETE /process-instance/{id}/comment/{commentId}` | Delete |
| `camunda7_delete_process_instance_comments` | `DELETE /process-instance/{id}/comment` | Delete ProcessInstance Comments |
| `camunda7_get_process_instance_comments` | `GET /process-instance/{id}/comment` | Get Process Instance Comments |
| `camunda7_update_process_instance_comment` | `PUT /process-instance/{id}/comment` | Update |

## Signal

| Tool | Call | Summary |
|---|---|---|
| `camunda7_throw_signal` | `POST /signal` | Event |

## Variable Instance

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_variable_instance` | `GET /variable-instance/{id}` | Get Variable Instance |
| `camunda7_get_variable_instance_binary` | `GET /variable-instance/{id}/data` | Get Variable Instance (Binary) |
| `camunda7_get_variable_instances` | `GET /variable-instance` | Get Variable Instances |
| `camunda7_get_variable_instances_count` | `GET /variable-instance/count` | Get Variable Instance Count |
| `camunda7_query_variable_instances` | `POST /variable-instance` | Get Variable Instances (POST) |
| `camunda7_query_variable_instances_count` | `POST /variable-instance/count` | Get Variable Instance Count (POST) |
