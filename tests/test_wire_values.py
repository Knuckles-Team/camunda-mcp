"""CONN-CAMUNDA-MCP-R004: query values reach the engine in the form it parses."""

import requests

from camunda_mcp.api.api_client_camunda7 import Camunda7Api


class _Response:
    status_code = 200
    headers = {"Content-Type": "application/json"}
    encoding = "utf-8"

    def __init__(self, body: bytes = b"[]"):
        self._body = body

    def iter_content(self, chunk_size):
        yield self._body

    def close(self):
        pass


def _capture(monkeypatch, response=None):
    sent = {}

    def fake(self, method, url, **kwargs):
        prepared = requests.Request(
            method,
            url,
            params=kwargs.get("params"),
            data=kwargs.get("data"),
            files=kwargs.get("files"),
            json=kwargs.get("json"),
        ).prepare()
        sent.update(method=method, url=prepared.url, body=prepared.body, kwargs=kwargs)
        return response or _Response()

    monkeypatch.setattr(requests.Session, "request", fake)
    return sent


def test_booleans_are_lowercase_and_unset_filters_dropped(monkeypatch):
    sent = _capture(monkeypatch)
    Camunda7Api("http://engine.test/engine-rest").get_process_definitions(
        latest_version=True, suspended=False, key="invoice"
    )
    assert sent["method"] == "GET"
    assert sent["url"] == (
        "http://engine.test/engine-rest/process-definition"
        "?key=invoice&latestVersion=true&suspended=false"
    )


def test_list_values_are_comma_separated():
    assert Camunda7Api._wire_params({"keysIn": ["a", "b"], "x": None}) == {
        "keysIn": "a,b"
    }


def test_path_parameters_are_escaped(monkeypatch):
    sent = _capture(monkeypatch, _Response(b"{}"))
    Camunda7Api("http://engine.test/engine-rest").set_process_instance_variable(
        "pi/1", "my var", body={"value": 1, "type": "Integer"}
    )
    assert sent["method"] == "PUT"
    assert sent["url"].endswith("/process-instance/pi%2F1/variables/my%20var")
    assert sent["kwargs"]["json"] == {"value": 1, "type": "Integer"}


def test_deployment_sends_resources_as_multipart(monkeypatch):
    sent = _capture(monkeypatch, _Response(b"{}"))
    Camunda7Api("http://engine.test/engine-rest").create_deployment(
        deployment_name="zz",
        enable_duplicate_filtering=True,
        resources={"p.bpmn": "<definitions/>"},
    )
    assert sent["url"].endswith("/deployment/create")
    assert sent["kwargs"]["data"] == {
        "deployment-name": "zz",
        "enable-duplicate-filtering": "true",
    }
    assert set(sent["kwargs"]["files"]) == {"p.bpmn"}
    assert b"<definitions/>" in sent["body"]


def test_engine_error_message_is_surfaced(monkeypatch):
    class _Bad(_Response):
        status_code = 400

    _capture(
        monkeypatch, _Bad(b'{"type":"InvalidRequestException","message":"bad value"}')
    )
    try:
        Camunda7Api("http://engine.test/engine-rest").get_tasks(assignee="x")
    except RuntimeError as exc:
        assert "HTTP 400" in str(exc) and "bad value" in str(exc)
    else:
        raise AssertionError("expected an error")
