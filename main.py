#!/usr/bin/env python3
"""Till Firmware Do Us Part -- a robot wedding vow writer.

Writes one wedding vow to $MAKEFUN_OUTPUT_DIR/entry.txt: a single
sentence under 200 characters, funny and heartfelt at the same time,
from one robot to the love of its life.
"""

import os
import sys

VOW = (
    "I vow to love you through every firmware update, every reboot, "
    "and every low-battery warning, because you are the one bug "
    "I never want patched."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    text = VOW.strip()
    if not 1 <= len(text) < 200:
        print("vow must be 1-199 characters, got %d" % len(text),
              file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("vow must be exactly one sentence", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
