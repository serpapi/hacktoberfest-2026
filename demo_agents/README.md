Three Pydantic AI demos show a local model using MCP tools, shell commands, and skills. Each script opens a browser chat interface.

You need uv, Python 3.13 or newer, and LM Studio. Run all commands below from the repository root.

Install the dependencies into the repository's `.venv`:

```sh
uv sync
```

In LM Studio, load `qwen/qwen3.6-35b-a3b` and start the local server at `http://127.0.0.1:1234`. The model needs tool-calling support.

Create or edit `demo_agents/.env` with your SerpApi key. Keep any existing settings:

```dotenv
SERPAPI_API_KEY=your_serpapi_key
```

The MCP and skill demos need this key; the CLI demo does not. `SERPAPI_KEY` is also supported. To use another local model or server address, set `LM_STUDIO_MODEL` and `LM_STUDIO_BASE_URL` in the same file. The default API base URL is `http://127.0.0.1:1234/v1`.

Start a demo with its command, then open its chat URL. Use separate terminals to run several demos at once. Press `Ctrl+C` in a demo's terminal to stop it and free its port.

| Script | What it demonstrates | Run from the repository root | Open in your browser |
| --- | --- | --- | --- |
| [mcp_demo.py](mcp_demo.py) | Live web searches and stock quotes through SerpApi MCP | `uv run demo_agents/mcp_demo.py` | [localhost:8774](http://127.0.0.1:8774) |
| [cli_demo.py](cli_demo.py) | Running `uv` commands to inspect Python and installed packages | `uv run demo_agents/cli_demo.py` | [localhost:8776](http://127.0.0.1:8776) |
| [skills_demo.py](skills_demo.py) | Loading a skill to extract a web page as Markdown through SerpApi | `uv run demo_agents/skills_demo.py` | [localhost:8780](http://127.0.0.1:8780) |

Try these prompts:

| Demo | Prompt |
| --- | --- |
| MCP | Get the current price of NVIDIA stock. Include currency and the source link. |
| CLI | Which Python version is being used for this agent? |
| Skills | Extract the page contents of https://placehold.co as Markdown. |

To compare the skill demo with the same agent without a skill, start [without_skill.py](without_skill.py) in another terminal:

```sh
uv run demo_agents/without_skill.py
```

Open [localhost:8781](http://127.0.0.1:8781). Use a fresh conversation in each chat and paste the same extraction prompt. Both agents have the same model, instructions, and MCP tools. Only `skills_demo.py` loads [serpapi-page-extract](skills/serpapi-page-extract/SKILL.md).

In the skill chat, watch for `load_capability` followed by `search` using `engine="extract"`, `output="md"`, `json_restrictor="text_content.markdown"`, and `include_markdown=true`. The answer should contain the retrieved page content. A web search snippet alone does not demonstrate extraction.
