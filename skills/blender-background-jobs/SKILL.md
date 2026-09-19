---
name: blender-background-jobs
description: Run snapshot-isolated Blender exports, durable animation frame sequences, explicit frame recovery, verified video composition, still renders, and simulation baking without blocking the foreground scene.
---

# Blender background jobs

Use for `job.*` when an approved output root exists. A submission saves a versioned source snapshot first; the child Blender process may write only inside its job directory. The foreground may continue editing, but the job remains bound to the submitted snapshot.

Route by `kind`: EXPORT and RENDER_STILL also use `blender-render-compositing`; BAKE_POINT_CACHES also uses `blender-simulation`. Use RENDER_ANIMATION_FRAMES for a persistent PNG or multilayer EXR sequence. Use COMPOSE_VIDEO only after its source FrameSequenceReceipt has complete frame hashes; it produces a separate H.264 receipt without rerendering Blender.

Query status until a terminal receipt and keep the job ID, snapshot hash, manifest hash, and artifact receipt together. Cancellation terminates only the child task. `job.recover` may mark a lost task `interrupted` but never restarts it. Resume only after an explicit `job.resume`; verified frames remain untouched while missing or hash-invalid frames are replaced. A background receipt does not approve external upload, publishing, payment, or Video Factory orchestration.

## 什么时候使用（When to Use）

渲染、导出或缓存烘焙会阻塞前台，或者任务要求断点恢复和逐帧校验时使用。快速且必须立即观察结果的操作继续走对应前台技能。

## 输入与前置条件（Prerequisites）

- 已提交的 `sceneRevision + snapshotId`、批准的输出根目录和不可覆盖约束。
- 明确任务类型、帧范围、格式、超时和磁盘预算，并确认子进程可读取依赖素材。

## 执行流程（Workflow）

Step 1. 按产物选择作业类型并保存不可变快照。
Step 2. 提交作业，记录 job ID、快照哈希、清单哈希和输出目录。
Step 3. 轮询至终态；中断后先恢复检查，只有显式 `job.resume` 才继续。
Step 4. 仅替换缺失或哈希错误的帧，最后生成终态收据与产物清单。

## 验证与交付证据（Validation）

核对终态、退出码、快照哈希、帧区间、逐帧哈希、文件大小和媒体探测结果。视频合成还需证明输入序列完整以及时长、帧率、尺寸符合约定。

## Rules 与能力边界（不适用场景）

后台成功不等于画面质量已接受，也不授权上传、发布或付费服务。作业不得写出批准目录，不自动重启未知状态任务。

## Gotchas（常见问题与恢复）

- 子进程消失：标记 `interrupted`，保留日志与已验证帧。
- 单帧损坏：按哈希定位并只重做该帧。
- 磁盘不足或路径越界：立即停止并报告实际路径与空间需求。
