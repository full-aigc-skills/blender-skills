---
name: blender-export
description: "Export an approved Blender snapshot to verified model, image, video, EXR, USD, or Alembic artifacts using compatible receipt contracts."
---

# Blender Export

Export only from the approved `sceneRevision + snapshotId` and under an approved output root.
Existing files require action-bound overwrite authorization.

In `auto_with_budget`, `export.file` may write a new file in an allowed format under the
session's approved root, using the current committed snapshot, without another user prompt.
`review_only` rejects export even with a claim. Following user takeover, inspect again and create
a new transaction/snapshot; old approvals must not be reused.

Call `export.file`; verify existence, non-zero size, SHA-256, format, and receipt schema. Model
formats require isolated re-import validation; images and MP4 require media probing. Distinguish
local export success from any downstream rendering system.

Use `export.extended` for EXR, USD/USDC and Alembic and preserve its receiptVersion 2.0.0 instead
of rewriting it as the legacy receipt. For a long EXPORT or RENDER_STILL, use
`blender-background-jobs`; `export.file` itself remains synchronous. Do not promise that
pause interrupts an already-running synchronous export.
