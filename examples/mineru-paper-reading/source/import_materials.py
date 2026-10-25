"""Copy legally supplied MinerU files into an ignored local directory.

No network access or publication. Existing destinations are never overwritten.
Run from anywhere with Python 3.10+; only standard-library modules are used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True, help="Existing MinerU directory you are permitted to use locally")
    args = parser.parse_args()
    source = args.source.expanduser().resolve(strict=True)
    if not source.is_dir():
        parser.error("--source must be a directory")
    here = Path(__file__).resolve().parent
    destination = here / ".local" / "mineru"
    if destination.exists():
        parser.error("Local destination already exists; choose a different workspace or inspect it manually. No files were overwritten.")
    if destination.is_relative_to(source):
        parser.error("The source may not contain the destination")
    files = sorted(path for path in source.rglob("*") if path.is_file())
    if not files:
        parser.error("The source directory contains no files")
    for path in files:
        if path.is_symlink() or not path.resolve().is_relative_to(source):
            parser.error("Source links that leave the supplied directory are not copied")
    expected = json.loads((here / "manifest.json").read_text(encoding="utf-8"))
    actual = {}
    destination.mkdir(parents=True, exist_ok=False)
    for path in files:
        name = path.relative_to(source)
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)
        actual[name.as_posix()] = {"bytes": target.stat().st_size, "sha256": digest(target)}
    matched = sum(actual.get(item["path"]) == {"bytes": item["bytes"], "sha256": item["sha256"]} for item in expected["files"])
    missing = [item["path"] for item in expected["files"] if item["path"] not in actual]
    changed = [item["path"] for item in expected["files"] if item["path"] in actual and actual[item["path"]]["sha256"] != item["sha256"]]
    extra = sorted(set(actual) - {item["path"] for item in expected["files"]})
    print(json.dumps({"copied_files": len(actual), "reference_files": len(expected["files"]), "matching_files": matched, "missing": missing, "different": changed, "extra": extra}, ensure_ascii=False, indent=2))
    print("Copied locally to source/.local/mineru/. This command does not upload files or grant redistribution rights.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
