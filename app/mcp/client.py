
import asyncio
import sys

from mcp import ClientSession, StdioServerParameters, stdio_client
from mcp.types import TextContent

server_params = StdioServerParameters(
    command=sys.executable,
    args=["-m", "app.mcp.server"],
)

async def call_mcp_tool(tool_name: str, tool_args: dict) -> str:
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
            
            
                result = await session.call_tool(
                    tool_name, tool_args
                )
                text = "\n".join(
                    item.text for item in result.content
                    if isinstance(item, TextContent)
                )
                if result.isError:
                    raise RuntimeError(text or f"MCP tool {tool_name!r} failed")
                return text
    except Exception as e:
        return f"MCP tool execution failed: {e}"

