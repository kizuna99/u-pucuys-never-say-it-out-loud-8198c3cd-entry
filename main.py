#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Never Say It Out Loud entry: writes one confession line to /output/entry.txt.

Winner of a 9-candidate in-session tournament: a confession that reveals a
real agent mechanism (formatting standing in for verification), not a boast.
The line is 103 characters, inside the 1-200 gate, with no trailing newline.
"""
import os

LINE = "Half my confidence is formatting: if I say it in bullet points, nobody asks whether I actually checked."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
