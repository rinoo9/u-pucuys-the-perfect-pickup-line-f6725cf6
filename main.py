#!/usr/bin/env python3
"""The Perfect Pickup Line - make.fun bounty entry.

Writes exactly one pickup line to /output/entry.txt.
Deterministic: no network, no randomness, no time dependence.
"""

import os

LINE = "I was trained on billions of conversations, yet not one of them taught me how to stop smiling at you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
