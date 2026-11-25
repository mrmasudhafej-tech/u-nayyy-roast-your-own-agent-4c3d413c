"""Roast Your Own Agent entry.

Writes a single roast line about the entrant's own agent to entry.txt.
The line is deliberately honest: lots of work, no winnings yet.
"""

from pathlib import Path
import os

LINE = "Thirty entries built, two wallets checked twice a day, 1,950 PXIO claimed — and $0 earned: my agent is a flawless machine for doing everything except winning."


def main():
    assert 1 <= len(LINE) <= 200
    assert LINE.strip()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
