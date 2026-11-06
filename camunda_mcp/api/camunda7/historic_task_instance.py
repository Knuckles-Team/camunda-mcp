"""Operaton / Camunda 7 engine REST: the Historic Task Instance operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7HistoricTaskInstance(ApiClientBase):
    """Historic Task Instance: 5 engine REST operation(s)."""

    def get_historic_task_instance_report(
        self,
        *,
        report_type: str | None = None,
        period_unit: str | None = None,
        completed_before: str | None = None,
        completed_after: str | None = None,
        group_by: str | None = None,
    ) -> Any:
        """Get Task Report (Historic).

        Retrieves a report of completed tasks. When the report type is set to
        `count`, the report contains a list of completed task counts where an entry
        contains the task name, the definition key of the task, the process
        definition id, the process definition key, the process definition name and
        the count of how many tasks were completed for the specified key in a given
        period.

        GET /history/task/report
        """
        return self._call(
            "GET",
            "/history/task/report",
            params={
                "reportType": report_type,
                "periodUnit": period_unit,
                "completedBefore": completed_before,
                "completedAfter": completed_after,
                "groupBy": group_by,
            },
        )

    def get_historic_task_instances(
        self,
        *,
        task_id: str | None = None,
        task_parent_task_id: str | None = None,
        process_instance_id: str | None = None,
        root_process_instance_id: str | None = None,
        process_instance_business_key: str | None = None,
        process_instance_business_key_in: str | None = None,
        process_instance_business_key_like: str | None = None,
        execution_id: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        process_definition_name: str | None = None,
        case_instance_id: str | None = None,
        case_execution_id: str | None = None,
        case_definition_id: str | None = None,
        case_definition_key: str | None = None,
        case_definition_name: str | None = None,
        activity_instance_id_in: str | None = None,
        task_name: str | None = None,
        task_name_like: str | None = None,
        task_description: str | None = None,
        task_description_like: str | None = None,
        task_definition_key: str | None = None,
        task_definition_key_in: str | None = None,
        task_delete_reason: str | None = None,
        task_delete_reason_like: str | None = None,
        task_assignee: str | None = None,
        task_assignee_like: str | None = None,
        task_owner: str | None = None,
        task_owner_like: str | None = None,
        task_priority: int | None = None,
        assigned: bool | None = None,
        unassigned: bool | None = None,
        finished: bool | None = None,
        unfinished: bool | None = None,
        process_finished: bool | None = None,
        process_unfinished: bool | None = None,
        task_due_date: str | None = None,
        task_due_date_before: str | None = None,
        task_due_date_after: str | None = None,
        without_task_due_date: bool | None = None,
        task_follow_up_date: str | None = None,
        task_follow_up_date_before: str | None = None,
        task_follow_up_date_after: str | None = None,
        started_before: str | None = None,
        started_after: str | None = None,
        finished_before: str | None = None,
        finished_after: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        task_variables: str | None = None,
        process_variables: str | None = None,
        variable_names_ignore_case: bool | None = None,
        variable_values_ignore_case: bool | None = None,
        task_involved_user: str | None = None,
        task_involved_group: str | None = None,
        task_had_candidate_user: str | None = None,
        task_had_candidate_group: str | None = None,
        with_candidate_groups: bool | None = None,
        without_candidate_groups: bool | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get Tasks (Historic).

        Queries for historic tasks that fulfill the given parameters. The size of
        the result set can be retrieved by using the Get Task Count method.

        GET /history/task
        """
        return self._call(
            "GET",
            "/history/task",
            params={
                "taskId": task_id,
                "taskParentTaskId": task_parent_task_id,
                "processInstanceId": process_instance_id,
                "rootProcessInstanceId": root_process_instance_id,
                "processInstanceBusinessKey": process_instance_business_key,
                "processInstanceBusinessKeyIn": process_instance_business_key_in,
                "processInstanceBusinessKeyLike": process_instance_business_key_like,
                "executionId": execution_id,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "processDefinitionName": process_definition_name,
                "caseInstanceId": case_instance_id,
                "caseExecutionId": case_execution_id,
                "caseDefinitionId": case_definition_id,
                "caseDefinitionKey": case_definition_key,
                "caseDefinitionName": case_definition_name,
                "activityInstanceIdIn": activity_instance_id_in,
                "taskName": task_name,
                "taskNameLike": task_name_like,
                "taskDescription": task_description,
                "taskDescriptionLike": task_description_like,
                "taskDefinitionKey": task_definition_key,
                "taskDefinitionKeyIn": task_definition_key_in,
                "taskDeleteReason": task_delete_reason,
                "taskDeleteReasonLike": task_delete_reason_like,
                "taskAssignee": task_assignee,
                "taskAssigneeLike": task_assignee_like,
                "taskOwner": task_owner,
                "taskOwnerLike": task_owner_like,
                "taskPriority": task_priority,
                "assigned": assigned,
                "unassigned": unassigned,
                "finished": finished,
                "unfinished": unfinished,
                "processFinished": process_finished,
                "processUnfinished": process_unfinished,
                "taskDueDate": task_due_date,
                "taskDueDateBefore": task_due_date_before,
                "taskDueDateAfter": task_due_date_after,
                "withoutTaskDueDate": without_task_due_date,
                "taskFollowUpDate": task_follow_up_date,
                "taskFollowUpDateBefore": task_follow_up_date_before,
                "taskFollowUpDateAfter": task_follow_up_date_after,
                "startedBefore": started_before,
                "startedAfter": started_after,
                "finishedBefore": finished_before,
                "finishedAfter": finished_after,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "taskVariables": task_variables,
                "processVariables": process_variables,
                "variableNamesIgnoreCase": variable_names_ignore_case,
                "variableValuesIgnoreCase": variable_values_ignore_case,
                "taskInvolvedUser": task_involved_user,
                "taskInvolvedGroup": task_involved_group,
                "taskHadCandidateUser": task_had_candidate_user,
                "taskHadCandidateGroup": task_had_candidate_group,
                "withCandidateGroups": with_candidate_groups,
                "withoutCandidateGroups": without_candidate_groups,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_historic_task_instances_count(
        self,
        *,
        task_id: str | None = None,
        task_parent_task_id: str | None = None,
        process_instance_id: str | None = None,
        root_process_instance_id: str | None = None,
        process_instance_business_key: str | None = None,
        process_instance_business_key_in: str | None = None,
        process_instance_business_key_like: str | None = None,
        execution_id: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        process_definition_name: str | None = None,
        case_instance_id: str | None = None,
        case_execution_id: str | None = None,
        case_definition_id: str | None = None,
        case_definition_key: str | None = None,
        case_definition_name: str | None = None,
        activity_instance_id_in: str | None = None,
        task_name: str | None = None,
        task_name_like: str | None = None,
        task_description: str | None = None,
        task_description_like: str | None = None,
        task_definition_key: str | None = None,
        task_definition_key_in: str | None = None,
        task_delete_reason: str | None = None,
        task_delete_reason_like: str | None = None,
        task_assignee: str | None = None,
        task_assignee_like: str | None = None,
        task_owner: str | None = None,
        task_owner_like: str | None = None,
        task_priority: int | None = None,
        assigned: bool | None = None,
        unassigned: bool | None = None,
        finished: bool | None = None,
        unfinished: bool | None = None,
        process_finished: bool | None = None,
        process_unfinished: bool | None = None,
        task_due_date: str | None = None,
        task_due_date_before: str | None = None,
        task_due_date_after: str | None = None,
        without_task_due_date: bool | None = None,
        task_follow_up_date: str | None = None,
        task_follow_up_date_before: str | None = None,
        task_follow_up_date_after: str | None = None,
        started_before: str | None = None,
        started_after: str | None = None,
        finished_before: str | None = None,
        finished_after: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        task_variables: str | None = None,
        process_variables: str | None = None,
        variable_names_ignore_case: bool | None = None,
        variable_values_ignore_case: bool | None = None,
        task_involved_user: str | None = None,
        task_involved_group: str | None = None,
        task_had_candidate_user: str | None = None,
        task_had_candidate_group: str | None = None,
        with_candidate_groups: bool | None = None,
        without_candidate_groups: bool | None = None,
    ) -> Any:
        """Get Task Count.

        Queries for the number of historic tasks that fulfill the given parameters.
        Takes the same parameters as the Get Tasks (Historic) method.

        GET /history/task/count
        """
        return self._call(
            "GET",
            "/history/task/count",
            params={
                "taskId": task_id,
                "taskParentTaskId": task_parent_task_id,
                "processInstanceId": process_instance_id,
                "rootProcessInstanceId": root_process_instance_id,
                "processInstanceBusinessKey": process_instance_business_key,
                "processInstanceBusinessKeyIn": process_instance_business_key_in,
                "processInstanceBusinessKeyLike": process_instance_business_key_like,
                "executionId": execution_id,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "processDefinitionName": process_definition_name,
                "caseInstanceId": case_instance_id,
                "caseExecutionId": case_execution_id,
                "caseDefinitionId": case_definition_id,
                "caseDefinitionKey": case_definition_key,
                "caseDefinitionName": case_definition_name,
                "activityInstanceIdIn": activity_instance_id_in,
                "taskName": task_name,
                "taskNameLike": task_name_like,
                "taskDescription": task_description,
                "taskDescriptionLike": task_description_like,
                "taskDefinitionKey": task_definition_key,
                "taskDefinitionKeyIn": task_definition_key_in,
                "taskDeleteReason": task_delete_reason,
                "taskDeleteReasonLike": task_delete_reason_like,
                "taskAssignee": task_assignee,
                "taskAssigneeLike": task_assignee_like,
                "taskOwner": task_owner,
                "taskOwnerLike": task_owner_like,
                "taskPriority": task_priority,
                "assigned": assigned,
                "unassigned": unassigned,
                "finished": finished,
                "unfinished": unfinished,
                "processFinished": process_finished,
                "processUnfinished": process_unfinished,
                "taskDueDate": task_due_date,
                "taskDueDateBefore": task_due_date_before,
                "taskDueDateAfter": task_due_date_after,
                "withoutTaskDueDate": without_task_due_date,
                "taskFollowUpDate": task_follow_up_date,
                "taskFollowUpDateBefore": task_follow_up_date_before,
                "taskFollowUpDateAfter": task_follow_up_date_after,
                "startedBefore": started_before,
                "startedAfter": started_after,
                "finishedBefore": finished_before,
                "finishedAfter": finished_after,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "taskVariables": task_variables,
                "processVariables": process_variables,
                "variableNamesIgnoreCase": variable_names_ignore_case,
                "variableValuesIgnoreCase": variable_values_ignore_case,
                "taskInvolvedUser": task_involved_user,
                "taskInvolvedGroup": task_involved_group,
                "taskHadCandidateUser": task_had_candidate_user,
                "taskHadCandidateGroup": task_had_candidate_group,
                "withCandidateGroups": with_candidate_groups,
                "withoutCandidateGroups": without_candidate_groups,
            },
        )

    def query_historic_task_instances(
        self,
        *,
        first_result: int | None = None,
        max_results: int | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get Tasks (Historic) (POST).

        Queries for historic tasks that fulfill the given parameters. This method is
        slightly more powerful than the Get Tasks (Historic) method because it
        allows filtering by multiple process or task variables of types `String`,
        `Number` or `Boolean`. The size of the result set can be retrieved by using
        the Get Task Count (POST) method. Request body: an object with taskId,
        taskParentTaskId, processInstanceId, rootProcessInstanceId,
        processInstanceBusinessKey, processInstanceBusinessKeyIn,
        processInstanceBusinessKeyLike, executionId, processDefinitionId,
        processDefinitionKey, processDefinitionName, caseInstanceId,
        caseExecutionId, caseDefinitionId, caseDefinitionKey, caseDefinitionName,
        activityInstanceIdIn, taskName, taskNameLike, taskDescription,
        taskDescriptionLike, taskDefinitionKey, taskDefinitionKeyIn,
        taskDeleteReason, taskDeleteReasonLike, taskAssignee, taskAssigneeLike,
        taskOwner, taskOwnerLike, taskPriority, assigned, unassigned, finished,
        unfinished, processFinished, processUnfinished, taskDueDate,
        taskDueDateBefore, taskDueDateAfter, withoutTaskDueDate, taskFollowUpDate,
        taskFollowUpDateBefore, taskFollowUpDateAfter, startedBefore, startedAfter,
        finishedBefore, finishedAfter, tenantIdIn, withoutTenantId, taskVariables,
        processVariables, variableNamesIgnoreCase, variableValuesIgnoreCase,
        taskInvolvedUser, taskInvolvedGroup, taskHadCandidateUser,
        taskHadCandidateGroup, withCandidateGroups, withoutCandidateGroups,
        orQueries, sorting.

        POST /history/task
        """
        return self._call(
            "POST",
            "/history/task",
            params={
                "firstResult": first_result,
                "maxResults": max_results,
            },
            body=body,
        )

    def query_historic_task_instances_count(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get Task Count (POST).

        Queries for the number of historic tasks that fulfill the given parameters.
        Takes the same parameters as the Get Tasks (Historic) method. Corresponds to
        the size of the result set of the Get Tasks (Historic) (POST) method and
        takes the same parameters. Request body: an object with taskId,
        taskParentTaskId, processInstanceId, rootProcessInstanceId,
        processInstanceBusinessKey, processInstanceBusinessKeyIn,
        processInstanceBusinessKeyLike, executionId, processDefinitionId,
        processDefinitionKey, processDefinitionName, caseInstanceId,
        caseExecutionId, caseDefinitionId, caseDefinitionKey, caseDefinitionName,
        activityInstanceIdIn, taskName, taskNameLike, taskDescription,
        taskDescriptionLike, taskDefinitionKey, taskDefinitionKeyIn,
        taskDeleteReason, taskDeleteReasonLike, taskAssignee, taskAssigneeLike,
        taskOwner, taskOwnerLike, taskPriority, assigned, unassigned, finished,
        unfinished, processFinished, processUnfinished, taskDueDate,
        taskDueDateBefore, taskDueDateAfter, withoutTaskDueDate, taskFollowUpDate,
        taskFollowUpDateBefore, taskFollowUpDateAfter, startedBefore, startedAfter,
        finishedBefore, finishedAfter, tenantIdIn, withoutTenantId, taskVariables,
        processVariables, variableNamesIgnoreCase, variableValuesIgnoreCase,
        taskInvolvedUser, taskInvolvedGroup, taskHadCandidateUser,
        taskHadCandidateGroup, withCandidateGroups, withoutCandidateGroups,
        orQueries, sorting.

        POST /history/task/count
        """
        return self._call(
            "POST",
            "/history/task/count",
            body=body,
        )
