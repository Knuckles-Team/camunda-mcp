"""Operaton / Camunda 7 engine REST: the Job operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7Job(ApiClientBase):
    """Job: 15 engine REST operation(s)."""

    def delete_job(
        self,
        id: str,
    ) -> Any:
        """Delete Job.

        Deletes a job by id.

        DELETE /job/{id}
        """
        return self._call(
            "DELETE",
            "/job/{id}",
            path={"id": id},
        )

    def execute_job(
        self,
        id: str,
    ) -> Any:
        """Execute Job.

        Executes a job by id. **Note:** The execution of the job happens
        synchronously in the same thread.

        POST /job/{id}/execute
        """
        return self._call(
            "POST",
            "/job/{id}/execute",
            path={"id": id},
        )

    def get_job(
        self,
        id: str,
    ) -> Any:
        """Get Job.

        Retrieves a job by id, according to the `Job` interface in the engine.

        GET /job/{id}
        """
        return self._call(
            "GET",
            "/job/{id}",
            path={"id": id},
        )

    def get_jobs(
        self,
        *,
        job_id: str | None = None,
        job_ids: str | None = None,
        job_definition_id: str | None = None,
        process_instance_id: str | None = None,
        process_instance_ids: str | None = None,
        execution_id: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        activity_id: str | None = None,
        with_retries_left: bool | None = None,
        executable: bool | None = None,
        timers: bool | None = None,
        messages: bool | None = None,
        due_dates: str | None = None,
        create_times: str | None = None,
        with_exception: bool | None = None,
        exception_message: str | None = None,
        failed_activity_id: str | None = None,
        no_retries_left: bool | None = None,
        active: bool | None = None,
        suspended: bool | None = None,
        priority_lower_than_or_equals: int | None = None,
        priority_higher_than_or_equals: int | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        include_jobs_without_tenant_id: bool | None = None,
        acquired: bool | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get Jobs.

        Queries for jobs that fulfill given parameters. The size of the result set
        can be retrieved by using the Get Job Count method.

        GET /job
        """
        return self._call(
            "GET",
            "/job",
            params={
                "jobId": job_id,
                "jobIds": job_ids,
                "jobDefinitionId": job_definition_id,
                "processInstanceId": process_instance_id,
                "processInstanceIds": process_instance_ids,
                "executionId": execution_id,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "activityId": activity_id,
                "withRetriesLeft": with_retries_left,
                "executable": executable,
                "timers": timers,
                "messages": messages,
                "dueDates": due_dates,
                "createTimes": create_times,
                "withException": with_exception,
                "exceptionMessage": exception_message,
                "failedActivityId": failed_activity_id,
                "noRetriesLeft": no_retries_left,
                "active": active,
                "suspended": suspended,
                "priorityLowerThanOrEquals": priority_lower_than_or_equals,
                "priorityHigherThanOrEquals": priority_higher_than_or_equals,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "includeJobsWithoutTenantId": include_jobs_without_tenant_id,
                "acquired": acquired,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_jobs_count(
        self,
        *,
        job_id: str | None = None,
        job_ids: str | None = None,
        job_definition_id: str | None = None,
        process_instance_id: str | None = None,
        process_instance_ids: str | None = None,
        execution_id: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        activity_id: str | None = None,
        with_retries_left: bool | None = None,
        executable: bool | None = None,
        timers: bool | None = None,
        messages: bool | None = None,
        due_dates: str | None = None,
        create_times: str | None = None,
        with_exception: bool | None = None,
        exception_message: str | None = None,
        failed_activity_id: str | None = None,
        no_retries_left: bool | None = None,
        active: bool | None = None,
        suspended: bool | None = None,
        priority_lower_than_or_equals: int | None = None,
        priority_higher_than_or_equals: int | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        include_jobs_without_tenant_id: bool | None = None,
        acquired: bool | None = None,
    ) -> Any:
        """Get Job Count.

        Queries for the number of jobs that fulfill given parameters. Takes the same
        parameters as the Get Jobs method.

        GET /job/count
        """
        return self._call(
            "GET",
            "/job/count",
            params={
                "jobId": job_id,
                "jobIds": job_ids,
                "jobDefinitionId": job_definition_id,
                "processInstanceId": process_instance_id,
                "processInstanceIds": process_instance_ids,
                "executionId": execution_id,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "activityId": activity_id,
                "withRetriesLeft": with_retries_left,
                "executable": executable,
                "timers": timers,
                "messages": messages,
                "dueDates": due_dates,
                "createTimes": create_times,
                "withException": with_exception,
                "exceptionMessage": exception_message,
                "failedActivityId": failed_activity_id,
                "noRetriesLeft": no_retries_left,
                "active": active,
                "suspended": suspended,
                "priorityLowerThanOrEquals": priority_lower_than_or_equals,
                "priorityHigherThanOrEquals": priority_higher_than_or_equals,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "includeJobsWithoutTenantId": include_jobs_without_tenant_id,
                "acquired": acquired,
            },
        )

    def get_stacktrace(
        self,
        id: str,
    ) -> Any:
        """Get Exception Stacktrace.

        Retrieves the exception stacktrace corresponding to the passed job id.

        GET /job/{id}/stacktrace
        """
        return self._call(
            "GET",
            "/job/{id}/stacktrace",
            path={"id": id},
        )

    def query_jobs(
        self,
        *,
        first_result: int | None = None,
        max_results: int | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get Jobs (POST).

        Queries for jobs that fulfill given parameters. This method is slightly more
        powerful than the Get Jobs method because it allows filtering by multiple
        jobs of types `String`, `Number` or `Boolean`. Request body: an object with
        jobId, jobIds, jobDefinitionId, processInstanceId, processInstanceIds,
        executionId, processDefinitionId, processDefinitionKey, activityId,
        withRetriesLeft, executable, timers, messages, dueDates, createTimes,
        withException, exceptionMessage, failedActivityId, noRetriesLeft, active,
        suspended, priorityLowerThanOrEquals, priorityHigherThanOrEquals,
        tenantIdIn, withoutTenantId, includeJobsWithoutTenantId, acquired, sorting.

        POST /job
        """
        return self._call(
            "POST",
            "/job",
            params={
                "firstResult": first_result,
                "maxResults": max_results,
            },
            body=body,
        )

    def query_jobs_count(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get Job Count (POST).

        Queries for jobs that fulfill given parameters. This method takes the same
        message body as the Get Jobs POST method and therefore it is slightly more
        powerful than the Get Job Count method. Request body: an object with jobId,
        jobIds, jobDefinitionId, processInstanceId, processInstanceIds, executionId,
        processDefinitionId, processDefinitionKey, activityId, withRetriesLeft,
        executable, timers, messages, dueDates, createTimes, withException,
        exceptionMessage, failedActivityId, noRetriesLeft, active, suspended,
        priorityLowerThanOrEquals, priorityHigherThanOrEquals, tenantIdIn,
        withoutTenantId, includeJobsWithoutTenantId, acquired, sorting.

        POST /job/count
        """
        return self._call(
            "POST",
            "/job/count",
            body=body,
        )

    def recalculate_duedate(
        self,
        id: str,
        *,
        creation_date_based: bool | None = None,
    ) -> Any:
        """Recalculate Job Due Date.

        Recalculates the due date of a job by id.

        POST /job/{id}/duedate/recalculate
        """
        return self._call(
            "POST",
            "/job/{id}/duedate/recalculate",
            path={"id": id},
            params={
                "creationDateBased": creation_date_based,
            },
        )

    def set_job_duedate(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Set Job Due Date.

        Updates the due date of a job by id. Request body: an object with duedate,
        cascade.

        PUT /job/{id}/duedate
        """
        return self._call(
            "PUT",
            "/job/{id}/duedate",
            path={"id": id},
            body=body,
        )

    def set_job_priority(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Set Job Priority.

        Sets the execution priority of a job by id. Request body: an object with
        priority.

        PUT /job/{id}/priority
        """
        return self._call(
            "PUT",
            "/job/{id}/priority",
            path={"id": id},
            body=body,
        )

    def set_job_retries(
        self,
        id: str,
        *,
        body: Any = None,
    ) -> Any:
        """Set Job Retries.

        Sets the retries of the job to the given number of retries by id.

        PUT /job/{id}/retries
        """
        return self._call(
            "PUT",
            "/job/{id}/retries",
            path={"id": id},
            body=body,
        )

    def set_job_retries_async_operation(
        self,
        *,
        body: Any = None,
    ) -> Any:
        """Set Job Retries Async (POST).

        Create a batch to set retries of jobs asynchronously.

        POST /job/retries
        """
        return self._call(
            "POST",
            "/job/retries",
            body=body,
        )

    def update_job_suspension_state(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Activate/Suspend Job By Id.

        Activates or suspends a given job by id. Request body: an object with
        suspended.

        PUT /job/{id}/suspended
        """
        return self._call(
            "PUT",
            "/job/{id}/suspended",
            path={"id": id},
            body=body,
        )

    def update_suspension_state_by(
        self,
        *,
        body: Any = None,
    ) -> Any:
        """Activate/Suspend Jobs.

        Activates or suspends jobs matching the given criterion. This can only be on
        of: * `jobDefinitionId` * `processDefinitionId` * `processInstanceId` *
        `processDefinitionKey`

        PUT /job/suspended
        """
        return self._call(
            "PUT",
            "/job/suspended",
            body=body,
        )
