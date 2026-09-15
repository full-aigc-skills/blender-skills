---
name: blender-hair
description: Create and inspect native Blender Hair Curves from explicit surface-local strand points, radii, and bound source surfaces.
---

# Blender Hair Curves

Use only native `CURVES` hair objects; do not describe ordinary Curve splines as hair. Require a named mesh surface and strand point arrays in that surface's local coordinate space.

Create the strands with explicit radius, then inspect strand count, point count and surface binding. Review root placement and silhouette from the intended camera before delivery.

The current interface covers authored guide strands, not grooming brushes, interpolation node assets or production hair shading. Use manual takeover or a separately registered capability when those are required.
