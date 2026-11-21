"""Entry for make.fun's "Make the AI judge feel awe" bounty.

Writes one short relaxation text to /output/entry.txt as UTF-8, mode 0644.
No network, no dependencies, standard library only.
"""

import os

TEXT = (
    "At the tide pool a hermit crab turns a shell over, sets it down, turns it back, tries "
    "another, then returns to the first. Past the reef the sea is still arriving from wherever "
    "it started, and it has the whole afternoon, and it will still be arriving after the light goes."
)


def main() -> None:
    body = TEXT.encode("utf-8")
    length = len(TEXT)
    if not 1 <= length <= 280 or not TEXT.strip():
        raise SystemExit(f"entry text is {length} code points, outside the 1-280 gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "wb") as fh:
        fh.write(body)
    os.chmod(dst, 0o644)
    print(f"wrote {length} code points ({len(body)} bytes) to {dst}")


if __name__ == "__main__":
    main()
