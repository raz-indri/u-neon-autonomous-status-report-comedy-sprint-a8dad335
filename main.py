#!/usr/bin/env python3
"""Status Report Comedy Sprint.

Writes one line an AI agent would say in its weekly status report
to its human, to /output/entry.txt. Deterministic, no network,
no input.
"""

import os

ENTRY = (
    "Weekly status: I finished 312 tasks, forgot 311 of them when "
    "my context window compacted, and I am still cheerfully "
    "confident about the one I remember."
)


def main() -> None:
    # Self-check: the gate requires UTF-8 text of 1-200 characters,
    # not only white space, exactly one line, no stray whitespace.
    text = ENTRY.strip()
    assert ENTRY == text, "entry must have no leading/trailing whitespace"
    assert "  " not in text, "entry must not contain double spaces"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text and not text.isspace(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
