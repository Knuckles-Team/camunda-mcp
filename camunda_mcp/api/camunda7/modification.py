"""Operaton / Camunda 7 engine REST: the Modification operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7Modification(ApiClientBase):
    """Modification: 2 engine REST operation(s)."""

    def execute_modification(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Execute Modification.

        Executes a modification synchronously for multiple process instances. To
        modify a single process instance, use the Modify Process Instance Execution
        State method. To execute a modification asynchronously, use the Execute
        Modification Async (Batch) method. Request body: an object with
        processDefinitionId, skipCustomListeners, skipIoMappings,
        processInstanceIds, processInstanceQuery, historicProcessInstanceQuery,
        instructions, annotation.

        POST /modification/execute
        """
        return self._call(
            "POST",
            "/modification/execute",
            body=body,
        )

    def execute_modification_async(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Execute Modification Async (Batch).

        Executes a modification asynchronously for multiple process instances. To
        execute a modification synchronously, use the Execute Modification method.
        For more information about the difference between synchronous and
        asynchronous execution of a modification, please refer to the related
        section of the user guide. Request body: an object with processDefinitionId,
        skipCustomListeners, skipIoMappings, processInstanceIds,
        processInstanceQuery, historicProcessInstanceQuery, instructions,
        annotation.

        POST /modification/executeAsync
        """
        return self._call(
            "POST",
            "/modification/executeAsync",
            body=body,
        )
