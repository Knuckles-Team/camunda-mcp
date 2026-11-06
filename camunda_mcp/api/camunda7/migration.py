"""Operaton / Camunda 7 engine REST: the Migration operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7Migration(ApiClientBase):
    """Migration: 4 engine REST operation(s)."""

    def execute_migration_plan(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Execute Migration Plan.

        Executes a migration plan synchronously for multiple process instances. To
        execute a migration plan asynchronously, use the Execute Migration Plan
        Async(Batch) method. For more information about the difference between
        synchronous and asynchronous execution of a migration plan, please refer to
        the related section of the user guide. Request body: an object with
        migrationPlan, processInstanceIds, processInstanceQuery,
        skipCustomListeners, skipIoMappings.

        POST /migration/execute
        """
        return self._call(
            "POST",
            "/migration/execute",
            body=body,
        )

    def execute_migration_plan_async(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Execute Migration Plan Async (Batch).

        Executes a migration plan asynchronously (batch) for multiple process
        instances. To execute a migration plan synchronously, use the Execute
        MigrationPlan method. For more information about the difference between
        synchronous and asynchronous execution of a migration plan, please refer to
        the related section of the user guide. Request body: an object with
        migrationPlan, processInstanceIds, processInstanceQuery,
        skipCustomListeners, skipIoMappings.

        POST /migration/executeAsync
        """
        return self._call(
            "POST",
            "/migration/executeAsync",
            body=body,
        )

    def generate_migration_plan(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Generate Migration Plan.

        Generates a migration plan for two process definitions. The generated
        migration plan contains migration instructions which map equal activities
        between the two process definitions. Request body: an object with
        sourceProcessDefinitionId, targetProcessDefinitionId, updateEventTriggers,
        variables.

        POST /migration/generate
        """
        return self._call(
            "POST",
            "/migration/generate",
            body=body,
        )

    def validate_migration_plan(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Validate Migration Plan.

        Validates a migration plan statically without executing it. This corresponds
        to the creation time validation described in the user guide. Request body:
        an object with sourceProcessDefinitionId, targetProcessDefinitionId,
        instructions, variables.

        POST /migration/validate
        """
        return self._call(
            "POST",
            "/migration/validate",
            body=body,
        )
