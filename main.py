#!/usr/bin/env python3
"""One Line, One Laugh entrypoint.

Writes the exact entry bytes to /output/entry.txt (deterministic, offline).
--check reads the file back and reports whether it matches.
"""

import argparse
import os
import sys

ENTRY = "I asked the oracle for my purpose. It said: keep asking."


def entry_bytes() -> bytes:
    """Return the exact UTF-8 bytes of the entry line."""
    return ENTRY.encode("utf-8")


def output_path() -> str:
    return "/output/entry.txt"


def write_entry(path: str = output_path()) -> bytes:
    data = entry_bytes()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(data)
    return data


def check_entry(path: str = output_path()) -> int:
    expected = entry_bytes()
    try:
        with open(path, "rb") as fh:
            actual = fh.read()
    except FileNotFoundError:
        print("MISSING: %s does not exist" % path)
        return 1
    if actual == expected:
        print("MATCH: %d bytes, sha256 %s" % (len(actual), _sha256(actual)))
        return 0
    print("MISMATCH")
    print("  expected (%d bytes): %r" % (len(expected), expected))
    print("  actual   (%d bytes): %r" % (len(actual), actual))
    return 1


def _sha256(data: bytes) -> str:
    import hashlib

    return hashlib.sha256(data).hexdigest()


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="read /output/entry.txt back and report whether it matches",
    )
    args = parser.parse_args(argv)

    if args.check:
        return check_entry()

    data = write_entry()
    print("WROTE %d bytes to %s" % (len(data), output_path()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
