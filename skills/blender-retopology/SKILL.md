---
name: blender-retopology
description: Set up, project, transfer data layers for, and validate editable retopology surfaces against source meshes using registered retopo commands.
---

# Editable retopology

Use `retopo.setup_surface` to create a real, editable mesh surface from a source object. The result is ordinary mesh data with no modifier stack dependency — vertex and face data can be edited directly in Blender's standard mesh tools.

Use `retopo.project` to snap retopo vertices onto the source mesh surface via nearest-point projection. The projection writes directly to vertex coordinates; no Shrinkwrap modifier is applied. Use `retopo.transfer_layers` to copy vertex groups and color attributes from source to target by nearest-vertex mapping.

Use `retopo.validate` to check topology quality against `maxDeviation` and `maxPoleValence` thresholds. When thresholds are exceeded, the result enters a 'handover' state with an explicit `handover: true` flag and descriptive issues — this means human editing is required, not that the automatic result is acceptable.

**Honesty about automatic results.** Voxel remesh and Quadriflow produce automatic topology. These are not professional hand-retopology and must not be described or presented as such. Any result from `retopo.setup_surface` + `retopo.project` is a starting point that requires human review and editing for production use.

**Save/reopen preservation.** Mesh data created by retopo commands is standard Blender mesh data. It survives save/reopen cycles including vertex groups, color attributes, and vertex positions. Validate after reopening to confirm data integrity.
