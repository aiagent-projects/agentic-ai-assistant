from langchain_openai import ChatOpenAI

from app.config import OPENAI_API_KEY
from app.mcp.tools import mcp_calculator, mcp_current_time


llm = ChatOpenAI(
    model="gpt-5-mini",
    api_key=OPENAI_API_KEY,
    temperature=0
)

mcp_tools = [mcp_calculator, mcp_current_time]

llm_with_mcp_tools = llm.bind_tools(mcp_tools)