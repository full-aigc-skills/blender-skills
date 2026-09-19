---
name: blender-inspect
description: "Inspect an active Blender scene read-only before Codex designs, modifies, previews, or exports it."
---

# Blender Scene Inspection

Send `scene.inspect` to the active Harness session. Report object names and types, collections,
active camera, frame range, materials, lights, missing assets, warnings, and `sceneRevision`.

Do not use mutating operators during inspection. If Blender changed outside Codex, re-inspect
instead of guessing and use the new revision for subsequent commands.

## 什么时候使用（When to Use）

任何设计、修改、预览、恢复或导出开始前，以及检测到外部修改、修订冲突或未知场景状态时使用。

## 输入与前置条件（Prerequisites）

- 可发现且已授权的 Harness 会话；检查行为必须只读。
- 明确本次关注范围，例如对象、集合、相机、材质、帧范围或缺失素材。

## 执行流程（Workflow）

Step 1. 读取会话状态和当前 `sceneRevision`。
Step 2. 调用 `scene.inspect`，收集对象、集合、相机、材质、灯光、时间线和警告。
Step 3. 对任务相关对象做聚焦检查，不执行任何修复或选择变更。
Step 4. 输出事实、未知项和建议的下一领域技能，并绑定本次修订号。

## 验证与交付证据（Validation）

保留检查时间、会话 ID、场景修订、对象统计、活动相机、帧区间、缺失素材和警告。后续命令必须引用同一或更新后的修订号。

## Rules 与能力边界（不适用场景）

检查不修改场景、不推断隐藏意图，也不把对象存在等同于质量通过。发现问题只报告，除非用户另行授权修复。

## Gotchas（常见问题与恢复）

- 修订号变化：丢弃旧假设并重新检查。
- 会话不可达：转到 `blender-mcp-setup`，不得伪造清单。
- 输出过大：按任务对象聚焦，但保留全局警告和修订证据。
