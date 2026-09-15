---
name: blender-hard-surface
description: Create editable hard-surface, product, mechanical, or prop geometry with registered Blender mesh, modifier, collection, and recipe commands.
---

# Hard-surface modeling

Inspect the scene, units, capability details, and supplied dimensions before mutation. Preserve separate functional parts and an editable modifier order. Prefer Mirror/Array for repetition, Boolean for openings, Bevel for manufactured edges, Solidify for sheet thickness, and Subdivision only when the intended silhouette needs it.

Use `recipe.hard_surface_shell` or `recipe.spear` when its declared output matches the task. Otherwise combine registered object, mesh, modifier, curve, and collection commands. Never use expert Python to claim missing hard-surface coverage.

After topology changes, discard old mesh selections and query a new topology version. Inspect designated solids with `mesh.inspect`; explicitly set `allowOpenSurface` only for intentionally open surfaces. Check dimensions, modifier order, helper visibility, normals, degenerate geometry, and whether requested parts remain independently editable. L2 recipe output is not L3 until a saved, reopened, visually reviewed and reimported deliverable passes.

If a required asset, exact dimension, unsupported modifier parameter, or extension is missing, report it. Only invent a proxy when the task already authorizes original design, and list that proxy in delivery.
