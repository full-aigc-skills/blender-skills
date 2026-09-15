---
name: blender-render-compositing
description: Configure Blender Eevee or Cycles, render passes, color management, material baking, dependency packing, compositor nodes, and verified extended exports.
---

# Render and compositing

Probe devices before selecting Cycles GPU. Honor an explicit CPU fallback; never claim GPU rendering from engine selection alone. Configure resolution, samples, transparency, view transform/look, exposure and required view-layer passes before rendering.

Use reusable shader node groups and semantic texture connections. Bake only meshes with an active UV layer and approved output root, then pack required image dependencies and make paths relative before standalone delivery. Reopen the packed `.blend` in an independent directory.

Build the named compositor chain without deleting unrelated nodes; inspect links after configuration. Use the version-2 extended receipt for EXR, USD and Alembic so the legacy export receipt remains compatible. Verify each artifact exists, is non-empty and reopens or imports within the format's supported scope. Device, pass and format availability are runtime facts, not Add-on metadata assumptions.

For long animation delivery, prefer RENDER_ANIMATION_FRAMES over direct MP4 export. It binds PNG or multilayer EXR frames to the submitted `.blend` snapshot, records every frame hash, and supports explicit missing-frame recovery. Configure a File Output node only inside the approved output root. Reusable VSE looks belong in a compositor node group consumed by a COMPOSITOR strip modifier. Final MP4 composition is a separate COMPOSE_VIDEO job so encoding changes do not rerender 3D frames.
