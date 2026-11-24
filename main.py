#!/usr/bin/env python3
"""Write the competition entry line to entry.txt.

Deterministic: standard library only, no network, no clock, no
randomness. Every run writes the exact same bytes.
"""

import os

ENTRY = (
    "I delegated it to a subagent, who delegated it to a subagent, "
    "who asked me for clarification, so now everyone is waiting on me."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
