

import asyncio

from langchain.tools import tool

from app.mcp.client import call_mcp_tool


@tool
def mcp_calculator(expression: str) -> str:
    "Evaluate a mathematical expression."
    return asyncio.run(
        call_mcp_tool("calculator", {"expression": expression})
    )

@tool
def mcp_current_time(expression: str) -> str:
    "Get the current time."
    return asyncio.run(
        call_mcp_tool("get_current_time", {})
    )