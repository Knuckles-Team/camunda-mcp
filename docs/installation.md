# Installation

`camunda-mcp` is a standard Python package and a prebuilt container image. Pick the
path that matches how you want to run it.

## Requirements

- **Python 3.11 – 3.14**.
- A reachable **Camunda 7 Engine REST** endpoint and/or a **Camunda 8** cluster
  (Zeebe / Operate / Tasklist REST) — see [Backing Platform](platform.md) to deploy
  one locally.

## From PyPI (recommended)

```bash
pip install camunda-mcp
```

### Optional extras

The base install is intentionally minimal. Install the extra for what you need:

| Extra | Install | Pulls in |
|---|---|---|
| `mcp` | `pip install "camunda-mcp[mcp]"` | FastMCP MCP-server runtime (`agent-utilities[mcp]`) |
| `agent` | `pip install "camunda-mcp[agent]"` | Pydantic-AI agent + Logfire tracing (`agent-utilities[agent,logfire]`) |
| `all` | `pip install "camunda-mcp[all]"` | Everything above |
| `test` | `pip install "camunda-mcp[test]"` | `pytest`, `pytest-asyncio`, `pytest-cov`, `pytest-xdist` |

```bash
# Typical: run the MCP server and the A2A agent server
pip install "camunda-mcp[all]"
```

## From source

```bash
git clone https://github.com/Knuckles-Team/camunda-mcp.git
cd camunda-mcp
pip install -e ".[all]"          # editable install with every extra
```

With [`uv`](https://docs.astral.sh/uv/):

```bash
uv pip install -e ".[all]"
uv run camunda-mcp
```

## Prebuilt Docker image

A multi-stage, slim image is published on every release (entrypoint `camunda-mcp`):

```bash
docker pull knucklessg1/camunda-mcp:latest

docker run --rm -i \
  -e CAMUNDA_PLATFORM=7 \
  -e CAMUNDA7_URL=http://your-camunda:8080/engine-rest \
  knucklessg1/camunda-mcp:latest        # stdio transport (default)
```

For an HTTP server with a published port, see [Deployment](deployment.md).

## Verify the install

```bash
camunda-mcp --help
python -c "import camunda_mcp; print(camunda_mcp.__version__)"
```

## Next steps

- **[Deployment](deployment.md)** — run it as a long-lived MCP server and agent behind Caddy + DNS.
- **[Usage](usage.md)** — call the tools, the `Api` client, and the CLI.
- **[Configuration](deployment.md#configuration-environment)** — every environment variable.
