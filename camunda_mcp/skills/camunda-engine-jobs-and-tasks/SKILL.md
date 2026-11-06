---
name: camunda-engine-jobs-and-tasks
skill_type: skill
description: >-
  Jobs, external tasks, user tasks and incidents. Use when the request is about job retries and definitions, external-task workers, user-task comments, attachments, variables and identity links, or incident records. Do NOT use for the business workflows covered by camunda-deploy-business-process, camunda-run-and-monitor-instance, camunda-work-human-task-queue and camunda-incident-recovery.
license: MIT
tags: [camunda, operaton, engine-rest]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# Jobs, external tasks, user tasks and incidents

Every operation here is its own typed `camunda7_<operation>` tool; arguments follow the engine REST API
(path parameters are required, query filters are snake_case optional arguments, a JSON request body is the
`body` argument). Read first (get, query, count), change second, and ask for approval before any delete,
suspend, migration or modification: those tools take `confirm=true` once the approval was given.


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
