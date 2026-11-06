# camunda-mcp tool catalog

Every Operaton / Camunda 7 engine REST operation, grouped by REST area: tool,
verb and path. Camunda 8 and knowledge-graph tools at the end.

## Authorization

| Tool | Call | Summary |
|---|---|---|
| `camunda7_create_authorization` | `POST /authorization/create` | Create a New Authorization |
| `camunda7_delete_authorization` | `DELETE /authorization/{id}` | Delete Authorization |
| `camunda7_get_authorization` | `GET /authorization/{id}` | Get Authorization |
| `camunda7_get_authorization_count` | `GET /authorization/count` | Get Authorization Count |
| `camunda7_is_user_authorized` | `GET /authorization/check` | Perform an Authorization Check |
| `camunda7_query_authorizations` | `GET /authorization` | Get Authorizations |
| `camunda7_update_authorization` | `PUT /authorization/{id}` | Update an Authorization |

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

## Decision Definition

| Tool | Call | Summary |
|---|---|---|
| `camunda7_evaluate_decision_by_id` | `POST /decision-definition/{id}/evaluate` | Evaluate By Id |
| `camunda7_evaluate_decision_by_key` | `POST /decision-definition/key/{key}/evaluate` | Evaluate By Key |
| `camunda7_evaluate_decision_by_key_and_tenant` | `POST /decision-definition/key/{key}/tenant-id/{tenant-id}/evaluate` | Evaluate By Key And Tenant |
| `camunda7_get_decision_definition_by_id` | `GET /decision-definition/{id}` | Get Decision Definition By Id |
| `camunda7_get_decision_definition_by_key` | `GET /decision-definition/key/{key}` | Get Decision Definition By Key |
| `camunda7_get_decision_definition_by_key_and_tenant_id` | `GET /decision-definition/key/{key}/tenant-id/{tenant-id}` | Get Decision Definition By Key And Tenant Id |
| `camunda7_get_decision_definition_diagram` | `GET /decision-definition/{id}/diagram` | Get Diagram |
| `camunda7_get_decision_definition_diagram_by_key` | `GET /decision-definition/key/{key}/diagram` | Get Diagram By Key |
| `camunda7_get_decision_definition_diagram_by_key_and_tenant` | `GET /decision-definition/key/{key}/tenant-id/{tenant-id}/diagram` | Get Diagram By Key And Tenant |
| `camunda7_get_decision_definition_dmn_xml_by_id` | `GET /decision-definition/{id}/xml` | Get XML By Id |
| `camunda7_get_decision_definition_dmn_xml_by_key` | `GET /decision-definition/key/{key}/xml` | Get XML By Key |
| `camunda7_get_decision_definition_dmn_xml_by_key_and_tenant` | `GET /decision-definition/key/{key}/tenant-id/{tenant-id}/xml` | Get XML By Key and Tenant |
| `camunda7_get_decision_definitions` | `GET /decision-definition` | Get List |
| `camunda7_get_decision_definitions_count` | `GET /decision-definition/count` | Get List Count |
| `camunda7_update_history_time_to_live_by_decision_definition_id` | `PUT /decision-definition/{id}/history-time-to-live` | Update History Time to Live |
| `camunda7_update_history_time_to_live_by_decision_definition_key` | `PUT /decision-definition/key/{key}/history-time-to-live` | Update History Time to Live By Key |
| `camunda7_update_history_time_to_live_by_decision_definition_key_and_tenant` | `PUT /decision-definition/key/{key}/tenant-id/{tenant-id}/history-time-to-live` | Update History Time to Live By Key And Tenant |

## Decision Requirements Definition

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_decision_requirements_definition_by_id` | `GET /decision-requirements-definition/{id}` | Get Decision Requirements Definition by ID |
| `camunda7_get_decision_requirements_definition_by_key` | `GET /decision-requirements-definition/key/{key}` | Get Decision Requirements Definition by Key |
| `camunda7_get_decision_requirements_definition_by_key_and_tenant_id` | `GET /decision-requirements-definition/key/{key}/tenant-id/{tenant-id}` | Get Decision Requirements Definition by Key and Tenant ID |
| `camunda7_get_decision_requirements_definition_diagram_by_id` | `GET /decision-requirements-definition/{id}/diagram` | Get Decision Requirements Diagram by ID |
| `camunda7_get_decision_requirements_definition_diagram_by_key` | `GET /decision-requirements-definition/key/{key}/diagram` | Get Decision Requirements Diagram by Key |
| `camunda7_get_decision_requirements_definition_diagram_by_key_and_tenant_id` | `GET /decision-requirements-definition/key/{key}/tenant-id/{tenant-id}/diagram` | Get Decision Requirements Diagram by Key and Tenant ID |
| `camunda7_get_decision_requirements_definition_dmn_xml_by_id` | `GET /decision-requirements-definition/{id}/xml` | Get DMN XML by ID |
| `camunda7_get_decision_requirements_definition_dmn_xml_by_key` | `GET /decision-requirements-definition/key/{key}/xml` | Get DMN XML by Key |
| `camunda7_get_decision_requirements_definition_dmn_xml_by_key_and_tenant_id` | `GET /decision-requirements-definition/key/{key}/tenant-id/{tenant-id}/xml` | Get DMN XML by Key and Tenant ID |
| `camunda7_get_decision_requirements_definitions` | `GET /decision-requirements-definition` | Get Decision Requirements Definitions |
| `camunda7_get_decision_requirements_definitions_count` | `GET /decision-requirements-definition/count` | Get Decision Requirements Definition Count |

## Deployment

| Tool | Call | Summary |
|---|---|---|
| `camunda7_create_deployment` | `POST /deployment/create` | Create |
| `camunda7_delete_deployment` | `DELETE /deployment/{id}` | Delete |
| `camunda7_get_deployment` | `GET /deployment/{id}` | Get |
| `camunda7_get_deployment_resource` | `GET /deployment/{id}/resources/{resourceId}` | Get Resource |
| `camunda7_get_deployment_resource_data` | `GET /deployment/{id}/resources/{resourceId}/data` | Get Resource (Binary) |
| `camunda7_get_deployment_resources` | `GET /deployment/{id}/resources` | Get Resources |
| `camunda7_get_deployments` | `GET /deployment` | Get List |
| `camunda7_get_deployments_count` | `GET /deployment/count` | Get List Count |
| `camunda7_get_registered_deployments` | `GET /deployment/registered` | Get Registered Deployments |
| `camunda7_redeploy` | `POST /deployment/{id}/redeploy` | Redeploy |

## Engine

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_process_engine_names` | `GET /engine` | Get List |

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

## External Task

| Tool | Call | Summary |
|---|---|---|
| `camunda7_complete_external_task_resource` | `POST /external-task/{id}/complete` | Complete |
| `camunda7_extend_lock` | `POST /external-task/{id}/extendLock` | Extend Lock |
| `camunda7_fetch_and_lock` | `POST /external-task/fetchAndLock` | Fetch and Lock |
| `camunda7_get_external_task` | `GET /external-task/{id}` | Get |
| `camunda7_get_external_task_error_details` | `GET /external-task/{id}/errorDetails` | Get Error Details |
| `camunda7_get_external_tasks` | `GET /external-task` | Get List |
| `camunda7_get_external_tasks_count` | `GET /external-task/count` | Get List Count |
| `camunda7_get_topic_names` | `GET /external-task/topic-names` | Get External Task Topic Names |
| `camunda7_handle_external_task_bpmn_error` | `POST /external-task/{id}/bpmnError` | Handle BPMN Error |
| `camunda7_handle_failure` | `POST /external-task/{id}/failure` | Handle Failure |
| `camunda7_lock` | `POST /external-task/{id}/lock` |  |
| `camunda7_query_external_tasks` | `POST /external-task` | Get List (POST) |
| `camunda7_query_external_tasks_count` | `POST /external-task/count` | Get List Count (POST) |
| `camunda7_set_external_task_resource_priority` | `PUT /external-task/{id}/priority` | Set Priority |
| `camunda7_set_external_task_resource_retries` | `PUT /external-task/{id}/retries` | Set Retries |
| `camunda7_set_external_task_retries` | `PUT /external-task/retries` | Set Retries Sync |
| `camunda7_set_external_task_retries_async_operation` | `POST /external-task/retries-async` | Set Retries Async |
| `camunda7_unlock` | `POST /external-task/{id}/unlock` | Unlock |

## Filter

| Tool | Call | Summary |
|---|---|---|
| `camunda7_create_filter` | `POST /filter/create` | Create Filter |
| `camunda7_delete_filter` | `DELETE /filter/{id}` | Delete Filter |
| `camunda7_execute_filter_count` | `GET /filter/{id}/count` | Execute Filter Count |
| `camunda7_execute_filter_list` | `GET /filter/{id}/list` | Execute Filter List |
| `camunda7_execute_filter_single_result` | `GET /filter/{id}/singleResult` | Execute Filter Single Result |
| `camunda7_get_filter_count` | `GET /filter/count` | Get Filter Count |
| `camunda7_get_filter_list` | `GET /filter` | Get Filters |
| `camunda7_get_single_filter` | `GET /filter/{id}` | Get Single Filter |
| `camunda7_post_execute_filter_count` | `POST /filter/{id}/count` | Execute Filter Count (POST) |
| `camunda7_post_execute_filter_list` | `POST /filter/{id}/list` | Execute Filter List (POST) |
| `camunda7_post_execute_filter_single_result` | `POST /filter/{id}/singleResult` | Execute Filter Single Result (POST) |
| `camunda7_update_filter` | `PUT /filter/{id}` | Update Filter |

## Group

| Tool | Call | Summary |
|---|---|---|
| `camunda7_create_group` | `POST /group/create` | Create Group |
| `camunda7_create_group_member` | `PUT /group/{id}/members/{userId}` | Create Group Member |
| `camunda7_delete_group` | `DELETE /group/{id}` | Delete Group |
| `camunda7_delete_group_member` | `DELETE /group/{id}/members/{userId}` | Delete a Group Member |
| `camunda7_get_group` | `GET /group/{id}` | Get Group |
| `camunda7_get_group_count` | `GET /group/count` | Get List Count |
| `camunda7_get_query_groups` | `GET /group` | Get List |
| `camunda7_post_query_groups` | `POST /group` | Get List (POST) |
| `camunda7_query_group_count` | `POST /group/count` | Get List Count (POST) |
| `camunda7_update_group` | `PUT /group/{id}` | Update Group |

## Historic Activity Instance

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_historic_activity_instance` | `GET /history/activity-instance/{id}` | Get |
| `camunda7_get_historic_activity_instances` | `GET /history/activity-instance` | Get List |
| `camunda7_get_historic_activity_instances_count` | `GET /history/activity-instance/count` | Get List Count |
| `camunda7_query_historic_activity_instances` | `POST /history/activity-instance` | Get List (POST) |
| `camunda7_query_historic_activity_instances_count` | `POST /history/activity-instance/count` | Get List Count (POST) |

## Historic Batch

| Tool | Call | Summary |
|---|---|---|
| `camunda7_delete_historic_batch` | `DELETE /history/batch/{id}` | Delete Historic Batch |
| `camunda7_get_cleanable_historic_batches_report` | `GET /history/batch/cleanable-batch-report` | Get Cleanable Batch Report |
| `camunda7_get_cleanable_historic_batches_report_count` | `GET /history/batch/cleanable-batch-report/count` | Get Cleanable Batch Report Count |
| `camunda7_get_historic_batch` | `GET /history/batch/{id}` | Get Historic Batch |
| `camunda7_get_historic_batches` | `GET /history/batch` | Get Historic Batches |
| `camunda7_get_historic_batches_count` | `GET /history/batch/count` | Get Historic Batch Count |
| `camunda7_set_removal_time_async_historic_batch` | `POST /history/batch/set-removal-time` | Set Removal Time Async (POST) |

## Historic Decision Definition

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_cleanable_historic_decision_instance_report` | `GET /history/decision-definition/cleanable-decision-instance-report` | Get Cleanable Decision Instance Report |
| `camunda7_get_cleanable_historic_decision_instance_report_count` | `GET /history/decision-definition/cleanable-decision-instance-report/count` | Get Cleanable Decision Instance Report Count |

## Historic Decision Instance

| Tool | Call | Summary |
|---|---|---|
| `camunda7_delete_async` | `POST /history/decision-instance/delete` | Delete Async (POST) |
| `camunda7_get_historic_decision_instance` | `GET /history/decision-instance/{id}` | Get Historic Decision Instance |
| `camunda7_get_historic_decision_instances` | `GET /history/decision-instance` | Get Historic Decision Instances |
| `camunda7_get_historic_decision_instances_count` | `GET /history/decision-instance/count` | Get Historic Decision Instance Count |
| `camunda7_set_removal_time_async_historic_decision_instance` | `POST /history/decision-instance/set-removal-time` | Set Removal Time Async (POST) |

## Historic Decision Requirements Definition

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_decision_statistics` | `GET /history/decision-requirements-definition/{id}/statistics` | Get DRD Statistics |

## Historic Detail

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_historic_details` | `GET /history/detail` | Get Historic Details |
| `camunda7_get_historic_details_count` | `GET /history/detail/count` | Get Historic Detail Count |
| `camunda7_historic_detail` | `GET /history/detail/{id}` | Get Historic Detail |
| `camunda7_historic_detail_binary` | `GET /history/detail/{id}/data` | Get Historic Detail (Binary) |
| `camunda7_query_historic_details` | `POST /history/detail` | Get Historic Details (POST) |

## Historic External Task Log

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_error_details_historic_external_task_log` | `GET /history/external-task-log/{id}/error-details` | Get External Task Log Error Details |
| `camunda7_get_historic_external_task_log` | `GET /history/external-task-log/{id}` | Get External Task Log |
| `camunda7_get_historic_external_task_logs` | `GET /history/external-task-log` | Get External Task Logs |
| `camunda7_get_historic_external_task_logs_count` | `GET /history/external-task-log/count` | Get External Task Log Count |
| `camunda7_query_historic_external_task_logs` | `POST /history/external-task-log` | Get External Task Logs (POST) |
| `camunda7_query_historic_external_task_logs_count` | `POST /history/external-task-log/count` | Get External Task Log Count (POST) |

## Historic Identity Link Log

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_historic_identity_links` | `GET /history/identity-link-log` | Get Identity Link Logs |
| `camunda7_get_historic_identity_links_count` | `GET /history/identity-link-log/count` | Get Identity Link Log Count |

## Historic Incident

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_historic_incidents` | `GET /history/incident` | Get Incidents |
| `camunda7_get_historic_incidents_count` | `GET /history/incident/count` | Get Incident Count |

## Historic Job Log

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_historic_job_log` | `GET /history/job-log/{id}` | Get Job Log |
| `camunda7_get_historic_job_logs` | `GET /history/job-log` | Get Job Logs |
| `camunda7_get_historic_job_logs_count` | `GET /history/job-log/count` | Get Job Log Count |
| `camunda7_get_stacktrace_historic_job_log` | `GET /history/job-log/{id}/stacktrace` | Get Job Log Exception Stacktrace |
| `camunda7_query_historic_job_logs` | `POST /history/job-log` | Get Job Logs (POST) |
| `camunda7_query_historic_job_logs_count` | `POST /history/job-log/count` | Get Job Log Count (POST) |

## Historic Process Definition

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_cleanable_historic_process_instance_report` | `GET /history/process-definition/cleanable-process-instance-report` | Get Cleanable Process Instance Report |
| `camunda7_get_cleanable_historic_process_instance_report_count` | `GET /history/process-definition/cleanable-process-instance-report/count` | Get Cleanable Process Instance Report Count |
| `camunda7_get_historic_activity_statistics` | `GET /history/process-definition/{id}/statistics` | Get Historic Activity Statistics |

## Historic Process Instance

| Tool | Call | Summary |
|---|---|---|
| `camunda7_delete_historic_process_instance` | `DELETE /history/process-instance/{id}` | Delete |
| `camunda7_delete_historic_process_instances_async` | `POST /history/process-instance/delete` | Delete Async (POST) |
| `camunda7_delete_historic_variable_instances_of_historic_process_instance` | `DELETE /history/process-instance/{id}/variable-instances` | Delete Variable Instances |
| `camunda7_get_historic_process_instance` | `GET /history/process-instance/{id}` | Get |
| `camunda7_get_historic_process_instance_duration_report` | `GET /history/process-instance/report` | Get Duration Report |
| `camunda7_get_historic_process_instances` | `GET /history/process-instance` | Get List |
| `camunda7_get_historic_process_instances_count` | `GET /history/process-instance/count` | Get List Count |
| `camunda7_query_historic_process_instances` | `POST /history/process-instance` | Get List (POST) |
| `camunda7_query_historic_process_instances_count` | `POST /history/process-instance/count` | Get List Count (POST) |
| `camunda7_set_removal_time_async` | `POST /history/process-instance/set-removal-time` | Set Removal Time Async (POST) |

## Historic Task Instance

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_historic_task_instance_report` | `GET /history/task/report` | Get Task Report (Historic) |
| `camunda7_get_historic_task_instances` | `GET /history/task` | Get Tasks (Historic) |
| `camunda7_get_historic_task_instances_count` | `GET /history/task/count` | Get Task Count |
| `camunda7_query_historic_task_instances` | `POST /history/task` | Get Tasks (Historic) (POST) |
| `camunda7_query_historic_task_instances_count` | `POST /history/task/count` | Get Task Count (POST) |

## Historic User Operation Log

| Tool | Call | Summary |
|---|---|---|
| `camunda7_clear_annotation_user_operation_log` | `PUT /history/user-operation/{operationId}/clear-annotation` | Clear Annotation of an User Operation Log (Historic) |
| `camunda7_query_user_operation_count` | `GET /history/user-operation/count` | Get User Operation Log Count |
| `camunda7_query_user_operation_entries` | `GET /history/user-operation` | Get User Operation Log (Historic) |
| `camunda7_set_annotation_user_operation_log` | `PUT /history/user-operation/{operationId}/set-annotation` | Set Annotation to an User Operation Log (Historic) |

## Historic Variable Instance

| Tool | Call | Summary |
|---|---|---|
| `camunda7_delete_historic_variable_instance` | `DELETE /history/variable-instance/{id}` | Delete Variable Instance |
| `camunda7_get_historic_variable_instance` | `GET /history/variable-instance/{id}` | Get Variable Instance |
| `camunda7_get_historic_variable_instance_binary` | `GET /history/variable-instance/{id}/data` | Get Variable Instance (Binary) |
| `camunda7_get_historic_variable_instances` | `GET /history/variable-instance` | Get Variable Instances |
| `camunda7_get_historic_variable_instances_count` | `GET /history/variable-instance/count` | Get Variable Instance Count |
| `camunda7_query_historic_variable_instances` | `POST /history/variable-instance` | Get Variable Instances (POST) |
| `camunda7_query_historic_variable_instances_count` | `POST /history/variable-instance/count` | Get Variable Instance Count (POST) |

## History Cleanup

| Tool | Call | Summary |
|---|---|---|
| `camunda7_cleanup_async` | `POST /history/cleanup` | Clean up history (POST) |
| `camunda7_find_cleanup_job` | `GET /history/cleanup/job` | Find clean up history job (GET) |
| `camunda7_find_cleanup_jobs` | `GET /history/cleanup/jobs` | Find clean up history jobs (GET) |
| `camunda7_get_history_cleanup_configuration` | `GET /history/cleanup/configuration` | Get History Cleanup Configuration |

## Identity

| Tool | Call | Summary |
|---|---|---|
| `camunda7_check_password` | `POST /identity/password-policy` | Validate Password |
| `camunda7_get_group_info` | `GET /identity/groups` | Get a User's Groups |
| `camunda7_get_password_policy` | `GET /identity/password-policy` | Get Password Policy |
| `camunda7_verify_user` | `POST /identity/verify` | Verify User |

## Incident

| Tool | Call | Summary |
|---|---|---|
| `camunda7_clear_incident_annotation` | `DELETE /incident/{id}/annotation` | Clear Incident Annotation |
| `camunda7_get_incident` | `GET /incident/{id}` | Get Incident |
| `camunda7_get_incidents` | `GET /incident` | Get List |
| `camunda7_get_incidents_count` | `GET /incident/count` | Get List Count |
| `camunda7_resolve_incident` | `DELETE /incident/{id}` | Resolve Incident |
| `camunda7_set_incident_annotation` | `PUT /incident/{id}/annotation` | Set Incident Annotation |

## Job

| Tool | Call | Summary |
|---|---|---|
| `camunda7_delete_job` | `DELETE /job/{id}` | Delete Job |
| `camunda7_execute_job` | `POST /job/{id}/execute` | Execute Job |
| `camunda7_get_job` | `GET /job/{id}` | Get Job |
| `camunda7_get_jobs` | `GET /job` | Get Jobs |
| `camunda7_get_jobs_count` | `GET /job/count` | Get Job Count |
| `camunda7_get_stacktrace` | `GET /job/{id}/stacktrace` | Get Exception Stacktrace |
| `camunda7_query_jobs` | `POST /job` | Get Jobs (POST) |
| `camunda7_query_jobs_count` | `POST /job/count` | Get Job Count (POST) |
| `camunda7_recalculate_duedate` | `POST /job/{id}/duedate/recalculate` | Recalculate Job Due Date |
| `camunda7_set_job_duedate` | `PUT /job/{id}/duedate` | Set Job Due Date |
| `camunda7_set_job_priority` | `PUT /job/{id}/priority` | Set Job Priority |
| `camunda7_set_job_retries` | `PUT /job/{id}/retries` | Set Job Retries |
| `camunda7_set_job_retries_async_operation` | `POST /job/retries` | Set Job Retries Async (POST) |
| `camunda7_update_job_suspension_state` | `PUT /job/{id}/suspended` | Activate/Suspend Job By Id |
| `camunda7_update_suspension_state_by` | `PUT /job/suspended` | Activate/Suspend Jobs |

## Job Definition

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_job_definition` | `GET /job-definition/{id}` | Get Job Definition |
| `camunda7_get_job_definitions` | `GET /job-definition` | Get Job Definitions |
| `camunda7_get_job_definitions_count` | `GET /job-definition/count` | Get Job Definition Count |
| `camunda7_query_job_definitions` | `POST /job-definition` | Get Job Definitions (POST) |
| `camunda7_query_job_definitions_count` | `POST /job-definition/count` | Get Job Definition Count (POST) |
| `camunda7_set_job_priority_job_definition` | `PUT /job-definition/{id}/jobPriority` | Set Job Definition Priority by Id |
| `camunda7_set_job_retries_job_definition` | `PUT /job-definition/{id}/retries` | Set Job Retries By Job Definition Id |
| `camunda7_update_suspension_state_job_definition` | `PUT /job-definition/{id}/suspended` | Activate/Suspend Job Definition By Id |
| `camunda7_update_suspension_state_job_definitions` | `PUT /job-definition/suspended` | Activate/Suspend Job Definitions |

## Message

| Tool | Call | Summary |
|---|---|---|
| `camunda7_deliver_message` | `POST /message` | Correlate |

## Metrics

| Tool | Call | Summary |
|---|---|---|
| `camunda7_delete_task_metrics` | `DELETE /metrics/task-worker` | Delete Task Worker Metrics |
| `camunda7_get_metrics` | `GET /metrics/{metrics-name}/sum` | Get Sum |
| `camunda7_interval` | `GET /metrics` | Get Metrics in Interval |

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

## Schema Log

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_schema_log` | `GET /schema/log` | Get List |
| `camunda7_query_schema_log` | `POST /schema/log` | Get List (POST) |

## Signal

| Tool | Call | Summary |
|---|---|---|
| `camunda7_throw_signal` | `POST /signal` | Event |

## Task

| Tool | Call | Summary |
|---|---|---|
| `camunda7_claim` | `POST /task/{id}/claim` | Claim |
| `camunda7_complete` | `POST /task/{id}/complete` | Complete |
| `camunda7_create_task` | `POST /task/create` | Create |
| `camunda7_delegate_task` | `POST /task/{id}/delegate` | Delegate |
| `camunda7_delete_task` | `DELETE /task/{id}` | Delete |
| `camunda7_get_deployed_form` | `GET /task/{id}/deployed-form` | Get Deployed Form |
| `camunda7_get_form` | `GET /task/{id}/form` | Get Form Key |
| `camunda7_get_form_variables` | `GET /task/{id}/form-variables` | Get Task Form Variables |
| `camunda7_get_rendered_form` | `GET /task/{id}/rendered-form` | Get Rendered Form |
| `camunda7_get_task` | `GET /task/{id}` | Get |
| `camunda7_get_task_count_by_candidate_group` | `GET /task/report/candidate-group-count` | Get Task Count By Candidate Group |
| `camunda7_get_tasks` | `GET /task` | Get List |
| `camunda7_get_tasks_count` | `GET /task/count` | Get List Count |
| `camunda7_handle_bpmn_error` | `POST /task/{id}/bpmnError` | Handle BPMN Error |
| `camunda7_handle_escalation` | `POST /task/{id}/bpmnEscalation` | Handle BPMN Escalation |
| `camunda7_query_tasks` | `POST /task` | Get List (POST) |
| `camunda7_query_tasks_count` | `POST /task/count` | Get List Count (POST) |
| `camunda7_resolve` | `POST /task/{id}/resolve` | Resolve |
| `camunda7_set_assignee` | `POST /task/{id}/assignee` | Set Assignee |
| `camunda7_submit` | `POST /task/{id}/submit-form` | Submit Form |
| `camunda7_unclaim` | `POST /task/{id}/unclaim` | Unclaim |
| `camunda7_update_task` | `PUT /task/{id}` | Update |

## Task Attachment

| Tool | Call | Summary |
|---|---|---|
| `camunda7_add_attachment` | `POST /task/{id}/attachment/create` | Create |
| `camunda7_delete_attachment` | `DELETE /task/{id}/attachment/{attachmentId}` | Delete |
| `camunda7_get_attachment` | `GET /task/{id}/attachment/{attachmentId}` | Get |
| `camunda7_get_attachment_data` | `GET /task/{id}/attachment/{attachmentId}/data` | Get (Binary) |
| `camunda7_get_attachments` | `GET /task/{id}/attachment` | Get List |

## Task Comment

| Tool | Call | Summary |
|---|---|---|
| `camunda7_create_comment` | `POST /task/{id}/comment/create` | Create |
| `camunda7_delete_task_comment` | `DELETE /task/{id}/comment/{commentId}` | Delete |
| `camunda7_delete_task_comments` | `DELETE /task/{id}/comment` | Delete Task Comments |
| `camunda7_get_comment` | `GET /task/{id}/comment/{commentId}` | Get |
| `camunda7_get_comments` | `GET /task/{id}/comment` | Get List |
| `camunda7_update_task_comment` | `PUT /task/{id}/comment` | Update |

## Task Identity Link

| Tool | Call | Summary |
|---|---|---|
| `camunda7_add_identity_link` | `POST /task/{id}/identity-links` | Add |
| `camunda7_delete_identity_link` | `POST /task/{id}/identity-links/delete` | Delete |
| `camunda7_get_identity_links` | `GET /task/{id}/identity-links` | Get List |

## Task Local Variable

| Tool | Call | Summary |
|---|---|---|
| `camunda7_delete_task_local_variable` | `DELETE /task/{id}/localVariables/{varName}` | Delete Local Task Variable |
| `camunda7_get_task_local_variable` | `GET /task/{id}/localVariables/{varName}` | Get Local Task Variable |
| `camunda7_get_task_local_variable_binary` | `GET /task/{id}/localVariables/{varName}/data` | Get Local Task Variable (Binary) |
| `camunda7_get_task_local_variables` | `GET /task/{id}/localVariables` | Get Local Task Variables |
| `camunda7_modify_task_local_variables` | `POST /task/{id}/localVariables` | Update/Delete Local Task Variables |
| `camunda7_put_task_local_variable` | `PUT /task/{id}/localVariables/{varName}` | Update Local Task Variable |
| `camunda7_set_binary_task_local_variable` | `POST /task/{id}/localVariables/{varName}/data` | Update Local Task Variable (Binary) |

## Task Variable

| Tool | Call | Summary |
|---|---|---|
| `camunda7_delete_task_variable` | `DELETE /task/{id}/variables/{varName}` | Delete Task Variable |
| `camunda7_get_task_variable` | `GET /task/{id}/variables/{varName}` | Get Task Variable |
| `camunda7_get_task_variable_binary` | `GET /task/{id}/variables/{varName}/data` | Get Task Variable (Binary) |
| `camunda7_get_task_variables` | `GET /task/{id}/variables` | Get Task Variables |
| `camunda7_modify_task_variables` | `POST /task/{id}/variables` | Update/Delete Task Variables |
| `camunda7_put_task_variable` | `PUT /task/{id}/variables/{varName}` | Update Task Variable |
| `camunda7_set_binary_task_variable` | `POST /task/{id}/variables/{varName}/data` | Update Task Variable (Binary) |

## Telemetry

| Tool | Call | Summary |
|---|---|---|
| `camunda7_configure_telemetry` | `POST /telemetry/configuration` | Configure Telemetry |
| `camunda7_get_telemetry_configuration` | `GET /telemetry/configuration` | Fetch Telemetry Configuration |
| `camunda7_get_telemetry_data` | `GET /telemetry/data` | Fetch Telemetry Data |

## Tenant

| Tool | Call | Summary |
|---|---|---|
| `camunda7_create_group_membership` | `PUT /tenant/{id}/group-members/{groupId}` | Create Tenant Group Membership |
| `camunda7_create_tenant` | `POST /tenant/create` | Create Tenant |
| `camunda7_create_user_membership` | `PUT /tenant/{id}/user-members/{userId}` | Create Tenant User Membership |
| `camunda7_delete_group_membership` | `DELETE /tenant/{id}/group-members/{groupId}` | Create Tenant Group Membership |
| `camunda7_delete_tenant` | `DELETE /tenant/{id}` | Delete Tenant |
| `camunda7_delete_user_membership` | `DELETE /tenant/{id}/user-members/{userId}` | Delete a Tenant User Membership |
| `camunda7_get_tenant` | `GET /tenant/{id}` | Get Tenant |
| `camunda7_get_tenant_count` | `GET /tenant/count` | Get Tenant Count |
| `camunda7_query_tenants` | `GET /tenant` | Get Tenants |
| `camunda7_update_tenant` | `PUT /tenant/{id}` | Update Tenant |

## User

| Tool | Call | Summary |
|---|---|---|
| `camunda7_create_user` | `POST /user/create` | Create |
| `camunda7_delete_user` | `DELETE /user/{id}` | Delete |
| `camunda7_get_user_count` | `GET /user/count` | Get List Count |
| `camunda7_get_user_profile` | `GET /user/{id}/profile` | Get Profile |
| `camunda7_get_users` | `GET /user` | Get List |
| `camunda7_unlock_user` | `POST /user/{id}/unlock` | Unlock User |
| `camunda7_update_credentials` | `PUT /user/{id}/credentials` | Update Credentials |
| `camunda7_update_profile` | `PUT /user/{id}/profile` | Update User Profile |

## Variable Instance

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_variable_instance` | `GET /variable-instance/{id}` | Get Variable Instance |
| `camunda7_get_variable_instance_binary` | `GET /variable-instance/{id}/data` | Get Variable Instance (Binary) |
| `camunda7_get_variable_instances` | `GET /variable-instance` | Get Variable Instances |
| `camunda7_get_variable_instances_count` | `GET /variable-instance/count` | Get Variable Instance Count |
| `camunda7_query_variable_instances` | `POST /variable-instance` | Get Variable Instances (POST) |
| `camunda7_query_variable_instances_count` | `POST /variable-instance/count` | Get Variable Instance Count (POST) |

## Version

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_rest_api_version` | `GET /version` | Get Rest API version |

## Camunda 8 (Zeebe, Operate, Tasklist REST)

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

## Knowledge graph

- `camunda_ingest_processes`: mirror definitions and instances into the knowledge graph.
