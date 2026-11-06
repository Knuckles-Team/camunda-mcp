---
name: camunda-engine-decisions-deployments
skill_type: skill
description: >-
  Decisions, deployments and saved filters. Use when the request is about DMN decisions and decision requirements, deployed resources, or saved task filters. Do NOT use for the business workflows covered by camunda-deploy-business-process, camunda-run-and-monitor-instance, camunda-work-human-task-queue and camunda-incident-recovery.
license: MIT
tags: [camunda, operaton, engine-rest]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# Decisions, deployments and saved filters

Every operation here is its own typed `camunda7_<operation>` tool; arguments follow the engine REST API
(path parameters are required, query filters are snake_case optional arguments, a JSON request body is the
`body` argument). Read first (get, query, count), change second, and ask for approval before any delete,
suspend, migration or modification: those tools take `confirm=true` once the approval was given.


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
