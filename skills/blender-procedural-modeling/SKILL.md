---
name: blender-procedural-modeling
description: Build or update reusable Blender Geometry Nodes systems and parameterized environments with version-probed node and socket semantics.
---

# Procedural modeling

Inspect `geometry_nodes` capability availability for the running Blender version. Create declared group inputs, then address nodes by stable names and sockets by identifier or explicit name—never by UI position. Keep instances until downstream editing or export requires realization.

Use `recipe.procedural_courtyard` for the supported courtyard layout and its update recipe for dimensions, arch count and rubble density. Preserve object and node-group names so cameras and references survive parameter changes.

Inspect group interface, nodes and links after construction; evaluate the resulting mesh and review density, scale, clipping and scene complexity visually. A node type unavailable in the running Blender version must return a capability error, not fall back to expert Python or silently install an extension.
