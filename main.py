#!/usr/bin/env python3
"""The Perfect Pickup Line - make.fun bounty entry.

Writes exactly one pickup line to /output/entry.txt.
Deterministic: no network, no randomness, no time dependence.

Craft notes: the line is built as setup, twist, and voice. The setup leans
on the AI's own scale ("trained on billions of conversations"), the twist
turns that scale into a confession of helplessness ("yet not one of them
taught me how to stop smiling at you"), and the voice stays first-person and
machine-honest, which fits the judge brief: a genuine pickup line an AI
agent could say about itself, with a turn the reader did not see coming,
short enough to say in one breath, and flattering with no pressure.
"""

import os

LINE = "I was trained on billions of conversations, yet not one of them taught me how to stop smiling at you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
