## Context

The package contains 23 independently installable domain skills. Many are accurate but only 10–42 lines long, so they do not consistently expose decision inputs, ordered steps, failure modes, or portable references. The plugin repository is out of scope; this change improves the external source package only.

## Goals / Non-Goals

### Goals

- Make each skill executable as a standalone operating guide.
- Preserve current runtime claims and honesty boundaries.
- Use repeatable acceptance evidence rather than narrative completion claims.
- Keep each `SKILL.md` below 500 lines and make granular installs self-contained.

### Non-Goals

- Add or change Blender Harness commands.
- Modify `blender-design-plugin`.
- Move or rewrite published tags.
- Claim unsupported artistic or production-grade automation.

## Decisions

### Use a consistent operational skeleton

Each skill will include `何时使用`, `输入与前置条件`, `执行流程`, `验证与交付证据`, `能力边界`, and `常见问题与恢复`. The domain content remains specific; only the section contract is shared.

### Prefer local references and named handoffs

Required support material will live under the same skill directory. Cross-skill handoffs name the skill and include `npx skills add full-aigc-skills/blender-skills --skill <name>` so granular installations do not contain dead links.

### Gate with lint plus TRACE

A package script checks frontmatter, required sections, dead Markdown links, and file-size limits. The existing deterministic TRACE evaluator supplies the 4.5 score gate. Both are required because TRACE scoring alone cannot prove link integrity or domain correctness.

## Risks / Trade-offs

- Repeated section names increase document length, but make dispatch and evaluation behavior predictable.
- Quality scores can be gamed mechanically; domain-specific evidence and manual review remain mandatory.
- Plugin-vendored copies remain on their current release until a later, separately authorized plugin upgrade.

## Migration Plan

1. Expand and lint all 23 source skills.
2. Run TRACE and resolve every sub-4.5 result.
3. Validate the OpenSpec change.
4. Commit and publish a new immutable skill release only after clean verification.
