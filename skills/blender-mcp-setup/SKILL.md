---
name: blender-mcp-setup
description: "Set up or diagnose the plugin-owned Blender MCP connection when Blender is missing, the Add-on is disabled, Start MCP Server has not been clicked, or no guarded Harness session is discoverable."
---

# Blender MCP Setup

Use this for first use and connection failures. Call `blender_connection_status` before asking the
user to repeat setup. If it is not connected, call `blender_getting_started` and present its actual
Blender discovery result, official download URL, Add-on name, steps, and bundled screenshots.

Use this user-facing summary:

> 还没有 Blender？下载安装包
>
> 打开 Blender，在 偏好设置 > 插件 中启用 MCP 插件，然后在 N 面板中点击 Start MCP Server。

Clarify that the trusted Add-on name is **Blender Connector** and its N-panel category is
**Codex**. A separately installed community Add-on named **MCP for Blender** is not the endpoint for
this plugin and must not be treated as proof that the Blender Harness is connected.

Use the screenshots and steps returned by `blender_getting_started`; do not depend on package-level
documents that disappear in granular installs. Do not install Blender, enable Add-ons, or change MCP
configuration without the user's authorization. Never request or display the private Harness
descriptor token.

For error-specific recovery, supported/unsupported boundaries, common misrouting patterns, and
first-use examples, follow the workflow and recovery table below; granular installs must not rely
on package-level files that may be absent.

## 什么时候使用（When to Use）

首次连接，或出现 Blender 未安装、Add-on 未启用、服务器未启动、端口不可达、会话不可发现时使用。

## 输入与前置条件（Prerequisites）

- 先取得当前连接状态和实际 Blender 探测结果，不让用户重复已完成步骤。
- 区分官方 **Blender Connector** 与社区 **MCP for Blender**；不得索取私有 token。

## 执行流程（Workflow）

Step 1. 调用 `blender_connection_status` 并按失败层级分类。
Step 2. 未连接时调用 `blender_getting_started`，展示其实际路径、官方 URL、步骤与截图。
Step 3. 逐项确认 Blender、Add-on、N 面板按钮和本地端点，不自动安装或改配置。
Step 4. 连接后重新探测并执行一次只读场景检查，证明 Harness 会话可用。

## 验证与交付证据（Validation）

记录 CLI/插件版本、Blender 路径、Add-on 名称、连接状态、会话发现和只读检查结果；对 token 只报告存在性，不回显值。

## Rules 与能力边界（不适用场景）

未经授权不下载安装、不启用 Add-on、不编辑 MCP 配置，不把社区 Add-on 或端口占用当成可信 Harness 已连接。

## Gotchas（常见问题与恢复）

- 找到错误 Add-on：指出名称差异并按本地说明切换。
- 服务已启动但不可达：检查监听地址、进程与防火墙，不要求披露 token。
- 版本不兼容：报告探测版本和受支持范围，停止猜测性修复。
