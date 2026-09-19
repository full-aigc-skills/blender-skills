---
name: blender-tracking
description: Load approved footage, create normalized Blender tracking markers, solve a foreground camera, set up the scene, and validate reprojection error.
---

# Blender motion tracking

Load clips only from approved asset roots. Add named tracks with normalized coordinates and explicit frames. Confirm enough common tracks and meaningful parallax before solving.

Camera solve and scene setup require a foreground CLIP_EDITOR. Accept a solve only after inspecting bundle count and measured reprojection error against the task threshold; operator success alone is insufficient.

Preserve the original footage path and solved `.blend` receipt. Tracking does not imply masking or editing; combine with render-compositing or sequence-editing only when the task requests those outcomes.

## 什么时候使用（When to Use）

批准的实拍素材需要创建跟踪点、求解相机、建立场景并以重投影误差验收时使用。

## 输入与前置条件（Prerequisites）

- 本地批准素材、镜头信息、帧范围、marker 名称/坐标和误差阈值。
- 确认有足够共同 tracks、视差与前台 CLIP_EDITOR。

## 执行流程（Workflow）

Step 1. 从批准根目录加载 clip，记录原始路径和媒体属性。
Step 2. 以归一化坐标和明确帧添加命名 tracks，检查持续可见性。
Step 3. 在 CLIP_EDITOR 前台执行相机求解和场景设置。
Step 4. 检查 bundle 数、覆盖区间、重投影误差和异常 tracks。
Step 5. 保存 solved `.blend`，重开并复核相机与素材绑定。

## 验证与交付证据（Validation）

提供素材哈希、tracks/bundles 数、帧覆盖、平均/最大重投影误差、阈值、相机参数和重开收据。

## Rules 与能力边界（不适用场景）

operator 成功不等于求解合格；跟踪不包含 masking、剪辑或合成，缺少视差时不得伪造稳定求解。

## Gotchas（常见问题与恢复）

- 误差过高：剔除异常 track、确认镜头参数后重新求解。
- 求解不稳定：检查共同 track 数和视差，必要时标记无法验证。
- 素材路径丢失：保留 provenance，等待重新授权路径。
