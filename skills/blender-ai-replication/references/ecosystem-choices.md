# Blender MCP Ecosystem Decision Matrix

Three independent ecosystems call themselves "Blender MCP". They are **not** interchangeable — different Add-on names, N-panel categories, setup paths, and capability schemas.

## Quick reference

| Ecosystem | Source | Add-on name | N-panel category | Setup entry point | Plugin cache | Local clone |
|---|---|---|---|---|---|---|
| **PartMe** | `full-aigc-plugins/blender-design-plugin` | **PartMe Blender MCP** | **PartMe MCP** | `blender_auto_setup` (auto) | v0.14.1 | ❌ not present |
| **Codex** | `full-aigc-skills/blender-skills` | **Blender Connector** | **Codex** | `blender_getting_started` (manual fallback) | ❌ not present | v1.1.0 |
| **ahujasid** | github.com/ahujasid/blender-mcp | `blender-mcp` (community) | varies per fork | git clone + manual install | ❌ not present | ❌ not present |

## Decision tree

### Pick **PartMe** when

- You want product-graded safety: every export is bound to an approved `snapshotId`.
- You need `auto_with_budget` execution policy with disk reservation + transaction gates.
- You are willing to live with the harness protocol overhead (closed envelope JSON, `expectedSceneRevision` threading).
- You don't mind that the plugin cache lags behind newer features (currently v0.14.1; the local `blender-skills` clone doesn't track it).

### Pick **Codex** when

- You are already inside the `full-aigc-skills` ecosystem (this package).
- You prefer a manual, user-authorized setup over auto-install.
- Your Add-on installation must survive future plugin cache updates.
- You accept that the "Codex" N-panel category is rare outside Codex CLI.

### Pick **ahujasid** when

- You are replicating a community tutorial that uses it (like the original 豆包 + Blender 清明上河图 post).
- You need the simplest possible install path (`uvx blender-mcp` or git clone + zip).
- You are willing to lose all the PartMe safety nets (no snapshot binding, no transaction gate, no budget policy).

## Why this matters: a worked example

The original 清上河图 3D blog post says:

> "请连接 Blender MCP, 如果本机没有, 请下载安装。链接: https://github.com/ahujasid/blender-mcp"

That URL is **ahujasid** (community). It is not the endpoint that the `full-aigc-plugins/blender-design-plugin` or `full-aigc-skills/blender-skills` plugins expect. Installing ahujasid does not satisfy the connection check of either plugin.

If a user's only goal is "follow the tutorial exactly", install ahujasid and stop. If they want to use the plugin harness (PartMe/Codex), the tutorial's setup section does NOT apply — they need their own plugin's setup skill.

## The skill/Add-on naming trap

Both PartMe and Codex plugins have documentation that mentions "MCP for Blender" or "Blender MCP" interchangeably. **These are different things**:

- The trusted Add-on for **PartMe** is `PartMe Blender MCP` (N-panel `PartMe MCP`).
- The trusted Add-on for **Codex** is `Blender Connector` (N-panel `Codex`).
- The community Add-on `MCP for Blender` (N-panel varies) is **not** a trusted endpoint for either plugin. Treat its presence as cosmetic, not as proof of connection.

`blender_connection_status` will return the right answer if the trusted Add-on is enabled and Start MCP Server was clicked.

## Drift between plugin cache and local clone

| | Plugin cache v0.14.1 | Local clone v1.1.0 |
|---|---|---|
| Skill count | 36 | 25 |
| Has `blender-harness` | ✅ | ❌ |
| Has `blender-seedance-pipeline` | ✅ | ❌ |
| Has `blender-managed` | ✅ | ❌ |
| Has `blender-recover` | ❌ | ✅ |
| Has `blender-video-original` | ❌ | ✅ |
| Has `blender-video-recreate` | ❌ | ✅ |

The local clone v1.1.0 is a **different upstream** than the plugin cache v0.14.1 — possibly an older snapshot, possibly a maintained fork. **Do not assume** their SKILL.md content matches even when skill names are the same.

Before running a skill from one side, verify:
1. The skill exists in the directory you'll actually install from.
2. The MCP bridge you're using is the one the skill targets.
3. The Add-on name in any setup steps matches the bridge you installed.

## Cross-references

- `pitfalls.md` — auto_setup false-positive on stale MCP servers.
- `qingming-sequence.md` — assumes PartMe (uses `harness_cli.py` + `transaction.*`).
- The local `blender-mcp-setup` SKILL.md — assumes Codex.