
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

import uvicorn
from pydantic_ai import Agent
from pydantic_ai.capabilities import LocalWorkspace
from pydantic_ai.mcp import MCPToolset
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai_harness import Skills

model = OpenAIChatModel(
    os.getenv("LM_STUDIO_MODEL", "qwen/qwen3.6-35b-a3b"),
    provider=OpenAIProvider(
        base_url=os.getenv("LM_STUDIO_BASE_URL", "http://127.0.0.1:1234/v1"),
    ),
)

system_prompt = """
Complete the user's task using the available tools.
If extraction fails, say so; do not substitute search snippets or remembered content.
"""

serpapi_key = os.getenv("SERPAPI_KEY") or os.environ["SERPAPI_API_KEY"]
mcp = MCPToolset(
    "https://mcp.serpapi.com/mcp",
    headers={"Authorization": f"Bearer {serpapi_key}"},
)

root = Path(__file__).resolve().parent
agent = Agent(
    model,
    instructions=system_prompt,
    toolsets=[mcp],
    capabilities=[LocalWorkspace(root, read_only=True), Skills("skills")],
)

if __name__ == "__main__":
    port = 8780
    print(f"Open http://127.0.0.1:{port}")
    uvicorn.run(agent.to_web(), host="127.0.0.1", port=port)

    """
    Extract the page contents of https://placehold.co as Markdown.
    """
