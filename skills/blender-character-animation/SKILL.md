---
name: blender-character-animation
description: Animate a registered Blender character rig and a single interactive prop with editable timing, IK controls, constraints, and continuity checks.
---

# Character and prop animation

Work from named action beats and frame intervals. Pose controls or bones, key only intended channels, and retain editable constraints. For grip/release/catch, use one prop object: keep grip influence at one before release, zero through a visible free-flight interval, and restore it only after the prop reaches the catch pose.

Inspect the release distance and duration, catch position/rotation discontinuity, planted foot drift, limb-length preservation and floor proxies. A passing numeric check is necessary but not sufficient: also review silhouette, balance, contact readability and camera composition.

Use `blender-quality-validation` for measurements and `blender-cinematography` when
the task includes camera paths, focus or handheld behavior. Keep those acceptance decisions
separate from pose authoring.

When timing changes, move the release/apex/catch parameters or keyframes without rebuilding unrelated animation. Do not add skin detail, effects, sound or downstream rendering to a white-model task unless separately requested and supported.

## 什么时候使用（When to Use）

为已登记角色骨架制作姿态、动作节拍、IK/FK 控制或单个道具交互时使用。缺少可验证骨架或权重时先交给 `blender-character-rigging`。

## 输入与前置条件（Prerequisites）

- 明确 Action、帧率、帧区间、动作节拍、接触点和交付相机。
- 指定可动画控制器、道具约束及允许修改的通道，并保存初始姿态。

## 执行流程（Workflow）

Step 1. 把动作拆成准备、主要动作、缓冲与结束姿态并分配帧区间。
Step 2. 先建立重心、脚底接触和轮廓，再处理手臂、视线与次级动作。
Step 3. 仅给目标通道插帧；抓取、释放和接住使用同一道具及约束影响值。
Step 4. 检查关键姿态与完整播放，在不重建无关动画的前提下调整节拍。

## 验证与交付证据（Validation）

提交关键帧、约束曲线、脚底漂移、肢体长度、道具交接连续性及首中末预览。数值通过后仍需检查轮廓、平衡与接触可读性。

## Rules 与能力边界（不适用场景）

不创建新骨架，不承担权重修复、毛发布料模拟、声音或最终渲染；没有表演意图时不自行添加复杂次级动作。

## Gotchas（常见问题与恢复）

- IK 翻转：检查 pole、链长和旋转轴，不用多余关键帧掩盖。
- 脚底滑动：锁定接触区间并复测世界坐标。
- 道具跳变：比较切换前后世界矩阵并修正约束反矩阵。
