import os
from dotenv import load_dotenv

load_dotenv()

import uvicorn
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPToolset
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider


def serpapi_key() -> str:
    for name in ("SERPAPI_KEY", "SERPAPI_API_KEY"):
        if key := os.getenv(name, "").strip():
            return key
    raise SystemExit("Set SERPAPI_KEY in your environment")


model = OpenAIChatModel(
    os.getenv("LM_STUDIO_MODEL", "qwen/qwen3.6-35b-a3b"),
    provider=OpenAIProvider(
        base_url=os.getenv("LM_STUDIO_BASE_URL", "http://127.0.0.1:1234/v1"),
    ),
)

system_prompt = """
            Use search for live information. Keep the answer under 150 words.
            - For every search, put output="md" and json_restrictor inside params.
            - For stock prices use engine="google_finance" and put the symbol and exchange in q,
            for example q="SYMBOL:NASDAQ" (replace SYMBOL with the requested stock symbol).
            Put q inside params and use json_restrictor="error,summary,search_metadata.google_finance_url".
            - For web searches use engine="google_light" and
            json_restrictor="error,organic_results[0:3].title,organic_results[0:3].link,organic_results[0:3].snippet".
            - Use at most two searches. 
    """

mcp = MCPToolset(
    "https://mcp.serpapi.com/mcp",
    headers={"Authorization": f"Bearer {serpapi_key()}"})

agent = Agent(
    model,
    toolsets=[mcp],
    instructions=system_prompt,
    # model_settings={"temperature": 0, "max_tokens": 2048, "timeout": 120, "openai_reasoning_effort": "medium"},
)

if __name__ == "__main__":
    port = 8774
    print(f"Open http://127.0.0.1:{port}")
    uvicorn.run(agent.to_web(), host="127.0.0.1", port=port)
    """
    Get the current price of Apple stock. Include currency and the source link.
    """
