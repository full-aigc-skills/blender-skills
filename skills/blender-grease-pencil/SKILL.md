---
name: blender-grease-pencil
description: Create editable Blender Grease Pencil layers, materials, frame drawings, and mixed 2D/3D scenes with structured stroke data.
---

# Grease Pencil

Create named layers and Grease Pencil materials before strokes. Add points in object-local 3D coordinates with explicit radius, opacity, frame and cyclic state. Keep line art, guides and fills on separate layers when they have different editing or animation needs.

Inspect frame/stroke/point counts and material indices, then review the drawing from the delivery camera and at edit-friendly views. Save and reopen to prove the strokes remain editable. The current interface creates stroke frames and materials; advanced modifiers and hand-drawn brush dynamics require a later explicit capability or manual takeover.

## 什么时候使用（When to Use）

需要可编辑的 Grease Pencil 图层、分镜线稿、注释、逐帧绘制或 2D/3D 混合元素时使用。

## 输入与前置条件（Prerequisites）

- 明确坐标空间、图层、帧号、材质、点序列、半径、透明度和闭合状态。
- 区分线稿、辅助线与填充；确认交付相机和时间线范围。

## 执行流程（Workflow）

Step 1. 创建命名对象、图层与材质，并固定对象变换。
Step 2. 按帧写入结构化 stroke 和点，不把屏幕坐标冒充局部 3D 坐标。
Step 3. 检查材质索引、点序和闭合状态，再从编辑视图修正几何。
Step 4. 从交付相机审阅遮挡与线宽，保存重开验证可编辑性。

## 验证与交付证据（Validation）

报告图层、帧、stroke、点和材质索引计数，提供交付相机预览以及保存重开后的同项检查。

## Rules 与能力边界（不适用场景）

不声称支持高级 modifier、手绘笔刷动力学或完整传统动画工具链；缺少能力时交由人工接管。

## Gotchas（常见问题与恢复）

- 笔画不可见：检查帧号、图层可见性、材质和相机裁剪。
- 线条跳跃：复核点顺序与坐标空间。
- 重开丢失：停止交付并保留原始 stroke 数据用于重建。
