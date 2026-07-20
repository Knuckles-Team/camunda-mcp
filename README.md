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

#### Condensed action-routed tools (default — `MCP_TOOL_MODE=condensed`)

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

#### Verbose 1:1 API-mapped tools (`MCP_TOOL_MODE=verbose` or `both`)

<details>
<summary>1 per-operation tools — one per public API method (click to expand)</summary>

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `camunda_client` | `APITOOL` | Return the platform client (defaults to the configured platform). |

</details>

_10 action-routed tool(s) (default) · 1 verbose 1:1 tool(s). Each is enabled unless its `<DOMAIN>TOOL` toggle is set false; `MCP_TOOL_MODE` selects the surface (`condensed` default · `verbose` 1:1 · `both`). Auto-generated — do not edit._
<!-- MCP-TOOLS-TABLE:END -->

## Environment Variables

<!-- ENV-VARS-TABLE:START -->

#### Package environment variables

| Variable | Example | Description |
|----------|---------|-------------|
| `CAMUNDA_PLATFORM` | `7` | Platform selector: "7" (Engine REST) or "8" (Zeebe/Operate/Tasklist) |
| `CAMUNDA_TLS_PROFILE` | — | Verify TLS certificates for Camunda HTTP calls |
| `CAMUNDA_TLS_PROFILE_REF` | — |  |
| `CAMUNDA7_URL` | `http://localhost:8080/engine-rest` |  |
| `CAMUNDA7_TOKEN` | secret-injected |  |
| `CAMUNDA7_USERNAME` | `demo` |  |
| `CAMUNDA7_PASSWORD` | secret-injected |  |
| `CAMUNDA8_ZEEBE_REST_URL` | `http://localhost:8080` |  |
| `CAMUNDA8_OPERATE_URL` | `http://localhost:8081` |  |
| `CAMUNDA8_TASKLIST_URL` | `http://localhost:8082` |  |
| `CAMUNDA8_CLIENT_ID` | `changeme` |  |
| `CAMUNDA8_CLIENT_SECRET` | secret-injected |  |
| `CAMUNDA8_OAUTH_URL` | `https://login.cloud.camunda.io/oauth/token` |  |
| `CAMUNDA8_AUDIENCE` | `zeebe.camunda.io` |  |
| `CAMUNDATOOL` | `True` | Toggle registration of the Camunda tool group |

#### Inherited agent-utilities variables (apply to every connector)

| Variable | Example | Description |
|----------|---------|-------------|
| `TRANSPORT` | `stdio` | MCP transport: `stdio` \| `streamable-http` \| `sse` |
| `HOST` | `127.0.0.1` | Loopback bind host (set an authenticated ingress explicitly) |
| `PORT` | `8000` | Bind port (HTTP transports) |
| `MCP_TOOL_MODE` | `intent` | Tool surface: `intent` \| `condensed` \| `verbose` \| `both` |
| `MCP_ENABLED_TOOLS` | — | Comma-separated tool allow-list |
| `MCP_DISABLED_TOOLS` | — | Comma-separated tool deny-list |
| `MCP_ENABLED_TAGS` | — | Comma-separated tag allow-list |
| `MCP_DISABLED_TAGS` | — | Comma-separated tag deny-list |
| `EUNOMIA_TYPE` | `none` | Authorization mode: `none` \| `embedded` \| `remote` |
| `EUNOMIA_POLICY_FILE` | `mcp_policies.json` | Embedded Eunomia policy file |
| `EUNOMIA_REMOTE_URL` | — | Remote Eunomia authorization server URL |
| `ENABLE_OTEL` | `False` | Enable OpenTelemetry export |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | — | OTLP collector endpoint |
| `MCP_CLIENT_AUTH` | — | Outbound MCP child auth: `oidc-client-credentials` \| `basic` \| `none` |
| `OIDC_CLIENT_ID` | — | OIDC client id (service-account auth) |
| `OIDC_CLIENT_SECRET_REF` | `secret://identity/oidc-client-secret` | Runtime secret reference for the OIDC service account |
| `MCP_BASIC_AUTH_USERNAME` | — | HTTP Basic username (`MCP_CLIENT_AUTH=basic`) |
| `MCP_BASIC_AUTH_PASSWORD_REF` | `secret://identity/mcp-basic-password` | Runtime secret reference for HTTP Basic auth (`MCP_CLIENT_AUTH=basic`) |
| `DEBUG` | `False` | Verbose logging |
| `PYTHONUNBUFFERED` | `1` | Unbuffered stdout (recommended in containers) |
| `MCP_URL` | `http://localhost:8000/mcp` | URL of the MCP server the agent connects to |
| `PROVIDER` | `openai` | LLM provider for the agent |
| `MODEL_ID` | `gpt-4o` | Model id for the agent |
| `ENABLE_WEB_UI` | `True` | Serve the AG-UI web interface |

_15 package + 24 inherited variable(s). Auto-generated from `.env.example` + the shared agent-utilities set — do not edit._
<!-- ENV-VARS-TABLE:END -->


Every variable the server reads, grouped by purpose. Credentials left blank leave the
corresponding platform inactive — the connector remains inactive when credentials are
absent. A starter [`.env.example`](.env.example) ships with the repository; copy it to
`.env` and populate the values for the platform you use.

### Connection & Credentials
| Var | Default | Meaning |
|---|---|---|
| `CAMUNDA_PLATFORM` | `7` | Target platform: `7` or `8` |
| `CAMUNDA_TLS_PROFILE` | `system` | Named outbound TLS policy from AgentConfig |
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
| `camunda-mcp[mcp]` | Connector-focused MCP server (`agent-utilities[mcp]` — FastMCP/FastAPI + `epistemic-graph[full]`) | You only run the **MCP server** (smallest install / image) |
| `camunda-mcp[agent]` | Agent runtime (`agent-utilities[agent-runtime,logfire]` — model orchestration + `epistemic-graph[full]`) | You run the **integrated agent** |
| `camunda-mcp[all]` | Everything (`mcp` + `agent`) | Development / both surfaces |

```bash
# Connector-focused MCP server (includes the shared graph engine)
uv pip install "camunda-mcp[mcp]"

# Agent runtime (adds model orchestration to the shared graph engine)
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
| `example/camunda-mcp:mcp` | `--target mcp` | `camunda-mcp[mcp]` — **connector-focused**, includes `epistemic-graph[full]`; no model-orchestration stack | `camunda-mcp` |
| `example/camunda-mcp@sha256:<digest>` | `--target agent` (default) | `camunda-mcp[agent]` — **agent runtime**, model orchestration + `epistemic-graph[full]` | `camunda-agent` |

```bash
docker build --target mcp   -t example/camunda-mcp:mcp    docker/   # connector-focused MCP server
docker build --target agent -t example/camunda-mcp:agent-local docker/   # agent runtime
```

`docker/mcp.compose.yml` runs the connector-focused `:mcp` server; `docker/agent.compose.yml` runs the
agent (`immutable agent digest`) with a co-located `:mcp` sidecar.

### Knowledge-graph database (`epistemic-graph`)

Both `[mcp]` and `[agent]` carry the **epistemic-graph** engine through the required
Agent Utilities core dependency (`epistemic-graph[full]`). The `[mcp]` extra keeps
the server connector-focused; `[agent]` additionally enables model orchestration. Local
deployments can use the bundled engine. For production or shared state, run
**epistemic-graph as a dedicated database service** and configure the runtime to use it.
Deployment recipes (single-node + Raft HA), connection configuration, and architecture
diagrams are documented in the
[epistemic-graph deployment guide](https://knuckles-team.github.io/epistemic-graph/deployment/).

## MCP config

Register in the multiplexer under nickname `camun` (tools surface as
`camun__process`, `camun__instance`, `camun__task`, …). See
`camunda_mcp/mcp_config.json`.

<!-- BEGIN GENERATED: additional-deployment-options -->
### Additional Deployment Options

`camunda-mcp` can run as a local stdio process or container, or behind a remote
network boundary. The
[Deployment guide](https://knuckles-team.github.io/camunda-mcp/deployment/) carries
the detailed transport contract.

- **Local container** — launch a reviewed immutable image as a least-privilege
  stdio child with no listener or published port.
- **Remote URL** — connect through an operator-supplied authenticated HTTPS
  ingress. Keep its URL, outbound identity references, trust profile, and exact
  `MCP_ALLOWED_HOSTS` in `AgentConfig`.
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


<!-- BEGIN agent-utilities-deployment (generated; do not edit between markers) -->

## Deploy with `agent-utilities-deployment`

Provision this package with the consolidated **`agent-utilities-deployment`**
workflow. It selects an installed-package, editable-source, or immutable-container
path; records only runtime secret and TLS-profile references in `AgentConfig`; and
runs doctor, registration, policy, observability, and rollback gates. Ask your agent
to **"deploy `camunda-mcp` with agent-utilities-deployment"**.

| Install mode | Command |
|------|---------|
| Installed package | `uv tool install "camunda-mcp[mcp]"`, then run `camunda-mcp` |
| Editable source | `uv pip install -e ".[agent]"`, then run `camunda-mcp` |
| Immutable container | deploy `registry.example.invalid/camunda-mcp@sha256:<digest>` through the operator-selected orchestrator |

The repository embeds no deployment profile, credential value, certificate path, or
environment-specific endpoint. Supply those at runtime through `AgentConfig` and the
configured secret provider.

<!-- END agent-utilities-deployment -->

<!-- GOVERNED-CAPABILITY:START -->
## Governed capability contract

This package ships a compact canonical skill surface with specialist procedures
kept as referenced workflows. The current MCP tools, skill metadata,
`connector_manifest.yml`, ontology, mappings, shapes, fixtures, migrations,
tool-schema fingerprints, and certification metadata form one versioned
capability contract. Validate them together; do not rely on stale tool names or
historical per-task skill wrappers.

Runtime endpoints, credentials, certificate trust, tenant identity, retention,
and observability policy are deployment inputs and are never packaged values.
See [Configuration, trust, and privacy](docs/configuration.md) before enabling a
network transport, connector ingestion, GraphOS delegation, or trace export.
<!-- GOVERNED-CAPABILITY:END -->
