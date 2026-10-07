from app.llm import llm, llm_with_mcp_tools, mcp_tools


def test_mcp_calculator() :
    messages =[
        ("human", "What is 125 multiplied by 37?")
    ]
    response = llm.bind_tools(mcp_tools, tool_choice="mcp_calculator").invoke(messages)
    print("\nLLM response:")
    print(response)

    print("\nTool calls:")
    print(response.tool_calls)

    assert response.tool_calls, "LLM did not request any tool"

    tool_call = response.tool_calls[0]

    assert tool_call["name"] == "mcp_calculator"

def test_mcp_current_time() :
    messages = [
        ("human", "What is the current time?")
    ]
    response = llm_with_mcp_tools.invoke(messages)
    print("\nLLM response:")
    print(response)

    print("\nTool calls:")
    print(response.tool_calls)

    assert response.tool_calls, "LLM did not request any tool"

    tool_call = response.tool_calls[0]

    assert tool_call["name"] == "mcp_current_time"

def test_mcp_general_question() :
    messages = [
        ("human", "What is the capital of France?")
    ]
    response = llm_with_mcp_tools.invoke(messages)
    print("\nLLM response:")
    print(response)

    print("\nTool calls:")
    print(response.tool_calls)

    assert not response.tool_calls, "LLM requested a tool when it shouldn't have"