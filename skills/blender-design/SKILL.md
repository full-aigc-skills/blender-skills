---
name: blender-design
description: "Turn a user's idea into a Blender scene through milestone-based modeling, materials, lighting, camera, and animation commands."
---

# Blender Design Workflow

Inspect, then create an implementation brief before mutation: requested assets, supplied
references, missing references, scene constraints, camera route, animation beats, duration, and
required exports. If a required reference is missing, ask the user for it by default. Create a
Blender-designed proxy only when the user explicitly requests design of the missing asset, and
record its assumptions and deviations in the delivery receipt.

For an `auto_with_budget` request, execute the approved brief through every safe milestone
without asking after each preview. Capture the same previews and validation evidence, but present
them together with the final artifact inventory. Stop only for a forbidden missing asset, path
escape, deletion/overwrite, expert Python or failed validation requiring recovery. Remote budget
enforcement is owned by the downstream plugin.

Translate the approved brief into named components, then complete Scene Structure, Modeling,
Materials, Lighting and Camera, Animation, and Final Preview milestones. Use one transaction per
milestone and `expectedSceneRevision` on every mutation.

Delegate each milestone to the precise domain Skill advertised by `capability.describe`; do not
keep advanced animation, cinematography, quality validation, background jobs, or simulation under
this general workflow. Multi-domain recipes may load multiple Skills declared by the capability.

Prefer registered commands over expert Python. Read `session.status` and show the actual scene
in the foreground before work. Update `session.set_progress` with an honest stage and optional
progress fraction; report actual objects changed, not a synthetic completion percentage.
After each milestone generate fresh previews. In interactive mode wait for approval; in automatic
mode assess the previews against the approved brief, then commit without another prompt.
On failure recover the transaction only if the user has not taken over. Command success alone is not
design acceptance. Before final export, verify all brief constraints that are observable in the
scene and preview: object count and uniqueness, animation beat order, frame range, camera route,
and required deliverable formats. Return the artifact inventory and explicitly ask whether the
user wants to finish locally or hand off only when that choice was not already made.
Downstream AI rendering is outside this Skill.

Read [foreground control and recovery](../blender-use/references/foreground-policy.md).
On `SESSION_PAUSED`, stop design commands. Only a user resume permits continuation; then inspect
again and begin a new transaction. Never roll back the pre-takeover transaction over user edits.
