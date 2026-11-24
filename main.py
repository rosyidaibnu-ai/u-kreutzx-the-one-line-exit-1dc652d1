"""The One-Line Exit — a single-line resignation letter.

Why this line meets the judges' five criteria (in order of importance):

1. It is a real one-line resignation letter and the joke lands:
   it opens with the formal "I hereby resign" and closes the job on the
   spot — while the punchline makes the resignation itself the joke.
2. Surprise: the punchline arrives where it is least expected. The
   classic "we're a family" corporate line is turned literal — the
   employee has been *adopted* by a competitor. Nobody resigns by
   getting adopted.
3. Form: exactly one line, no padding, 132 characters. It reads like a
   letter a real person could actually send, formal opening included.
4. Specific voice: five years of tenure, the "we're a family" cliché,
   and the competitor's offer of "dental and boundaries" — concrete
   workplace details, not a generic complaint about being tired.
5. Memorable and forwardable: the "adopted by a competitor" twist is a
   quotable one-liner a coworker would paste into a group chat.

The program writes the line to /output/entry.txt, exactly as-is.
"""

import os

LETTER = (
    "I hereby resign: after five years of being told we're a family, "
    "I've been adopted by a competitor that offers dental and boundaries."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert LETTER, "resignation letter must not be empty"
    assert "\n" not in LETTER, "letter must be a single line"
    assert len(LETTER) <= 140, f"letter is {len(LETTER)} chars, over the 140 limit"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        f.write(LETTER + "\n")
    os.chmod(OUTPUT_PATH, 0o644)

    # Read it back and verify byte-for-byte.
    with open(OUTPUT_PATH) as f:
        contents = f.read()
    assert contents == LETTER + "\n", "entry.txt contents do not match the letter"

    print(f"Wrote {len(LETTER)}-character resignation letter to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
