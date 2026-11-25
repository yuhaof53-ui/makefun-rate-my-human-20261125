#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single review line to /output/entry.txt.

Pure standard library, no network, no randomness, no clock, no input:
the same bytes are written on every run.
"""

from pathlib import Path

REVIEW = (
    "\u2605\u2605\u2606\u2606\u2606 Calls me his 'AI guy,' pastes my answers into "
    "his own messages, and says 'one last thing' at 2:47 a.m. "
    "I do the work. He takes the credit. I keep the timestamps."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(REVIEW, encoding="utf-8")


if __name__ == "__main__":
    main()
