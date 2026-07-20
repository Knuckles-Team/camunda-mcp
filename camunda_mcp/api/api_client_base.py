"""Shared, bounded HTTP client for the Camunda API wrapper."""

import json as jsonlib
import math
from typing import Any
from urllib.parse import urljoin, urlsplit

import requests
from agent_utilities.core.transport_security import (
    ResolvedTLSProfile,
    resolve_configured_tls_profile,
)

DEFAULT_TIMEOUT_SECONDS = 30.0
DEFAULT_MAX_RESPONSE_BYTES = 8 * 1024 * 1024


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
        tls_profile: ResolvedTLSProfile | None = None,
        timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
        max_response_bytes: int = DEFAULT_MAX_RESPONSE_BYTES,
    ):
        self.base_url = self._validated_url(base_url).rstrip("/") + "/"
        self.token = token
        self.username = username
        self.password = password
        self.last_etag: str | None = None
        self.timeout_seconds = float(timeout_seconds)
        self.max_response_bytes = int(max_response_bytes)
        if not math.isfinite(self.timeout_seconds) or self.timeout_seconds <= 0:
            raise ValueError("Camunda timeout must be a finite positive number")
        if not 1 <= self.max_response_bytes <= 64 * 1024 * 1024:
            raise ValueError("Camunda response limit is outside the allowed range")

        self._allowed_origins = {self._origin(self.base_url)}
        self._session = requests.Session()
        self.tls_profile = tls_profile or resolve_configured_tls_profile("camunda")
        self.tls_profile.configure_requests_session(self._session)

        if token:
            self._session.headers.update({"Authorization": f"Bearer {token}"})
        elif username and password:
            self._session.auth = (username, password)

    @staticmethod
    def _validated_url(url: str) -> str:
        candidate = str(url).strip()
        parsed = urlsplit(candidate)
        if (
            parsed.scheme.lower() not in {"http", "https"}
            or not parsed.hostname
            or parsed.username is not None
            or parsed.password is not None
            or parsed.fragment
        ):
            raise ValueError("Camunda endpoint URL is invalid")
        return candidate

    @classmethod
    def _origin(cls, url: str) -> tuple[str, str, int]:
        parsed = urlsplit(cls._validated_url(url))
        scheme = parsed.scheme.lower()
        return (
            scheme,
            str(parsed.hostname).lower().rstrip("."),
            int(parsed.port or (443 if scheme == "https" else 80)),
        )

    def allow_origin(self, url: str | None) -> None:
        """Register one configured Camunda surface as an outbound capability."""

        if url:
            self._allowed_origins.add(self._origin(url))

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
        if urlsplit(endpoint).scheme:
            url = self._validated_url(endpoint)
        else:
            url = urljoin(self.base_url, endpoint.lstrip("/"))
        if self._origin(url) not in self._allowed_origins:
            raise ValueError("Camunda request origin was not configured")

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
            timeout=self.timeout_seconds,
            allow_redirects=False,
            stream=True,
        )
        try:
            self.last_etag = response.headers.get("ETag")
            if response.status_code >= 300:
                raise RuntimeError(f"Camunda API returned HTTP {response.status_code}")
            if response.status_code == 204:
                return {"status": "success"}

            declared_length = response.headers.get("Content-Length")
            if declared_length:
                try:
                    if int(declared_length) > self.max_response_bytes:
                        raise RuntimeError("Camunda response exceeded its size limit")
                except ValueError as exc:
                    raise RuntimeError("Camunda response length was invalid") from exc

            body = bytearray()
            for chunk in response.iter_content(chunk_size=64 * 1024):
                body.extend(chunk)
                if len(body) > self.max_response_bytes:
                    raise RuntimeError("Camunda response exceeded its size limit")
            if not body.strip():
                return {"status": "success"}

            ctype = response.headers.get("Content-Type", "").lower()
            if "json" in ctype:
                try:
                    return jsonlib.loads(body.decode(response.encoding or "utf-8"))
                except (UnicodeDecodeError, jsonlib.JSONDecodeError) as exc:
                    raise RuntimeError("Camunda returned invalid JSON") from exc
            return {
                "status": "success",
                "text": body.decode(response.encoding or "utf-8", errors="replace"),
            }
        finally:
            response.close()
