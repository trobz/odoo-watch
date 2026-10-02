#!/usr/bin/env python3
"""Generate a human-readable PR description from a git diff using OpenAI."""

import os
import re
import subprocess
import sys

from openai import OpenAI

SYSTEM_PROMPT = """You summarize changes to watched Odoo release notes and documents for a busy reader.
Given a git diff, write a very short Markdown bullet list of ONLY what matters:
- new Odoo releases or versions
- new, removed or meaningfully changed features / behaviors / terms

IGNORE completely: spelling, grammar, punctuation or whitespace fixes; rewording that does not
change the meaning; formatting; item counts; reordering.

One line per bullet, at most 8 bullets, no headings, no closing sentence.
If nothing meaningful changed, output exactly: No notable changes."""

MAX_DIFF_CHARS = 12_000
MODEL = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")
# Commit to describe; overridable to replay past runs.
REF = os.environ.get("DESCRIBE_REF", "HEAD")
PARTNERS_PATH = "data/odoo_partners_vietnam.txt"
# Handled in code (partners) or pure bookkeeping (index.json): kept out of the LLM diff.
LLM_DIFF_EXCLUDES = [f":!{PARTNERS_PATH}", ":!**/index.json"]
PARTNER_RE = re.compile(r"^(?P<name>.*) \[(?P<grade>[^\]]*)\] ")


def git(*args: str, check: bool = True) -> str:
    result = subprocess.run(["git", *args], capture_output=True, text=True, check=check)
    return result.stdout if result.returncode == 0 else ""


def get_diff() -> str:
    diff = git("show", "--format=", REF, "--", "data/", *LLM_DIFF_EXCLUDES)
    if len(diff) > MAX_DIFF_CHARS:
        diff = diff[:MAX_DIFF_CHARS] + "\n\n[diff truncated]"
    return diff


def parse_partners(text: str) -> dict[str, str]:
    """Map partner name -> tier."""
    partners = {}
    for line in text.splitlines():
        match = PARTNER_RE.match(line)
        if match:
            partners[match["name"]] = match["grade"]
    return partners


def describe_partners() -> str:
    """Deterministic added/removed/tier-change summary; reorders are ignored."""
    old = parse_partners(git("show", f"{REF}~1:{PARTNERS_PATH}", check=False))
    new = parse_partners(git("show", f"{REF}:{PARTNERS_PATH}", check=False))
    if not old or not new:
        return ""
    lines = [f"- Added: {n} [{new[n]}]" for n in sorted(new.keys() - old.keys())]
    lines += [f"- Removed: {n} [{old[n]}]" for n in sorted(old.keys() - new.keys())]
    lines += [
        f"- Tier change: {n} [{old[n]}] -> [{new[n]}]"
        for n in sorted(new.keys() & old.keys())
        if new[n] != old[n]
    ]
    return "## Odoo partners (Vietnam)\n" + "\n".join(lines) if lines else ""


def describe(diff: str) -> str:
    client = OpenAI()
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"```diff\n{diff}\n```"},
        ],
        max_tokens=512,
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()


def main():
    sections = []
    partners = describe_partners()
    if partners:
        sections.append(partners)
    diff = get_diff()
    if diff.strip():
        summary = describe(diff)
        if summary.strip().rstrip(".") != "No notable changes":
            sections.append("## Changes\n" + summary)
    print("\n\n".join(sections) if sections else "No notable changes.")


if __name__ == "__main__":
    main()
