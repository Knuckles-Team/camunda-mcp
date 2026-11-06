"""Operaton / Camunda 7 engine REST: the External Task operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7ExternalTask(ApiClientBase):
    """External Task: 18 engine REST operation(s)."""

    def complete_external_task_resource(
        self,
        id: str,
        *,
        body: Any = None,
    ) -> Any:
        """Complete.

        Completes an external task by id and updates process variables.

        POST /external-task/{id}/complete
        """
        return self._call(
            "POST",
            "/external-task/{id}/complete",
            path={"id": id},
            body=body,
        )

    def extend_lock(
        self,
        id: str,
        *,
        body: Any = None,
    ) -> Any:
        """Extend Lock.

        Extends the timeout of the lock by a given amount of time.

        POST /external-task/{id}/extendLock
        """
        return self._call(
            "POST",
            "/external-task/{id}/extendLock",
            path={"id": id},
            body=body,
        )

    def fetch_and_lock(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Fetch and Lock.

        Fetches and locks a specific number of external tasks for execution by a
        worker. Query can be restricted to specific task topics and for each task
        topic an individual lock time can be provided. Request body: an object with
        workerId, maxTasks, usePriority, asyncResponseTimeout, topics, sorting.

        POST /external-task/fetchAndLock
        """
        return self._call(
            "POST",
            "/external-task/fetchAndLock",
            body=body,
        )

    def get_external_task(
        self,
        id: str,
    ) -> Any:
        """Get.

        Retrieves an external task by id, corresponding to the `ExternalTask`
        interface in the engine.

        GET /external-task/{id}
        """
        return self._call(
            "GET",
            "/external-task/{id}",
            path={"id": id},
        )

    def get_external_task_error_details(
        self,
        id: str,
    ) -> Any:
        """Get Error Details.

        Retrieves the error details in the context of a running external task by id.

        GET /external-task/{id}/errorDetails
        """
        return self._call(
            "GET",
            "/external-task/{id}/errorDetails",
            path={"id": id},
        )

    def get_external_tasks(
        self,
        *,
        external_task_id: str | None = None,
        external_task_id_in: str | None = None,
        topic_name: str | None = None,
        worker_id: str | None = None,
        locked: bool | None = None,
        not_locked: bool | None = None,
        with_retries_left: bool | None = None,
        no_retries_left: bool | None = None,
        lock_expiration_after: str | None = None,
        lock_expiration_before: str | None = None,
        activity_id: str | None = None,
        activity_id_in: str | None = None,
        execution_id: str | None = None,
        process_instance_id: str | None = None,
        process_instance_id_in: str | None = None,
        process_definition_id: str | None = None,
        tenant_id_in: str | None = None,
        active: bool | None = None,
        suspended: bool | None = None,
        priority_higher_than_or_equals: int | None = None,
        priority_lower_than_or_equals: int | None = None,
        process_definition_key: str | None = None,
        process_definition_key_in: str | None = None,
        process_definition_name: str | None = None,
        process_definition_name_like: str | None = None,
        variable_names_ignore_case: bool | None = None,
        variable_values_ignore_case: bool | None = None,
        process_variables: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get List.

        Queries for the external tasks that fulfill given parameters. Parameters may
        be static as well as dynamic runtime properties of executions. The size of
        the result set can be retrieved by using the Get External Task Count method.

        GET /external-task
        """
        return self._call(
            "GET",
            "/external-task",
            params={
                "externalTaskId": external_task_id,
                "externalTaskIdIn": external_task_id_in,
                "topicName": topic_name,
                "workerId": worker_id,
                "locked": locked,
                "notLocked": not_locked,
                "withRetriesLeft": with_retries_left,
                "noRetriesLeft": no_retries_left,
                "lockExpirationAfter": lock_expiration_after,
                "lockExpirationBefore": lock_expiration_before,
                "activityId": activity_id,
                "activityIdIn": activity_id_in,
                "executionId": execution_id,
                "processInstanceId": process_instance_id,
                "processInstanceIdIn": process_instance_id_in,
                "processDefinitionId": process_definition_id,
                "tenantIdIn": tenant_id_in,
                "active": active,
                "suspended": suspended,
                "priorityHigherThanOrEquals": priority_higher_than_or_equals,
                "priorityLowerThanOrEquals": priority_lower_than_or_equals,
                "processDefinitionKey": process_definition_key,
                "processDefinitionKeyIn": process_definition_key_in,
                "processDefinitionName": process_definition_name,
                "processDefinitionNameLike": process_definition_name_like,
                "variableNamesIgnoreCase": variable_names_ignore_case,
                "variableValuesIgnoreCase": variable_values_ignore_case,
                "processVariables": process_variables,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_external_tasks_count(
        self,
        *,
        external_task_id: str | None = None,
        external_task_id_in: str | None = None,
        topic_name: str | None = None,
        worker_id: str | None = None,
        locked: bool | None = None,
        not_locked: bool | None = None,
        with_retries_left: bool | None = None,
        no_retries_left: bool | None = None,
        lock_expiration_after: str | None = None,
        lock_expiration_before: str | None = None,
        activity_id: str | None = None,
        activity_id_in: str | None = None,
        execution_id: str | None = None,
        process_instance_id: str | None = None,
        process_instance_id_in: str | None = None,
        process_definition_id: str | None = None,
        tenant_id_in: str | None = None,
        active: bool | None = None,
        suspended: bool | None = None,
        priority_higher_than_or_equals: int | None = None,
        priority_lower_than_or_equals: int | None = None,
        process_definition_key: str | None = None,
        process_definition_key_in: str | None = None,
        process_definition_name: str | None = None,
        process_definition_name_like: str | None = None,
        variable_names_ignore_case: bool | None = None,
        variable_values_ignore_case: bool | None = None,
        process_variables: str | None = None,
    ) -> Any:
        """Get List Count.

        Queries for the number of external tasks that fulfill given parameters.
        Takes the same parameters as the Get External Tasks method.

        GET /external-task/count
        """
        return self._call(
            "GET",
            "/external-task/count",
            params={
                "externalTaskId": external_task_id,
                "externalTaskIdIn": external_task_id_in,
                "topicName": topic_name,
                "workerId": worker_id,
                "locked": locked,
                "notLocked": not_locked,
                "withRetriesLeft": with_retries_left,
                "noRetriesLeft": no_retries_left,
                "lockExpirationAfter": lock_expiration_after,
                "lockExpirationBefore": lock_expiration_before,
                "activityId": activity_id,
                "activityIdIn": activity_id_in,
                "executionId": execution_id,
                "processInstanceId": process_instance_id,
                "processInstanceIdIn": process_instance_id_in,
                "processDefinitionId": process_definition_id,
                "tenantIdIn": tenant_id_in,
                "active": active,
                "suspended": suspended,
                "priorityHigherThanOrEquals": priority_higher_than_or_equals,
                "priorityLowerThanOrEquals": priority_lower_than_or_equals,
                "processDefinitionKey": process_definition_key,
                "processDefinitionKeyIn": process_definition_key_in,
                "processDefinitionName": process_definition_name,
                "processDefinitionNameLike": process_definition_name_like,
                "variableNamesIgnoreCase": variable_names_ignore_case,
                "variableValuesIgnoreCase": variable_values_ignore_case,
                "processVariables": process_variables,
            },
        )

    def get_topic_names(
        self,
        *,
        with_locked_tasks: bool | None = None,
        with_unlocked_tasks: bool | None = None,
        with_retries_left: bool | None = None,
    ) -> Any:
        """Get External Task Topic Names.

        Queries for distinct topic names of external tasks that fulfill given
        parameters. Query can be restricted to only tasks with retries left, tasks
        that are locked, or tasks that are unlocked. The parameters withLockedTasks
        and withUnlockedTasks are exclusive. Setting them both to true will return
        an empty list.

        GET /external-task/topic-names
        """
        return self._call(
            "GET",
            "/external-task/topic-names",
            params={
                "withLockedTasks": with_locked_tasks,
                "withUnlockedTasks": with_unlocked_tasks,
                "withRetriesLeft": with_retries_left,
            },
        )

    def handle_external_task_bpmn_error(
        self,
        id: str,
        *,
        body: Any = None,
    ) -> Any:
        """Handle BPMN Error.

        Reports a business error in the context of a running external task by id.
        The error code must be specified to identify the BPMN error handler.

        POST /external-task/{id}/bpmnError
        """
        return self._call(
            "POST",
            "/external-task/{id}/bpmnError",
            path={"id": id},
            body=body,
        )

    def handle_failure(
        self,
        id: str,
        *,
        body: Any = None,
    ) -> Any:
        """Handle Failure.

        Reports a failure to execute an external task by id. A number of retries and
        a timeout until the task can be retried can be specified. If retries are set
        to 0, an incident for this task is created.

        POST /external-task/{id}/failure
        """
        return self._call(
            "POST",
            "/external-task/{id}/failure",
            path={"id": id},
            body=body,
        )

    def lock(
        self,
        id: str,
        *,
        body: Any = None,
    ) -> Any:
        """.

        Lock an external task by a given id for a specified worker and amount of
        time.

        POST /external-task/{id}/lock
        """
        return self._call(
            "POST",
            "/external-task/{id}/lock",
            path={"id": id},
            body=body,
        )

    def query_external_tasks(
        self,
        *,
        first_result: int | None = None,
        max_results: int | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get List (POST).

        Queries for external tasks that fulfill given parameters in the form of a
        JSON object. This method is slightly more powerful than the Get External
        Tasks method because it allows to specify a hierarchical result sorting.
        Request body: an object with externalTaskId, externalTaskIdIn, topicName,
        workerId, locked, notLocked, withRetriesLeft, noRetriesLeft,
        lockExpirationAfter, lockExpirationBefore, activityId, activityIdIn,
        executionId, processInstanceId, processInstanceIdIn, processDefinitionId,
        tenantIdIn, active, suspended, priorityHigherThanOrEquals,
        priorityLowerThanOrEquals, processDefinitionKey, processDefinitionKeyIn,
        processDefinitionName, processDefinitionNameLike, variableNamesIgnoreCase,
        variableValuesIgnoreCase, processVariables, sorting.

        POST /external-task
        """
        return self._call(
            "POST",
            "/external-task",
            params={
                "firstResult": first_result,
                "maxResults": max_results,
            },
            body=body,
        )

    def query_external_tasks_count(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get List Count (POST).

        Queries for the number of external tasks that fulfill given parameters. This
        method takes the same message body as the Get External Tasks (POST) method.
        Request body: an object with externalTaskId, externalTaskIdIn, topicName,
        workerId, locked, notLocked, withRetriesLeft, noRetriesLeft,
        lockExpirationAfter, lockExpirationBefore, activityId, activityIdIn,
        executionId, processInstanceId, processInstanceIdIn, processDefinitionId,
        tenantIdIn, active, suspended, priorityHigherThanOrEquals,
        priorityLowerThanOrEquals, processDefinitionKey, processDefinitionKeyIn,
        processDefinitionName, processDefinitionNameLike, variableNamesIgnoreCase,
        variableValuesIgnoreCase, processVariables, sorting.

        POST /external-task/count
        """
        return self._call(
            "POST",
            "/external-task/count",
            body=body,
        )

    def set_external_task_resource_priority(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Set Priority.

        Sets the priority of an existing external task by id. The default value of a
        priority is 0. Request body: an object with priority.

        PUT /external-task/{id}/priority
        """
        return self._call(
            "PUT",
            "/external-task/{id}/priority",
            path={"id": id},
            body=body,
        )

    def set_external_task_resource_retries(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Set Retries.

        Sets the number of retries left to execute an external task by id. If
        retries are set to 0, an incident is created. Request body: an object with
        retries.

        PUT /external-task/{id}/retries
        """
        return self._call(
            "PUT",
            "/external-task/{id}/retries",
            path={"id": id},
            body=body,
        )

    def set_external_task_retries(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Set Retries Sync.

        Sets the number of retries left to execute external tasks by id
        synchronously. If retries are set to 0, an incident is created. Request
        body: an object with retries, externalTaskIds, processInstanceIds,
        externalTaskQuery, processInstanceQuery, historicProcessInstanceQuery.

        PUT /external-task/retries
        """
        return self._call(
            "PUT",
            "/external-task/retries",
            body=body,
        )

    def set_external_task_retries_async_operation(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Set Retries Async.

        Sets the number of retries left to execute external tasks by id
        asynchronously. If retries are set to 0, an incident is created. Request
        body: an object with retries, externalTaskIds, processInstanceIds,
        externalTaskQuery, processInstanceQuery, historicProcessInstanceQuery.

        POST /external-task/retries-async
        """
        return self._call(
            "POST",
            "/external-task/retries-async",
            body=body,
        )

    def unlock(
        self,
        id: str,
    ) -> Any:
        """Unlock.

        Unlocks an external task by id. Clears the task's lock expiration time and
        worker id.

        POST /external-task/{id}/unlock
        """
        return self._call(
            "POST",
            "/external-task/{id}/unlock",
            path={"id": id},
        )
