# Backing Platform — Camunda

`camunda-mcp` is a **client** of a Camunda process automation platform. This page
provides a Docker recipe for deploying one locally to serve as the target of
`CAMUNDA7_URL` (Camunda 7) or the Camunda 8 REST endpoints. For production
topologies, follow the upstream [Camunda documentation](https://docs.camunda.io/).

!!! note "Backing-system recipe"
    Each connector in the ecosystem follows the same convention — a
    `docs/platform.md` recipe for the system it integrates with, accompanied by a
    sample Compose stack that mirrors [`services/`](https://github.com/Knuckles-Team).
    Systems offered only as a managed service have no local recipe.

## Single-node deployment (Compose)

Camunda publishes the `camunda/camunda-bpm-platform` image for Camunda 7. The
following stack runs one Engine REST platform on `:8080`, mirroring
[`services/camunda/compose.yml`](https://github.com/Knuckles-Team):

```yaml
# docker/camunda-platform.compose.yml
services:
  camunda:
    image: camunda/camunda-bpm-platform:latest
    container_name: camunda
    hostname: camunda
    restart: unless-stopped
    ports:
      - "8080:8080"            # Engine REST + Cockpit / Tasklist webapps
    volumes:
      - camunda_data:/camunda
    healthcheck:
      test: ["CMD", "curl", "-fsS", "http://localhost:8080/engine-rest/engine"]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 40s

volumes:
  camunda_data:
```

```bash
docker compose -f docker/camunda-platform.compose.yml up -d

# Wait for the Engine REST API to answer
curl http://localhost:8080/engine-rest/engine
```

The default Camunda 7 demo credentials are `demo` / `demo`.

## Connect camunda-mcp

```bash
export CAMUNDA_PLATFORM=7
export CAMUNDA7_URL=http://localhost:8080/engine-rest
export CAMUNDA7_USERNAME=demo
export CAMUNDA7_PASSWORD=demo

camunda-mcp --transport streamable-http --host 0.0.0.0 --port 8000
```

## Combined deployment

A combined stack places the platform and the MCP server on one Docker network, so the
server reaches Camunda by container name:

```yaml
# docker/stack.compose.yml
services:
  camunda:
    image: camunda/camunda-bpm-platform:latest
    hostname: camunda
    ports: ["8080:8080"]
    volumes: ["camunda_data:/camunda"]

  camunda-mcp:
    image: knucklessg1/camunda-mcp:latest
    depends_on: [camunda]
    environment:
      - CAMUNDA_PLATFORM=7
      - CAMUNDA7_URL=http://camunda:8080/engine-rest
      - CAMUNDA7_USERNAME=demo
      - CAMUNDA7_PASSWORD=demo
      - TRANSPORT=streamable-http
      - HOST=0.0.0.0
      - PORT=8000
    ports: ["8000:8000"]

volumes:
  camunda_data:
```

```bash
docker compose -f docker/stack.compose.yml up -d
```

## Camunda 8

For Camunda 8, deploy the upstream Zeebe / Operate / Tasklist stack from the official
[Camunda 8 self-managed distribution](https://docs.camunda.io/docs/self-managed/setup/deploy/local/docker-compose/),
then point the connector at the REST endpoints:

```bash
export CAMUNDA_PLATFORM=8
export CAMUNDA8_ZEEBE_REST_URL=http://localhost:8088
export CAMUNDA8_OPERATE_URL=http://localhost:8081
export CAMUNDA8_TASKLIST_URL=http://localhost:8082
```

When the cluster requires OAuth, also set `CAMUNDA8_CLIENT_ID`,
`CAMUNDA8_CLIENT_SECRET`, `CAMUNDA8_OAUTH_URL`, and `CAMUNDA8_AUDIENCE`.
