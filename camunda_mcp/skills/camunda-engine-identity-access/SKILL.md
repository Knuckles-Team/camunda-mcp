---
name: camunda-engine-identity-access
skill_type: skill
description: >-
  Identity, users, groups, tenants and authorizations of the engine. Use when the request is about who may do what in the engine: users and groups, memberships, tenants, authorizations and authorization checks. Do NOT use for the business workflows covered by camunda-deploy-business-process, camunda-run-and-monitor-instance, camunda-work-human-task-queue and camunda-incident-recovery.
license: MIT
tags: [camunda, operaton, engine-rest]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# Identity, users, groups, tenants and authorizations of the engine

Every operation here is its own typed `camunda7_<operation>` tool; arguments follow the engine REST API
(path parameters are required, query filters are snake_case optional arguments, a JSON request body is the
`body` argument). Read first (get, query, count), change second, and ask for approval before any delete,
suspend, migration or modification: those tools take `confirm=true` once the approval was given.


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

## Identity

| Tool | Call | Summary |
|---|---|---|
| `camunda7_check_password` | `POST /identity/password-policy` | Validate Password |
| `camunda7_get_group_info` | `GET /identity/groups` | Get a User's Groups |
| `camunda7_get_password_policy` | `GET /identity/password-policy` | Get Password Policy |
| `camunda7_verify_user` | `POST /identity/verify` | Verify User |

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
