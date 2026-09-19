---
name: blender-preview
description: "Capture fresh camera, front, side, and top Blender previews for milestone review or visual diagnosis."
---

# Blender Milestone Preview

Call `preview.capture` for the current revision and snapshot. Require camera/front/side/top PNGs;
animation also needs first/middle/last frames. Verify file existence and SHA-256 before display.

Never reuse images from an older revision. Describe visible strengths and defects, and bind user
approval to the exact `sceneRevision + snapshotId`.

## 什么时候使用（When to Use）

每个建模、材质、灯光、镜头或动画里程碑需要视觉审阅，或需要定位构图与几何缺陷时使用。

## 输入与前置条件（Prerequisites）

- 当前 `sceneRevision + snapshotId`、交付相机和批准的预览输出目录。
- 明确所需视角、分辨率、帧号和审阅重点；动画至少包含首中末帧。

## 执行流程（Workflow）

Step 1. 核对修订与快照仍是当前状态。
Step 2. 捕获相机、前、侧、顶视图，动画补充关键帧。
Step 3. 校验文件存在、大小和 SHA-256，再按视角展示。
Step 4. 描述可见优点、缺陷和遮挡，将确认绑定到该修订与快照。

## 验证与交付证据（Validation）

提供每张 PNG 的视角、帧号、修订、快照、路径、尺寸和哈希；不得复用旧修订图片。

## Rules 与能力边界（不适用场景）

预览是视觉证据而非最终渲染、几何测量或格式交付；不根据单视角断言所有面均正确。

## Gotchas（常见问题与恢复）

- 图片为空或全黑：检查相机裁剪、灯光和对象可见性后重捕获。
- 修订已变化：废弃旧图并生成新预览。
- 视角遮挡：补充局部或正交视图，不用文字猜测隐藏结构。
