---
name: blender-uv-material
description: Prepare UVs and physically based Blender materials for editable product or character assets, including texture color-space and normal-map semantics.
---

# UV and material workflow

Apply intended object scale before unwrapping. Obtain a fresh topology-bound selection, mark deliberate seams, unwrap selected faces and pack islands with explicit margins. Re-query selections after topology edits. Use `uv.inspect` to check missing, out-of-bounds and degenerate UVs; the current checker does not prove islands are non-overlapping, so visually inspect important assets.

Create PBR materials with finite normalized values. Connect base-color images as sRGB and roughness, metallic and normal data as Non-Color. Normal usage must pass through a Normal Map node. Import textures only from approved asset roots and preserve their source paths in delivery evidence.

Use `material.create_node_group` for the supported reusable shader controls and `material.bake` only with an active UV layer and approved output root. Save a working `.blend` before making paths relative, pack required images, then reopen the packed project from an independent directory.

Check node links, image paths, color spaces, UV coverage and material assignment before export. UV island overlap detection and arbitrary shader-node authoring remain outside the current verified interface; state that limitation rather than treating a successful bake as complete look development.

## 什么时候使用（When to Use）

资产需要 UV 展开、PBR 材质、纹理色彩空间、法线贴图、材质烘焙或依赖打包时使用。

## 输入与前置条件（Prerequisites）

- 明确对象、拓扑版本、scale、seam 意图、texel 目标、贴图来源和输出根目录。
- 纹理必须来自批准资产根；烘焙前确认活动 UV 和目标图像。

## 执行流程（Workflow）

Step 1. 应用预期 scale，获取绑定当前拓扑的面选择并标记 seams。
Step 2. 展开并按明确 margin 打包，运行 UV 缺失、越界和退化检查。
Step 3. 创建有限范围 PBR 参数并按语义连接纹理与 Normal Map 节点。
Step 4. 在授权目录烘焙，保存工作 `.blend`，打包依赖并相对化路径。
Step 5. 从独立目录重开，检查材质分配、链接、色彩空间与预览。

## 验证与交付证据（Validation）

提供 UV layer、覆盖/越界/退化统计、seam 与 margin、节点链接、图像路径、色彩空间、烘焙文件哈希和重开结果。

## Rules 与能力边界（不适用场景）

当前检查不证明 islands 无重叠，也不支持任意 shader 节点创作；成功烘焙不等于完整 lookdev。

## Gotchas（常见问题与恢复）

- UV 拉伸：复核 scale、seam 与投影方式后重展。
- 法线方向错误：确保数据纹理为 Non-Color 并经过 Normal Map 节点。
- 独立打开丢贴图：检查 pack 与相对路径，再执行重开验证。
