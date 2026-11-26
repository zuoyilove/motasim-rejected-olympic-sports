"""Rejected Olympic Sports -- one funny single-line sport the Olympics turned down.

The grader runs this in a bare python:3.13 sandbox with no network, so the
program is stdlib-only and writes exactly one line of text to
``<output dir>/entry.txt``. The output directory is ``$MAKEFUN_OUTPUT_DIR``
when set, otherwise ``/output``.
"""

import os

ENTRY = (
    "Synchronized Apologizing: four Canadians say sorry in perfect unison "
    "while a fifth apologizes for the noise they made apologizing."
)


def main() -> None:
    # Gate check, mirroring the sealed scorer: 1-200 characters, not only
    # whitespace. Fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
