"""Create the portable evidence templates required by every Blender skill.

The files are deliberately skill-local so a granular `npx skills add --skill`
installation remains complete. Existing files are never overwritten.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render(skill_name: str) -> dict[str, str]:
    title = skill_name.replace("-", " ").title()
    return {
        "examples/request.md": f"""# {title} request example

Use this request shape to remove ambiguity before mutation:

```text
Use {skill_name} for <target object or artifact>.
Inputs: <approved local assets, object names, frame range, units>.
Constraints: <must preserve, forbidden changes, output root>.
Acceptance: <observable measurements, previews, reopen/import checks>.
```

If a required input is unknown, ask for it or report `UNVERIFIED`; do not invent it.
""",
        "examples/validation.md": f"""# {title} validation example

Return a compact evidence packet after the workflow:

```yaml
skill: {skill_name}
scene_revision: <revision>
snapshot_id: <snapshot>
status: PASS | FAIL | UNVERIFIED
measurements: []
previews: []
artifacts: []
remaining_risks: []
```

Command success alone is not `PASS`; attach the checks required by the skill.
""",
        "examples/recovery.md": f"""# {title} recovery example

For a failed or interrupted operation:

1. Stop further mutation and preserve the failing receipt or error.
2. Compare the current scene revision with the operation's expected revision.
3. Classify the cause as missing input, unsupported capability, validation failure, or user takeover.
4. Recover only the affected transaction or artifact; do not overwrite later user work.
5. Re-run the same validation and report both the original failure and recovery evidence.
""",
        "references/acceptance-checklist.md": f"""# {title} acceptance checklist

- [ ] The target, units, frame range, asset roots, and output root are explicit.
- [ ] The operation is supported by the current capability description.
- [ ] Every mutation is bound to the expected scene revision or snapshot.
- [ ] Required measurements, previews, receipts, and file hashes were collected.
- [ ] Save/reopen or re-import was performed when the skill requires persistence proof.
- [ ] Unsupported behavior and unverified claims are disclosed.
- [ ] No upload, publication, payment, installation, or overwrite occurred without authorization.
""",
    }


def main() -> None:
    for skill_dir in sorted((ROOT / "skills").iterdir()):
        if not (skill_dir / "SKILL.md").is_file():
            continue
        for relative, content in render(skill_dir.name).items():
            target = skill_dir / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                continue
            target.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
