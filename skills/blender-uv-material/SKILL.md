---
name: blender-uv-material
description: Prepare UVs and physically based Blender materials for editable product or character assets, including texture color-space and normal-map semantics.
---

# UV and material workflow

Apply intended object scale before unwrapping. Obtain a fresh topology-bound selection, mark deliberate seams, unwrap selected faces and pack islands with explicit margins. Re-query selections after topology edits. Use `uv.inspect` to check missing, out-of-bounds and degenerate UVs; the current checker does not prove islands are non-overlapping, so visually inspect important assets.

Create PBR materials with finite normalized values. Connect base-color images as sRGB and roughness, metallic and normal data as Non-Color. Normal usage must pass through a Normal Map node. Import textures only from approved asset roots and preserve their source paths in delivery evidence.

Use `material.create_node_group` for the supported reusable shader controls and `material.bake` only with an active UV layer and approved output root. Save a working `.blend` before making paths relative, pack required images, then reopen the packed project from an independent directory.

Check node links, image paths, color spaces, UV coverage and material assignment before export. UV island overlap detection and arbitrary shader-node authoring remain outside the current verified interface; state that limitation rather than treating a successful bake as complete look development.
