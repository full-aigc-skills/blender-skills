---
name: blender-cinematography
description: Design and validate Blender cameras, lenses, subject aiming, path motion, focus, framing, and controlled handheld response.
---

# Blender cinematography

Use for camera creation, lens choice, composition, path following, focus and handheld motion. Obtain the subject list, intended shot size, frame range and movement beats before changing the camera.

Create or select one delivery camera, aim it at an explicit point or object, then add path and handheld behavior only when required. Handheld noise must remain parameterized and visually subordinate to readable subject motion.

Run `validation.camera_visibility` over the specified frames and inspect camera plus orthographic previews. Report missed objects and frame ranges rather than claiming that a constraint or keyframe guarantees good composition. Camera work does not authorize rendering, export or downstream generation.

## 什么时候使用（When to Use）

任务涉及镜头创建、焦段、构图、运镜、景深、跟焦或可控手持效果时使用。只需审阅截图时使用 `blender-preview`。

## 输入与前置条件（Prerequisites）

- 明确主体、镜头尺寸、画幅、分辨率、帧率、区间和运动节拍。
- 指定不可遮挡对象、允许裁切范围、焦点对象和相机移动限制。

## 执行流程（Workflow）

Step 1. 检查现有相机、主体包围盒和时间线，选定唯一交付相机。
Step 2. 先确定焦段、位置和瞄准点，再配置路径、景深和手持参数。
Step 3. 在关键帧和区间采样点检查可见性、屏幕占比、地平线与运动连续性。
Step 4. 捕获相机与正交视图，记录失败帧和调整理由。

## 验证与交付证据（Validation）

提供相机名、焦段、画幅、关键帧、约束、焦点距离，以及 `validation.camera_visibility` 的对象和失败帧；视觉验收覆盖首中末及运动极值帧。

## Rules 与能力边界（不适用场景）

不授权渲染、导出或外部生成。可见性检查不能证明审美构图，约束成功也不能证明镜头没有遮挡或晕动风险。

## Gotchas（常见问题与恢复）

- 主体出框：定位失败帧后调整路径或焦段。
- 路径翻转：检查 forward/up 轴和曲线方向。
- 景深漂移：核对焦点对象、单位比例和无意动画通道。
