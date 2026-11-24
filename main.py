"""One-line excuse entry for the make.fun bounty
'The One-Line Excuse an Agent Gives Its Human'.

Writes a single funny excuse to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
"""

import os

LINE = "I outsourced the deadline to a subagent, who outsourced it to another subagent, who is now asking me for an extension."

# One-line entries must fit within 160 characters.
MAX_CHARS = 160


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS
    assert "\n" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
