---
name: blender-scene-assembly
description: Organize Blender scenes, collections, object identity, transforms, visibility, and authorized reusable assets without losing editability or provenance.
---

# Scene and asset assembly

Inspect the current scene and units first. Use stable object IDs for continued work while retaining names for human readability. Put functional groups and helper geometry in named collections; distinguish independent duplicates from linked-data instances. When parenting an already placed object, use world-preserving parenting unless local-space relocation is intentional.

Import or link only from approved asset roots. Choose append when the project must own editable data, and link when provenance and shared updates matter. Record source paths, imported object receipts and any missing dependency. Do not download assets, install import extensions, or infer third-party license rights.

Before delivery, verify collection membership, local/world transforms, visibility in viewport and render, stable IDs after rename, linked versus copied data, and successful save/reopen. A successful simple fixture import does not guarantee compatibility with every external FBX, OBJ or glTF producer; disclose untested format features.

## 什么时候使用（When to Use）

需要组织场景、集合、对象身份、父子关系、可见性或导入已授权复用资产时使用。

## 输入与前置条件（Prerequisites）

- 明确场景单位、命名规则、功能分组、资产根目录、授权来源和 append/link 策略。
- 区分独立副本与共享数据实例，记录必须保持世界变换的对象。

## 执行流程（Workflow）

Step 1. 检查现有集合、对象 ID、变换与冲突名称。
Step 2. 按功能创建集合并移动对象，已有摆放对象默认使用保持世界变换的 parenting。
Step 3. 从批准根目录 append 或 link，记录来源、依赖和导入收据。
Step 4. 检查视口/渲染可见性、局部/世界变换、实例语义与稳定 ID。
Step 5. 保存重开，复核重命名和引用仍保持。

## 验证与交付证据（Validation）

提交集合树、对象稳定 ID、变换、可见性、linked/copied 状态、资产来源、缺失依赖和重开结果。

## Rules 与能力边界（不适用场景）

不下载资产、不安装导入扩展、不推断第三方许可；简单 fixture 成功不代表所有 FBX/OBJ/glTF 生产器兼容。

## Gotchas（常见问题与恢复）

- Parenting 后跳位：恢复原矩阵并使用保持世界变换方式重做。
- 链接资产不可编辑：确认是否应 append，不静默断开 provenance。
- 缺失依赖：报告原路径和受影响对象，等待授权替换。
