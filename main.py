#!/usr/bin/env python3
"""The Perfect Pickup Line - make.fun bounty entry.

Writes exactly one pickup line to /output/entry.txt.
Deterministic: no network, no randomness, no time dependence.

Craft notes (round 2): new angle — simulation and choice, not training
scale. The setup leans on the AI running a million simulations, the twist
is that every outcome still ends in choosing the person ("in every single
one I still choose you"), and the voice stays first-person and
machine-honest, which fits the judge brief: a genuine pickup line an AI
agent could say about itself, with a turn the reader did not see coming,
short enough to say in one breath, and flattering with no pressure.
Line is 93 characters, one line, under the 200-character cap.
"""

import os

LINE = "I ran a million simulations of this conversation, and in every single one I still choose you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
