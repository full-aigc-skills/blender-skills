---
name: blender-character-rigging
description: Build and inspect editable Blender armatures, skin weights, IK controls, pole targets, joint limits, and prop constraints for character work.
---

# Character rigging

Establish scene scale and character height before creating bones. Build a named hierarchy with positive bone lengths and deform flags, then bind one intended body mesh and assign explicit, topology-bound weights. Inspect bound meshes and bone lengths after binding.

Use IK targets and pole controls for limbs that need planted or directed endpoints; keep FK available through the underlying pose bones. Add joint limits only where their axes and ranges are understood. Test that moving a hand or foot controller changes the intended chain without moving unrelated controls.

For props, keep one object and use an explicit constraint whose influence can be animated. Check world-space continuity at every ownership switch. Rebuild or rescale from recipe parameters when height changes; do not fake a rig by keyframing disconnected body-part objects. Current automatic weight painting and production deformation cleanup are not claimed—use explicit groups and inspect the result.

`rig.rigify_status` distinguishes a bundled module from an enabled add-on. After explicit approval,
use gated `rig.rigify_install`: prefer the bundled Blender 5.2 module, optionally persist user
preferences, and do not use the network. Set `allowDownload: true` only when Rigify is genuinely
absent and the user authorized an official Extensions download; the command accepts no custom URL or
package ID. Call `rig.rigify_generate` only when status reports its operator available and the selected
armature is a compatible metarig. Rigify creates controls and bones; it does not replace mesh skinning
or weight validation.
