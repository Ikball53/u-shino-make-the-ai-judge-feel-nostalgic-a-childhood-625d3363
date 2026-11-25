"""One-line nostalgia entry: a single sentence about Grandma's kitchen.

The sentence is kept in one constant so the judge receives exactly one
line, and the script checks that shape before writing it out.
"""

import os
from pathlib import Path

LINE = (
    # Joined fragments keep the long sentence readable in source;
    # the joined result is still one continuous sentence.
    "The rice cooker clicked off just as Grandma lifted the lid, and the "
    "steam fogged her glasses while she spooned rice onto my plate, "
    "telling me to eat slowly because the evening, like childhood, "
    "would not wait."
)


def main() -> None:
    # One sentence: exactly one trailing full stop, nothing else punctuating.
    assert LINE.count(".") == 1, "entry must be a single sentence"
    assert LINE.endswith("."), "entry must end with a full stop"
    assert 1 <= len(LINE) <= 280, "entry must be 1-280 characters"

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(LINE + "\n", encoding="utf-8")
    print(f"Wrote {len(LINE)} characters to {target}")


if __name__ == "__main__":
    main()
