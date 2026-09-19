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

## 什么时候使用（When to Use）

高密度源网格需要可编辑低模起点、表面投射、数据层传递与阈值验收时使用。

## 输入与前置条件（Prerequisites）

- 指定源网格、目标面数或密度、最大偏差、最大极点 valence 和需传递的数据层。
- 明确自动结果只是起点，生产角色拓扑仍需人工编辑与审核。

## 执行流程（Workflow）

Step 1. 检查源网格变换、法线与拓扑，创建独立可编辑目标表面。
Step 2. 投射目标顶点到源表面并记录实际偏差。
Step 3. 按最近顶点传递已声明顶点组和颜色属性。
Step 4. 运行阈值验证；超限时设置 handover，而不是伪造通过。
Step 5. 保存重开并复核顶点、面、数据层和位置完整性。

## 验证与交付证据（Validation）

报告源/目标对象、顶点面数、最大/平均偏差、极点统计、传递层、handover 状态和重开结果。

## Rules 与能力边界（不适用场景）

Voxel Remesh 与 Quadriflow 不是专业手工 retopo；投射结果不自动满足变形流线、UV 或生产质量。

## Gotchas（常见问题与恢复）

- 偏差超限：定位区域并交由人工编辑，不反复自动重拓扑碰运气。
- 数据层缺失：核对源层名称与映射范围。
- 重开不一致：停止交付并从保存前快照复查序列。
