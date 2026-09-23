# 清上河图微缩场景 — blender-harness JSON 命令序列

> 教程里"豆包 10-15 分钟跑完的首版粗模"对应的 blender-harness 命令流。
> 全程在一个事务里完成（建模→材质→截图）→ 提交 → 起灯/相机 → 渲两张图 → 导 glb。
> 不含 dream-loop 迭代；迭代层交给 [[dream_loop.py]] 即可叠加。

## 0. 前置

```bash
python3 ~/.zcode/cli/plugins/cache/full-aigc-plugins/blender-design/0.14.1/scripts/launch_harness.py \
    --session-id "qingming-v1" \
    --output-root "/Users/wandl/partme/blender/design-outputs" \
    --execution-mode "auto_with_budget" \
    --export-format "glb"
#   ↑ 拿 descriptor（socket + json path）
```

把所有 harness_cli.py 调用都加 `--descriptor <descriptor>` `--request <req.json>`。
以下每步展示一个完整 JSON envelope。

---

## 1. 探测（读命令，tx_id="READ" 占位即可）

### 1.1 列出 mesh 域能力（验连接）

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-probe-mesh-1",
  "transactionId": "READ",
  "command": "capability.list",
  "arguments": {"domain": "mesh", "limit": 5}
}
```

### 1.2 当前场景盘点（拿到起始 sceneRevision）

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-inspect-1",
  "transactionId": "READ",
  "command": "scene.inspect",
  "arguments": {}
}
```

> 期望：拿到 `sceneRevision: 1`（默认 Blender 启动场含 Camera/Light/Cube 三件套，加载后常为 1）。
> 用这个 rev 喂给后续 modify 命令的 `expectedSceneRevision`。

---

## 2. 建模事务（一个事务包住步骤 3 ~ 7）

### 2.1 开事务

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-tx-begin-1",
  "transactionId": "tx-qm-build-001",
  "command": "transaction.begin",
  "arguments": {}
}
```

> 响应里记下 `result.transactionId` 和 `result.snapshotId`。
> 后续 modify 命令必须带**同一个** `transactionId`，并把每次响应里的 `sceneRevision` 续上去。

---

### 2.2 沙盘底座（plane）

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-mesh-base-1",
  "transactionId": "tx-qm-build-001",
  "expectedSceneRevision": 1,
  "command": "object.create_mesh",
  "arguments": {
    "name": "Sand_Base",
    "primitive": "PLANE",
    "location": [0, 0, 0],
    "scale": [30, 20, 1],
    "rotation": [0, 0, 0]
  }
}
```

> 教程里首版的微缩沙盘底座。先放一个 30×20 的平面，z=0 当作地面。

---

### 2.3 河道（半透明水面）

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-mesh-river-1",
  "transactionId": "tx-qm-build-001",
  "expectedSceneRevision": 2,
  "command": "object.create_mesh",
  "arguments": {
    "name": "River_Water",
    "primitive": "PLANE",
    "location": [0, 6, 0.05],
    "scale": [30, 4, 1],
    "rotation": [0, 0, 0]
  }
}
```

> 平面略浮于地面 0.05，避免 z-fighting。后续迭代里河面用 wave modifier + 透明材质。

---

### 2.4 虹桥（用 box 拼接成桥面 + 拱）

教程里作者要求"参考北宋贯木拱：无河中桥墩、桥面中隆、两侧栏杆"。首版用 3 个 box 拼：

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-mesh-bridge-deck-1",
  "transactionId": "tx-qm-build-001",
  "expectedSceneRevision": 3,
  "command": "object.create_mesh",
  "arguments": {
    "name": "Bridge_Deck",
    "primitive": "CUBE",
    "location": [0, 6, 1.0],
    "scale": [5, 2, 0.2]
  }
}
```

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-mesh-bridge-arch-L-1",
  "transactionId": "tx-qm-build-001",
  "expectedSceneRevision": 4,
  "command": "object.create_mesh",
  "arguments": {
    "name": "Bridge_Arch_Left",
    "primitive": "CUBE",
    "location": [-2.3, 6, 0.5],
    "scale": [0.4, 2, 1.0],
    "rotation": [0, 0, 0.3]
  }
}
```

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-mesh-bridge-arch-R-1",
  "transactionId": "tx-qm-build-001",
  "expectedSceneRevision": 5,
  "command": "object.create_mesh",
  "arguments": {
    "name": "Bridge_Arch_Right",
    "primitive": "CUBE",
    "location": [2.3, 6, 0.5],
    "scale": [0.4, 2, 1.0],
    "rotation": [0, 0, -0.3]
  }
}
```

> 首版三件套：桥面 + 左右拱。后续 dream-loop 会拆出斗拱、榫卯栏杆。

---

### 2.5 沿街建筑（5 个简化双层小楼，沿河 y=4 排列）

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-mesh-bldg-1",
  "transactionId": "tx-qm-build-001",
  "expectedSceneRevision": 6,
  "command": "object.create_mesh",
  "arguments": {
    "name": "Building_Shop_1",
    "primitive": "CUBE",
    "location": [-10, 4, 0.8],
    "scale": [1.5, 1.2, 1.6]
  }
}
```

> 重复 4 次，把 `name` / `location` 改成 `Building_Shop_2..5`、x 间距 5。
> 每个 build 把 `expectedSceneRevision` 续上去（这里 +1）。

### 2.6 民居院落（小尺度 box）

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-mesh-house-1",
  "transactionId": "tx-qm-build-001",
  "expectedSceneRevision": 11,
  "command": "object.create_mesh",
  "arguments": {
    "name": "House_1",
    "primitive": "CUBE",
    "location": [-8, -4, 0.6],
    "scale": [1.2, 1.0, 1.2]
  }
}
```

> 重复 3 次，y=-4 排列。

---

### 2.7 材质（PBR — 米白墙 + 灰蓝瓦 + 暖木色）

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-mat-wall-1",
  "transactionId": "tx-qm-build-001",
  "expectedSceneRevision": 14,
  "command": "material.create_pbr",
  "arguments": {
    "name": "Mat_Wall_Cream",
    "baseColor": [0.92, 0.88, 0.78, 1.0],
    "roughness": 0.85,
    "metallic": 0.0
  }
}
```

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-mat-roof-1",
  "transactionId": "tx-qm-build-001",
  "expectedSceneRevision": 15,
  "command": "material.create_pbr",
  "arguments": {
    "name": "Mat_Roof_Slate",
    "baseColor": [0.32, 0.36, 0.42, 1.0],
    "roughness": 0.55,
    "metallic": 0.05
  }
}
```

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-mat-water-1",
  "transactionId": "tx-qm-build-001",
  "expectedSceneRevision": 16,
  "command": "material.create_pbr",
  "arguments": {
    "name": "Mat_Water",
    "baseColor": [0.45, 0.55, 0.62, 0.85],
    "roughness": 0.15,
    "metallic": 0.0,
    "alpha": 0.85
  }
}
```

### 2.8 把材质绑给对象

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-mat-assign-wall-1",
  "transactionId": "tx-qm-build-001",
  "expectedSceneRevision": 17,
  "command": "material.assign",
  "arguments": {
    "material": "Mat_Wall_Cream",
    "object": "Building_Shop_1"
  }
}
```

> 重复：把 Roof 给所有 `Building_*` + `House_*`，Water 给 `River_Water`，Sand_Base 给沙盘底座。

---

### 2.9 事务内截图（教程里"豆包每轮反馈给视窗的截图"）

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-shot-mid-1",
  "transactionId": "tx-qm-build-001",
  "expectedSceneRevision": 25,
  "command": "scene.screenshot",
  "arguments": {
    "path": "/Users/wandl/partme/blender/design-outputs/qingming/round-00.png",
    "width": 1280,
    "height": 720,
    "format": "PNG"
  }
}
```

> ⚠️ 必须落 `output-root` 内，否则 `OUTPUT_NOT_AUTHORIZED`。

---

### 2.10 提交事务（拿到 approved snapshotId）

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-tx-commit-1",
  "transactionId": "tx-qm-build-001",
  "expectedSceneRevision": 25,
  "command": "transaction.commit",
  "arguments": {}
}
```

> 响应里 `result.snapshotId` 是 approved snapshot。后续 `export.file` 必须**逐字等于**这个值。

---

## 3. 起灯 + 起相机（新事务；读 / 创建都可放在一起）

### 3.1 开新事务

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-tx-begin-2",
  "transactionId": "tx-qm-lighting-001",
  "command": "transaction.begin",
  "arguments": {}
}
```

### 3.2 太阳光（directional）

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-light-sun-1",
  "transactionId": "tx-qm-lighting-001",
  "expectedSceneRevision": 26,
  "command": "light.create",
  "arguments": {
    "name": "Sun",
    "type": "SUN",
    "location": [0, -10, 15],
    "energy": 4.0,
    "color": [1.0, 0.95, 0.85]
  }
}
```

### 3.3 环境光（world background）

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-light-world-1",
  "transactionId": "tx-qm-lighting-001",
  "expectedSceneRevision": 27,
  "command": "light.set_world_color",
  "arguments": {
    "color": [0.65, 0.78, 0.92]
  }
}
```

### 3.4 相机 1 — 全景俯视

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-cam-overall-1",
  "transactionId": "tx-qm-lighting-001",
  "expectedSceneRevision": 28,
  "command": "camera.create",
  "arguments": {
    "name": "Camera_Overall",
    "active": true,
    "lens": 35.0,
    "location": [0, -22, 18],
    "rotation": [1.1, 0, 0]
  }
}
```

### 3.5 相机 2 — 虹桥特写

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-cam-bridge-1",
  "transactionId": "tx-qm-lighting-001",
  "expectedSceneRevision": 29,
  "command": "camera.create",
  "arguments": {
    "name": "Camera_Bridge",
    "lens": 50.0,
    "location": [-6, 6, 1.5],
    "rotation": [1.45, 0.6, 0]
  }
}
```

### 3.6 提交

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-tx-commit-2",
  "transactionId": "tx-qm-lighting-001",
  "expectedSceneRevision": 29,
  "command": "transaction.commit",
  "arguments": {}
}
```

---

## 4. 渲两张图（每张一个独立 job）

> blender-harness 的 `job.submit` 走后台队列，最大并发 2，磁盘保留 `max(20% 卷容量, 20GB)`。

### 4.1 渲全景

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-job-overall-1",
  "transactionId": "READ",
  "command": "job.submit",
  "arguments": {
    "jobId": "render_overall_001",
    "kind": "RENDER_STILL",
    "parameters": {
      "camera": "Camera_Overall",
      "engine": "BLENDER_EEVEE",
      "samples": 64,
      "width": 1920,
      "height": 1080,
      "output_path": "/Users/wandl/partme/blender/design-outputs/qingming/render-overall.png"
    }
  }
}
```

### 4.2 渲虹桥特写

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-job-bridge-1",
  "transactionId": "READ",
  "command": "job.submit",
  "arguments": {
    "jobId": "render_bridge_001",
    "kind": "RENDER_STILL",
    "parameters": {
      "camera": "Camera_Bridge",
      "engine": "BLENDER_EEVEE",
      "samples": 96,
      "width": 1920,
      "height": 1080,
      "output_path": "/Users/wandl/partme/blender/design-outputs/qingming/render-bridge.png"
    }
  }
}
```

### 4.3 轮询状态

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-job-poll-1",
  "transactionId": "READ",
  "command": "job.status",
  "arguments": {"jobId": "render_overall_001"}
}
```

> `state ∈ pending | running | succeeded | failed`。`succeeded` 后 `result.output_path` 是真实产物。
> 失败 → `result.error` + `result.error_category`。常见：路径不在 output-root / 显存不足 / 工程有循环引用。

---

## 5. 导 glb（独立事务，必须用 commit 的 snapshotId）

### 5.1 拿一次新 snapshot（确保导出版本与最后提交一致）

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-tx-begin-3",
  "transactionId": "tx-qm-export-001",
  "command": "transaction.begin",
  "arguments": {}
}
```

> 注意：begin 会返回 snapshot。`commit` 也会返回同一个 snapshot（实测）。
> 整个事务不修改任何东西，纯为了让 export.file 拿到 approved snapshot。

### 5.2 commit（保持导出快照）

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-tx-commit-3",
  "transactionId": "tx-qm-export-001",
  "command": "transaction.commit",
  "arguments": {}
}
```

### 5.3 export.file

```json
{
  "protocolVersion": "codex-blender/v1",
  "sessionId": "qingming-v1",
  "requestId": "req-export-glb-1",
  "transactionId": "EXPORT",
  "command": "export.file",
  "arguments": {
    "path": "/Users/wandl/partme/blender/design-outputs/qingming/qm-v1.glb",
    "snapshotId": "<从 5.2 拿到的 snapshotId 逐字填入>"
  }
}
```

> ⚠️ export.file 不接 `format` 参数 —— session 启动时已定。**实测拒收 `format`**。
> ⚠️ snapshotId 必须 = 5.2 commit 的 snapshotId 字符串，**逐字不一致 → MILESTONE_NOT_APPROVED**。

响应里 `result.artifact.sha256` 是产物哈希。`validation.status: passed` 是产物媒体探测（exists / non_empty / sha256）通过。

---

## 6. 端到端检查表

跑完一遍后核对：

| 检查项 | 期望 |
|---|---|
| `scene.inspect` 对象数 ≥ 12 | Sand_Base + River_Water + Bridge_Deck + 2 Arch + 5 Shop + 4 House + 2 Camera + 1 Light = 17 |
| `render-overall.png` 文件存在 + 体积 > 100KB | RENDER_STILL 输出 |
| `render-bridge.png` 文件存在 + 体积 > 100KB | RENDER_STILL 输出 |
| `qm-v1.glb` 文件存在 + `file` 报 "glTF binary model" | export 产物 |
| `result.artifact.sha256` 与本地 `shasum -a 256 qm-v1.glb` 一致 | 防 producer 谎报 |

---

## 7. 跟教程的对应

| 教程章节 | 这一序列的步骤 |
|---|---|
| 二·建模「初版 10-15 分钟跑完」 | 步骤 2 全部（沙盘 + 河 + 桥 + 5 沿街 + 4 民居 + 3 材质） |
| 二·建模「每轮反馈调整截图」 | 步骤 2.9 mid-tx screenshot（教程要 commit 后才看，这里演示了事务内也可） |
| 四·交互「沿街商铺/双层酒楼/民居/虹桥」 | 步骤 2.5 + 2.6 + 2.4（首版简化） |
| 四·交互「开启漫游模式」 | 步骤 3.5 桥头相机 + 后续 character.rigging（**不在本序列**） |
| — 渲两张图 | 步骤 4 |
| — 导 glb | 步骤 5 |

dream-loop 迭代闭环见 [[dream_loop.py]]；用它把这个序列包起来即可得到教程里"2 小时跑 4-5 轮"的效果。

---

## 8. 已知陷阱（实测）

| 陷阱 | 表现 | 解法 |
|---|---|---|
| auto_setup 的 pgrep `-f Blender` 误判 MCP server 为 GUI Blender | "Blender 正在运行" 但 ps 看不到 | 绕走 `launch_harness.py` + `harness_cli.py` 直接路径 |
| `transactionId` 用 placeholder `"READ"` 跑 modify | `TRANSACTION_NOT_FOUND` | modify 必须用 begin 返回的 tx_id |
| `expectedSceneRevision` 漏掉或错位 | `STALE_SCENE_REVISION` (retryable) | 每次响应里续 `sceneRevision` 续上去 |
| `export.file` 带 `format` 字段 | `INVALID_ARGUMENT: unknown argument fields: ['format']` | format 在 session 启动时定，不要带 |
| 截图/export 路径不在 output-root | `OUTPUT_NOT_AUTHORIZED` | 落 `--output-root` 下面 |
| screenshot 没 sceneRevision 字段 | export 报"differs from scene rev" | screenshot 走的是 modify 协议，需带 expectedSceneRevision |

---

## 9. 关于材质的进一步迭代（预告）

教程里说"豆包会自主生成纹理，不再用代码直接画屋顶"。blender-harness 的 `material.create_pbr` + `material.connect_image_texture` + `material.bake` 三件套支持：
- 程序化基础色（这一步）
- 加载外部纹理 PNG（用 `connect_image_texture`）
- 烘焙复杂材质到 UV（用 `bake`）

后续轮迭代（dream-loop）可以专门替换 `Mat_Roof_Slate` 为程序生成纹理 + wave modifier 让屋顶瓦片颜色/疏密变化。命令序列太长不在此展开。