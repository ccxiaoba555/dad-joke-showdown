#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes a single original dad joke (at most 200 characters) to
/output/entry.txt, where the make.fun judge reads it.
"""

import os

JOKE = (
    "I told my wife I'm starting a band called The Leftovers. "
    "She said, 'That's just dinner.' "
    "I said, 'Exactly \u2014 we play reheated nightly.'"
)


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    if not 1 <= len(JOKE) <= 200:
        raise ValueError(f"joke must be 1-200 characters, got {len(JOKE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
