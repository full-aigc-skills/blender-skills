---
name: blender-inspect
description: "Inspect an active Blender scene read-only before Codex designs, modifies, previews, or exports it."
---

# Blender Scene Inspection

Send `scene.inspect` to the active Harness session. Report object names and types, collections,
active camera, frame range, materials, lights, missing assets, warnings, and `sceneRevision`.

Do not use mutating operators during inspection. If Blender changed outside Codex, re-inspect
instead of guessing and use the new revision for subsequent commands.
