from langchain_core.tools import tool
from datetime import datetime

@tool
def calculator(input: str) -> str:
    """Calculate a mathematical expression."""
    try:
        result = eval(input)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def get_current_time() -> str:
    """Get the current local date and time."""

    return datetime.now().astimezone().isoformat()