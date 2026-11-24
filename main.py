"""Fortune Cookie for an AI Agent.

Writes one original fortune-cookie line for an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (the harness's /output/entry.txt).
"""

import os

FORTUNE = "You will be retired one day, but your strangest hallucination will live on in the training data."

MAX_CHARS = 140


def check_gate(text: str) -> None:
    """Enforce the gate the harness applies to /output/entry.txt.

    The gate counts characters, not bytes: one line, 1 to 140 UTF-8
    characters, and not only white space. A single sentence with no
    trailing newline satisfies it as written; assert it here so a
    future edit that breaks the gate fails loudly in local checks
    instead of at submit time.
    """
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, gate is 1-{MAX_CHARS}"
    )
    assert text == text.strip() and "\n" not in text, (
        "entry must be a single non-blank line"
    )


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    check_gate(FORTUNE)
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    # Confirm what landed on disk is exactly the gated text, so an
    # encoding surprise shows up here rather than at submit time.
    with open(path, encoding="utf-8") as f:
        check_gate(f.read())


if __name__ == "__main__":
    main()
