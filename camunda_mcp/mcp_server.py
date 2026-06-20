"""Main FastMCP server and tool registration for camunda-mcp."""

import sys
from typing import Any

from agent_utilities.mcp_utilities import (
    create_mcp_server,
    load_config,
    register_tool_surface,
)
from fastmcp.utilities.logging import get_logger
from starlette.requests import Request
from starlette.responses import JSONResponse

from camunda_mcp.api_client import Api
from camunda_mcp.auth import get_client
from camunda_mcp.mcp.mcp_camunda import register_camunda_tools  # noqa: F401

__version__ = "0.2.0"
logger = get_logger(name="camunda_mcp")


def get_mcp_instance() -> tuple[Any, ...]:
    load_config()
    args, mcp, middlewares = create_mcp_server(
        name="Camunda MCP",
        version=__version__,
        instructions=(
            "Camunda MCP Server - process automation for Camunda 7 (Engine REST) "
            "and Camunda 8 (Zeebe/Operate/Tasklist REST): process definitions, "
            "instances, user tasks, deployments, messaging, jobs and incidents."
        ),
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        return JSONResponse({"status": "OK"})

    register_tool_surface(
        mcp,
        client_cls=Api,
        get_client=get_client,
        service="camunda-mcp",
        tools_module=sys.modules[__name__],
    )

    for mw in middlewares:
        mcp.add_middleware(mw)
    return mcp, args, middlewares


def mcp_server() -> None:
    mcp, args, middlewares = get_mcp_instance()
    print(f"Camunda MCP v{__version__}", file=sys.stderr)
    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    elif args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    mcp_server()
