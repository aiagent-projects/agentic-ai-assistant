from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode

from app.graph.state import AgentState
from app.graph.node import greeting_node, response_node
from app.graph.node import route_after_greeting
from app.graph.node import alternative_node, call_llm

from app.mcp.tools import (
    mcp_calculator,
    mcp_current_time,
)

# MCP tools available to the graph
tools = [
    mcp_calculator,
    mcp_current_time,
]

tool_node = ToolNode(tools)

builder = StateGraph(AgentState)


builder.add_node("llm",call_llm)
builder.add_node("tool", tool_node)

builder.add_edge(START, "llm")


graph = builder.compile()