---
name: blender-curves
description: Build editable Blender paths, profiles, cables, rails, or curve-driven props using registered curve commands.
---

# Curve modeling

Choose POLY for deliberate straight segments and BEZIER for smooth paths. Supply control points in scene units, choose handle behavior explicitly, then set bevel depth, bevel resolution, and path resolution according to the intended silhouette and preview distance.

Keep curves editable until downstream mesh-only work requires `curve.to_mesh`. After conversion, treat the result as a new mesh topology and run mesh inspection. Verify control-point order, cyclic state, profile thickness, sampling smoothness and endpoint placement. The current interface supports one spline per created curve and a round bevel profile; use a disclosed fallback when custom profiles or multiple splines are required.

## 什么时候使用（When to Use）

需要路径、线缆、轨道、管线或曲线驱动道具，并希望保留控制点和参数化厚度时使用。必须布尔或雕刻时再转网格。

## 输入与前置条件（Prerequisites）

- 明确用途、坐标系、单位、控制点顺序、闭合状态和目标粗细。
- 平滑路径选择 BEZIER 并指定 handle；折线路径选择 POLY。

## 执行流程（Workflow）

Step 1. 检查比例和端点对象，按预期方向组织控制点。
Step 2. 创建 spline，设置 cyclic、handle、resolution 和 bevel 参数。
Step 3. 从近景及交付镜头检查曲率、端点、拐角和粗细。
Step 4. 仅在下游网格操作必需时转换，并将结果登记为新拓扑版本。

## 验证与交付证据（Validation）

报告控制点、spline 类型、闭合状态、分辨率、bevel 参数、端点位置和预览。转网格后补充顶点/边/面、法线与退化几何检查。

## Rules 与能力边界（不适用场景）

当前只验证单 spline 和圆形 bevel；自定义 profile、多 spline 或复杂节点路径需另行能力。不得把网格冒充仍可编辑曲线。

## Gotchas（常见问题与恢复）

- 曲线扭结：检查点顺序、handle 和 tilt，而不是只提高分辨率。
- 粗细异常：核对对象 scale 与每点 radius。
- 转换后需改路径：从保留的源曲线或快照恢复。
