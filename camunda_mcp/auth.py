"""Identity credentials loader for the Camunda client facade."""

import os

from agent_utilities.base_utilities import get_logger, to_boolean

from camunda_mcp.api_client import Api

logger = get_logger(__name__)


def get_client() -> Api:
    """Build a configured Camunda :class:`Api` facade from the environment.

    Camunda 7 (Engine REST):
        ``CAMUNDA7_URL`` (default ``http://localhost:8080/engine-rest``),
        ``CAMUNDA7_TOKEN`` (bearer), ``CAMUNDA7_USERNAME``/``CAMUNDA7_PASSWORD``
        (basic auth).

    Camunda 8 (Zeebe/Operate/Tasklist REST):
        ``CAMUNDA8_ZEEBE_REST_URL`` (default ``http://localhost:8080``),
        ``CAMUNDA8_OPERATE_URL``, ``CAMUNDA8_TASKLIST_URL``,
        ``CAMUNDA8_CLIENT_ID``/``CAMUNDA8_CLIENT_SECRET``/``CAMUNDA8_OAUTH_URL``
        (client_credentials), ``CAMUNDA8_AUDIENCE``.

    Shared:
        ``CAMUNDA_PLATFORM`` (``7`` or ``8``, default ``7``),
        ``CAMUNDA_SSL_VERIFY`` (default ``True``).
    """
    platform = os.getenv("CAMUNDA_PLATFORM", "7")
    verify = to_boolean(os.getenv("CAMUNDA_SSL_VERIFY", "True"))

    v7_kwargs = {
        "base_url": os.getenv(
            "CAMUNDA7_URL", "http://localhost:8080/engine-rest"
        ),
        "token": os.getenv("CAMUNDA7_TOKEN") or None,
        "username": os.getenv("CAMUNDA7_USERNAME") or None,
        "password": os.getenv("CAMUNDA7_PASSWORD") or None,
        "verify": verify,
    }

    v8_kwargs = {
        "zeebe_url": os.getenv(
            "CAMUNDA8_ZEEBE_REST_URL", "http://localhost:8080"
        ),
        "operate_url": os.getenv("CAMUNDA8_OPERATE_URL") or None,
        "tasklist_url": os.getenv("CAMUNDA8_TASKLIST_URL") or None,
        "client_id": os.getenv("CAMUNDA8_CLIENT_ID") or None,
        "client_secret": os.getenv("CAMUNDA8_CLIENT_SECRET") or None,
        "oauth_url": os.getenv("CAMUNDA8_OAUTH_URL") or None,
        "audience": os.getenv("CAMUNDA8_AUDIENCE", "zeebe.camunda.io"),
        "verify": verify,
    }

    return Api(platform=platform, v7_kwargs=v7_kwargs, v8_kwargs=v8_kwargs)
