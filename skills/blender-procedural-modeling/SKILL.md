---
name: blender-procedural-modeling
description: Build or update reusable Blender Geometry Nodes systems and parameterized environments with version-probed node and socket semantics.
---

# Procedural modeling

Inspect `geometry_nodes` capability availability for the running Blender version. Create declared group inputs, then address nodes by stable names and sockets by identifier or explicit name—never by UI position. Keep instances until downstream editing or export requires realization.

Use `recipe.procedural_courtyard` for the supported courtyard layout and its update recipe for dimensions, arch count and rubble density. Preserve object and node-group names so cameras and references survive parameter changes.

Inspect group interface, nodes and links after construction; evaluate the resulting mesh and review density, scale, clipping and scene complexity visually. A node type unavailable in the running Blender version must return a capability error, not fall back to expert Python or silently install an extension.

## 什么时候使用（When to Use）

需要可复用 Geometry Nodes、参数化环境、重复实例或可通过输入更新的生成系统时使用。

## 输入与前置条件（Prerequisites）

- 明确 Blender 版本、节点能力、输入参数、对象/节点组稳定名称和性能预算。
- 记录实例是否必须保留，以及何时允许 realization。

## 执行流程（Workflow）

Step 1. 探测运行时节点与 socket 能力，缺失时返回明确能力错误。
Step 2. 创建命名 group inputs，按稳定节点名和 socket identifier 建立节点与链接。
Step 3. 使用小规模参数验证拓扑和语义，再扩展密度与范围。
Step 4. 检查接口、节点、链接及评估网格，并从交付视角审阅。
Step 5. 更新时复用稳定名称，只改变已声明参数，不重建无关引用。

## 验证与交付证据（Validation）

报告节点组接口、节点/链接清单、输入值、实例/实现状态、评估几何统计、性能信息和预览。

## Rules 与能力边界（不适用场景）

不通过 expert Python 或静默安装扩展绕过缺失节点；不在下游没有要求时实现全部实例。

## Gotchas（常见问题与恢复）

- Socket 不匹配：按 identifier/name 重新探测，不依赖 UI 位置。
- 场景过重：降低密度并保留实例，记录性能预算。
- 更新破坏引用：恢复稳定对象和节点组名称后重新验证依赖。
