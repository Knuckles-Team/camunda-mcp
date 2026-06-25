# Camunda Mcp
## API | MCP Server | A2A Agent

![PyPI - Version](https://img.shields.io/pypi/v/camunda-mcp)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
![PyPI - Downloads](https://img.shields.io/pypi/dd/camunda-mcp)
![GitHub Repo stars](https://img.shields.io/github/stars/Knuckles-Team/camunda-mcp)
![GitHub forks](https://img.shields.io/github/forks/Knuckles-Team/camunda-mcp)
![GitHub contributors](https://img.shields.io/github/contributors/Knuckles-Team/camunda-mcp)
![PyPI - License](https://img.shields.io/pypi/l/camunda-mcp)
![GitHub](https://img.shields.io/github/license/Knuckles-Team/camunda-mcp)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Knuckles-Team/camunda-mcp)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Knuckles-Team/camunda-mcp)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Knuckles-Team/camunda-mcp)
![GitHub issues](https://img.shields.io/github/issues/Knuckles-Team/camunda-mcp)
![GitHub top language](https://img.shields.io/github/languages/top/Knuckles-Team/camunda-mcp)
![GitHub language count](https://img.shields.io/github/languages/count/Knuckles-Team/camunda-mcp)
![GitHub repo size](https://img.shields.io/github/repo-size/Knuckles-Team/camunda-mcp)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/Knuckles-Team/camunda-mcp)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/camunda-mcp)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/camunda-mcp)

Camunda (7 & 8) process automation **API + MCP Server + A2A Agent** for the
agent-utilities ecosystem.

*Version: 0.5.0*

> **Documentation** — Installation, deployment, usage across the API, CLI, and MCP
> interfaces, and guidance for provisioning the Camunda platform are maintained in the
> [official documentation](https://knuckles-team.github.io/camunda-mcp/).

`camunda-mcp` wraps the Camunda process automation APIs with thin, deterministic MCP
tools, targeting both platforms from a single server: the **Camunda 7** Engine REST
API and the **Camunda 8** Zeebe / Operate / Tasklist REST APIs. It additionally ships
an **A2A agent server** that exposes the same capability through a Pydantic-AI graph
agent for agent-to-agent orchestration.

## What it provides

- **`Api`** (`camunda_mcp.api_client`) — a facade holding both the Camunda 7 Engine
  REST client (`Camunda7Api`) and the Camunda 8 Zeebe / Operate / Tasklist client
  (`Camunda8Api`), each constructed lazily so a server configured for one platform
  never needs the other's URLs or credentials.
- **Action-dispatch MCP tools** (`camunda-mcp` console script): `camunda_process`,
  `camunda_instance`, `camunda_task`, `camunda_deploy`, `camunda_message`,
  `camunda_external_task`, `camunda_job`, `camunda_history`, `camunda_deployment`,
  and `camunda_ops`. Each takes a `platform` argument (`7` or `8`). See
  [`docs/overview.md`](docs/overview.md) for the full surface.
- **An A2A agent server** (`camunda-agent` console script, described by
  [`a2a.json`](a2a.json)) wrapping the tool surface in a Pydantic-AI graph agent.

## Available MCP Tools

_Auto-generated — do not edit (synced by the `mcp-readme-table` pre-commit hook)._

<!-- MCP-TOOLS-TABLE:START -->

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `camunda_deploy` | `CAMUNDATOOL` | Deploy a BPMN/DMN/form resource to Camunda 7 or Camunda 8. |
| `camunda_deployment` | `CAMUNDATOOL` | Manage Camunda 7 deployments (list/get/delete). |
| `camunda_external_task` | `CAMUNDATOOL` | Camunda 7 external task worker operations. |
| `camunda_history` | `CAMUNDATOOL` | Query Camunda 7 historic data. |
| `camunda_instance` | `CAMUNDATOOL` | Work with process instances on Camunda 7 or Camunda 8. |
| `camunda_job` | `CAMUNDATOOL` | Manage jobs and incidents on Camunda 7 or Camunda 8. |
| `camunda_message` | `CAMUNDATOOL` | Correlate/publish a message or broadcast a signal. |
| `camunda_ops` | `CAMUNDATOOL` | Search Camunda 8 Operate / Tasklist surfaces. |
| `camunda_process` | `CAMUNDATOOL` | Work with process definitions on Camunda 7 or Camunda 8. |
| `camunda_task` | `CAMUNDATOOL` | Work with user tasks on Camunda 7 or Camunda 8 (Tasklist). |

_10 action-routed tools (default `MCP_TOOL_MODE=condensed`). Each is enabled unless its toggle is set false; set `MCP_TOOL_MODE=verbose` (or `both`) for the 1:1 per-operation surface. Auto-generated — do not edit._
<!-- MCP-TOOLS-TABLE:END -->

## Environment Variables

Every variable the server reads, grouped by purpose. Credentials left blank leave the
corresponding platform inactive — the connector remains inactive when credentials are
absent. A starter [`.env.example`](.env.example) ships with the repository; copy it to
`.env` and populate the values for the platform you use.

### Connection & Credentials
| Var | Default | Meaning |
|---|---|---|
| `CAMUNDA_PLATFORM` | `7` | Target platform: `7` or `8` |
| `CAMUNDA_SSL_VERIFY` | `True` | Verify TLS (set `False` for self-signed homelab) |
| `CAMUNDA7_URL` | `http://localhost:8080/engine-rest` | Camunda 7 Engine REST base URL |
| `CAMUNDA7_TOKEN` / `CAMUNDA7_USERNAME` / `CAMUNDA7_PASSWORD` | — | Camunda 7 bearer or basic auth |
| `CAMUNDA8_ZEEBE_REST_URL` | `http://localhost:8080` | Camunda 8 Zeebe REST base URL |
| `CAMUNDA8_OPERATE_URL` / `CAMUNDA8_TASKLIST_URL` | — | Camunda 8 Operate / Tasklist URLs |
| `CAMUNDA8_CLIENT_ID` / `CAMUNDA8_CLIENT_SECRET` / `CAMUNDA8_OAUTH_URL` / `CAMUNDA8_AUDIENCE` | — | Camunda 8 OAuth `client_credentials` |

### MCP server / transport
| Variable | Description | Default |
|----------|-------------|---------|
| `TRANSPORT` | `stdio`, `streamable-http`, or `sse` | `stdio` |
| `HOST` | Bind host (HTTP transports) | `0.0.0.0` |
| `PORT` | Bind port (HTTP transports) | `8000` |
| `MCP_TOOL_MODE` | Tool surface: `condensed`, `verbose`, or `both` | `condensed` |
| `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS` | Comma-separated tool allow/deny list | — |
| `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS` | Comma-separated tag allow/deny list | — |
| `DEBUG` | Verbose logging | `False` |
| `PYTHONUNBUFFERED` | Unbuffered stdout (recommended in containers) | `1` |

### Tool toggles
Each action-routed tool can be disabled individually via its toggle env var (set to `false`).
See the [Available MCP Tools](#available-mcp-tools) table above for the authoritative names.

| Variable | Description | Default |
|----------|-------------|---------|
| `CAMUNDATOOL` | Register the Camunda tool set | `True` |

### Telemetry & governance
| Variable | Description | Default |
|----------|-------------|---------|
| `ENABLE_OTEL` | Enable OpenTelemetry export | `True` |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP collector endpoint | — |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` / `OTEL_EXPORTER_OTLP_SECRET_KEY` | OTLP auth keys | — |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | OTLP protocol (e.g. `http/protobuf`) | — |
| `EUNOMIA_TYPE` | Authorization mode: `none`, `embedded`, `remote` | `none` |
| `EUNOMIA_POLICY_FILE` | Embedded policy file | `mcp_policies.json` |
| `EUNOMIA_REMOTE_URL` | Remote Eunomia server URL | — |

### Agent CLI (full `[agent]` runtime only)
| Variable | Description | Default |
|----------|-------------|---------|
| `MCP_URL` | URL of the MCP server the agent connects to | `http://localhost:8000/mcp` |
| `PROVIDER` | LLM provider (e.g. `openai`) | `openai` |
| `MODEL_ID` | Model id (e.g. `gpt-4o`) | `gpt-4o` |
| `ENABLE_WEB_UI` | Serve the AG-UI web interface | `True` |

## Installation

Pick the extra that matches what you want to run:

| Extra | Installs | Use when |
|-------|----------|----------|
| `camunda-mcp[mcp]` | Slim MCP server only (`agent-utilities[mcp]` — FastMCP/FastAPI) | You only run the **MCP server** (smallest install / image) |
| `camunda-mcp[agent]` | Full agent runtime (`agent-utilities[agent,logfire]` — Pydantic AI + the epistemic-graph engine) | You run the **integrated agent** |
| `camunda-mcp[all]` | Everything (`mcp` + `agent`) | Development / both surfaces |

```bash
# MCP server only (recommended for tool hosting — slim deps)
uv pip install "camunda-mcp[mcp]"

# Full agent runtime (Pydantic AI + epistemic-graph engine)
uv pip install "camunda-mcp[agent]"

# Everything (development)
uv pip install "camunda-mcp[all]"      # or: python -m pip install "camunda-mcp[all]"
```

Run the servers:

```bash
camunda-mcp                       # stdio MCP server (default transport)
camunda-mcp --transport streamable-http --host 0.0.0.0 --port 8000

# A2A agent server against a deployed MCP endpoint
MCP_URL=http://camunda-mcp:8000/mcp camunda-agent --host 0.0.0.0 --port 8001
```

### Container images (`:mcp` vs `:agent`)

One multi-stage `docker/Dockerfile` builds two right-sized images, selected by `--target`:

| Image tag | Build target | Contents | Entrypoint |
|-----------|--------------|----------|------------|
| `knucklessg1/camunda-mcp:mcp` | `--target mcp` | `camunda-mcp[mcp]` — **slim**, no engine/`pydantic-ai`/`dspy`/`llama-index`/`tree-sitter` | `camunda-mcp` |
| `knucklessg1/camunda-mcp:latest` | `--target agent` (default) | `camunda-mcp[agent]` — **full** agent runtime + epistemic-graph engine | `camunda-agent` |

```bash
docker build --target mcp   -t knucklessg1/camunda-mcp:mcp    docker/   # slim MCP server
docker build --target agent -t knucklessg1/camunda-mcp:latest docker/   # full agent
```

`docker/mcp.compose.yml` runs the slim `:mcp` server; `docker/agent.compose.yml` runs the
agent (`:latest`) with a co-located `:mcp` sidecar.

### Knowledge-graph database (`epistemic-graph`)

The **full agent** (`[agent]` / `:latest`) embeds the **epistemic-graph** engine (pulled in
transitively via `agent-utilities[agent]`). For production — or to share one knowledge graph
across multiple agents — run **epistemic-graph as its own database container** and point the
agent at it instead of embedding it. Deployment recipes (single-node + Raft HA), connection
config, and the full database architecture (with diagrams) are documented in the
[epistemic-graph deployment guide](https://knuckles-team.github.io/epistemic-graph/deployment/).
The slim `[mcp]` server does **not** require the database.

## MCP config

Register in the multiplexer under nickname `camun` (tools surface as
`camun__process`, `camun__instance`, `camun__task`, …). See
`camunda_mcp/mcp_config.json`.

<!-- BEGIN GENERATED: additional-deployment-options -->
### Additional Deployment Options

`camunda-mcp` can also run as a **local container** (Docker / Podman / `uv`) or be
consumed from a **remote deployment**. The
[Deployment guide](https://knuckles-team.github.io/camunda-mcp/deployment/) has full, copy-paste
`mcp_config.json` for all four transports — **stdio**, **streamable-http**,
**local container / uv**, and **remote URL**:

- **Local container / uv** — launch the server from `mcp_config.json` via `uvx`,
  `docker run`, or `podman run`, or point at a local streamable-http container by `url`.
- **Remote URL** — connect to a server deployed behind Caddy at
  `http://camunda-mcp.arpa/mcp` using the `"url"` key.
<!-- END GENERATED: additional-deployment-options -->

## Documentation

The complete documentation is published as the
[official documentation site](https://knuckles-team.github.io/camunda-mcp/) and is the
recommended reference for installation, deployment, and day-to-day operation.

| Page | Contents |
|---|---|
| [Installation](https://knuckles-team.github.io/camunda-mcp/installation/) | pip, source, extras, prebuilt Docker image |
| [Deployment](https://knuckles-team.github.io/camunda-mcp/deployment/) | run the MCP and agent servers, Compose, Caddy + Technitium, env config |
| [Usage](https://knuckles-team.github.io/camunda-mcp/usage/) | the MCP tools, the `Api` client, the CLI |
| [Backing Platform](https://knuckles-team.github.io/camunda-mcp/platform/) | deploy Camunda with Docker |
| [Overview](https://knuckles-team.github.io/camunda-mcp/overview/) | the Camunda 7 / Camunda 8 surface |
| [Concepts](https://knuckles-team.github.io/camunda-mcp/concepts/) | concept registry (`CONCEPT:CAMUNDA-*`) |

`AGENTS.md` is the canonical contributor/agent guidance.


<!-- BEGIN agent-os-genesis-deploy (generated; do not edit between markers) -->

## Deploy with `agent-os-genesis`

This package can be provisioned for you — skill-guided — by the **`agent-os-genesis`**
universal skill (its *single-package deploy mode*): it picks your install method, seeds
secrets to OpenBao/Vault (or `.env`), trusts your enterprise CA, registers the MCP
server, and verifies it — the same machinery that stands up the whole Agent OS, narrowed
to just this package. Ask your agent to **"deploy `camunda-mcp` with agent-os-genesis"**.

| Install mode | Command |
|------|---------|
| Bare-metal, prod (PyPI) | `uvx camunda-mcp` · or `uv tool install camunda-mcp` |
| Bare-metal, dev (editable) | `uv pip install -e ".[all]"` · or `pip install -e ".[all]"` |
| Container, prod | deploy `knucklessg1/camunda-mcp:latest` via docker-compose / swarm / podman / podman-compose / kubernetes |
| Container, dev (editable) | deploy `docker/compose.dev.yml` (source-mounted at `/src`; edits live on restart) |

Secrets are read-existing + seeded via `vault_sync` — you are only prompted for what's missing.

<!-- END agent-os-genesis-deploy -->
