# smolagents Starter

A minimal, code-first starter for building web-search agents with
[Hugging Face smolagents](https://github.com/huggingface/smolagents) and
[Nebius Token Factory](https://studio.nebius.ai/).

Live website: coming soon after deployment.

## What This Project Does

`smolagents Starter` gives you a clean starting point for an AI agent that can
search the web, reason over fresh information, and answer questions through a
Python-first workflow.

The project uses `CodeAgent`, which means the agent solves tasks by writing and
executing Python code with the tools you provide. Instead of hiding the reasoning
pipeline behind a large app shell, this starter keeps the core loop visible,
hackable, and easy to extend.

## Highlights

- Code-first agent built with `smolagents.CodeAgent`
- DuckDuckGo web search tool included out of the box
- Nebius Token Factory configured as an OpenAI-compatible inference provider
- Qwen/Qwen3-30B-A3B as the default model
- Interactive CLI for asking live research questions
- Simple `.env` configuration with no secrets committed
- Static deployment-ready website included in `site/`

## Tech Stack

- Framework: `smolagents`
- Agent: `CodeAgent`
- Model adapter: `OpenAIServerModel`
- Provider: Nebius Token Factory
- Default model: `Qwen/Qwen3-30B-A3B`
- Tools: `DuckDuckGoSearchTool` plus smolagents base tools
- Language: Python 3.10+

## How It Works

The CLI loads your Nebius API key from `.env`, creates an OpenAI-compatible
model client, attaches a DuckDuckGo search tool, and starts an interactive
prompt loop.

When you ask a question, the agent can write Python, call search, process the
results, and produce a final response. This makes it a practical base for
research assistants, market scanners, documentation helpers, news summarizers,
or any small agent that benefits from fresh web context.

## Installation

```bash
git clone https://github.com/tirth1263/smolagents-starter.git
cd smolagents-starter

# pip
pip install -r requirements.txt
```

If you use `uv`, you can create an environment and sync the same requirements:

```bash
uv venv
uv pip install -r requirements.txt
```

## Environment Setup

Create your environment file:

```bash
cp .env.example .env
```

Then edit `.env` and add your Nebius API key:

```bash
NEBIUS_API_KEY=your_nebius_api_key_here
```

The default Nebius Token Factory endpoint and model are already included in
`.env.example`, but you can override them if you want to experiment.

## Usage

```bash
python main.py
```

Example prompts:

- "Who won the latest F1 race and by how many seconds?"
- "Summarize today's top story on Hacker News."
- "Find three recent papers about agentic RAG."
- "Compare the latest releases from two AI model providers."

Type `exit`, `quit`, or press `Ctrl+C` to leave the CLI.

## Project Structure

```text
.
├── main.py                 # Interactive smolagents CLI
├── requirements.txt        # Runtime dependencies
├── pyproject.toml          # Project metadata
├── .env.example            # Safe environment template
├── site/                   # Deployment-ready static website
│   ├── index.html
│   ├── styles.css
│   └── assets/
└── .github/workflows/ci.yml
```

## Configuration

| Variable | Default | Description |
| --- | --- | --- |
| `NEBIUS_API_KEY` | Required | Your Nebius Token Factory API key |
| `NEBIUS_BASE_URL` | `https://api.tokenfactory.nebius.com/v1/` | OpenAI-compatible base URL |
| `MODEL_ID` | `Qwen/Qwen3-30B-A3B` | Model used by the agent |
| `SMOLAGENTS_MAX_STEPS` | `6` | Maximum reasoning/tool-use steps per request |

## Why This Starter Is Useful

Many agent demos are either too abstract or too large to adapt quickly. This
starter focuses on the essentials:

- A real agent loop
- A real web-search tool
- A real hosted inference provider
- A small codebase you can understand in minutes

From here, you can add custom tools, connect APIs, save research summaries,
wrap the agent in a web UI, or turn it into a scheduled monitor.

## Security Notes

- Never commit `.env` or API keys.
- Keep tool permissions narrow when adding custom tools.
- Review generated code execution behavior before using this in production.
- Treat web-search results as untrusted input and validate important claims.

## License

MIT License. See [LICENSE](LICENSE).
