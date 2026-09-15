---
name: blender-sculpt-surface
description: Create and refine Blender surface detail with topology-bound masks, displacement, foreground sculpt strokes, voxel remesh, Multires, and cleanup modifiers.
---

# Sculpt and surface detail

Use topology-bound selections for masks and deterministic displacement. `sculpt.brush_stroke` requires a foreground VIEW_3D and an active compatible sculpt brush; use it for reproducible strokes, then inspect the actual vertex change.

Record that voxel remesh invalidates old element selections. Keep Multires levels bounded and editable. Decimate/Shrinkwrap cleanup may prepare a proxy but is not production character retopology.

For artistic refinement beyond structured strokes, pause for user takeover, then re-inspect and start a new transaction before continuing. Report topology changes, modifier state and known loss of detail.
