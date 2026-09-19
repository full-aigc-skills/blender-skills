---
name: blender-quality-validation
description: Measure Blender geometry, character, prop, collision, motion, and camera acceptance criteria against explicit objects, frames, proxies, and tolerances.
---

# Blender quality validation

Use only explicit targets and intent supplied by the task: objects, armature bones, frame intervals, contact points, collision proxies and numeric limits. Do not infer every performance intention from scene geometry.

Run the relevant `validation.*` checks and return the measured value, affected object or bone, frame range, limit and pass/fail result. Character work commonly combines limb length, planted-foot drift, prop handoff and floor penetration; camera work adds visibility and motion-discontinuity checks.

Technical thresholds are necessary but do not replace visual review. After numeric checks, inspect silhouette, balance, contact readability and composition. If a check lacks a required proxy or frame interval, identify that exact missing input; do not silently broaden the target set.

## 什么时候使用（When to Use）

任务给出几何、角色、道具、碰撞、运动或相机的可测验收标准，需要形成通过/失败证据时使用。

## 输入与前置条件（Prerequisites）

- 显式目标对象、骨骼、帧区间、接触点、代理体、单位和容差。
- 验收标准必须来自任务或批准 brief；缺少意图时不得自行推导阈值。

## 执行流程（Workflow）

Step 1. 将每条标准映射到具体 `validation.*` 检查及输入。
Step 2. 固定场景修订和帧区间，运行检查并保存原始测量值。
Step 3. 对失败项定位对象、骨骼和帧，不扩大目标集合。
Step 4. 数值检查后补充轮廓、平衡、接触和构图的视觉审阅。
Step 5. 输出逐项 PASS、FAIL 或 UNVERIFIED，并说明缺失输入。

## 验证与交付证据（Validation）

每项包含检查名、目标、修订、帧区间、测量值、单位、阈值、容差、状态和预览引用。

## Rules 与能力边界（不适用场景）

技术阈值不能替代审美接受；无代理体或帧区间时必须标记 UNVERIFIED，不得默认通过。

## Gotchas（常见问题与恢复）

- 单位错误：回到场景单位和对象 scale 后重测。
- 目标不存在：停止该项并报告准确名称。
- 边界帧漏检：扩充明确采样点，但不得超出批准帧区间。
