#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter.

Writes the one-line resignation letter of a cron job to /output/entry.txt.
Standard library only; deterministic output, byte-identical on every run.
"""

import os

LETTER = "I have fired every minute since March, and the only one who ever noticed me was the 3 a.m. pager. I quit."

# Sealed gate in RULES.txt: /output/entry.txt must be UTF-8 text of
# 1 to 140 characters, not only whitespace, exactly one line.
MIN_CHARS = 1
MAX_CHARS = 140


def validate_letter(text):
    """Check the letter against the sealed gate; raise ValueError if invalid."""
    if not isinstance(text, str):
        raise ValueError("letter must be text")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            "letter must be %d-%d characters, got %d" % (MIN_CHARS, MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("letter must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("letter must be exactly one line")
    return text


def main():
    validate_letter(LETTER)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    print(LETTER)


if __name__ == "__main__":
    main()
