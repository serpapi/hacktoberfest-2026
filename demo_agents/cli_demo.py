import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

import uvicorn
from pydantic_ai import Agent
from pydantic_ai.capabilities import LocalWorkspace
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai_harness import Shell

model = OpenAIChatModel(
    os.getenv("LM_STUDIO_MODEL", "qwen/qwen3.6-35b-a3b"),
    provider=OpenAIProvider(
        base_url=os.getenv("LM_STUDIO_BASE_URL", "http://127.0.0.1:1234/v1"),
        api_key=os.getenv("LM_STUDIO_API_KEY", "lm-studio"),
    ),
)

system_prompt = """
Use uv to inspect Python installations and packages.
Base answers on command output and keep them short.
"""

agent = Agent(
    model,
    instructions=system_prompt,
    capabilities=[
        LocalWorkspace(Path(__file__).resolve().parent.parent),
        Shell(
            allowed_commands=["uv"],
            tools=["run_command"],
            denied_operators=[";", "&", "|", ">", "<", "$", "`", "\n"],
        ),
    ],
)


if __name__ == "__main__":
    port = 8776
    print(f"Open http://127.0.0.1:{port}")
    uvicorn.run(agent.to_web(), host="127.0.0.1", port=port)
    """
    Which is the current python version being used for the agent?
    """
