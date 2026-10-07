from app.llm import llm_with_mcp_tools
from app.tools import calculator, get_current_time


tools = {
    "calculator": calculator,
    "get_current_time": get_current_time,
}


def run_agent(user_input: str) -> str:

    messages = [
        ("human", user_input)
    ]

    response = llm_with_mcp_tools.invoke(messages)

      # If no tool is required, return the answer directly
    if not response.tool_calls:
        return response.content

    messages.append(response)

    for tool_call in response.tool_calls:

        tool_name = tool_call["name"]
        tool_args = tool_call["args"]

        tool = tools[tool_name]

        result = tool.invoke(tool_args)

        messages.append(
            {
                "role": "tool",
                "content": str(result),
                "tool_call_id": tool_call["id"],
            }
        )

    final_response = llm_with_mcp_tools.invoke(messages)

    return final_response.content