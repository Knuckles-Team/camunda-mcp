"""Operaton / Camunda 7 engine REST: the Task operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase
from camunda_mcp.lifecycle import TaskEvent, guarded


class Camunda7Task(ApiClientBase):
    """Task: 22 engine REST operation(s)."""

    @guarded("task", 7, TaskEvent.CLAIM)
    def claim(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Claim.

        Claims a task for a specific user. **Note:** The difference with the Set
        Assignee method is that here a check is performed to see if the task already
        has a user assigned to it. Request body: an object with userId.

        POST /task/{id}/claim
        """
        return self._call(
            "POST",
            "/task/{id}/claim",
            path={"id": id},
            body=body,
        )

    @guarded("task", 7, TaskEvent.COMPLETE)
    def complete(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Complete.

        Completes a task and updates process variables. Request body: an object with
        variables, withVariablesInReturn.

        POST /task/{id}/complete
        """
        return self._call(
            "POST",
            "/task/{id}/complete",
            path={"id": id},
            body=body,
        )

    def create_task(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Create.

        Creates a new task. Request body: an object with id, name, assignee, owner,
        created, lastUpdated, due, followUp, delegationState, description,
        executionId, parentTaskId, priority, processDefinitionId, processInstanceId,
        caseExecutionId, caseDefinitionId, caseInstanceId, taskDefinitionKey,
        suspended, formKey, operatonFormRef, tenantId, taskState.

        POST /task/create
        """
        return self._call(
            "POST",
            "/task/create",
            body=body,
        )

    def delegate_task(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Delegate.

        Delegates a task to another user. Request body: an object with userId.

        POST /task/{id}/delegate
        """
        return self._call(
            "POST",
            "/task/{id}/delegate",
            path={"id": id},
            body=body,
        )

    def delete_task(
        self,
        id: str,
    ) -> Any:
        """Delete.

        Removes a task by id.

        DELETE /task/{id}
        """
        return self._call(
            "DELETE",
            "/task/{id}",
            path={"id": id},
        )

    def get_deployed_form(
        self,
        id: str,
    ) -> Any:
        """Get Deployed Form.

        Retrieves the deployed form that is referenced from a given task. For
        further information please refer to the User Guide.

        GET /task/{id}/deployed-form
        """
        return self._call(
            "GET",
            "/task/{id}/deployed-form",
            path={"id": id},
        )

    def get_form(
        self,
        id: str,
    ) -> Any:
        """Get Form Key.

        Retrieves the form key for a task. The form key corresponds to the
        `FormData#formKey` property in the engine. This key can be used to do
        task-specific form rendering in client applications. Additionally, the
        context path of the containing process application is returned.

        GET /task/{id}/form
        """
        return self._call(
            "GET",
            "/task/{id}/form",
            path={"id": id},
        )

    def get_form_variables(
        self,
        id: str,
        *,
        variable_names: str | None = None,
        deserialize_values: bool | None = None,
    ) -> Any:
        """Get Task Form Variables.

        Retrieves the form variables for a task. The form variables take form data
        specified on the task into account. If form fields are defined, the variable
        types and default values of the form fields are taken into account.

        GET /task/{id}/form-variables
        """
        return self._call(
            "GET",
            "/task/{id}/form-variables",
            path={"id": id},
            params={
                "variableNames": variable_names,
                "deserializeValues": deserialize_values,
            },
        )

    def get_rendered_form(
        self,
        id: str,
    ) -> Any:
        """Get Rendered Form.

        Retrieves the rendered form for a task. This method can be used to get the
        HTML rendering of a Generated Task Form.

        GET /task/{id}/rendered-form
        """
        return self._call(
            "GET",
            "/task/{id}/rendered-form",
            path={"id": id},
        )

    def get_task(
        self,
        id: str,
    ) -> Any:
        """Get.

        Retrieves a task by id.

        GET /task/{id}
        """
        return self._call(
            "GET",
            "/task/{id}",
            path={"id": id},
        )

    def get_task_count_by_candidate_group(
        self,
    ) -> Any:
        """Get Task Count By Candidate Group.

        Retrieves the number of tasks for each candidate group.

        GET /task/report/candidate-group-count
        """
        return self._call(
            "GET",
            "/task/report/candidate-group-count",
        )

    def get_tasks(
        self,
        *,
        task_id: str | None = None,
        task_id_in: str | None = None,
        process_instance_id: str | None = None,
        process_instance_id_in: str | None = None,
        process_instance_business_key: str | None = None,
        process_instance_business_key_expression: str | None = None,
        process_instance_business_key_in: str | None = None,
        process_instance_business_key_like: str | None = None,
        process_instance_business_key_like_expression: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        process_definition_key_in: str | None = None,
        process_definition_name: str | None = None,
        process_definition_name_like: str | None = None,
        execution_id: str | None = None,
        case_instance_id: str | None = None,
        case_instance_business_key: str | None = None,
        case_instance_business_key_like: str | None = None,
        case_definition_id: str | None = None,
        case_definition_key: str | None = None,
        case_definition_name: str | None = None,
        case_definition_name_like: str | None = None,
        case_execution_id: str | None = None,
        activity_instance_id_in: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        assignee: str | None = None,
        assignee_expression: str | None = None,
        assignee_like: str | None = None,
        assignee_like_expression: str | None = None,
        assignee_in: str | None = None,
        assignee_not_in: str | None = None,
        owner: str | None = None,
        owner_expression: str | None = None,
        candidate_group: str | None = None,
        candidate_group_like: str | None = None,
        candidate_group_expression: str | None = None,
        candidate_user: str | None = None,
        candidate_user_expression: str | None = None,
        include_assigned_tasks: bool | None = None,
        involved_user: str | None = None,
        involved_user_expression: str | None = None,
        assigned: bool | None = None,
        unassigned: bool | None = None,
        task_definition_key: str | None = None,
        task_definition_key_in: str | None = None,
        task_definition_key_not_in: str | None = None,
        task_definition_key_like: str | None = None,
        name: str | None = None,
        name_not_equal: str | None = None,
        name_like: str | None = None,
        name_not_like: str | None = None,
        description: str | None = None,
        description_like: str | None = None,
        priority: int | None = None,
        max_priority: int | None = None,
        min_priority: int | None = None,
        due_date: str | None = None,
        due_date_expression: str | None = None,
        due_after: str | None = None,
        due_after_expression: str | None = None,
        due_before: str | None = None,
        due_before_expression: str | None = None,
        without_due_date: bool | None = None,
        follow_up_date: str | None = None,
        follow_up_date_expression: str | None = None,
        follow_up_after: str | None = None,
        follow_up_after_expression: str | None = None,
        follow_up_before: str | None = None,
        follow_up_before_expression: str | None = None,
        follow_up_before_or_not_existent: str | None = None,
        follow_up_before_or_not_existent_expression: str | None = None,
        created_on: str | None = None,
        created_on_expression: str | None = None,
        created_after: str | None = None,
        created_after_expression: str | None = None,
        created_before: str | None = None,
        created_before_expression: str | None = None,
        updated_after: str | None = None,
        updated_after_expression: str | None = None,
        delegation_state: str | None = None,
        candidate_groups: str | None = None,
        candidate_groups_expression: str | None = None,
        with_candidate_groups: bool | None = None,
        without_candidate_groups: bool | None = None,
        with_candidate_users: bool | None = None,
        without_candidate_users: bool | None = None,
        active: bool | None = None,
        suspended: bool | None = None,
        task_variables: str | None = None,
        process_variables: str | None = None,
        case_instance_variables: str | None = None,
        variable_names_ignore_case: bool | None = None,
        variable_values_ignore_case: bool | None = None,
        parent_task_id: str | None = None,
        with_comment_attachment_info: bool | None = None,
        with_task_variables_in_return: bool | None = None,
        with_task_local_variables_in_return: bool | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get List.

        Queries for tasks that fulfill a given filter. The size of the result set
        can be retrieved by using the Get Task Count method. **Security
        Consideration:** There are several query parameters (such as
        assigneeExpression) for specifying an EL expression. These are disabled by
        default to prevent remote code execution.

        GET /task
        """
        return self._call(
            "GET",
            "/task",
            params={
                "taskId": task_id,
                "taskIdIn": task_id_in,
                "processInstanceId": process_instance_id,
                "processInstanceIdIn": process_instance_id_in,
                "processInstanceBusinessKey": process_instance_business_key,
                "processInstanceBusinessKeyExpression": process_instance_business_key_expression,
                "processInstanceBusinessKeyIn": process_instance_business_key_in,
                "processInstanceBusinessKeyLike": process_instance_business_key_like,
                "processInstanceBusinessKeyLikeExpression": process_instance_business_key_like_expression,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "processDefinitionKeyIn": process_definition_key_in,
                "processDefinitionName": process_definition_name,
                "processDefinitionNameLike": process_definition_name_like,
                "executionId": execution_id,
                "caseInstanceId": case_instance_id,
                "caseInstanceBusinessKey": case_instance_business_key,
                "caseInstanceBusinessKeyLike": case_instance_business_key_like,
                "caseDefinitionId": case_definition_id,
                "caseDefinitionKey": case_definition_key,
                "caseDefinitionName": case_definition_name,
                "caseDefinitionNameLike": case_definition_name_like,
                "caseExecutionId": case_execution_id,
                "activityInstanceIdIn": activity_instance_id_in,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "assignee": assignee,
                "assigneeExpression": assignee_expression,
                "assigneeLike": assignee_like,
                "assigneeLikeExpression": assignee_like_expression,
                "assigneeIn": assignee_in,
                "assigneeNotIn": assignee_not_in,
                "owner": owner,
                "ownerExpression": owner_expression,
                "candidateGroup": candidate_group,
                "candidateGroupLike": candidate_group_like,
                "candidateGroupExpression": candidate_group_expression,
                "candidateUser": candidate_user,
                "candidateUserExpression": candidate_user_expression,
                "includeAssignedTasks": include_assigned_tasks,
                "involvedUser": involved_user,
                "involvedUserExpression": involved_user_expression,
                "assigned": assigned,
                "unassigned": unassigned,
                "taskDefinitionKey": task_definition_key,
                "taskDefinitionKeyIn": task_definition_key_in,
                "taskDefinitionKeyNotIn": task_definition_key_not_in,
                "taskDefinitionKeyLike": task_definition_key_like,
                "name": name,
                "nameNotEqual": name_not_equal,
                "nameLike": name_like,
                "nameNotLike": name_not_like,
                "description": description,
                "descriptionLike": description_like,
                "priority": priority,
                "maxPriority": max_priority,
                "minPriority": min_priority,
                "dueDate": due_date,
                "dueDateExpression": due_date_expression,
                "dueAfter": due_after,
                "dueAfterExpression": due_after_expression,
                "dueBefore": due_before,
                "dueBeforeExpression": due_before_expression,
                "withoutDueDate": without_due_date,
                "followUpDate": follow_up_date,
                "followUpDateExpression": follow_up_date_expression,
                "followUpAfter": follow_up_after,
                "followUpAfterExpression": follow_up_after_expression,
                "followUpBefore": follow_up_before,
                "followUpBeforeExpression": follow_up_before_expression,
                "followUpBeforeOrNotExistent": follow_up_before_or_not_existent,
                "followUpBeforeOrNotExistentExpression": follow_up_before_or_not_existent_expression,
                "createdOn": created_on,
                "createdOnExpression": created_on_expression,
                "createdAfter": created_after,
                "createdAfterExpression": created_after_expression,
                "createdBefore": created_before,
                "createdBeforeExpression": created_before_expression,
                "updatedAfter": updated_after,
                "updatedAfterExpression": updated_after_expression,
                "delegationState": delegation_state,
                "candidateGroups": candidate_groups,
                "candidateGroupsExpression": candidate_groups_expression,
                "withCandidateGroups": with_candidate_groups,
                "withoutCandidateGroups": without_candidate_groups,
                "withCandidateUsers": with_candidate_users,
                "withoutCandidateUsers": without_candidate_users,
                "active": active,
                "suspended": suspended,
                "taskVariables": task_variables,
                "processVariables": process_variables,
                "caseInstanceVariables": case_instance_variables,
                "variableNamesIgnoreCase": variable_names_ignore_case,
                "variableValuesIgnoreCase": variable_values_ignore_case,
                "parentTaskId": parent_task_id,
                "withCommentAttachmentInfo": with_comment_attachment_info,
                "withTaskVariablesInReturn": with_task_variables_in_return,
                "withTaskLocalVariablesInReturn": with_task_local_variables_in_return,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_tasks_count(
        self,
        *,
        task_id: str | None = None,
        task_id_in: str | None = None,
        process_instance_id: str | None = None,
        process_instance_id_in: str | None = None,
        process_instance_business_key: str | None = None,
        process_instance_business_key_expression: str | None = None,
        process_instance_business_key_in: str | None = None,
        process_instance_business_key_like: str | None = None,
        process_instance_business_key_like_expression: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        process_definition_key_in: str | None = None,
        process_definition_name: str | None = None,
        process_definition_name_like: str | None = None,
        execution_id: str | None = None,
        case_instance_id: str | None = None,
        case_instance_business_key: str | None = None,
        case_instance_business_key_like: str | None = None,
        case_definition_id: str | None = None,
        case_definition_key: str | None = None,
        case_definition_name: str | None = None,
        case_definition_name_like: str | None = None,
        case_execution_id: str | None = None,
        activity_instance_id_in: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        assignee: str | None = None,
        assignee_expression: str | None = None,
        assignee_like: str | None = None,
        assignee_like_expression: str | None = None,
        assignee_in: str | None = None,
        assignee_not_in: str | None = None,
        owner: str | None = None,
        owner_expression: str | None = None,
        candidate_group: str | None = None,
        candidate_group_like: str | None = None,
        candidate_group_expression: str | None = None,
        candidate_user: str | None = None,
        candidate_user_expression: str | None = None,
        include_assigned_tasks: bool | None = None,
        involved_user: str | None = None,
        involved_user_expression: str | None = None,
        assigned: bool | None = None,
        unassigned: bool | None = None,
        task_definition_key: str | None = None,
        task_definition_key_in: str | None = None,
        task_definition_key_not_in: str | None = None,
        task_definition_key_like: str | None = None,
        name: str | None = None,
        name_not_equal: str | None = None,
        name_like: str | None = None,
        name_not_like: str | None = None,
        description: str | None = None,
        description_like: str | None = None,
        priority: int | None = None,
        max_priority: int | None = None,
        min_priority: int | None = None,
        due_date: str | None = None,
        due_date_expression: str | None = None,
        due_after: str | None = None,
        due_after_expression: str | None = None,
        due_before: str | None = None,
        due_before_expression: str | None = None,
        without_due_date: bool | None = None,
        follow_up_date: str | None = None,
        follow_up_date_expression: str | None = None,
        follow_up_after: str | None = None,
        follow_up_after_expression: str | None = None,
        follow_up_before: str | None = None,
        follow_up_before_expression: str | None = None,
        follow_up_before_or_not_existent: str | None = None,
        follow_up_before_or_not_existent_expression: str | None = None,
        created_on: str | None = None,
        created_on_expression: str | None = None,
        created_after: str | None = None,
        created_after_expression: str | None = None,
        created_before: str | None = None,
        created_before_expression: str | None = None,
        updated_after: str | None = None,
        updated_after_expression: str | None = None,
        delegation_state: str | None = None,
        candidate_groups: str | None = None,
        candidate_groups_expression: str | None = None,
        with_candidate_groups: bool | None = None,
        without_candidate_groups: bool | None = None,
        with_candidate_users: bool | None = None,
        without_candidate_users: bool | None = None,
        active: bool | None = None,
        suspended: bool | None = None,
        task_variables: str | None = None,
        process_variables: str | None = None,
        case_instance_variables: str | None = None,
        variable_names_ignore_case: bool | None = None,
        variable_values_ignore_case: bool | None = None,
        parent_task_id: str | None = None,
        with_comment_attachment_info: bool | None = None,
        with_task_variables_in_return: bool | None = None,
        with_task_local_variables_in_return: bool | None = None,
    ) -> Any:
        """Get List Count.

        Retrieves the number of tasks that fulfill a provided filter. Corresponds to
        the size of the result set when using the Get Tasks method. **Security
        Consideration:** There are several query parameters (such as
        assigneeExpression) for specifying an EL expression. These are disabled by
        default to prevent remote code execution.

        GET /task/count
        """
        return self._call(
            "GET",
            "/task/count",
            params={
                "taskId": task_id,
                "taskIdIn": task_id_in,
                "processInstanceId": process_instance_id,
                "processInstanceIdIn": process_instance_id_in,
                "processInstanceBusinessKey": process_instance_business_key,
                "processInstanceBusinessKeyExpression": process_instance_business_key_expression,
                "processInstanceBusinessKeyIn": process_instance_business_key_in,
                "processInstanceBusinessKeyLike": process_instance_business_key_like,
                "processInstanceBusinessKeyLikeExpression": process_instance_business_key_like_expression,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "processDefinitionKeyIn": process_definition_key_in,
                "processDefinitionName": process_definition_name,
                "processDefinitionNameLike": process_definition_name_like,
                "executionId": execution_id,
                "caseInstanceId": case_instance_id,
                "caseInstanceBusinessKey": case_instance_business_key,
                "caseInstanceBusinessKeyLike": case_instance_business_key_like,
                "caseDefinitionId": case_definition_id,
                "caseDefinitionKey": case_definition_key,
                "caseDefinitionName": case_definition_name,
                "caseDefinitionNameLike": case_definition_name_like,
                "caseExecutionId": case_execution_id,
                "activityInstanceIdIn": activity_instance_id_in,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "assignee": assignee,
                "assigneeExpression": assignee_expression,
                "assigneeLike": assignee_like,
                "assigneeLikeExpression": assignee_like_expression,
                "assigneeIn": assignee_in,
                "assigneeNotIn": assignee_not_in,
                "owner": owner,
                "ownerExpression": owner_expression,
                "candidateGroup": candidate_group,
                "candidateGroupLike": candidate_group_like,
                "candidateGroupExpression": candidate_group_expression,
                "candidateUser": candidate_user,
                "candidateUserExpression": candidate_user_expression,
                "includeAssignedTasks": include_assigned_tasks,
                "involvedUser": involved_user,
                "involvedUserExpression": involved_user_expression,
                "assigned": assigned,
                "unassigned": unassigned,
                "taskDefinitionKey": task_definition_key,
                "taskDefinitionKeyIn": task_definition_key_in,
                "taskDefinitionKeyNotIn": task_definition_key_not_in,
                "taskDefinitionKeyLike": task_definition_key_like,
                "name": name,
                "nameNotEqual": name_not_equal,
                "nameLike": name_like,
                "nameNotLike": name_not_like,
                "description": description,
                "descriptionLike": description_like,
                "priority": priority,
                "maxPriority": max_priority,
                "minPriority": min_priority,
                "dueDate": due_date,
                "dueDateExpression": due_date_expression,
                "dueAfter": due_after,
                "dueAfterExpression": due_after_expression,
                "dueBefore": due_before,
                "dueBeforeExpression": due_before_expression,
                "withoutDueDate": without_due_date,
                "followUpDate": follow_up_date,
                "followUpDateExpression": follow_up_date_expression,
                "followUpAfter": follow_up_after,
                "followUpAfterExpression": follow_up_after_expression,
                "followUpBefore": follow_up_before,
                "followUpBeforeExpression": follow_up_before_expression,
                "followUpBeforeOrNotExistent": follow_up_before_or_not_existent,
                "followUpBeforeOrNotExistentExpression": follow_up_before_or_not_existent_expression,
                "createdOn": created_on,
                "createdOnExpression": created_on_expression,
                "createdAfter": created_after,
                "createdAfterExpression": created_after_expression,
                "createdBefore": created_before,
                "createdBeforeExpression": created_before_expression,
                "updatedAfter": updated_after,
                "updatedAfterExpression": updated_after_expression,
                "delegationState": delegation_state,
                "candidateGroups": candidate_groups,
                "candidateGroupsExpression": candidate_groups_expression,
                "withCandidateGroups": with_candidate_groups,
                "withoutCandidateGroups": without_candidate_groups,
                "withCandidateUsers": with_candidate_users,
                "withoutCandidateUsers": without_candidate_users,
                "active": active,
                "suspended": suspended,
                "taskVariables": task_variables,
                "processVariables": process_variables,
                "caseInstanceVariables": case_instance_variables,
                "variableNamesIgnoreCase": variable_names_ignore_case,
                "variableValuesIgnoreCase": variable_values_ignore_case,
                "parentTaskId": parent_task_id,
                "withCommentAttachmentInfo": with_comment_attachment_info,
                "withTaskVariablesInReturn": with_task_variables_in_return,
                "withTaskLocalVariablesInReturn": with_task_local_variables_in_return,
            },
        )

    def handle_bpmn_error(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Handle BPMN Error.

        Reports a business error in the context of a running task by id. The error
        code must be specified to identify the BPMN error handler. See the
        documentation for Reporting Bpmn Error in User Tasks. Request body: an
        object with errorCode, errorMessage, variables.

        POST /task/{id}/bpmnError
        """
        return self._call(
            "POST",
            "/task/{id}/bpmnError",
            path={"id": id},
            body=body,
        )

    def handle_escalation(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Handle BPMN Escalation.

        Reports an escalation in the context of a running task by id. The escalation
        code must be specified to identify the escalation handler. See the
        documentation for Reporting Bpmn Escalation in User Tasks. Request body: an
        object with escalationCode, variables.

        POST /task/{id}/bpmnEscalation
        """
        return self._call(
            "POST",
            "/task/{id}/bpmnEscalation",
            path={"id": id},
            body=body,
        )

    def query_tasks(
        self,
        *,
        first_result: int | None = None,
        max_results: int | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get List (POST).

        Queries for tasks that fulfill a given filter. This method is slightly more
        powerful than the Get Tasks method because it allows filtering by multiple
        process or task variables of types `String`, `Number` or `Boolean`. The size
        of the result set can be retrieved by using the Get Task Count (POST)
        method. Request body: an object with taskId, taskIdIn, processInstanceId,
        processInstanceIdIn, processInstanceBusinessKey,
        processInstanceBusinessKeyExpression, processInstanceBusinessKeyIn,
        processInstanceBusinessKeyLike, processInstanceBusinessKeyLikeExpression,
        processDefinitionId, processDefinitionKey, processDefinitionKeyIn,
        processDefinitionName, processDefinitionNameLike, executionId,
        caseInstanceId, caseInstanceBusinessKey, caseInstanceBusinessKeyLike,
        caseDefinitionId, caseDefinitionKey, caseDefinitionName,
        caseDefinitionNameLike, caseExecutionId, activityInstanceIdIn, tenantIdIn,
        withoutTenantId, assignee, assigneeExpression, assigneeLike,
        assigneeLikeExpression, assigneeIn, assigneeNotIn, owner, ownerExpression,
        candidateGroup, candidateGroupLike, candidateGroupExpression, candidateUser,
        candidateUserExpression, includeAssignedTasks, involvedUser,
        involvedUserExpression, assigned, unassigned, taskDefinitionKey,
        taskDefinitionKeyIn, taskDefinitionKeyNotIn, taskDefinitionKeyLike, name,
        nameNotEqual, nameLike, nameNotLike, description, descriptionLike, priority,
        maxPriority, minPriority, dueDate, dueDateExpression, dueAfter,
        dueAfterExpression, dueBefore, dueBeforeExpression, withoutDueDate,
        followUpDate, followUpDateExpression, followUpAfter,
        followUpAfterExpression, followUpBefore, followUpBeforeExpression,
        followUpBeforeOrNotExistent, followUpBeforeOrNotExistentExpression,
        createdOn, createdOnExpression, createdAfter, createdAfterExpression,
        createdBefore, createdBeforeExpression, updatedAfter,
        updatedAfterExpression, delegationState, candidateGroups,
        candidateGroupsExpression, withCandidateGroups, withoutCandidateGroups,
        withCandidateUsers, withoutCandidateUsers, active, suspended, taskVariables,
        processVariables, caseInstanceVariables, variableNamesIgnoreCase,
        variableValuesIgnoreCase, parentTaskId, orQueries, sorting.

        POST /task
        """
        return self._call(
            "POST",
            "/task",
            params={
                "firstResult": first_result,
                "maxResults": max_results,
            },
            body=body,
        )

    def query_tasks_count(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get List Count (POST).

        Retrieves the number of tasks that fulfill the given filter. Corresponds to
        the size of the result set of the Get Tasks (POST) method and takes the same
        parameters. **Security Consideration**: There are several parameters (such
        as `assigneeExpression`) for specifying an EL expression. These are disabled
        by default to prevent remote code execution. Request body: an object with
        taskId, taskIdIn, processInstanceId, processInstanceIdIn,
        processInstanceBusinessKey, processInstanceBusinessKeyExpression,
        processInstanceBusinessKeyIn, processInstanceBusinessKeyLike,
        processInstanceBusinessKeyLikeExpression, processDefinitionId,
        processDefinitionKey, processDefinitionKeyIn, processDefinitionName,
        processDefinitionNameLike, executionId, caseInstanceId,
        caseInstanceBusinessKey, caseInstanceBusinessKeyLike, caseDefinitionId,
        caseDefinitionKey, caseDefinitionName, caseDefinitionNameLike,
        caseExecutionId, activityInstanceIdIn, tenantIdIn, withoutTenantId,
        assignee, assigneeExpression, assigneeLike, assigneeLikeExpression,
        assigneeIn, assigneeNotIn, owner, ownerExpression, candidateGroup,
        candidateGroupLike, candidateGroupExpression, candidateUser,
        candidateUserExpression, includeAssignedTasks, involvedUser,
        involvedUserExpression, assigned, unassigned, taskDefinitionKey,
        taskDefinitionKeyIn, taskDefinitionKeyNotIn, taskDefinitionKeyLike, name,
        nameNotEqual, nameLike, nameNotLike, description, descriptionLike, priority,
        maxPriority, minPriority, dueDate, dueDateExpression, dueAfter,
        dueAfterExpression, dueBefore, dueBeforeExpression, withoutDueDate,
        followUpDate, followUpDateExpression, followUpAfter,
        followUpAfterExpression, followUpBefore, followUpBeforeExpression,
        followUpBeforeOrNotExistent, followUpBeforeOrNotExistentExpression,
        createdOn, createdOnExpression, createdAfter, createdAfterExpression,
        createdBefore, createdBeforeExpression, updatedAfter,
        updatedAfterExpression, delegationState, candidateGroups,
        candidateGroupsExpression, withCandidateGroups, withoutCandidateGroups,
        withCandidateUsers, withoutCandidateUsers, active, suspended, taskVariables,
        processVariables, caseInstanceVariables, variableNamesIgnoreCase,
        variableValuesIgnoreCase, parentTaskId, orQueries, sorting.

        POST /task/count
        """
        return self._call(
            "POST",
            "/task/count",
            body=body,
        )

    def resolve(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Resolve.

        Resolves a task and updates execution variables. Resolving a task marks that
        the assignee is done with the task delegated to them, and that it can be
        sent back to the owner. Can only be executed when the task has been
        delegated. The assignee will be set to the owner, who performed the
        delegation. Request body: an object with variables, withVariablesInReturn.

        POST /task/{id}/resolve
        """
        return self._call(
            "POST",
            "/task/{id}/resolve",
            path={"id": id},
            body=body,
        )

    def set_assignee(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Set Assignee.

        Changes the assignee of a task to a specific user. **Note:** The difference
        with the Claim Task method is that this method does not check if the task
        already has a user assigned to it. Request body: an object with userId.

        POST /task/{id}/assignee
        """
        return self._call(
            "POST",
            "/task/{id}/assignee",
            path={"id": id},
            body=body,
        )

    @guarded("task", 7, TaskEvent.COMPLETE)
    def submit(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Submit Form.

        Completes a task and updates process variables using a form submit. There
        are two difference between this method and the `complete` method: * If the
        task is in state `PENDING` - i.e., has been delegated before, it is not
        completed but resolved. Otherwise it will be completed. Request body: an
        object with variables, withVariablesInReturn.

        POST /task/{id}/submit-form
        """
        return self._call(
            "POST",
            "/task/{id}/submit-form",
            path={"id": id},
            body=body,
        )

    @guarded("task", 7, TaskEvent.UNCLAIM)
    def unclaim(
        self,
        id: str,
    ) -> Any:
        """Unclaim.

        Resets a task's assignee. If successful, the task is not assigned to a user.

        POST /task/{id}/unclaim
        """
        return self._call(
            "POST",
            "/task/{id}/unclaim",
            path={"id": id},
        )

    def update_task(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update.

        Updates a task. Request body: an object with id, name, assignee, owner,
        created, lastUpdated, due, followUp, delegationState, description,
        executionId, parentTaskId, priority, processDefinitionId, processInstanceId,
        caseExecutionId, caseDefinitionId, caseInstanceId, taskDefinitionKey,
        suspended, formKey, operatonFormRef, tenantId, taskState.

        PUT /task/{id}
        """
        return self._call(
            "PUT",
            "/task/{id}",
            path={"id": id},
            body=body,
        )
