from __future__ import annotations

import pytest

from camunda_mcp.api.api_client_base import ApiClientBase


class _Response:
    def __init__(
        self,
        body: bytes = b'{}',
        *,
        status: int = 200,
        headers: dict[str, str] | None = None,
    ) -> None:
        self._body = body
        self.status_code = status
        self.headers = {"Content-Type": "application/json", **(headers or {})}
        self.encoding = "utf-8"
        self.closed = False

    def iter_content(self, chunk_size: int):
        for offset in range(0, len(self._body), chunk_size):
            yield self._body[offset : offset + chunk_size]

    def close(self) -> None:
        self.closed = True


class _Session:
    def __init__(self, response: _Response) -> None:
        self.response = response
        self.kwargs = None

    def request(self, **kwargs):
        self.kwargs = kwargs
        return self.response


def test_rejects_unconfigured_absolute_origin() -> None:
    client = ApiClientBase("https://configured.example")

    with pytest.raises(ValueError, match="not configured"):
        client.request("GET", "https://other.example/resource")


def test_request_is_bounded_and_redirects_are_disabled() -> None:
    response = _Response(b'{"ok": true}')
    session = _Session(response)
    client = ApiClientBase("https://configured.example", timeout_seconds=7)
    client._session = session

    assert client.request("GET", "/resource") == {"ok": True}
    assert session.kwargs["timeout"] == 7
    assert session.kwargs["allow_redirects"] is False
    assert session.kwargs["stream"] is True
    assert response.closed is True


def test_rejects_oversized_or_redirected_response() -> None:
    oversized = _Response(b"0123456789")
    client = ApiClientBase("https://configured.example", max_response_bytes=8)
    client._session = _Session(oversized)
    with pytest.raises(RuntimeError, match="size limit"):
        client.request("GET", "/resource")
    assert oversized.closed is True

    redirect = _Response(b"", status=302, headers={"Location": "https://other"})
    client = ApiClientBase("https://configured.example")
    client._session = _Session(redirect)
    with pytest.raises(RuntimeError, match="HTTP 302"):
        client.request("GET", "/resource")
    assert redirect.closed is True


@pytest.mark.parametrize(
    "url",
    [
        "file:///tmp/data",
        "https://user:secret@example.test",
        "https://example.test/path#fragment",
    ],
)
def test_rejects_unsafe_configured_urls(url: str) -> None:
    with pytest.raises(ValueError, match="invalid"):
        ApiClientBase(url)
