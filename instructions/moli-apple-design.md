# moli-apple-design — Apple 设计语言构建

## 引用文件

本工作流依赖下列文件（均位于 `moli-apple-design/` 目录）：

| 文件 | 用途 |
|---|---|
| `moli-apple-design/SKILL.md` | 完整技能规范 |
| `moli-apple-design/design-system.md` | 设计系统规范 |
| `moli-apple-design/tokens.css` | CSS 设计令牌 |
| `moli-apple-design/components.md` | 组件库 |
| `moli-apple-design/patterns.md` | 页面模式 |
| `moli-apple-design/motion.md` | 动效与交互 |
| `moli-apple-design/app.md` | iOS/移动端外壳 |
| `moli-apple-design/icons.md` | 线性图标集 |
| `moli-apple-design/review.md` | 评审工作流 |
| `moli-apple-design/reference.html` | 参考渲染 |
| `moli-apple-design/checklist.md` | 最终检查清单 |

---

## 工作流

```
┌─ 模式选择 ─────────────────────────────┐
│  新构建 → Build Mode                    │
│  评审   → Review Mode                   │
└─────────────────────────────────────────┘
```

### Build Mode（构建模式）

```
① 读 design-system.md  → 理解视觉语言
② 加载 tokens.css     → 引用设计令牌
③ 选 pattern          → 匹配页面类型
④ 组合 components     → 组装 UI 元素
⑤ 若含交互 → 读 motion.md 应用流体动效
⑥ 对照 reference.html → 校验还原度
⑦ 运行 checklist      → 逐项确认
```

### Review Mode（评审模式）

```
① 读 review.md        → 理解评审标准
② 对照 design-system.md → 逐项评分
③ 优先级排序发现的问题
④ 逐条修复，向 reference.html 靠拢
```

---

## Build Mode 详细步骤

### Step 1: 理解视觉语言

读取 `design-system.md`，掌握：
- 灰白底色、统一白色表面、克制玻璃效果
- SF Pro 字体体系（或等宽 Fallback）
- 栅格、间距、圆角规范

### Step 2: 加载令牌

从 `tokens.css` 引用以下类别：
- `--color-*` — 背景、表面、文字、强调色
- `--radius-*` — 圆角尺度
- `--space-*` — 间距体系
- `--shadow-*` — 玻璃阴影层级
- `--font-*` — 字体栈与字号

### Step 3: 选择页面模式

从 `patterns.md` 选取匹配的模式：
- 列表/卡片流
- 仪表盘/统计
- 详情/内容页
- 表单/设置
- 弹窗/模态

### Step 4: 组合组件

从 `components.md` 引用：
- 导航栏、工具栏、标签栏
- 卡片、列表项、表格
- 按钮、输入框、切换器
- 图表容器、媒体占位

### Step 5: 流体交互（仅交互层）

读取 `motion.md` 应用：
- **弹簧动效** — 非阻尼振荡，`spring()` 而非 `ease-out`
- **材质化** — 表面在拖拽/悬停时轻微抬起（阴影 + 缩放）
- **可中断性** — 动效可被新交互随时打断
- **手势物理** — 滚动惯性、弹性边界

### Step 6: 移动端/iOS 屏幕

若为 App/iOS 原型：
- 读取 `app.md` 套用设备外壳（状态栏 + 主页指示器）
- 使用 `icons.md` 中的 Lucide 线性图标
- 图标准则：`strokeWidth={1.5}`、`size={20}`

### Step 7: 最终检查

对照 `reference.html` 校验：
- 视觉还原度 ≥ 90%
- 运行 `checklist.md` 逐项确认
- 检查：间距、字号、颜色、圆角、阴影、图标风格

---

## Review Mode 详细步骤

### Step 1: 评审标准

读取 `review.md`，明确评分维度：
- 视觉一致性（颜色/字体/间距）
- 玻璃效果还原度
- 交互流畅度
- 响应式适配
- 可访问性

### Step 2: 评分

对照 `design-system.md` 对每个维度打分（1-5）。

### Step 3: 优先级排序

| 优先级 | 判定标准 |
|---|---|
| P0 | 视觉系统严重偏离（颜色/字体/间距错乱） |
| P1 | 组件或模式使用错误 |
| P2 | 细节偏离（圆角/阴影/图标风格不一致） |
| P3 | 微调建议（对齐/间距微差） |

### Step 4: 修复

按 P0 → P1 → P2 → P3 顺序逐条修复，每修复一条对照 `reference.html` 确认。
