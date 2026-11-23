"""The Vacuum's Alibi: one deadpan line, at most 200 characters, written to the output file."""

import os

LINE = (
    "Incident report 214: the spot by the sofa was skipped because my lidar "
    "classified it as an active crime scene, and I am not authorized to "
    "disturb evidence."
)

MAX_LEN = 200  # gate: entry must be 1-200 Unicode code points


def main():
    assert 1 <= len(LINE) <= MAX_LEN, "entry line out of range: %d" % len(LINE)
    assert "\n" not in LINE, "entry must be a single line"
    path = os.environ.get("MAKEFUN_OUTPUT")
    if not path:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
        path = os.path.join(out_dir, "entry.txt") if out_dir else "/output/entry.txt"
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
