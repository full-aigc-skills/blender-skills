"""Lint gate for independently installable Blender skills.

Rules (exit 1 on any violation):
- every directory under skills/ contains SKILL.md
- the package manifest declares every and only packaged skill directory
- frontmatter has a `name` equal to its directory name
- `description` is present, single-line (block scalars break some hosts), 20-1024 chars
- skill names are lowercase kebab-case without a `codex-` prefix
- each skill contains the operational sections required by the package contract
- SKILL.md stays below 500 lines and local Markdown links resolve
- relative links may not escape the current skill directory
- adapted video workflow skills retain their upstream MIT attribution
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
REQUIRED_HEADINGS = (
    "## 什么时候使用（When to Use）",
    "## 输入与前置条件（Prerequisites）",
    "## 执行流程（Workflow）",
    "## 验证与交付证据（Validation）",
    "## Rules 与能力边界（不适用场景）",
    "## Gotchas（常见问题与恢复）",
)


def frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    fields = {}
    for line in text[4:end].splitlines():
        if line and not line.startswith(" ") and ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
        elif line.startswith(" ") or line.startswith("-"):
            # continuation of a block scalar or list: mark parent as multiline
            if fields:
                last = next(reversed(fields))
                fields[last] = fields[last] + "\n" + line
    return fields


def main() -> int:
    errors = []
    skills_dir = ROOT / "skills"
    dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir())
    if not dirs:
        errors.append("skills/ has no skill directories")
    manifest_path = ROOT / ".claude-plugin" / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid package manifest: {exc}")
        manifest = {}
    declared = manifest.get("skills", [])
    declared_names = {
        Path(item.removeprefix("./")).name
        for item in declared
        if isinstance(item, str) and item.startswith("./skills/")
    }
    directory_names = {path.name for path in dirs}
    if declared_names != directory_names:
        missing = sorted(directory_names - declared_names)
        extra = sorted(declared_names - directory_names)
        errors.append(f"manifest skill mismatch: missing={missing}, extra={extra}")
    for skill_dir in dirs:
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{skill_dir.name}: missing SKILL.md")
            continue
        text = skill_md.read_text(encoding="utf-8")
        fm = frontmatter(text)
        name = fm.get("name", "")
        desc = fm.get("description", "")
        if not name:
            errors.append(f"{skill_dir.name}: frontmatter missing name")
        elif name != skill_dir.name:
            errors.append(f"{skill_dir.name}: name '{name}' != directory name")
        if not NAME_RE.match(skill_dir.name):
            errors.append(f"{skill_dir.name}: not lowercase kebab-case")
        if skill_dir.name.startswith("codex-"):
            errors.append(f"{skill_dir.name}: host-prefixed names are not allowed in source packages")
        if not desc:
            errors.append(f"{skill_dir.name}: frontmatter missing description")
        else:
            if "\n" in desc or desc in ("|", ">", "|-", ">-", "|+", ">+"):
                errors.append(f"{skill_dir.name}: description must be single-line (no block scalars)")
            elif not (20 <= len(desc) <= 1024):
                errors.append(f"{skill_dir.name}: description length {len(desc)} outside 20..1024")
        line_count = len(text.splitlines())
        if line_count >= 500:
            errors.append(f"{skill_dir.name}: SKILL.md has {line_count} lines; must stay below 500")
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                errors.append(f"{skill_dir.name}: missing required heading '{heading}'")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (skill_dir / target).resolve()
            try:
                resolved.relative_to(skill_dir.resolve())
            except ValueError:
                errors.append(f"{skill_dir.name}: relative link escapes skill directory: {raw_target}")
                continue
            if not resolved.exists():
                errors.append(f"{skill_dir.name}: broken local link: {raw_target}")
    video_skills = {"blender-video-original", "blender-video-recreate"}
    if video_skills & directory_names:
        notice_path = ROOT / "NOTICE"
        notice = notice_path.read_text(encoding="utf-8") if notice_path.is_file() else ""
        if "modengsir/blender-video-workflows" not in notice or "MIT License" not in notice:
            errors.append("NOTICE must retain blender-video-workflows MIT attribution")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"lint_skills: {len(dirs)} skills, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
