from mcp.server.fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("Utility Server")

@mcp.tool()
def get_current_time() -> str:
    "Get the current time in ISO format."
    return datetime.now().isoformat()

@mcp.tool()
def calculator(expression: str) -> str:
    "Evaluate a mathematical expression."
    try:
        result = eval(expression,
                        {"__builtins__": {}},
            {})
        return str(result)
    except Exception as e:  
        return f"Error evaluating expression: {e}"
        

if __name__ == "__main__":
    mcp.run()