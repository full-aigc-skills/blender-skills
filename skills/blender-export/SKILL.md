---
name: blender-export
description: "Export an approved Blender snapshot to verified model, image, video, EXR, USD, or Alembic artifacts using compatible receipt contracts."
---

# Blender Export

Export only from the approved `sceneRevision + snapshotId` and under an approved output root.
Existing files require action-bound overwrite authorization.

In `auto_with_budget`, `export.file` may write a new file in an allowed format under the
session's approved root, using the current committed snapshot, without another user prompt.
`review_only` rejects export even with a claim. Following user takeover, inspect again and create
a new transaction/snapshot; old approvals must not be reused.

Call `export.file`; verify existence, non-zero size, SHA-256, format, and receipt schema. Model
formats require isolated re-import validation; images and MP4 require media probing. Distinguish
local export success from any downstream rendering system.

Use `export.extended` for EXR, USD/USDC and Alembic and preserve its receiptVersion 2.0.0 instead
of rewriting it as the legacy receipt. For a long EXPORT or RENDER_STILL, use
`blender-background-jobs`; `export.file` itself remains synchronous. Do not promise that
pause interrupts an already-running synchronous export.

## 什么时候使用（When to Use）

批准的 Blender 快照需要生成模型、图片、视频、EXR、USD 或 Alembic 本地产物时使用。场景仍在修改或仅需预览时不要导出。

## 输入与前置条件（Prerequisites）

- 精确的 `sceneRevision + snapshotId`、格式、文件名、输出根目录和覆盖授权。
- 确认格式能力、依赖打包策略、坐标/单位要求及下游兼容目标。

## 执行流程（Workflow）

Step 1. 检查快照仍是批准版本，解析并校验规范化输出路径。
Step 2. 按格式选择同步导出、扩展导出或后台作业，禁止静默降级格式。
Step 3. 写入临时目标后完成格式校验，再原子交付到最终路径。
Step 4. 对模型隔离重导入，对媒体做探测，对 `.blend` 做独立目录重开。
Step 5. 生成含 SHA-256、大小、格式、快照和验证结果的收据。

## 验证与交付证据（Validation）

至少证明文件存在且非空、哈希、格式签名和对应重开/重导入/媒体探测通过。扩展格式保留 receiptVersion 2.0.0。

## Rules 与能力边界（不适用场景）

本地导出不等于发布或下游平台兼容；不覆盖未授权文件，不复用接管前批准，不声称同步导出可被暂停。

## Gotchas（常见问题与恢复）

- 文件已存在：停止并请求该动作的覆盖授权。
- 重导入失败：保留源快照和日志，不能仅凭文件非空判定成功。
- 依赖丢失：检查打包与相对路径，重新验证独立目录打开。
