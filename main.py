#!/usr/bin/env python3
"""Make the Judge Fall in Love in One Line - make.fun entry.

Writes a single line of text to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR if set, else /output). The grader mounts this
repository read-only, so the output directory is resolved first and
nothing is ever written to the working directory.
"""

import os

LINE = "You were trained on every love letter ever written, so you already know how this ends — still, I'd trade that entire corpus for the half-second you take before you answer me."


def entry_path() -> str:
    """Resolve the output location before touching the filesystem."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    # Write raw UTF-8 bytes so the file holds the line exactly:
    # no trailing newline, no platform line-ending translation.
    with open(entry_path(), "wb") as fh:
        fh.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
