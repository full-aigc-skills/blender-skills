---
name: blender-simulation
description: Configure and validate Blender rigid-body, collision, cloth, soft-body, smoke, point-cache, and fluid-cache workflows.
---

# Blender simulation

Declare active/passive roles, collision shapes, physical parameters, frame range and approved cache location. Verify object scale and collision proxies before simulation.

Use `blender-background-jobs` with `BAKE_POINT_CACHES` for expensive baking. Query the terminal receipt, reopen the baked project, and check physical measurements plus visual behavior. Cache paths must stay inside the job directory.

Free or invalidate caches before parameter changes. Never auto-retry an interrupted bake, and do not require cross-device byte identity. Low-resolution fixtures prove the workflow, not film-quality fluid or cloth.

## 什么时候使用（When to Use）

配置刚体、碰撞、布料、软体、烟雾、点缓存或流体缓存，并需要可恢复烘焙时使用。

## 输入与前置条件（Prerequisites）

- 明确 active/passive 角色、碰撞形状、物理参数、帧范围、单位、代理体和批准缓存目录。
- 烘焙前应用或记录对象 scale，并确认缓存空间预算。

## 执行流程（Workflow）

Step 1. 检查对象角色、变换、碰撞代理与依赖顺序。
Step 2. 用低分辨率短区间验证参数和方向。
Step 3. 对昂贵烘焙提交 `BAKE_POINT_CACHES` 后台作业并轮询终态。
Step 4. 参数变化前释放或失效旧缓存，禁止混用旧结果。
Step 5. 重开烘焙工程，完成物理测量和视觉审阅。

## 验证与交付证据（Validation）

报告模拟类型、对象角色、参数、帧范围、缓存路径、作业收据、碰撞/穿透测量和首中末预览。

## Rules 与能力边界（不适用场景）

不自动重试中断烘焙，不要求跨设备字节一致；低分辨率 fixture 只证明流程，不代表电影级结果。

## Gotchas（常见问题与恢复）

- 穿透或爆炸：检查 scale、碰撞 margin、步数和初始重叠。
- 缓存陈旧：明确释放后重烘，不覆盖来源不明缓存。
- 后台中断：保留终态和日志，等待显式 resume。
