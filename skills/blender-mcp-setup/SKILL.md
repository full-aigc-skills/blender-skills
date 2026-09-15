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

For illustrated steps, read [the Chinese setup guide](../../docs/getting-started.zh-CN.md) or
[the English setup guide](../../docs/getting-started.md). Do not install Blender, enable Add-ons, or
change MCP configuration without the user's authorization. Never request or display the private
Harness descriptor token.

For error-specific recovery, supported/unsupported boundaries, common misrouting patterns, and
first-use examples, read [setup troubleshooting](references/setup-troubleshooting.md).
