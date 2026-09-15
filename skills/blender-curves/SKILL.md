---
name: blender-curves
description: Build editable Blender paths, profiles, cables, rails, or curve-driven props using registered curve commands.
---

# Curve modeling

Choose POLY for deliberate straight segments and BEZIER for smooth paths. Supply control points in scene units, choose handle behavior explicitly, then set bevel depth, bevel resolution, and path resolution according to the intended silhouette and preview distance.

Keep curves editable until downstream mesh-only work requires `curve.to_mesh`. After conversion, treat the result as a new mesh topology and run mesh inspection. Verify control-point order, cyclic state, profile thickness, sampling smoothness and endpoint placement. The current interface supports one spline per created curve and a round bevel profile; use a disclosed fallback when custom profiles or multiple splines are required.
