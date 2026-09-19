---
name: blender-hair
description: Create and inspect native Blender Hair Curves from explicit surface-local strand points, radii, and bound source surfaces.
---

# Blender Hair Curves

Use only native `CURVES` hair objects; do not describe ordinary Curve splines as hair. Require a named mesh surface and strand point arrays in that surface's local coordinate space.

Create the strands with explicit radius, then inspect strand count, point count and surface binding. Review root placement and silhouette from the intended camera before delivery.

The current interface covers authored guide strands, not grooming brushes, interpolation node assets or production hair shading. Use manual takeover or a separately registered capability when those are required.

## 什么时候使用（When to Use）

需要基于网格表面的原生 Hair Curves 引导束，并要求根部绑定和可编辑 strand 数据时使用。

## 输入与前置条件（Prerequisites）

- 指定表面网格、局部坐标 strand 点、半径、数量和期望轮廓。
- 确认对象确为原生 `CURVES` hair，而非普通 Curve spline。

## 执行流程（Workflow）

Step 1. 检查表面对象、变换和局部坐标系。
Step 2. 按根到梢顺序创建 strand 点，设置半径并绑定表面。
Step 3. 检查根部位置、点数、strand 数和异常长度。
Step 4. 从编辑视图及交付相机审阅轮廓，保存重开验证绑定。

## 验证与交付证据（Validation）

提供对象类型、源表面、strand/点计数、根部距离、半径范围和相机预览；重开后复核相同数据。

## Rules 与能力边界（不适用场景）

不覆盖 grooming brush、插值节点资产、动力学或生产级毛发着色，不把普通曲线描述为 Hair Curves。

## Gotchas（常见问题与恢复）

- 根部漂浮：核对局部坐标与表面变换。
- 毛束方向反转：调整点序而非旋转整个对象掩盖。
- 轮廓稀疏：先确认需求是否需要插值能力，不擅自复制大量引导束。
