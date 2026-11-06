"""Operaton / Camunda 7 engine REST: the Job Definition operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7JobDefinition(ApiClientBase):
    """Job Definition: 9 engine REST operation(s)."""

    def get_job_definition(
        self,
        id: str,
    ) -> Any:
        """Get Job Definition.

        Retrieves a job definition by id, according to the `JobDefinition` interface
        in the engine.

        GET /job-definition/{id}
        """
        return self._call(
            "GET",
            "/job-definition/{id}",
            path={"id": id},
        )

    def get_job_definitions(
        self,
        *,
        job_definition_id: str | None = None,
        activity_id_in: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        job_type: str | None = None,
        job_configuration: str | None = None,
        active: bool | None = None,
        suspended: bool | None = None,
        with_overriding_job_priority: bool | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        include_job_definitions_without_tenant_id: bool | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get Job Definitions.

        Queries for job definitions that fulfill given parameters. The size of the
        result set can be retrieved by using the Get Job Definition Count method.

        GET /job-definition
        """
        return self._call(
            "GET",
            "/job-definition",
            params={
                "jobDefinitionId": job_definition_id,
                "activityIdIn": activity_id_in,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "jobType": job_type,
                "jobConfiguration": job_configuration,
                "active": active,
                "suspended": suspended,
                "withOverridingJobPriority": with_overriding_job_priority,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "includeJobDefinitionsWithoutTenantId": include_job_definitions_without_tenant_id,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_job_definitions_count(
        self,
        *,
        job_definition_id: str | None = None,
        activity_id_in: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        job_type: str | None = None,
        job_configuration: str | None = None,
        active: bool | None = None,
        suspended: bool | None = None,
        with_overriding_job_priority: bool | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        include_job_definitions_without_tenant_id: bool | None = None,
    ) -> Any:
        """Get Job Definition Count.

        Queries for the number of job definitions that fulfill given parameters.
        Takes the same parameters as the Get Job Definitions method.

        GET /job-definition/count
        """
        return self._call(
            "GET",
            "/job-definition/count",
            params={
                "jobDefinitionId": job_definition_id,
                "activityIdIn": activity_id_in,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "jobType": job_type,
                "jobConfiguration": job_configuration,
                "active": active,
                "suspended": suspended,
                "withOverridingJobPriority": with_overriding_job_priority,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "includeJobDefinitionsWithoutTenantId": include_job_definitions_without_tenant_id,
            },
        )

    def query_job_definitions(
        self,
        *,
        first_result: int | None = None,
        max_results: int | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get Job Definitions (POST).

        Queries for job definitions that fulfill given parameters. This method is
        slightly more powerful than the Get Job Definitions method because it allows
        filtering by multiple job definitions of types `String`, `Number` or
        `Boolean`. Request body: an object with jobDefinitionId, activityIdIn,
        processDefinitionId, processDefinitionKey, jobType, jobConfiguration,
        active, suspended, withOverridingJobPriority, tenantIdIn, withoutTenantId,
        includeJobDefinitionsWithoutTenantId, sorting.

        POST /job-definition
        """
        return self._call(
            "POST",
            "/job-definition",
            params={
                "firstResult": first_result,
                "maxResults": max_results,
            },
            body=body,
        )

    def query_job_definitions_count(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Get Job Definition Count (POST).

        Queries for the number of job definitions that fulfill given parameters.
        This method takes the same message body as the Get Job Definitions (POST)
        method and therefore it is slightly more powerful than the Get Job
        Definition Count method. Request body: an object with jobDefinitionId,
        activityIdIn, processDefinitionId, processDefinitionKey, jobType,
        jobConfiguration, active, suspended, withOverridingJobPriority, tenantIdIn,
        withoutTenantId, includeJobDefinitionsWithoutTenantId, sorting.

        POST /job-definition/count
        """
        return self._call(
            "POST",
            "/job-definition/count",
            body=body,
        )

    def set_job_priority_job_definition(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Set Job Definition Priority by Id.

        Sets an overriding execution priority for jobs with the given definition id.
        Optionally, the priorities of all the definitions' existing jobs are updated
        accordingly. The priority can be reset by setting it to `null`, meaning that
        a new job's priority will not be determined based on its definition's
        priority any longer. See the user guide on job prioritization for details.
        Request body: an object with priority, includeJobs.

        PUT /job-definition/{id}/jobPriority
        """
        return self._call(
            "PUT",
            "/job-definition/{id}/jobPriority",
            path={"id": id},
            body=body,
        )

    def set_job_retries_job_definition(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Set Job Retries By Job Definition Id.

        Sets the number of retries of all **failed** jobs associated with the given
        job definition id. Request body: an object with retries.

        PUT /job-definition/{id}/retries
        """
        return self._call(
            "PUT",
            "/job-definition/{id}/retries",
            path={"id": id},
            body=body,
        )

    def update_suspension_state_job_definition(
        self,
        id: str,
        *,
        body: Any = None,
    ) -> Any:
        """Activate/Suspend Job Definition By Id.

        Activates or suspends a given job definition by id.

        PUT /job-definition/{id}/suspended
        """
        return self._call(
            "PUT",
            "/job-definition/{id}/suspended",
            path={"id": id},
            body=body,
        )

    def update_suspension_state_job_definitions(
        self,
        *,
        body: Any = None,
    ) -> Any:
        """Activate/Suspend Job Definitions.

        Activates or suspends job definitions with the given process definition id
        or process definition key.

        PUT /job-definition/suspended
        """
        return self._call(
            "PUT",
            "/job-definition/suspended",
            body=body,
        )
