## 1. Skill contract

- [x] 1.1 Add `blender-ai-replication` with discriminating triggers (when to use vs. `blender-design`),
      prerequisites (Blender MCP session + harness_cli + target image + output dir), 6-stage workflow
      (launch session → first-version JSON → dream-loop iteration → verify → close session),
      observable validation evidence (`critic.json` per round + final `export.artifact.sha256`
      check), capability boundaries, and Gotchas section referencing `references/pitfalls.md`.
- [x] 1.2 Ship `scripts/dream_loop.py` (~175 lines) — closed-envelope harness wrapper, transaction-
      threaded edits, pluggable critic (`stub` default + `vlm` placeholder). Codeguard-clean.
- [x] 1.3 Ship `references/qingming-sequence.md` — complete first-version JSON command sequence for a
      《清明上河图》 micro-scene: 9 phases, ~30 envelopes, end-to-end from session launch to
      `qm-v1.glb` on disk.
- [x] 1.4 Ship `references/ecosystem-choices.md` — PartMe vs Codex vs ahujasid decision matrix
      with Add-on names, N-panel categories, setup entry points, and drift notes.
- [x] 1.5 Ship `references/pitfalls.md` — 8 verified pitfalls from the 2026-09-23 smoke-test,
      including the `pgrep -f Blender` false-positive workaround.

## 2. Package integration

- [x] 2.1 Add `blender-ai-replication` to the package manifest (`plugin.json`) and bump
      package version `1.1.0` → `1.2.0`. Skills count 25 → 26.
- [x] 2.2 Update bilingual skill catalogs (`README.md` + `README.zh-CN.md`) with the new
      skill row, the bumped count, and the bumped version.
- [x] 2.3 Add a `CHANGELOG.md` entry for 1.2.0 listing the five new artifacts and the
      verified smoke-test provenance.

## 3. Verification

- [x] 3.1 Run `python3 scripts/lint_skills.py` and confirm 26 skills, 0 errors.
- [x] 3.2 Run the live smoke-test (`smoke-test-001`, PartMe plugin cache v0.14.1):
      launch → `capability.list` → `scene.inspect` → `transaction.begin` →
      `scene.screenshot` → `transaction.commit` → `export.file`. Verify:
      173KB PNG + 3.4KB glb + sha256 hash match in artifact receipt.
- [x] 3.3 Validate the OpenSpec change strictly and confirm the lint gate passes after
      including the openspec change artifacts in the staged diff.
- [x] 3.4 Review the final diff, record remaining runtime/provider validation gaps (real
      VLM critic, multi-round convergence, web frontend handoff) as OPEN, and leave
      publication as a separate authorized release action.