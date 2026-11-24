"""Produce the single-line office joke for the make.fun bounty.

The program places one line of text at /output/entry.txt. The judge
reads that file, so the run has to leave exactly one line there, with
nothing extra trailing behind it.
"""

from pathlib import Path

# The joke itself. Kept in one place so its length stays easy to check.
ENTRY = "My calendar has a meeting called 'Quick Sync' that has outlasted two managers and one marriage."

# The competition gate wants between 1 and 199 characters.
assert 1 <= len(ENTRY) <= 199, "entry length is outside the allowed range"

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the entry line, leaving no newline after it.

    Creating the parent directory first means the script works whether
    /output already exists or the run is starting from a clean image.
    """
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
