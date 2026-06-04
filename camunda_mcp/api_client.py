"""Public client facade for camunda_mcp.

Exposes a single ``Api`` object that holds both platform clients:

* ``api.v7`` -> :class:`~camunda_mcp.api.api_client_camunda7.Camunda7Api`
* ``api.v8`` -> :class:`~camunda_mcp.api.api_client_camunda8.Camunda8Api`

Both are constructed lazily so a server configured for only one platform never
needs the other's URLs/credentials.
"""

from typing import Any

from camunda_mcp.api.api_client_camunda7 import Camunda7Api
from camunda_mcp.api.api_client_camunda8 import Camunda8Api

__version__ = "0.2.0"


class Api:
    """Facade holding both Camunda 7 and Camunda 8 clients."""

    def __init__(
        self,
        platform: str = "7",
        v7_kwargs: dict[str, Any] | None = None,
        v8_kwargs: dict[str, Any] | None = None,
    ):
        self.platform = str(platform)
        self._v7_kwargs = v7_kwargs or {}
        self._v8_kwargs = v8_kwargs or {}
        self._v7: Camunda7Api | None = None
        self._v8: Camunda8Api | None = None

    @property
    def v7(self) -> Camunda7Api:
        """The Camunda 7 Engine REST client (lazily constructed)."""
        if self._v7 is None:
            self._v7 = Camunda7Api(**self._v7_kwargs)
        return self._v7

    @property
    def v8(self) -> Camunda8Api:
        """The Camunda 8 REST client (lazily constructed)."""
        if self._v8 is None:
            self._v8 = Camunda8Api(**self._v8_kwargs)
        return self._v8

    def client(self, platform: str | None = None) -> Camunda7Api | Camunda8Api:
        """Return the platform client (defaults to the configured platform)."""
        plat = str(platform or self.platform)
        return self.v8 if plat in ("8", "c8") else self.v7
