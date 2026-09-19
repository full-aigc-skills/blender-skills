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

## 什么时候使用（When to Use）

角色需要可编辑骨架、蒙皮、IK 控制、关节限制或道具约束时使用。仅制作动作时交给 `blender-character-animation`。

## 输入与前置条件（Prerequisites）

- 已确认角色网格、场景单位、目标身高、拓扑版本和变形需求。
- 明确骨骼命名、层级、对称规则、IK 链、pole 方向和关节活动范围。

## 执行流程（Workflow）

Step 1. 检查网格变换、法线、非流形区域和对象比例，保存基线修订号。
Step 2. 建立正骨长、明确 roll 与 deform 标记的层级并验证对称关系。
Step 3. 绑定唯一目标网格，创建显式顶点组并清理未归一权重。
Step 4. 添加 IK、pole、限制和道具约束，逐个移动控制器验证影响范围。
Step 5. 保存重开，并以极限姿态测试主要关节和接触区域。

## 验证与交付证据（Validation）

报告骨骼数、零长度骨骼、层级、绑定网格、未加权顶点、权重和、控制器测试与极限姿态预览。Rigify 还需记录状态探测和 operator 可用性。

## Rules 与能力边界（不适用场景）

骨架生成不等于高质量蒙皮；自动权重必须人工检查。本技能不声称完成人脸绑定、肌肉系统或生产级变形清理。

## Gotchas（常见问题与恢复）

- 网格不随骨架：检查 modifier、对象绑定和顶点组名称。
- IK 不稳定：复核 bone roll、pole 角和链长。
- 权重爆点：定位受影响顶点并归一化，不重绑整个角色掩盖问题。
