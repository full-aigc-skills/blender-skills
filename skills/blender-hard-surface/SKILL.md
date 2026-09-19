---
name: blender-hard-surface
description: Create editable hard-surface, product, mechanical, or prop geometry with registered Blender mesh, modifier, collection, and recipe commands.
---

# Hard-surface modeling

Inspect the scene, units, capability details, and supplied dimensions before mutation. Preserve separate functional parts and an editable modifier order. Prefer Mirror/Array for repetition, Boolean for openings, Bevel for manufactured edges, Solidify for sheet thickness, and Subdivision only when the intended silhouette needs it.

Use `recipe.hard_surface_shell` or `recipe.spear` when its declared output matches the task. Otherwise combine registered object, mesh, modifier, curve, and collection commands. Never use expert Python to claim missing hard-surface coverage.

After topology changes, discard old mesh selections and query a new topology version. Inspect designated solids with `mesh.inspect`; explicitly set `allowOpenSurface` only for intentionally open surfaces. Check dimensions, modifier order, helper visibility, normals, degenerate geometry, and whether requested parts remain independently editable. L2 recipe output is not L3 until a saved, reopened, visually reviewed and reimported deliverable passes.

If a required asset, exact dimension, unsupported modifier parameter, or extension is missing, report it. Only invent a proxy when the task already authorizes original design, and list that proxy in delivery.

## 什么时候使用（When to Use）

创建产品、机械件、道具、外壳、开孔和可编辑重复结构时使用；需要有机雕刻时改用表面雕刻技能。

## 输入与前置条件（Prerequisites）

- 明确单位、关键尺寸、公差、功能分件、对称/阵列规则和参考素材授权。
- 记录允许的 modifier、开放表面意图和必须保持独立编辑的部件。

## 执行流程（Workflow）

Step 1. 检查比例与命名，按功能拆分对象和集合。
Step 2. 先完成主轮廓，再按意图添加 Mirror、Array、Boolean、Bevel、Solidify。
Step 3. 保持可解释 modifier 顺序，拓扑改变后重新查询选择与版本。
Step 4. 检查尺寸、法线、退化几何、helper 可见性和独立编辑性。
Step 5. 保存重开并从交付相机审阅制造边缘与轮廓。

## 验证与交付证据（Validation）

提交实际尺寸、对象/集合清单、modifier 顺序、`mesh.inspect` 结果、开放表面声明、预览和重开证据。

## Rules 与能力边界（不适用场景）

不以 expert Python 冒充缺失能力，不下载未授权资产，不把简单夹具通过当成所有格式或生产制造验证。

## Gotchas（常见问题与恢复）

- Boolean 破面：检查应用 scale、相交体和求解器，不堆叠重复 Boolean。
- Bevel 不均匀：先处理对象 scale 与法线。
- 尺寸漂移：回到参数和基准面，禁止用视觉缩放代替精确值。
