---
name: blender-design
description: "Turn a user's idea into a Blender scene through milestone-based modeling, materials, lighting, camera, and animation commands."
---

# Blender Design Workflow

Inspect, then create an implementation brief before mutation: requested assets, supplied
references, missing references, scene constraints, camera route, animation beats, duration, and
required exports. If a required reference is missing, ask the user for it by default. Create a
Blender-designed proxy only when the user explicitly requests design of the missing asset, and
record its assumptions and deviations in the delivery receipt.

For an `auto_with_budget` request, execute the approved brief through every safe milestone
without asking after each preview. Capture the same previews and validation evidence, but present
them together with the final artifact inventory. Stop only for a forbidden missing asset, path
escape, deletion/overwrite, expert Python or failed validation requiring recovery. Remote budget
enforcement is owned by the downstream plugin.

Translate the approved brief into named components, then complete Scene Structure, Modeling,
Materials, Lighting and Camera, Animation, and Final Preview milestones. Use one transaction per
milestone and `expectedSceneRevision` on every mutation.

Delegate each milestone to the precise domain Skill advertised by `capability.describe`; do not
keep advanced animation, cinematography, quality validation, background jobs, or simulation under
this general workflow. Multi-domain recipes may load multiple Skills declared by the capability.

Prefer registered commands over expert Python. Read `session.status` and show the actual scene
in the foreground before work. Update `session.set_progress` with an honest stage and optional
progress fraction; report actual objects changed, not a synthetic completion percentage.
After each milestone generate fresh previews. In interactive mode wait for approval; in automatic
mode assess the previews against the approved brief, then commit without another prompt.
On failure recover the transaction only if the user has not taken over. Command success alone is not
design acceptance. Before final export, verify all brief constraints that are observable in the
scene and preview: object count and uniqueness, animation beat order, frame range, camera route,
and required deliverable formats. Return the artifact inventory and explicitly ask whether the
user wants to finish locally or hand off only when that choice was not already made.
Downstream AI rendering is outside this Skill.

For foreground control and recovery, hand off to the **`blender-use`** skill when the plugin provides
it. Install: `npx skills add full-aigc-skills/blender-skills --skill blender-use`. If that optional
skill is not published in the current package, follow the session boundary below without inventing
a local file dependency. On `SESSION_PAUSED`, stop design commands. Only a user resume permits
continuation; then inspect again and begin a new transaction. Never roll back the pre-takeover
transaction over user edits.

## 什么时候使用（When to Use）

用户给出多阶段 Blender 成品目标，需要协调建模、材质、灯光、镜头、动画和交付时使用。单一领域任务应直接触发对应技能。

## 输入与前置条件（Prerequisites）

- 记录目标、参考素材、禁止项、场景限制、镜头路线、动作节拍和交付格式。
- 缺少关键素材或验收标准时先澄清；确认自动模式、预算和输出根目录。

## 执行流程（Workflow）

Step 1. 只读检查场景和能力，形成可验收实施 brief。
Step 2. 依次执行场景结构、建模、材质、灯光镜头、动画和最终预览里程碑。
Step 3. 每个里程碑单独事务化，使用预期修订号并交给精确领域技能。
Step 4. 生成新预览和测量证据；交互模式等待确认，自动模式按批准 brief 自检。
Step 5. 导出前复核全部可观察约束，返回真实产物清单与未完成项。

## 验证与交付证据（Validation）

绑定每个里程碑的事务、场景修订、快照、对象变化、预览哈希和领域验收结果。命令成功不能替代设计接受。

## Rules 与能力边界（不适用场景）

本技能只负责编排，不吞并高级动画、模拟、后台作业或外部 AI 渲染能力；不自行下载素材、发布或支付。

## Gotchas（常见问题与恢复）

- 用户接管：立即暂停，恢复后重新检查并开启新事务。
- 修订冲突：停止写入，读取最新场景，不覆盖用户变更。
- 验收失败：回到对应里程碑和领域技能，不用最终预览掩盖缺陷。
