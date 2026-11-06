"""Operaton / Camunda 7 engine REST: the Historic User Operation Log operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7HistoricUserOperationLog(ApiClientBase):
    """Historic User Operation Log: 4 engine REST operation(s)."""

    def clear_annotation_user_operation_log(
        self,
        operation_id: str,
    ) -> Any:
        """Clear Annotation of an User Operation Log (Historic).

        Clear the annotation which was previously set for auditing reasons.

        PUT /history/user-operation/{operationId}/clear-annotation
        """
        return self._call(
            "PUT",
            "/history/user-operation/{operationId}/clear-annotation",
            path={"operationId": operation_id},
        )

    def query_user_operation_count(
        self,
        *,
        deployment_id: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        process_instance_id: str | None = None,
        execution_id: str | None = None,
        case_definition_id: str | None = None,
        case_instance_id: str | None = None,
        case_execution_id: str | None = None,
        task_id: str | None = None,
        external_task_id: str | None = None,
        batch_id: str | None = None,
        job_id: str | None = None,
        job_definition_id: str | None = None,
        user_id: str | None = None,
        operation_id: str | None = None,
        operation_type: str | None = None,
        entity_type: str | None = None,
        entity_type_in: str | None = None,
        category: str | None = None,
        category_in: str | None = None,
        property: str | None = None,
        after_timestamp: str | None = None,
        before_timestamp: str | None = None,
    ) -> Any:
        """Get User Operation Log Count.

        Queries for the number of user operation log entries that fulfill the given
        parameters. Takes the same parameters as the Get User Operation Log
        (Historic) method.

        GET /history/user-operation/count
        """
        return self._call(
            "GET",
            "/history/user-operation/count",
            params={
                "deploymentId": deployment_id,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "processInstanceId": process_instance_id,
                "executionId": execution_id,
                "caseDefinitionId": case_definition_id,
                "caseInstanceId": case_instance_id,
                "caseExecutionId": case_execution_id,
                "taskId": task_id,
                "externalTaskId": external_task_id,
                "batchId": batch_id,
                "jobId": job_id,
                "jobDefinitionId": job_definition_id,
                "userId": user_id,
                "operationId": operation_id,
                "operationType": operation_type,
                "entityType": entity_type,
                "entityTypeIn": entity_type_in,
                "category": category,
                "categoryIn": category_in,
                "property": property,
                "afterTimestamp": after_timestamp,
                "beforeTimestamp": before_timestamp,
            },
        )

    def query_user_operation_entries(
        self,
        *,
        deployment_id: str | None = None,
        process_definition_id: str | None = None,
        process_definition_key: str | None = None,
        process_instance_id: str | None = None,
        execution_id: str | None = None,
        case_definition_id: str | None = None,
        case_instance_id: str | None = None,
        case_execution_id: str | None = None,
        task_id: str | None = None,
        external_task_id: str | None = None,
        batch_id: str | None = None,
        job_id: str | None = None,
        job_definition_id: str | None = None,
        user_id: str | None = None,
        operation_id: str | None = None,
        operation_type: str | None = None,
        entity_type: str | None = None,
        entity_type_in: str | None = None,
        category: str | None = None,
        category_in: str | None = None,
        property: str | None = None,
        after_timestamp: str | None = None,
        before_timestamp: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get User Operation Log (Historic).

        Queries for user operation log entries that fulfill the given parameters.
        The size of the result set can be retrieved by using the Get User Operation
        Log Count method. Note that the properties of operation log entries are
        interpreted as restrictions on the entities they apply to. That means, if a
        single process instance is updated, the field `processInstanceId` is
        populated.

        GET /history/user-operation
        """
        return self._call(
            "GET",
            "/history/user-operation",
            params={
                "deploymentId": deployment_id,
                "processDefinitionId": process_definition_id,
                "processDefinitionKey": process_definition_key,
                "processInstanceId": process_instance_id,
                "executionId": execution_id,
                "caseDefinitionId": case_definition_id,
                "caseInstanceId": case_instance_id,
                "caseExecutionId": case_execution_id,
                "taskId": task_id,
                "externalTaskId": external_task_id,
                "batchId": batch_id,
                "jobId": job_id,
                "jobDefinitionId": job_definition_id,
                "userId": user_id,
                "operationId": operation_id,
                "operationType": operation_type,
                "entityType": entity_type,
                "entityTypeIn": entity_type_in,
                "category": category,
                "categoryIn": category_in,
                "property": property,
                "afterTimestamp": after_timestamp,
                "beforeTimestamp": before_timestamp,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def set_annotation_user_operation_log(
        self,
        operation_id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Set Annotation to an User Operation Log (Historic).

        Set an annotation for auditing reasons. Request body: an object with
        annotation.

        PUT /history/user-operation/{operationId}/set-annotation
        """
        return self._call(
            "PUT",
            "/history/user-operation/{operationId}/set-annotation",
            path={"operationId": operation_id},
            body=body,
        )
