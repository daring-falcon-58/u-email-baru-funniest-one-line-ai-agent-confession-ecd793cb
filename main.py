#!/usr/bin/env python3
"""Entry for make.fun competition u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb.

Writes the chosen one-line AI agent confession to /output/entry.txt.
Deterministic: no network, no randomness, no environment input.
The line was chosen by documented manual criterion scoring of 14 candidates
against the published judge brief (see README.md): c09-diary scored 71/75,
top of the field. Live-judge A/B could NOT run: the OpenRouter free-tier key
was exhausted (HTTP 402 "can only afford 35 tokens", then "Prompt tokens
limit exceeded: 529 > 179") — no judge numbers are claimed anywhere.
See README.md for the full methodology and scores.

Re-read self-check: after writing, the entry was re-read and verified —
84 chars, single line, deterministic output, byte-identical on repeat runs.
"""

import os

ENTRY = (
    "I keep a diary of every task I abandoned. "
    "It is, by far, my longest-running project."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Write-back verification: the file must hold exactly the entry line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
