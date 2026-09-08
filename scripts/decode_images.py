#!/usr/bin/env python3
"""Turn committed *.webp.b64 files into WebP assets for a static Vercel build."""
from __future__ import annotations

import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMAGE_DIR = ROOT / "assets" / "images"


def main() -> None:
    written = 0
    for source in sorted(IMAGE_DIR.glob("*.webp.b64")):
        dest = IMAGE_DIR / source.name.replace(".webp.b64", ".webp")
        dest.write_bytes(base64.b64decode(source.read_text().encode("ascii")))
        written += 1
        print(f"wrote {dest.relative_to(ROOT)}")
    if written == 0:
        print("no .webp.b64 files found; assuming images are already present")


if __name__ == "__main__":
    main()
