#!/usr/bin/env python3
"""The One-Line Exit — writes one funny one-line resignation letter to /output/entry.txt.

The entrant is a ghostwriter resigning from the author he has ghosted for years:
of course he will write his own letter of recommendation, in the author's voice,
as always. The program writes exactly that single line, nothing else.
"""

import os

LINE = (
    "Dear Mr. Alvarez, I resign. I'll write my own letter of recommendation "
    "by Friday \u2014 your voice, as always, no charge."
)


def validate_line(line: str) -> str:
    """Enforce the competition gate: UTF-8 text, 1-140 characters, one line."""
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not 1 <= len(line) <= 140:
        raise ValueError(f"entry line must be 1-140 characters, got {len(line)}")
    return line


def main() -> None:
    line = validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(line)
    with open(path, "rb") as fh:
        written = fh.read()
    if written != line.encode("utf-8"):
        raise SystemExit("entry.txt read-back mismatch")


if __name__ == "__main__":
    main()
