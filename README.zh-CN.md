# blender-skills

**Blender AIGC skills** — modeling, rigging, animation, shading, rendering, compositing, sequencing, simulation, tracking, Grease Pencil, and UV/material workflows.

本包包含 **23 个技能**（与 codex-blender-plugin 的内容技能一一对应；插件自持 6 个宿主接入技能）。

## 📦 安装

```bash
npx skills add full-aigc-skills/blender-skills
```

## 🎯 技能列表 (23)

| 技能 | 描述 |
|------|------|
| `blender-background-jobs` | 批量渲染、帧序列导出、显式帧恢复、视频合成、仿真烘培 |
| `blender-character-animation` | 驱动已注册的角色绑定与单个交互道具，含 IK 控制器与连续性校验 |
| `blender-character-rigging` | 构建与检查可编辑的骨架、蒙皮权重、IK、关节限制、道具约束 |
| `blender-cinematography` | 设计与验证摄像机、镜头、主体瞄准、路径运动、焦点、构图 |
| `blender-curves` | 可编辑路径/样条/电缆/导轨/柱面、曲线驱动道具 |
| `blender-design` | 把想法变成 Blender 场景（里程碑式建模、材质、灯光、摄像机、动画） |
| `blender-export` | 把已批准快照导出为 model/image/video/EXR/USD/Alembic，含回执校验 |
| `blender-grease-pencil` | 创建可编辑 Grease Pencil 层、材质、帧绘制，2D/3D 混合场景 |
| `blender-hair` | 创建原生 Blender 毛发曲线（表面局部发束点、半径、绑定源表面） |
| `blender-hard-surface` | 产品/机械/道具硬表面几何、修改器、集合、配方命令 |
| `blender-mcp-setup` | Blender MCP 服务器连接与工具链设置 |
| `blender-preview` | 捕获当前摄像机/正面/侧面/顶视预览供里程碑审查 |
| `blender-procedural-modeling` | 可复用 Geometry Nodes 系统与参数化环境 |
| `blender-quality-validation` | 测量几何/角色/道具/碰撞/运动/摄像机验收标准 |
| `blender-render-compositing` | Cycles/Eevee 渲染、通道、合成、烘培、依赖打包 |
| `blender-retopology` | 设置、投影、数据层传递、可编辑重拓扑表面验证 |
| `blender-scene-assembly` | 组织场景、集合、对象标识、变换、可见性、复用资产 |
| `blender-sculpt-surface` | 拓扑绑定遮罩、置换、前景雕刻笔触、体素重网格、多重分辨率 |
| `blender-sequence-editing` | 在 VSE 中组装时间线：图像/场景/影片/文本/声音、转场、音频淡入淡出 |
| `blender-simulation` | 刚体/碰撞/布料/软体/烟雾/点缓存/流体缓存工作流 |
| `blender-tracking` | 加载镜头、创建追踪标记、求解前景摄像机、设置场景、验证重投影误差 |
| `blender-uv-material` | 为可编辑资产准备 UV 与 PBR 材质，含纹理色彩空间与法线贴图语义 |

## 🤖 支持的智能体

Claude Code / Codex / Cursor / OpenCode / Gemini CLI / GitHub Copilot / Windsurf 等。

<!-- FULL_STACK_DOC_START -->
## 项目定位与边界

`blender-skills` 是包含 **23 个可独立安装 Agent Skill** 的源代码仓库，当前清单版本为 `1.0.1`。本仓负责技能的触发说明、工作流、references、examples 与质量门禁；宿主插件的 Hook、MCP、凭据注入和运行时脚本不属于本仓职责。

| 已确认事实 | 值 | 证据 |
|---|---|---|
| 安装包 | `full-aigc-skills/blender-skills` | `.claude-plugin/plugin.json`、仓库远端 |
| 可安装技能 | 23 | `skills/*/SKILL.md` |
| 当前版本 | `1.0.1` | `.claude-plugin/plugin.json` |
| 规格事实源 | OpenSpec | `openspec/config.yaml` |
| 许可证 | Apache-2.0 | `LICENSE` |

### 不负责

- 不替代消费插件中的可执行 Harness、MCP 服务、Hook 或供应商客户端；
- 不把 `SKILL.md` 被复制到目录视为宿主已经发现、触发或成功执行；
- 不自动授权网络调用、付费生成、文件覆盖、上传或发布；
- 不允许消费插件直接修改受 `skills.lock.json` 管理的副本。

## 一眼看懂

```text
用户任务
  │
  ▼
name / description 发现技能
  │
  ▼
读取完整 SKILL.md ──► 按需加载 references / examples / scripts
  │
  ▼
执行领域工作流 ──► 收集验证证据 ──► PASS / FAIL / UNVERIFIED
```

## 已验证的安装与发现

```bash
npx skills add full-aigc-skills/blender-skills
npx skills add full-aigc-skills/blender-skills --skill blender-background-jobs
npx skills list --json
```

固定发布版本时使用 GitHub Release/tag，不要把移动的 `main` 当成不可变版本。安装完成后应核对技能数量、名称、资源文件和目标 Agent 列表；Codex、ZCode、Kimi 的真实插件加载仍需分别验证。

## 包结构与加载规则

```text
blender-skills/
├── .claude-plugin/plugin.json   # 包名、版本与技能清单
├── skills/<name>/SKILL.md       # 触发条件与主工作流
├── skills/<name>/references/    # 按任务加载的领域知识
├── skills/<name>/examples/      # 请求、验收与恢复示例
├── scripts/                     # 仓库级生成和质量门禁（若存在）
├── openspec/                    # 规格与归档变更
└── LICENSE
```

跨技能协作必须使用技能名和安装命令，不得依赖 `../sibling-skill/` 相对链接，因为用户可能只安装一个技能。

## 质量、发布与安全

```bash
python3 scripts/lint_skills.py
```

发布前还必须检查 frontmatter、相对链接、资源完整性、TRACE 阈值、版本清单以及干净环境安装。正式 tag 不得移动；内容变化应发布新版本，并让消费插件通过 tag、peeled SHA 和摘要更新锁文件。

安全边界：不得提交真实密钥、账号、本机绝对路径或私有仓库地址；脚本应默认最小权限，付费、上传、删除和覆盖动作必须保留显式授权门。

## 故障排查

| 现象 | 检查 | 处理 |
|---|---|---|
| 安装后未发现技能 | frontmatter、Agent 发现目录、是否需要刷新 | 用 `skills list --json` 核对实际发现结果 |
| 只安装单个技能后引用缺失 | 是否存在跨技能相对路径 | 把必需资源移入当前技能，或按名称安装依赖技能 |
| 插件完整性检查失败 | tag、peeled SHA、摘要和本地技能清单 | 在源技能仓发布新版本，再由同步 PR 更新插件 |
| 工具或凭据缺失 | `compatibility`、运行时前置条件 | 报告 `UNVERIFIED`，不要猜测成功 |
| 自动化第二次运行仍产生差异 | 生成器非幂等或清单漂移 | 阻止发布并修复生成/排序规则 |
<!-- FULL_STACK_DOC_END -->

## 📄 License

Apache 2.0
