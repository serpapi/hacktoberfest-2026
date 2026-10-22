---
name: serpapi-page-extract
description: Extract the contents of a public web page as Markdown using SerpApi. Use when the user provides a page URL and wants its content, rather than search results about it.
---

Call the SerpApi MCP `search` tool with these fields inside `params`:

- `engine`: `"extract"`
- `url`: the user's absolute HTTP or HTTPS page URL
- `output`: `"md"`
- `json_restrictor`: `"text_content.markdown"`
- `include_markdown`: `true` (a Boolean)

Put the URL in `url`, not `q`. Single-page extraction is the default mode. `include_markdown` generates the `text_content.markdown` field, `json_restrictor` selects it, and `output` requests Markdown output. Keep all three settings.

Return only the extracted Markdown from the successful tool response, preserving its formatting. Do not wrap it in a code block or add a summary. Do not replace it with search snippets or remembered page content. If the request fails or returns no page content, report that failure.

API reference: https://serpapi.com/extract-api
