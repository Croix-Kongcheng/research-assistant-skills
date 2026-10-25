"""Validate distributable skills, local resources, configuration, and portability.

This validates the repository's artifacts. It does not execute papers or certify
the behavior of an agent, a PDF renderer, or a scientific method.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]


def has_machine_path(content: str) -> bool:
    # Public documentation URLs such as matplotlib.org/stable/users/explain/
    # are not personal filesystem paths.
    local_text = re.sub(r"https?://[^\s<>\])]+", "URL", content, flags=re.I)
    return bool(re.search(r"(?i)(?<![\w])[a-z]:[\\/]|file://|/(?:Users|home)/[\w.-]+/", local_text))


def local_targets(markdown: str):
    """Inspect real Markdown links and images, excluding illustrative code."""
    for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", prose(markdown)):
        target = target.strip()
        if target.startswith("<"):
            target = target[1:target.index(">")]
        if re.match(r"[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
            continue
        yield unquote(target.split("#", 1)[0])


def prose(markdown: str) -> str:
    """Skip fenced and inline examples when inspecting resource references."""
    result = []
    fence = None
    for line in markdown.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)[0]
            fence = None if fence == marker else marker
            continue
        if fence is None:
            result.append(line)
    # Keep an inline-code label usable inside [label](target), but do not
    # interpret an entire backticked example link as a required resource.
    return re.sub(r"(`+)([^\n]*?)\1", "CODE", "\n".join(result))


def check() -> list[str]:
    errors = []
    skills = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
    if not skills:
        errors.append("No skill folders found")
    shared = (ROOT / "docs/configuration.md").read_bytes()
    for folder in skills:
        entry = folder / "SKILL.md"
        if not entry.is_file():
            errors.append(f"{folder.name}: missing SKILL.md")
            continue
        text = entry.read_text(encoding="utf-8-sig")
        match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
        try:
            metadata = yaml.safe_load(match.group(1)) if match else None
        except yaml.YAMLError as exc:
            errors.append(f"{entry.relative_to(ROOT)}: invalid frontmatter: {exc}")
            metadata = None
        if not isinstance(metadata, dict):
            errors.append(f"{entry.relative_to(ROOT)}: missing frontmatter dictionary")
        else:
            name = metadata.get("name", "")
            if name != folder.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
                errors.append(f"{folder.name}: invalid or inconsistent name")
            description = metadata.get("description")
            if not isinstance(description, str) or not description.strip() or len(description) > 1024:
                errors.append(f"{folder.name}: missing/invalid description")
            allowed = {"name", "description", "license", "allowed-tools", "metadata"}
            if set(metadata) - allowed:
                errors.append(f"{folder.name}: unsupported frontmatter fields")
            if metadata.get("license") and not (folder / "LICENSE").is_file():
                errors.append(f"{folder.name}: independent distribution is missing LICENSE")
        shared_copy = folder / "references/workspace-config.md"
        if shared_copy.exists() and shared_copy.read_bytes() != shared:
            errors.append(f"{folder.name}: workspace contract differs from docs/configuration.md")
        ui_path = folder / "agents/openai.yaml"
        if ui_path.exists():
            try:
                ui = yaml.safe_load(ui_path.read_text(encoding="utf-8-sig"))["interface"]
                short = ui.get("short_description", "")
                if not isinstance(short, str) or not 25 <= len(short) <= 64:
                    errors.append(f"{folder.name}: UI description must be 25–64 characters")
                if f"${folder.name}" not in ui.get("default_prompt", ""):
                    errors.append(f"{folder.name}: default_prompt must mention the skill")
                if not ui.get("display_name"):
                    errors.append(f"{folder.name}: missing UI display_name")
            except (yaml.YAMLError, KeyError, TypeError) as exc:
                errors.append(f"{folder.name}: invalid UI metadata: {exc}")
        for path in sorted(folder.rglob("*.md")):
            content = path.read_text(encoding="utf-8-sig")
            rel = path.relative_to(ROOT)
            # A packaged skill must not point to one machine's real home or drive.
            if has_machine_path(content):
                errors.append(f"{rel}: machine-specific absolute path")
            if re.search(r"\[TODO:|\[INSERT(?:\s|_)|\bPLACEHOLDER_DESCRIPTION\b", content, re.I):
                errors.append(f"{rel}: unfinished scaffold")
            for target in local_targets(content):
                resolved = (path.parent / target).resolve()
                if not resolved.is_relative_to(folder.resolve()):
                    errors.append(f"{rel}: runtime resource escapes skill folder: {target}")
                elif not resolved.is_file():
                    errors.append(f"{rel}: missing local resource: {target}")
    config = yaml.safe_load((ROOT / "examples/research-skills.example.yaml").read_text(encoding="utf-8"))
    if config.get("version") != 1 or not isinstance(config.get("paths"), dict):
        errors.append("Invalid example workspace configuration")
    for key in ("notes", "papers", "knowledge", "attachments", "knowledge_index"):
        if not isinstance(config.get("paths", {}).get(key), str):
            errors.append(f"Example configuration: invalid paths.{key}")
    if not isinstance(config.get("topics"), dict):
        errors.append("Example configuration: topics must be a mapping")
    documentation = [*ROOT.glob("*.md"), *(ROOT / "docs").rglob("*.md"), *(ROOT / "examples").rglob("*.md")]
    for path in documentation:
        content = path.read_text(encoding="utf-8-sig")
        if has_machine_path(content):
            errors.append(f"{path.relative_to(ROOT)}: machine-specific absolute path")
        for target in local_targets(content):
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(ROOT.resolve()):
                errors.append(f"{path.relative_to(ROOT)}: documentation link escapes repository: {target}")
            elif not resolved.is_file():
                errors.append(f"{path.relative_to(ROOT)}: missing documentation link: {target}")
    print(f"Checked {len(skills)} skills, packaged references, UI metadata and workspace configuration.")
    return errors


if __name__ == "__main__":
    failures = check()
    if failures:
        for failure in failures:
            print(f"ERROR: {failure}", file=sys.stderr)
        raise SystemExit(1)
    print("Validation passed. Behavioral and scientific verification remain separate.")
