from __future__ import annotations

import os
import sys
from dataclasses import dataclass

from dotenv import load_dotenv
from smolagents import CodeAgent, DuckDuckGoSearchTool, OpenAIServerModel


DEFAULT_MODEL_ID = "Qwen/Qwen3-30B-A3B"
DEFAULT_NEBIUS_BASE_URL = "https://api.tokenfactory.nebius.com/v1/"
DEFAULT_MAX_STEPS = 6


@dataclass(frozen=True)
class AgentSettings:
    api_key: str
    api_base: str
    model_id: str
    max_steps: int


def _env_value(name: str, default: str | None = None) -> str:
    value = os.getenv(name, default or "")
    return value.strip()


def _read_max_steps() -> int:
    raw_value = _env_value("SMOLAGENTS_MAX_STEPS", str(DEFAULT_MAX_STEPS))
    try:
        max_steps = int(raw_value)
    except ValueError as exc:
        raise RuntimeError("SMOLAGENTS_MAX_STEPS must be an integer.") from exc

    if max_steps < 1:
        raise RuntimeError("SMOLAGENTS_MAX_STEPS must be greater than 0.")
    return max_steps


def read_settings() -> AgentSettings:
    load_dotenv()

    api_key = _env_value("NEBIUS_API_KEY")
    if not api_key:
        raise RuntimeError(
            "NEBIUS_API_KEY is not set. Create .env from .env.example and add your key."
        )

    return AgentSettings(
        api_key=api_key,
        api_base=_env_value("NEBIUS_BASE_URL", DEFAULT_NEBIUS_BASE_URL),
        model_id=_env_value("MODEL_ID", DEFAULT_MODEL_ID),
        max_steps=_read_max_steps(),
    )


def build_agent(settings: AgentSettings | None = None) -> CodeAgent:
    settings = settings or read_settings()
    model = OpenAIServerModel(
        model_id=settings.model_id,
        api_base=settings.api_base,
        api_key=settings.api_key,
    )

    return CodeAgent(
        tools=[DuckDuckGoSearchTool()],
        model=model,
        add_base_tools=True,
        max_steps=settings.max_steps,
    )


def main() -> int:
    try:
        agent = build_agent()
    except RuntimeError as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        return 1

    print("smolagents Starter")
    print("Ask a question that may need web search. Type 'exit' or 'quit' to stop.")

    while True:
        try:
            prompt = input("\nAsk> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            return 0

        if not prompt:
            continue

        if prompt.lower() in {"exit", "quit", "q"}:
            print("Goodbye.")
            return 0

        try:
            result = agent.run(prompt)
        except Exception as exc:  # noqa: BLE001 - keep CLI errors readable for starters.
            print(f"\nAgent error: {exc}", file=sys.stderr)
            continue

        print(f"\n{result}\n")


if __name__ == "__main__":
    raise SystemExit(main())
