## 1. Authoring contract

- [x] 1.1 Expand all 23 skills with trigger, prerequisites, workflow, validation, boundaries, and recovery guidance.
- [x] 1.2 Replace install-fragile cross-skill and package-document links with portable handoffs or skill-local references.

## 2. Quality gates

- [x] 2.1 Add deterministic package lint for frontmatter, required sections, link integrity, and length.
- [x] 2.2 Run lint with zero failures.
- [x] 2.3 Run TRACE for all 23 skills and reach overall score 4.5 or higher for every skill.
- [x] 2.4 Replace push-based dispatch to the obsolete repository with immutable release dispatch to `full-aigc-plugins/blender-design-plugin`.
- [x] 2.5 Enforce the pinned TRACE evaluator in CI and remove the obsolete Codex-only README identity.

## 3. OpenSpec and release

- [x] 3.1 Validate the change in strict mode.
- [x] 3.2 Review diff for runtime-claim accuracy and granular-install portability.
- [x] 3.3 Commit and push the source repository without moving an existing tag.
- [x] 3.4 Create a new immutable release and verify tag, commit, and release alignment.
- [x] 3.5 Verify the release dispatch contains the immutable tag and peeled commit SHA; record the scoped-token blocker.

> Blocked evidence: release run `35467321284` carried `ref=v1.0.1` and SHA
> `13c28068df82d3187f2e89f0fe96d8240fa42518`, but GitHub returned HTTP 403 because
> `SKILLS_SYNC_TOKEN` cannot dispatch to `full-aigc-plugins/blender-design-plugin`.

> Reconfirmed for immutable release `v1.0.2`: run `35472187103` resolved peeled
> SHA `335f78e74199658fa1c38db4830ead61c314988f`, then returned HTTP 403 for the
> current plugin repository. Source tag and Release are valid; token repository
> access remains the only blocker.
