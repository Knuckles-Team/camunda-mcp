"""Identity credentials loader for the Camunda client facade."""

from agent_utilities.base_utilities import get_logger
from agent_utilities.core.config import setting

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
    platform = setting("CAMUNDA_PLATFORM", "7")
    verify = setting("CAMUNDA_SSL_VERIFY", True)

    v7_kwargs = {
        "base_url": setting("CAMUNDA7_URL", "http://localhost:8080/engine-rest"),
        "token": setting("CAMUNDA7_TOKEN", None) or None,
        "username": setting("CAMUNDA7_USERNAME", None) or None,
        "password": setting("CAMUNDA7_PASSWORD", None) or None,
        "verify": verify,
    }

    v8_kwargs = {
        "zeebe_url": setting("CAMUNDA8_ZEEBE_REST_URL", "http://localhost:8080"),
        "operate_url": setting("CAMUNDA8_OPERATE_URL", None) or None,
        "tasklist_url": setting("CAMUNDA8_TASKLIST_URL", None) or None,
        "client_id": setting("CAMUNDA8_CLIENT_ID", None) or None,
        "client_secret": setting("CAMUNDA8_CLIENT_SECRET", None) or None,
        "oauth_url": setting("CAMUNDA8_OAUTH_URL", None) or None,
        "audience": setting("CAMUNDA8_AUDIENCE", "zeebe.camunda.io"),
        "verify": verify,
    }

    return Api(platform=platform, v7_kwargs=v7_kwargs, v8_kwargs=v8_kwargs)
