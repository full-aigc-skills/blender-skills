---
name: blender-sculpt-surface
description: Create and refine Blender surface detail with topology-bound masks, displacement, foreground sculpt strokes, voxel remesh, Multires, and cleanup modifiers.
---

# Sculpt and surface detail

Use topology-bound selections for masks and deterministic displacement. `sculpt.brush_stroke` requires a foreground VIEW_3D and an active compatible sculpt brush; use it for reproducible strokes, then inspect the actual vertex change.

Record that voxel remesh invalidates old element selections. Keep Multires levels bounded and editable. Decimate/Shrinkwrap cleanup may prepare a proxy but is not production character retopology.

For artistic refinement beyond structured strokes, pause for user takeover, then re-inspect and start a new transaction before continuing. Report topology changes, modifier state and known loss of detail.

## 什么时候使用（When to Use）

需要拓扑绑定遮罩、确定性位移、结构化雕刻笔触、Voxel Remesh、Multires 或表面清理时使用。

## 输入与前置条件（Prerequisites）

- 指定目标对象、拓扑版本、选择/遮罩、笔刷、强度、对称、细节尺度和允许的拓扑变化。
- 前台 sculpt stroke 必须有 VIEW_3D 与兼容活动笔刷。

## 执行流程（Workflow）

Step 1. 检查对象 scale、拓扑和活动模式，绑定选择到当前拓扑版本。
Step 2. 先执行可重复位移或结构化 stroke，并测量实际顶点变化。
Step 3. 仅在批准后进行 voxel remesh 或 Multires，随后废弃旧元素选择。
Step 4. 检查轮廓、细节损失、modifier 状态和后续 retopo 需求。
Step 5. 艺术性自由雕刻时暂停给用户接管，恢复后重新检查并新建事务。

## 验证与交付证据（Validation）

报告前后顶点统计、拓扑版本、stroke 参数、实际位移、remesh/Multires 状态、预览和已知细节损失。

## Rules 与能力边界（不适用场景）

清理 modifier 只能准备代理，不等于生产级角色 retopo；用户接管后不得回滚覆盖人工编辑。

## Gotchas（常见问题与恢复）

- 选择失效：拓扑改变后重新查询，不复用旧索引。
- 细节丢失：从事务快照恢复并调整 voxel size 或层级。
- Stroke 无变化：检查模式、活动笔刷、遮罩和可见几何。
