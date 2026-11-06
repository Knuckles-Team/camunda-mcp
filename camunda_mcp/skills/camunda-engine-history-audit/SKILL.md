---
name: camunda-engine-history-audit
skill_type: skill
description: >-
  History, audit, metrics and engine health. Use when the request is about what already happened or how the engine is doing: historic instances, tasks, variables, jobs, incidents, user-operation logs, history cleanup, metrics, telemetry, schema log, version and engine names. Do NOT use for the business workflows covered by camunda-deploy-business-process, camunda-run-and-monitor-instance, camunda-work-human-task-queue and camunda-incident-recovery.
license: MIT
tags: [camunda, operaton, engine-rest]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# History, audit, metrics and engine health

Every operation here is its own typed `camunda7_<operation>` tool; arguments follow the engine REST API
(path parameters are required, query filters are snake_case optional arguments, a JSON request body is the
`body` argument). Read first (get, query, count), change second, and ask for approval before any delete,
suspend, migration or modification: those tools take `confirm=true` once the approval was given.


## Engine

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_process_engine_names` | `GET /engine` | Get List |

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

## Metrics

| Tool | Call | Summary |
|---|---|---|
| `camunda7_delete_task_metrics` | `DELETE /metrics/task-worker` | Delete Task Worker Metrics |
| `camunda7_get_metrics` | `GET /metrics/{metrics-name}/sum` | Get Sum |
| `camunda7_interval` | `GET /metrics` | Get Metrics in Interval |

## Schema Log

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_schema_log` | `GET /schema/log` | Get List |
| `camunda7_query_schema_log` | `POST /schema/log` | Get List (POST) |

## Telemetry

| Tool | Call | Summary |
|---|---|---|
| `camunda7_configure_telemetry` | `POST /telemetry/configuration` | Configure Telemetry |
| `camunda7_get_telemetry_configuration` | `GET /telemetry/configuration` | Fetch Telemetry Configuration |
| `camunda7_get_telemetry_data` | `GET /telemetry/data` | Fetch Telemetry Data |

## Version

| Tool | Call | Summary |
|---|---|---|
| `camunda7_get_rest_api_version` | `GET /version` | Get Rest API version |
