"""Operaton / Camunda 7 engine REST: the Event Subscription operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7EventSubscription(ApiClientBase):
    """Event Subscription: 2 engine REST operation(s)."""

    def get_event_subscriptions(
        self,
        *,
        event_subscription_id: str | None = None,
        event_name: str | None = None,
        event_type: str | None = None,
        execution_id: str | None = None,
        process_instance_id: str | None = None,
        activity_id: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        include_event_subscriptions_without_tenant_id: bool | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get List.

        Queries for event subscriptions that fulfill given parameters. The size of
        the result set can be retrieved by using the Get Event Subscriptions count
        method.

        GET /event-subscription
        """
        return self._call(
            "GET",
            "/event-subscription",
            params={
                "eventSubscriptionId": event_subscription_id,
                "eventName": event_name,
                "eventType": event_type,
                "executionId": execution_id,
                "processInstanceId": process_instance_id,
                "activityId": activity_id,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "includeEventSubscriptionsWithoutTenantId": include_event_subscriptions_without_tenant_id,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def get_event_subscriptions_count(
        self,
        *,
        event_subscription_id: str | None = None,
        event_name: str | None = None,
        event_type: str | None = None,
        execution_id: str | None = None,
        process_instance_id: str | None = None,
        activity_id: str | None = None,
        tenant_id_in: str | None = None,
        without_tenant_id: bool | None = None,
        include_event_subscriptions_without_tenant_id: bool | None = None,
    ) -> Any:
        """Get List Count.

        Queries for the number of event subscriptions that fulfill given parameters.
        Takes the same parameters as the Get Event Subscriptions method.

        GET /event-subscription/count
        """
        return self._call(
            "GET",
            "/event-subscription/count",
            params={
                "eventSubscriptionId": event_subscription_id,
                "eventName": event_name,
                "eventType": event_type,
                "executionId": execution_id,
                "processInstanceId": process_instance_id,
                "activityId": activity_id,
                "tenantIdIn": tenant_id_in,
                "withoutTenantId": without_tenant_id,
                "includeEventSubscriptionsWithoutTenantId": include_event_subscriptions_without_tenant_id,
            },
        )
