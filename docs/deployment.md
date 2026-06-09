# Deployment

This page covers running `camunda-mcp` as long-lived servers: the transports, the
A2A agent server, a Docker Compose stack, putting it behind a Caddy reverse proxy,
and giving it a DNS name with Technitium. To provision the **Camunda platform** it
connects to, see [Backing Platform](platform.md).

> `camunda-mcp` ships both an **MCP server** (console script `camunda-mcp`) and an
> **A2A agent server** (console script `camunda-agent`). The MCP server is a typed,
> deterministic tool surface a policy router or agent calls; the agent server wraps
> that surface in a Pydantic-AI graph agent for agent-to-agent orchestration.

## Run the MCP server

The transport is selected with `--transport` (or the `TRANSPORT` env var):

=== "stdio (default)"

    ```bash
    camunda-mcp
    ```
    For IDE / desktop MCP clients that launch the server as a subprocess.

=== "streamable-http"

    ```bash
    camunda-mcp --transport streamable-http --host 0.0.0.0 --port 8000
    ```
    A network server with a `/health` endpoint and `/mcp` route.

=== "sse"

    ```bash
    camunda-mcp --transport sse --host 0.0.0.0 --port 8000
    ```

Health check (HTTP transports):

```bash
curl -s http://localhost:8000/health        # {"status":"OK"}
```

## Configuration (environment)

`camunda-mcp` is configured entirely from the environment. The **required** set
depends on which platform you target (`CAMUNDA_PLATFORM`):

| Var | Default | Meaning |
|---|---|---|
| `CAMUNDA_PLATFORM` | `7` | Target platform: `7` or `8` |
| `CAMUNDA_SSL_VERIFY` | `True` | Verify TLS (set `False` for self-signed homelab) |
| `CAMUNDA7_URL` | `http://localhost:8080/engine-rest` | Camunda 7 Engine REST base URL |
| `CAMUNDA7_TOKEN` | — | Camunda 7 bearer token (optional) |
| `CAMUNDA7_USERNAME` | — | Camunda 7 basic-auth user (optional) |
| `CAMUNDA7_PASSWORD` | — | Camunda 7 basic-auth password (optional) |
| `CAMUNDA8_ZEEBE_REST_URL` | `http://localhost:8080` | Camunda 8 Zeebe REST base URL |
| `CAMUNDA8_OPERATE_URL` | — | Camunda 8 Operate REST URL |
| `CAMUNDA8_TASKLIST_URL` | — | Camunda 8 Tasklist REST URL |
| `CAMUNDA8_CLIENT_ID` | — | Camunda 8 OAuth client id |
| `CAMUNDA8_CLIENT_SECRET` | — | Camunda 8 OAuth client secret |
| `CAMUNDA8_OAUTH_URL` | — | Camunda 8 OAuth token URL |
| `CAMUNDA8_AUDIENCE` | `zeebe.camunda.io` | Camunda 8 OAuth audience |
| `CAMUNDATOOL` | `True` | Register the Camunda tool set |

Plus `HOST` / `PORT` / `TRANSPORT` for HTTP transports. Credentials left blank leave
the corresponding platform inactive — the server **remains inactive when credentials
are absent**. A starter
[`.env.example`](https://github.com/Knuckles-Team/camunda-mcp/blob/main/.env.example)
ships with the repository; copy it to `.env` and fill in the values for the platform
you use.

## Docker Compose

The repository ships
[`docker/mcp.compose.yml`](https://github.com/Knuckles-Team/camunda-mcp/blob/main/docker/mcp.compose.yml).
A representative stack reads a sibling `.env` and publishes the HTTP server on
`:8000`:

```yaml
services:
  camunda-mcp:
    image: knucklessg1/camunda-mcp:latest
    container_name: camunda-mcp
    hostname: camunda-mcp
    restart: always
    env_file:
      - .env
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=streamable-http
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
```

```bash
cp .env.example .env          # then edit CAMUNDA_* values
docker compose -f docker/mcp.compose.yml up -d
docker compose -f docker/mcp.compose.yml logs -f
```

## Run the A2A agent server

`camunda-mcp` also ships an **agent server** (console script `camunda-agent`,
described by [`a2a.json`](https://github.com/Knuckles-Team/camunda-mcp/blob/main/a2a.json)).
It wraps the MCP tool surface in a Pydantic-AI graph agent and is wired to a running
MCP server through the `MCP_URL` environment variable:

```bash
export MCP_URL=http://camunda-mcp:8000/mcp
export DEFAULT_AGENT_NAME="Camunda Agent"
camunda-agent --host 0.0.0.0 --port 8001
```

The repository ships
[`docker/agent.compose.yml`](https://github.com/Knuckles-Team/camunda-mcp/blob/main/docker/agent.compose.yml).
A representative agent stack publishes the agent on `:8001` and points it at the MCP
server:

```yaml
services:
  camunda-agent:
    image: knucklessg1/camunda-mcp:latest
    container_name: camunda-agent
    hostname: camunda-agent
    restart: always
    command: ["camunda-agent", "--host", "0.0.0.0", "--port", "8001"]
    env_file:
      - .env
    environment:
      - PYTHONUNBUFFERED=1
      - MCP_URL=http://camunda-mcp:8000/mcp
    ports:
      - "8001:8001"
    depends_on:
      - camunda-mcp
```

## Behind a Caddy reverse proxy

Expose the HTTP server on a hostname with automatic TLS. Add to your `Caddyfile`:

```caddy
# Internal (self-signed) — homelab .arpa zone
camunda-mcp.arpa {
    tls internal
    reverse_proxy camunda-mcp:8000
}
```

```caddy
# Public — automatic Let's Encrypt
camunda-mcp.example.com {
    reverse_proxy camunda-mcp:8000
}
```

Reload Caddy:

```bash
docker compose -f services/caddy/compose.yml exec caddy caddy reload --config /etc/caddy/Caddyfile
```

## DNS with Technitium

Point the hostname at the host running Caddy. Via the Technitium API:

```bash
curl -s "http://technitium.arpa:5380/api/zones/records/add" \
  --data-urlencode "token=$TECHNITIUM_DNS_TOKEN" \
  --data-urlencode "domain=camunda-mcp.arpa" \
  --data-urlencode "zone=arpa" \
  --data-urlencode "type=A" \
  --data-urlencode "ipAddress=10.0.0.10" \
  --data-urlencode "ttl=3600"
```

…or add an **A record** `camunda-mcp.arpa → <caddy-host-ip>` in the Technitium web
console (`http://technitium.arpa:5380`). The ecosystem
[`technitium-dns-mcp`](https://knuckles-team.github.io/technitium-dns-mcp/) automates
this as a tool.

## Register with an MCP client

Add to your client's `mcp_config.json` (multiplexer nickname `camun`):

```json
{
  "mcpServers": {
    "camunda-mcp": {
      "command": "uv",
      "args": ["run", "camunda-mcp"],
      "env": {
        "CAMUNDA_PLATFORM": "7",
        "CAMUNDA7_URL": "http://your-camunda:8080/engine-rest",
        "CAMUNDATOOL": "True"
      }
    }
  }
}
```

For a remote HTTP server, point the client at `http://camunda-mcp.arpa/mcp` instead.
