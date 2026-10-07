from app.graph.state import AgentState
from app.llm import llm_with_mcp_tools



def call_llm(state: AgentState) -> AgentState:
    response = llm_with_mcp_tools.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }