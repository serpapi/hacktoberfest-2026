import os

from dotenv import load_dotenv

load_dotenv()

import httpx
import uvicorn
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

serpapi_key = os.getenv("SERPAPI_KEY") or os.environ["SERPAPI_API_KEY"]

model = OpenAIChatModel(
    os.getenv("LM_STUDIO_MODEL", "qwen/qwen3.6-35b-a3b"),
    provider=OpenAIProvider(
        base_url=os.getenv("LM_STUDIO_BASE_URL", "http://127.0.0.1:1234/v1"),
    ),
)

system_prompt = """
Use search_web for general information, search_news for news, and search_hotels for hotels.
For hotels, ask for check-in and check-out dates if the user has not provided them.
Include source links and keep the answer under 150 words. Show hotel prices with their currency.
Use at most two searches. If a search fails, say so.
"""


async def serpapi_search(params: dict[str, str | int]) -> str:
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(
                "https://serpapi.com/search",
                params={
                    **params,
                    "api_key": serpapi_key,
                    "output": "md",
                },
            )
    except httpx.RequestError:
        return "SerpApi search failed: could not reach the API."
    if response.is_error:
        return f"SerpApi search failed: HTTP {response.status_code}."
    return response.text


async def search_web(q: str) -> str:
    """Search the web for a query and return up to three results as Markdown.

    Args:
        q: The search query.
    """
    return await serpapi_search({
        "engine": "google_light",
        "q": q,
        "json_restrictor": (
            "error,organic_results[0:3].title,organic_results[0:3].link,"
            "organic_results[0:3].snippet"
        ),
    })


async def search_news(q: str) -> str:
    """Search for current news and return up to three articles as Markdown.

    Args:
        q: The topic to search for in the news.
    """
    return await serpapi_search({
        "engine": "google_news_light",
        "q": q,
        "json_restrictor": (
            "error,news_results[0:3].title,news_results[0:3].link,"
            "news_results[0:3].source,news_results[0:3].date,news_results[0:3].snippet"
        ),
    })


async def search_hotels(
    q: str,
    check_in_date: str,
    check_out_date: str,
    adults: int = 2,
    currency: str = "USD",
) -> str:
    """Search hotels for a stay and return up to three options as Markdown.

    Args:
        q: The destination or hotel search query.
        check_in_date: Check-in date in YYYY-MM-DD format.
        check_out_date: Check-out date in YYYY-MM-DD format, after check-in.
        adults: Number of adult guests.
        currency: Three-letter currency code, such as USD or INR.
    """
    return await serpapi_search({
        "engine": "google_hotels",
        "q": q,
        "check_in_date": check_in_date,
        "check_out_date": check_out_date,
        "adults": adults,
        "currency": currency,
        "json_restrictor": (
            "error,search_parameters.currency,properties[0:3].name,"
            "properties[0:3].link,properties[0:3].rate_per_night,"
            "properties[0:3].total_rate,properties[0:3].overall_rating"
        ),
    })


agent = Agent(model, tools=[search_web, search_news, search_hotels], instructions=system_prompt)

# Optional alternative using serpapi-search-tools (not installed for this demo):
# https://serpapi.github.io/serpapi-search-tools-python/
# from serpapi_search_tools import web_search, news_search, hotels_search
# agent = Agent(model, tools=[
#     web_search(provider="pydantic-ai"),
#     news_search(provider="pydantic-ai"),
#     hotels_search(provider="pydantic-ai"),
# ], instructions="Search for live information and include source links.")


if __name__ == "__main__":
    port = 8778
    print(f"Open http://127.0.0.1:{port}")
    uvicorn.run(agent.to_web(), host="127.0.0.1", port=port)

# Run: uv run demo_agents/tool_demo.py
# Sample prompt: Find the latest stable Python release. Include the official source link.
# Sample prompt: Find three recent news stories about renewable energy. Include dates and source links.
# Sample prompt: Find three hotels in Bengaluru for two adults, checking in on 2026-11-13 and out on 2026-11-15. Show nightly prices in INR and source links.
