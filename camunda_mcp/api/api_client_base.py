"""Shared HTTP base client for the Camunda API wrapper."""

from typing import Any
from urllib.parse import urljoin

import requests
import urllib3


class ApiClientBase:
    """Thin requests.Session wrapper with token / basic-auth support.

    Camunda speaks several content types (JSON for the engine REST and the
    Camunda 8 REST APIs, ``multipart/form-data`` for deployments). Callers pass
    an explicit ``content_type``/``accept`` so this base never forces JSON on a
    payload that needs otherwise.
    """

    def __init__(
        self,
        base_url: str,
        token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        verify: bool = True,
    ):
        self.base_url = base_url.rstrip("/") + "/"
        self.token = token
        self.username = username
        self.password = password
        self.last_etag: str | None = None
        self._session = requests.Session()
        self._session.verify = verify

        if not verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        if token:
            self._session.headers.update({"Authorization": f"Bearer {token}"})
        elif username and password:
            self._session.auth = (username, password)

    def request(
        self,
        method: str,
        endpoint: str,
        params: dict[str, Any] | None = None,
        data: Any | None = None,
        json: Any | None = None,
        files: Any | None = None,
        content_type: str | None = None,
        accept: str | None = None,
        headers: dict[str, str] | None = None,
    ) -> Any:
        """Perform an HTTP request and return parsed JSON, or raw text.

        Returns a dict when the response is JSON, otherwise
        ``{"status": "success", "text": <body>}``. Raises on HTTP >= 400.
        """
        if endpoint.startswith("http"):
            url = endpoint
        else:
            url = urljoin(self.base_url, endpoint.lstrip("/"))

        req_headers: dict[str, str] = {}
        if content_type:
            req_headers["Content-Type"] = content_type
        if accept:
            req_headers["Accept"] = accept
        if headers:
            req_headers.update(headers)

        response = self._session.request(
            method=method,
            url=url,
            headers=req_headers or None,
            params=params,
            data=data,
            json=json,
            files=files,
        )

        self.last_etag = response.headers.get("ETag")

        if response.status_code >= 400:
            raise Exception(f"API error: {response.status_code} - {response.text}")

        if response.status_code == 204 or not response.text.strip():
            return {"status": "success"}

        ctype = response.headers.get("Content-Type", "")
        if "json" in ctype:
            try:
                return response.json()
            except Exception:
                pass
        return {"status": "success", "text": response.text}
