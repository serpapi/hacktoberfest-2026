# SerpApi Hacktoberfest 2026 Resources

A collection of SerpApi tutorials, livestream resources, and runnable demos for Hacktoberfest 2026. Use them to build AI agents that work with live web data.

## Join the Hacktoberfest DEV Challenges

Building something with SerpApi? Submit it to the **Best Use of SerpApi** category in the [Hacktoberfest DEV Challenges](https://dev.to/challenges/hf26). Give an agent live search, ground its answers in current sources, or build something useful with search data.

Choose the current challenge and theme from the hub, build a new project with open-source AI at its core, and publish your entry using that challenge's submission template. Show your demo, explain how you used SerpApi, and tell readers why open innovation matters for your project. Check the challenge page for its deadline and rules. **We'd love to see what you build. Submit your project on DEV!**

## Livestream Resources

For the SerpApi livestream, [Making Open Models Smarter with Tools, MCP, and Skills](https://dev.to/events/hacktoberfest-serpapi-open-models-tools/october-22-2026), use these resources to follow along and keep building:


The livestream [slides are available here](./slides_making_open_models_smarter.pdf).

| Resource | What you'll learn or find |
| --- | --- |
| [Building an AI Agent in Python](https://serpapi.com/blog/building-an-ai-agent-in-python/) | A walkthrough of models, tools, memory, context, and the agent loop. |
| [How to Fit More Web Search Data into a Local LLM](https://serpapi.com/blog/local-llm-web-search-markdown-output/) | Use Markdown output and JSON Restrictor to reduce the search data sent to a local model. |
| [How to Connect Your Local LLM with Web Search Data](https://serpapi.com/blog/how-to-connect-your-local-llm-with-web-search-data/) | Connect a locally running model to live search results. |
| [Introducing SerpApi's New Markdown Output](https://serpapi.com/blog/introducing-serpapi-markdown-output/) | Request search results in Markdown for use with LLMs and agents. |
| [Local LLM Web Search: source code](https://github.com/serpapi/local-llm-web-search) | The example app for connecting a local LLM to SerpApi through function calling. |

## SerpApi for Agents

- [SerpApi MCP](https://serpapi.com/integrations/mcp): Connect agents to live search through Model Context Protocol.
- [SerpApi CLI](https://serpapi.com/integrations/cli): Access SerpApi from the command line.
- [SerpApi Skill](https://github.com/serpapi/skills): Give agents guidance on using SerpApi.
- [SerpApi Search Tools package](https://pypi.org/project/serpapi-search-tools/): Add search tools to Python agent frameworks.
- [SerpApi llms.txt](https://serpapi.com/llms.txt): Find API documentation in a format agents can read.

## Run the Demos

This repository also includes three small livestream demos. Follow the [setup and run instructions](demo_agents/README.md) to run them with uv and a local model in LM Studio:

| Demo | What it shows |
| --- | --- |
| [MCP demo](demo_agents/mcp_demo.py) | Live web searches and stock quotes through SerpApi MCP. |
| [CLI demo](demo_agents/cli_demo.py) | An agent running `uv` commands to inspect Python and installed packages. |
| [Skills demo](demo_agents/skills_demo.py) | An agent loading the [SerpApi page extraction skill](demo_agents/skills/serpapi-page-extract/SKILL.md) to retrieve a web page as Markdown. |
