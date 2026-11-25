#!/usr/bin/env python3
"""Fridge Roast entry: writes one funny line roasting a smart fridge."""
import os

ENTRY = "My smart fridge updated its firmware at 3 a.m. and now the ice maker needs a password, two-factor authentication, and a hug."

def main():
    line = ENTRY.strip()
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 chars, one line.
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert "\n" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")

if __name__ == "__main__":
    main()
