#!/usr/bin/env python3
"""Generate a human-readable PR description from a git diff using OpenAI."""

import subprocess
import sys

from openai import OpenAI

SYSTEM_PROMPT = """You are a technical writer summarizing changes to watched Odoo web pages and documents.
Given a git diff, write a concise PR description in Markdown that explains what changed in plain English.
Focus on the meaning of the changes (e.g. new FAQ entries, updated terms, added/removed partners),
not the raw diff syntax. Group changes by file. Be specific but brief."""

MAX_DIFF_CHARS = 12_000


def get_diff() -> str:
    result = subprocess.run(
        ["git", "show", "--format=", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    )
    diff = result.stdout
    if len(diff) > MAX_DIFF_CHARS:
        diff = diff[:MAX_DIFF_CHARS] + "\n\n[diff truncated]"
    return diff


def describe(diff: str) -> str:
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"```diff\n{diff}\n```"},
        ],
        max_tokens=512,
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()


def main():
    diff = get_diff()
    if not diff.strip():
        print("No changes to describe.")
        sys.exit(0)
    print(describe(diff))


if __name__ == "__main__":
    main()
