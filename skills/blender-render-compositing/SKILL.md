---
name: blender-render-compositing
description: Configure Blender Eevee or Cycles, render passes, color management, material baking, dependency packing, compositor nodes, and verified extended exports.
---

# Render and compositing

Probe devices before selecting Cycles GPU. Honor an explicit CPU fallback; never claim GPU rendering from engine selection alone. Configure resolution, samples, transparency, view transform/look, exposure and required view-layer passes before rendering.

Use reusable shader node groups and semantic texture connections. Bake only meshes with an active UV layer and approved output root, then pack required image dependencies and make paths relative before standalone delivery. Reopen the packed `.blend` in an independent directory.

Build the named compositor chain without deleting unrelated nodes; inspect links after configuration. Use the version-2 extended receipt for EXR, USD and Alembic so the legacy export receipt remains compatible. Verify each artifact exists, is non-empty and reopens or imports within the format's supported scope. Device, pass and format availability are runtime facts, not Add-on metadata assumptions.

For long animation delivery, prefer RENDER_ANIMATION_FRAMES over direct MP4 export. It binds PNG or multilayer EXR frames to the submitted `.blend` snapshot, records every frame hash, and supports explicit missing-frame recovery. Configure a File Output node only inside the approved output root. Reusable VSE looks belong in a compositor node group consumed by a COMPOSITOR strip modifier. Final MP4 composition is a separate COMPOSE_VIDEO job so encoding changes do not rerender 3D frames.

## 什么时候使用（When to Use）

配置 Eevee/Cycles、渲染通道、色彩管理、材质烘焙、依赖打包、合成节点或扩展格式交付时使用。

## 输入与前置条件（Prerequisites）

- 明确引擎、设备回退、分辨率、采样、色彩设置、通道、帧范围和输出根目录。
- 烘焙对象必须有活动 UV；长动画使用不可变快照与后台帧序列。

## 执行流程（Workflow）

Step 1. 探测设备和格式能力，选择引擎并记录真实设备，不能只凭配置宣称 GPU。
Step 2. 设置分辨率、采样、透明、view transform、曝光与 view-layer passes。
Step 3. 构建或复用命名材质/合成节点组，检查所有语义链接。
Step 4. 烘焙或渲染到批准目录；长动画逐帧输出后再独立合成视频。
Step 5. 打包依赖、相对化路径并在独立目录重开或重导入。

## 验证与交付证据（Validation）

提交设备探测、引擎、通道、色彩设置、节点链接、帧哈希、媒体探测、依赖清单和独立重开结果。

## Rules 与能力边界（不适用场景）

引擎选择不证明 GPU 实际工作；简单夹具不代表电影级质量。不得把视频编码变更触发为 3D 全量重渲。

## Gotchas（常见问题与恢复）

- GPU 不可用：按批准策略回退 CPU 并披露性能影响。
- 黑帧或缺通道：检查 view layer、相机、输出节点和帧清单。
- 外部打开丢贴图：重新检查打包与相对路径后独立重开。
