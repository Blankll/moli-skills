---
name: moli-apple-design
description: Apple 设计语言 — 液态玻璃视觉系统 + 流体交互哲学。使用场景：构建 Apple 风格页面/组件、iOS 原型、需要"苹果风"设计评审。涵盖灰白底统一表面系统、克制玻璃、弹簧动效、手势物理、中断响应、材质深度与无障碍动效。
license: Apache-2.0
compatibility: opencode
metadata:
  author: Integrated from naplesblue/apple-design-skill & emilkowalski/skills apple-design, MIT
  version: "1.0.0"
  category: design
---

# Moli Apple Design — 液态玻璃视觉系统 + 流体交互哲学

> 融合两套设计思想：**naplesblue/apple-design-skill** 的液态玻璃（Liquid Glass）视觉规范与 **emilkowalski/skills apple-design** 的 WWDC 流体交互哲学。你同时获得 Apple 的"外观"和"感觉"。

**一句话：** 冷静、高级、克制。浅灰白底色 + 统一白色面板 + 发丝分隔线；玻璃只出现在层叠处。交互从指尖当前值开始，继承用户速度，投射动量，且可随时被抓取和反转。弹簧是实现这一切的工具。

---

## 目录

1. [设计哲学](#1-设计哲学)
2. [交互设计原理（八大原则）](#2-交互设计原理八大原则)
3. [核心理念](#3-核心理念)
4. [视觉系统概览](#4-视觉系统概览)
5. [色彩系统](#5-色彩系统)
6. [字体与排版](#6-字体与排版)
7. [间距 · 圆角 · 阴影](#7-间距--圆角--阴影)
8. [液态玻璃材质系统](#8-液态玻璃材质系统)
9. [材质与深度哲学](#9-材质与深度哲学)
10. [动效与物理交互](#10-动效与物理交互)
11. [交互层运动系统](#11-交互层运动系统)
12. [手势设计](#12-手势设计)
13. [减少动效与无障碍](#13-减少动效与无障碍)
14. [多模态反馈](#14-多模态反馈)
15. [组件库](#15-组件库)
16. [页面模式与决策树](#16-页面模式与决策树)
17. [App / iOS 原型壳](#17-app--ios-原型壳)
18. [图标层](#18-图标层)
19. [两种工作模式](#19-两种工作模式)
20. [Build 模式工作流](#20-build-模式工作流)
21. [Review 模式工作流](#21-review-模式工作流)
22. [反模式清单（Anti-slop）](#22-反模式清单anti-slop)
23. [自查清单](#23-自查清单)
24. [交互层运动自查](#24-交互层运动自查)
25. [App 自查](#25-app-自查)
26. [运动物理快速参考](#26-运动物理快速参考)
27. [排版快速参考](#27-排版快速参考)
28. [处理流程与过程](#28-处理流程与过程)
29. [本技能文件结构](#29-本技能文件结构)

---

## 1. 设计哲学

### 5 条视觉哲学规则（naplesblue — 以此顺序决策）

> 这些规则源于观察 Apple 在 macOS Big Sur+、iOS 14+、apple.com、Apple Newsroom 和 WWDC 视觉语言中的设计模式。它们并非主观喜好，而是从 Apple 数百个界面中归纳出的共同特征。

**优先级声明：** 当一条规则与另一条冲突时，编号更靠前的规则胜出。例如，如果"添加颜色能帮助建立层次"但"打破颜色铁律"，那么规则 4（层级来自灰度）胜过你的直觉。先遵守系统，再思考例外。

这些规则构成了视觉决策的框架。当你在颜色、布局或材质之间犹豫时，按此顺序回溯到规则：

**规则 1 — 统一表面 > 碎片卡片**

多个同级项放在**一块白色面板 + 发丝分隔线**上，而不是一堆各自有边框和背景色的卡片。碎片化是头号敌人。

为什么？Apple 的设计中，内容是一个连续的整体。每添加一个边框、一个背景色、一个投影，都在增加视觉噪声。单一白色面板让用户的眼睛平滑地扫过内容，发丝分隔线只在需要的地方给出提示。这种处理方式在以下场景中适用：
- 设置页面中的多个选项行
- 文章列表
- 交易历史记录
- 联系人列表

反例：一个个各自有白色背景、投影和有色左边栏的卡片堆叠在一起——这是最需要避免的。

**规则 2 — 玻璃是调味料，不是主菜**

`backdrop-filter` 毛玻璃**只用于层叠处**：粘性导航栏、模态框/弹出框、彩色 CTA 区块。纯内容区块使用实色 `#fff` + 柔和阴影——永远不要用玻璃。

为什么？网页上的层叠天然就很少。如果整个页面都用玻璃效果，就像在一道菜里放了过量的盐——每样东西都一个味道，失去了层次感。玻璃的价值在于它"透出"背后的内容，所以必须有内容给它透。两个白色区块之间的模糊没有任何意义，只会让 CPU 发热。

**规则 3 — 克制即奢侈**

用一千个"不"换一个"是"。如果空白和层级能解决问题，就不加边框、填充、图标或数字。拒绝数据填充。

这条规则执行起来最难。当你觉得页面"不够丰富"时，自然的冲动是加东西——加一个图标、加一条分隔线、加一个数字标记。但 Apple 的方式恰恰相反：先问"我能去掉什么"。足够的留白本身就是一种视觉信号——它告诉用户"这里是重要的，请停下来阅读"。

**规则 4 — 层级来自字重 + 字号 + 灰度，不是颜色**

正文世界是黑-白-灰。颜色只用于**强调色**（一种蓝）、**热度**（一种橙）、**品牌/在线**。永远不用颜色填充空间。

这意味着：
- 标题用更重的字重和更大的字号来突出，而不是用蓝色或紫色
- 次要文本用更浅的灰色，而不是用更小的字号或不同的颜色
- 颜色是稀缺资源，只在需要用户注意的地方使用——且一次只用一个强调色

**规则 5 — Apple 的品质在细节中**

大字标题负字间距、`tabular-nums` 数字、发丝分隔线、柔和悬浮抬升、180% 饱和度玻璃——所有这些小事的**总和**才构成"Apple 风"。

没有哪一个细节单独看起来重要，但把它们全部加起来，效果就明显了。一个标题如果缺少负字间距，看起来就不够"紧致"；一个数字如果没有 `tabular-nums`，在列表中对不齐；一个没有悬浮效果的卡片，交互感就弱了。

### 交互基础原则（用这些名称推理）

这些原则补充了上述视觉规则，涵盖了交互设计的基本面：

- **寻路 —— 每个屏幕回答四个问题：** 我在哪？我能去哪？那里有什么？我怎么出去？永远不要困住用户。每个屏幕都应该有明确的标题、清晰的导航路径和可见的退出方式。
- **反馈分四种：** 状态（status，正在发生什么）、完成（completion，操作已完成）、警告（warning，可能出问题）、错误（error，出问题了）。内联验证（不要提交时校验）；暴露进行中状态。
- **分组与映射。** 把控件放在它影响的东西旁边；排列控件时反映它们改变的对象。如果一个控件需要标签才能被理解，说明映射关系薄弱——用户不应该需要阅读标签才能明白一个滑块控制的是音量还是亮度。
- **自主权与宽恕。** 轻松撤销优于确认对话框；只为真正破坏性、不可逆的操作保留确认（过度使用会训练人们盲目点击）。每次确认对话框都在消耗用户的耐心。
- **直接、具体的标签优于安全通用的。** "进度"/"资料库"，而不是"首页"。具体性创造可预测性——用户不需要猜测一个按钮会带他们去哪。

### 人类需求四象限

Apple 将设计视为服务于四种人类需求（来自 WWDC 2018），每个设计决策应服务于其中之一：

| 需求 | 含义 | 设计实施 |
|---|---|---|
| 安全/可预测性 | 用户知道接下来会发生什么 | 一致的交互模式、可逆操作、明确的视觉反馈 |
| 理解 | 信息易于消化 | 清晰的层次、有逻辑的分组、平实的语言 |
| 成就 | 用户可以完成目标 | 高效的操作路径、最小化步骤数 |
| 愉悦 | 使用体验正面 | 流畅的动效、周到的细节、出人意料的用心之处 |

---

## 2. 交互设计原理（八大原则）

> 来自 Apple *Principles of Great Design*（WWDC 2026），由 emilkowalski/skills 转化并翻译为 Web 平台。这些是你推理时使用的名称——运动与工艺服务于这些原则。

**1. Purpose（目的）**

带着意图制作；决定**不**做什么。每个功能都在请求用户的时间、注意力和信任——只把预算花在值得的地方。

实施方式：
- 每个功能上线前问：这解决了什么真实问题？用户会用吗？没有明确答案就不要做
- 功能上线后关注留存数据——如果没人用，就考虑移除
- 一个功能的设计越简单，说明你对它的目的越清楚

**2. Agency（自主权）**

让人们保持控制：提供选择，不要强加单一路径。用宽恕来支持——轻松撤销误操作，确认对话框只用于真正破坏性、不可逆的操作（谨慎使用；过度使用会训练人们盲目点击）。

实施方式：
- 操作一般都应该可以撤销（Cmd+Z / 垃圾桶 / 还原）
- 确认对话框只留给删除账户、付款等不可逆操作
- 提供默认值，但允许用户自定义关键设置

**3. Responsibility（责任）**

为用户利益行事。隐私：在合适的时机询问，只索取必要信息，透明告知。安全：预见误用和伤害——尤其是 AI（一个过敏感知的食谱应用绝不能推荐有害成分）。添加预览、确认、免责声明；如果风险超过价值，就砍掉这个功能。

实施方式：
- 权限请求在需要时弹出，不要在首次启动时全部要求
- 敏感操作前提供预览（"这条消息将发送给 5 个人"）
- AI 生成内容确保有适当的安全护栏

**4. Familiarity（熟悉感）**

建立在人们已知的事物上。使用既不太字面也不太抽象的隐喻（垃圾桶表示删除），并尊重它们的物理规律。保持一致：看起来相同的事物必须行为相同且在相同的位置（macOS 上关闭按钮总是在左上角），这样人们才能预测接下来会发生什么。只有在能证明更好时才打破熟悉模式——然后测试它，不要假设。

实施方式：
- 使用平台标准控件和交互模式
- 系统字体优先——用户已经熟悉它的阅读体验
- 图标应该有明确的语义（放大镜=搜索，齿轮=设置）
- 打破惯例必须带来足够大的收益，并且通过可用性测试验证

**5. Flexibility（灵活性）**

为不同上下文、设备和全部能力范围设计。适配平台（iPhone = 快速触摸；桌面 = 深度工作流 + 精确指针控制）和情境。包容性地设计（年龄、语言、专业度、无障碍）。当单一布局不适合所有人时，让人们个性化——重新排列控件，隐藏不用的内容。

实施方式：
- 响应式设计：布局适应不同屏幕尺寸
- 支持 Dynamic Type：用户调整字体大小后 UI 不破裂
- 提供暗色模式（dark mode）
- 高级用户功能不干扰新手——默认显示基本操作，高级选项可展开

**6. Simplicity（简洁 —— 不是极简）**

剥离不必要的内容，让核心目的闪耀；把所有东西埋在一个地方看起来很极简，但并不简洁。精炼（平实的语言、没有行话、更少的步骤）和清晰（使用层次——顺序、间距、对比——让最重要的东西最显眼）。每个元素都赢得它的位置；有时**添加**上下文反而能简化（一个显示剩余时间的视频进度条）。先展示常用路径，高级选项深入一层。

实施方式：
- 核心操作路径不超过 3 步
- 使用平实的语言，避免术语
- 重要的内容用更大的字号和更重的字重突出
- 不要让用户思考——最好的界面是用户不需要说明书就能使用的

**7. Craft（工艺）**

对细节毫不妥协的追求建立信任。优美的排版、适应亮暗的主题色、清晰的图标、以及提供即时自然反馈的响应式动画。没有什么是随机的——每个间距、时间和对齐值都是你可以辩护的深思熟虑的选择。抖动的滚动、错位的图标和旋转屏幕时崩溃的布局读作粗心大意。工艺需要迭代和长久的维护——随着功能和硬件的变化持续演变设计。

实施方式：
- 像素级对齐：即使是无意的 1px 偏差也值得修正
- 动画时间参数化：不是随意的 300ms，而是来自设计系统的命名缓动曲线
- 主题化：颜色、间距、圆角来自中央 Token，不是硬编码值
- 测试暗色模式、旋转屏幕、大字体等边缘情况

**8. Delight（愉悦）**

是把其他七条做对的结果，而不是贴在上面的五彩纸屑。决定你希望人们感受的情绪（平静、自信、兴奋），并在每个决策中强化它。

实施方式：
- 愉悦是副产品——它来自精心的工艺、流畅的交互和出人意料的周到细节
- 不要强行加"好玩"的东西（动画表情、五彩纸屑）。那只是噪音
- 用户在使用过程中自然微笑——不是因为某个元素本身有趣，而是因为整个体验令人愉悦

---

## 3. 核心理念

> 来自 emilkowalski/skills apple-design，源自 Apple WWDC *Designing Fluid Interfaces*（2018）

### 核心线索

**界面在运动从当前屏幕值开始、继承用户速度、向前投射动量、且可在任何瞬间被抓住并反转时，才显得有生命力。弹簧是实现这一切的工具。**

当我们将界面与我们的思维和运动方式对齐时，神奇的事情发生了——它不再像一台电脑，而开始感觉像我们的无缝延伸。

### 什么是流畅的界面？

一个界面在以下情况下是流畅的：

1. **即时响应** —— 反馈出现在触摸的瞬间，没有延迟
2. **连续运动** —— 动画从不跳跃或卡顿
3. **承载动量** —— 轻弹一个元素，它会自然减速而不是突然停止
4. **边界抵抗** —— 拉到边界时感受到柔和阻力而不是硬撞
5. **可重定向** —— 任何动画都可以中途被抓住并改变方向

### Apple 设计哲学核心

> "当我们把界面与我们的思考和运动方式对齐时，魔法发生了——它不再感觉像一台电脑，而开始感觉像我们的无缝延伸。"

---

## 4. 视觉系统概览

> 完整规范见 `design-system.md`；Token 值见 `tokens.css`；渲染效果见 `reference.html`。

### 核心 Token 速查

```
ground   #f5f5f7          页面底色（冷色调，不是暖色/米色）
surface  #ffffff           表面/卡片色
hover    #fbfbfd           行悬浮色

text     #1d1d1f           主文本（近乎黑色）
text-2   #424245           正文/次要文本（深灰）
text-3   #6e6e73           三级文本（中灰）
text-4   #86868b           四级文本
text-5   #aeaeb2           占位符
faint    #d2d2d7           弱显（数字、箭头）
hairline rgba(0,0,0,.07)   发丝分隔线

accent   #0071e3           Apple 蓝（操作/链接/聚焦）
indigo   #5e5ce6           靛蓝（渐变第二停点）
x-blue   #1d9bf0           平台蓝（如 X/Twitter）
heat     #ff6b00           热度橙
live     #30d158           在线绿（脉冲）

radius   pill 999 · chip 6 · thumb 12 · sheet 16 · card 18 · panel 22 · hero 26
shadow   card / panel / lift / cta / overlay（全部双层，从不单层硬阴影）
track    #e8e8ed           进度轨道/开关关闭态

container 720 read / 1080 grid
pad-x   22px               侧边距
sec-gap  clamp(34,6vw,56)  区块间距

glass    rgba(245,245,247,.72) + blur(20px) saturate(180%)  导航玻璃配方

ease-spring     cubic-bezier(0.32, 0.72, 0, 1)    弹簧缓动（入场）
ease-out-quart  cubic-bezier(0.25, 1, 0.5, 1)     悬浮/小动量
```

### Token 文件引用

所有值通过 `var(--…)` 自定义属性引用。**永远不要硬编码 Token 已命名的原生 hex/px。**

```css
:root {
  --bg: #f5f5f7;
  --surface: #ffffff;
  --hover: #fbfbfd;
  --text: #1d1d1f;
  --text-2: #424245;
  --text-3: #6e6e73;
  --text-4: #86868b;
  --text-5: #aeaeb2;
  --faint: #d2d2d7;
  --hairline: rgba(0,0,0,0.07);
  --accent: #0071e3;
  --accent-hover: #0066cc;
  --indigo: #5e5ce6;
  --x-blue: #1d9bf0;
  --heat: #ff6b00;
  --heat-bg: rgba(255,107,0,0.1);
  --live: #30d158;
  --grad-cta: linear-gradient(135deg,#0071e3,#5e5ce6);
  --track: #e8e8ed;
  --r-pill: 999px;
  --r-chip: 6px;
  --r-thumb: 12px;
  --r-sheet: 16px;
  --r-card: 18px;
  --r-panel: 22px;
  --r-hero: 26px;
  --sh-card: 0 1px 2px rgba(0,0,0,.04), 0 8px 24px rgba(0,0,0,.05);
  --sh-panel: 0 1px 3px rgba(0,0,0,.05), 0 14px 40px rgba(0,0,0,.05);
  --sh-lift: 0 12px 32px rgba(0,0,0,.1);
  --sh-cta: 0 20px 54px rgba(0,113,227,.24);
  --sh-overlay: 0 2px 8px rgba(0,0,0,.10), 0 30px 80px rgba(0,0,0,.24);
  --max-read: 720px;
  --max-grid: 1080px;
  --pad-x: 22px;
  --sec-gap: clamp(34px,6vw,56px);
  --ease-spring: cubic-bezier(0.32, 0.72, 0, 1);
  --ease-out-quart: cubic-bezier(0.25, 1, 0.5, 1);
  --font-stack: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'SF Pro Display',
    'Helvetica Neue', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
  --mono: ui-monospace, 'SF Mono', 'Menlo', 'Consolas', monospace;
}
```

---

## 5. 色彩系统

### 中性色（骨架）

中性色构成了页面 95% 的色彩面积。它们必须精确——微小的偏差会破坏 Apple 特有的"冷静感"。

| 角色 | 色值 | 使用场景 | 注意 |
|---|---|---|---|
| 页面底色 | `#f5f5f7` | 整个页面的背景 | **必须是冷色调**。不要用 `#f7f7f5`（微暖）或 `#f5f0eb`（奶油色） |
| 表面 | `#ffffff` | 面板、卡片、列表 | 纯白，不用 `#fcfcfc` 或 `#fafafa` |
| 行悬浮 | `#fbfbfd` | 可点击行的悬浮态 | 极微妙，比底色亮一个阶梯 |
| 主文本 | `#1d1d1f` | 标题、重点信息 | 近乎黑色但比 `#000` 柔和 |
| 正文 | `#424245` | 正文段落、次要信息 | 阅读舒适度优化 |
| 摘要 | `#6e6e73` | 元信息、摘要、标签 | 仍可读，但退居次要 |
| 四级 | `#86868b` | 更次要的信息 | 大段阅读时应避免使用 |
| 占位符 | `#aeaeb2` | 输入框占位符 | 足够浅但仍有存在感 |
| 弱显 | `#d2d2d7` | 页码箭头、装饰数字 | 最浅的灰色 |
| 发丝 | `rgba(0,0,0,0.07)` | 分割线、边框 | 极细的半透明，适应任何背景 |

### 强调色（仅用于强调）

颜色是稀缺资源，只能用于以下四种情况之一：

| 角色 | 色值 | 何时使用 | 何时不用 |
|---|---|---|---|
| Apple 蓝 | `#0071e3` | 主按钮、链接、聚焦状态、激活态 | 不要作为装饰色填充空白区域 |
| Apple 蓝悬浮 | `#0066cc` | 蓝色按钮/链接的 hover/active 态 | 不要单独使用，总是与 `#0071e3` 配对 |
| 靛蓝 | `#5e5ce6` | 仅用于渐变 CTA 的次要色停点 | 不要单独作为强调色使用 |
| 平台蓝 | `#1d9bf0` | 第三方品牌集成 | 不要在自己品牌的 UI 中使用 |
| 热度橙 | `#ff6b00`（文本），`rgba(255,107,0,0.1)`（背景） | 最热门、最紧急、突破性内容 | 不要用于常规操作按钮，**一件**内容同时使用 |
| 在线绿 | `#30d158` | 直播状态、在线指示器、成功状态 | 不要用于列表值着色（收入绿/支出红是陷阱） |

### 签名渐变（有限使用）

只在以下场景使用渐变：
- **英雄区/封面图背景** —— 作为视觉焦点
- **CTA 按钮区块** —— 与液态玻璃配合
- **占位艺术图** —— 在真实图片不可用时的优雅替代

```css
--grad-blue-purple: linear-gradient(135deg, #0a84ff, #5e5ce6);
--grad-warm:        linear-gradient(135deg, #ff9f0a, #ff375f);
--grad-green-blue:  linear-gradient(135deg, #30d158, #0a84ff);
--grad-cta:         linear-gradient(135deg, #0071e3, #5e5ce6);
```

**禁止清单：**
- ❌ 全出血渐变洗墙
- ❌ 发明新的色相
- ❌ 暖色/米色/奶油色底色
- ❌ 单个视图中使用两种以上强调色

### 暗色模式适配

暗色模式的核心策略是反转灰度层次，保持强调色：

```css
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #000000;
    --surface: #1c1c1e;
    --hover: #2c2c2e;
    --text: #f5f5f7;
    --text-2: #a1a1a6;
    --text-3: #6e6e73;
    --hairline: rgba(255,255,255,0.12);
  }
}
```

---

## 6. 字体与排版

### 字体栈（总是系统字体；永远不用 Inter/Roboto）

```css
--font-stack: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'SF Pro Display',
  'Helvetica Neue', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
```

规则：
- 第一选择是 Apple 系统字体（SF Pro），它在 Apple 设备上提供最佳阅读体验
- 在非 Apple 设备上回退到系统无衬线字体
- 专为中文用户添加 PingFang、Hiragino Sans GB、Microsoft YaHei
- `-webkit-font-smoothing: antialiased;` 始终开启
- `font-optical-sizing: auto` 在根元素上 —— SF 已经内置光学尺寸表

### 字号 · 字重 · 字间距 · 行高

| 角色 | 字号 | 字重 | 字间距 | 行高 | 使用场景 |
|---|---|---|---|---|---|
| H1 | `clamp(27px,5vw,46px)` | 700 | `-0.03em` | 1.1–1.18 | 页面标题、文章大标题 |
| H2 | `clamp(20px,3.4vw,26px)` | 700 | `-0.02em` | 1.25 | 章节标题、区块标题 |
| H3 / 项目标题 | `15.5–18px` | 600 | `-0.01em` | 1.4–1.45 | 卡片标题、列表项标题 |
| 长文正文 | `clamp(16px,2.6vw,18px)` | 400 | 0 | **1.85–1.9** | 文章正文、描述文字 |
| 摘要 / 导语 | `15–19px` | 400 | 0 | 1.55–1.7 | 文章导语、卡片摘要 |
| 元信息 / 署名 | `12–13.5px` | 400–550 | 0 | 1.6 | 日期、作者、面包屑 |
| 标签 / Chip | `11–12px` | 500–650 | — | — | 分类标签、状态指示器 |

### 排版铁律

1. **大字标题负字间距**（越大越负）：H1 `-0.03em`、H2 `-0.02em`、H3 `-0.01em`
2. **长文行高 ≥ 1.85**
3. 数字使用 `font-variant-numeric: tabular-nums`
4. 多行截断使用 `-webkit-line-clamp`
5. CJK↔Latin 之间使用**半角空格**（"iPhone 17 Pro 号称…"）

### 排版优化（来自 emilkowalski，源自 WWDC 2020）

**规则 1 — 字间距与尺寸相关**

大号展示文本需要**负**字间距（字母随着尺寸增大看起来太散）；小号文本需要略**正**的字间距以提高可读性。固定的 `letter-spacing` 在某个尺寸上一定出错。

```css
.display-large { letter-spacing: -0.03em; }
.body-text     { letter-spacing: 0; }
.caption       { letter-spacing: 0.02em; }
```

**规则 2 — 行高与尺寸成反比**

大标题行高紧，正文行高松。上表已经编码了这个规则。

**规则 3 — 层次来自字重 + 字号 + 行高的组合**

一个 600 字重的 16px 标题比一个 400 字重的 18px 文字更像标题。先用字重，再用字号。

**规则 4 — 尊重用户的文本尺寸设置**

使用 `rem`/`em` 做与文本相关的间距，这样当用户调整系统字体大小时布局不会破裂。

```css
.card { padding: 1em; gap: 0.5em; }   /* 好：随字体缩放 */
.card { padding: 16px; gap: 8px; }     /* 不好：固定 px */
```

**规则 5 — 系统字体优先**

系统字体已经内置了光学尺寸表、字间距表和可读性调优。只有在有明确理由时才覆盖。

### 排版示例

```html
<article style="max-width: var(--max-read); margin: 0 auto; padding: 0 var(--pad-x);">
  <div style="font-size:12px; font-weight:600; letter-spacing:0.14em; color:var(--text-3); margin-bottom:12px;">
    设计系统 · 排版
  </div>
  <h1 style="font-size:clamp(27px,5vw,46px); font-weight:700; letter-spacing:-0.03em; line-height:1.1;">
    排版让设计可信
  </h1>
  <p style="font-size:clamp(15px,2.5vw,19px); color:var(--text-2); line-height:1.6; max-width:560px; margin-top:16px;">
    优美的排版是 Apple 设计中最容易被忽视但最重要的部分。
  </p>
  <p style="font-size:clamp(16px,2.6vw,18px); line-height:1.85; color:var(--text-2); margin-top:24px;">
    正文的排版决定了阅读体验。行高 1.85 保证了大段文本中每行之间有足够的呼吸空间，
    视线不会在行间跳跃。负字间距则让大标题看起来紧凑而精致，不会有松散的感觉。
  </p>
  <div style="margin-top:32px; padding-top:16px; border-top:1px solid var(--hairline);
              font-size:13px; color:var(--text-3);">
    2026 年 7 月 · 3 分钟阅读 ·
    <span style="font-variant-numeric:tabular-nums;">1,284</span> 次浏览
  </div>
</article>
```

---

## 7. 间距 · 圆角 · 阴影

### 圆角层级

**规则：不要发明中间值。** 每个层级都有明确的使用场景。

| 层级 | Token | 值 | 使用场景 | 原理 |
|---|---|---|---|---|
| Pill | `--r-pill` | `999px` | 按钮、分段控件、标签、输入框 | 完全圆角，Apple 标志性胶囊形状 |
| Chip | `--r-chip` | `6px` | 品牌标识小角标、mono 标签 | 微圆角，不干扰文字 |
| Thumb | `--r-thumb` | `12px` | 小图片、头像方形、图标容器 | 视觉上轻微的软化 |
| Sheet | `--r-sheet` | `16px` | 覆盖层中全宽堆叠按钮 | 比缩略图更圆，但不到卡片级别 |
| Card | `--r-card` | `18px` | 独立卡片、文章卡片、弹窗 | 明确软化的卡片边缘 |
| Panel | `--r-panel` | `22px` | 统一列表面板、设置分组 | 最大的功能性圆角 |
| Hero | `--r-hero` | `26px` | CTA 区块、封面图、特色模块 | 最圆润的结构性元素 |

### 阴影规则（双层阴影系统）

**规则：永远使用双层阴影（近层接触 + 远层扩散）。** 单层硬阴影看起来廉价。

| 层级 | Token | 值 |
|---|---|---|
| 卡片 | `--sh-card` | `0 1px 2px rgba(0,0,0,.04), 0 8px 24px rgba(0,0,0,.05)` |
| 面板 | `--sh-panel` | `0 1px 3px rgba(0,0,0,.05), 0 14px 40px rgba(0,0,0,.05)` |
| 悬浮抬升 | `--sh-lift` | `0 12px 32px rgba(0,0,0,.1)`（配合 `translateY(-3px)`） |
| CTA | `--sh-cta` | `0 20px 54px rgba(0,113,227,.24)` |
| 覆盖层 | `--sh-overlay` | `0 2px 8px rgba(0,0,0,.10), 0 30px 80px rgba(0,0,0,.24)` |

阴影工作原理：
```css
/* 正确的双层阴影 */
box-shadow: 0 1px 2px rgba(0,0,0,.04),    /* 紧贴层 —— 模拟真实接触 */
            0 8px 24px rgba(0,0,0,.05);    /* 发散层 —— 模拟环境光遮蔽 */
```

### 间距系统

| 参数 | Token | 值 | 使用场景 |
|---|---|---|---|
| 阅读容器 | `--max-read` | 720px | 文章、详情页、表单 |
| 网格容器 | `--max-grid` | 1080px | 首页、索引页、仪表盘 |
| 侧边距 | `--pad-x` | 22px | 容器与视口边缘 |
| 区块间距 | `--sec-gap` | `clamp(34px,6vw,56px)` | 主要区块垂直间距 |
| 触摸目标 | — | 44px 最小值 | 所有可点击元素 |

**原则：** flex/grid + `gap`（不用 inline + margin）；区块呼吸；面板按内容高度调整。

---

## 8. 液态玻璃材质系统

### 什么是液态玻璃（Liquid Glass）

Apple 在 macOS Big Sur 及以后版本中推广的视觉语言：表面像一层极薄的玻璃，能透出背后的内容，但又足够实在以承载 UI 元素。关键在于**克制**——只有层叠的地方才需要玻璃。

### Glass 使用规则

| 场景 | 玻璃配方 | 必须？ |
|---|---|---|
| 粘性导航栏 | `rgba(245,245,247,0.72)` + `blur(20px)` + `saturate(180%)` | ✅ |
| 模态框/弹出框 | 同上，加 `--sh-overlay` 阴影 | ✅ |
| Tab 栏 | `rgba(245,245,247,0.82)` + `blur(20px)` | ✅ |
| CTA 中的标签 | `rgba(255,255,255,0.16)` + `blur(8px)` + `border` | ✅ |
| 纯内容卡片 | **不透明 `#fff`** + `--sh-card` | ❌ |
| 列表行 | **不透明 `#fff`**（面板背景） | ❌ |
| 两个白色区块之间 | **不透明 `#fff`** | ❌ |

### 玻璃配方详解

**配方 1：标准导航玻璃**

```css
.glass-nav {
  background: rgba(245, 245, 247, 0.72);
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  border-bottom: 1px solid rgba(0, 0, 0, 0.07);
}
```

**配方 2：深色地面上的玻璃**

```css
.glass-on-dark {
  background: rgba(255, 255, 255, 0.16);
  border: 1px solid rgba(255, 255, 255, 0.22);
  backdrop-filter: blur(8px);
}
```

**配方 3：玻璃 + 模糊光晕**

玻璃需要"折射"才能看起来真实。在玻璃元素后方放置模糊的半透明光晕：

```html
<section style="position:relative; overflow:hidden; border-radius:var(--r-hero);">
  <!-- 光晕层 -->
  <div style="position:absolute; width:260px; height:260px; border-radius:50%;
              background:rgba(255,255,255,0.18); filter:blur(46px);
              top:-80px; right:-40px; pointer-events:none;"></div>
  <div style="position:absolute; width:200px; height:200px; border-radius:50%;
              background:rgba(120,80,255,0.5); filter:blur(50px);
              bottom:-90px; left:12%; pointer-events:none;"></div>
  <!-- 内容在光晕上方 -->
  <div style="position:relative;"><!-- ... --></div>
</section>
```

### 滚动边缘效果

粘性导航栏下方不要使用永久边框。只在实际滚动后才显示：

```css
.nav-sticky {
  position: sticky;
  top: 0;
  z-index: 50;
  border-bottom: 1px solid transparent;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}
.nav-sticky.scrolled {
  border-bottom-color: rgba(0, 0, 0, 0.07);
  box-shadow: 0 1px 12px rgba(0, 0, 0, 0.04);
}
```
```js
addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', scrollY > 8);
}, { passive: true });
```

---

## 9. 材质与深度哲学

> 来自 emilkowalski/skills apple-design，源自 Apple 的材质系统设计理念。

### 半透明材料的角色

Apple 使用半透明材质作为浮动的功能性层——它们带来结构，但不窃取焦点。在 Web 上，我们用 `backdrop-filter` 来近似。

**核心概念：透明度和模糊程度的组合编码了层次信息。**

### 材质重量编码层次

| 材质重量 | 透明度 | 模糊 | 使用场景 | 视觉效果 |
|---|---|---|---|---|
| 最轻 | `rgba(255,255,255,0.16)` | `8px` | CTA 上的玻璃标签 | 几乎透明，颜色从背景透出 |
| 轻 | `rgba(245,245,247,0.72)` | `20px` | 导航栏 | 半透明，内容隐约可见 |
| 中 | `rgba(245,245,247,0.82)` | `20px` | Tab 栏 | 略不透明，强调功能性 |
| 重 | `rgba(245,245,247,0.92)` | `20px` | 覆盖层 | 几乎不透明，聚焦内容区域 |

**规则：材质重量递减 = 视觉优先级递增。** 最亮的材质（最透明）吸引最多注意力；最重的材质（最不透明）提供结构支撑。

### 场景决策：遮罩 vs 无遮罩

| 场景 | 使用遮罩？ | 原因 |
|---|---|---|
| 模态任务 | ✅ 变暗背景遮罩 | 用户需要专注在模态内容上，背景被推远 |
| 非阻塞面板 | ❌ 不用遮罩 | 并列的内容流不应被打断 |
| 堆叠面板 | ✅ 逐步变暗各父层 | 每一层都向下推远前一层 |

### 玻璃上的文字处理（Vibrancy/光彩效果）

在半透明表面上，不要使用常规灰色文本——对比度不够：

```css
.text-on-glass {
  color: rgba(0, 0, 0, 0.85);
  font-weight: 550;
  letter-spacing: 0.01em;
}

.text-on-glass-dark {
  color: rgba(255, 255, 255, 0.92);
  font-weight: 550;
}
```

### 材质物化效果

```css
.glass-surface {
  opacity: 0;
  transform: scale(0.98);
  transition:
    opacity 0.4s var(--ease-spring),
    transform 0.4s var(--ease-spring),
    backdrop-filter 0.4s var(--ease-spring);
}
.glass-surface.open {
  opacity: 1;
  transform: none;
}
```

---

## 10. 动效与物理交互

> 来自 emilkowalski/skills apple-design（MIT），源自 Apple WWDC *Designing Fluid Interfaces*（2018）。这是本技能中"感觉"的部分。

### 10.1 为什么动效是"感觉"而非"外观"

Apple 与其他设计系统的关键区别在于：动效不是装饰，而是功能。

在 Apple 的设计中，动效回答了三个问题：
1. **我做了什么？** —— 点击、拖动、轻弹后的即时反馈确认操作已注册
2. **发生了什么？** —— 面板的升起、内容的移动、状态的改变被动效自然呈现
3. **接下来会怎样？** —— 方向提示、弹簧过冲、速度交接让用户预判运动终点

如果动效不能回答至少一个上述问题，它就应该被移除。

### 10.2 层面分离（保持克制的关键决策）

**规则：动效预算是有限的资源。在正确的地方花大钱，在其他地方不花。**

| 层面 | 动效预算 | 举例 |
|---|---|---|
| **静态内容**（文章、列表、面板） | **极小**：悬浮抬升、脉冲点、分段滑动 | 卡片 hover 抬升 3px，0.2s |
| **交互层**（对话框、面板、弹出框、抽屉） | **完整流体处理**（见下方） | 面板从底部升起，弹簧缓动，可中断 |
| **装饰性元素** | **无** | 不做入场动画、不做背景动画 |

**关键规则：异步渲染的内容不做透明度淡入关键帧。** 一个重新渲染可能把元素卡在 `opacity: 0`。直接渲染它。

### 10.3 响应 —— 消除延迟

> "当延迟出现时，直接感会'坠下悬崖'。"—— WWDC 2018

**规则：反馈在指针按下时发生，不是在释放时。**

```css
/* 正确的反馈时机：按下即发生 */
.button:active {
  transform: scale(0.97);
  transition: transform 100ms ease-out;
}
```

**审计清单：**
- [ ] 是否有去抖延迟了响应？视觉反馈不应去抖
- [ ] 是否有人为的定时器？移除
- [ ] 是否有 `transition-delay`？交互元素不应有
- [ ] 移动端是否有 300ms 点击延迟？使用 `touch-action: manipulation` 或 Pointer Events

### 10.4 直接操控 —— 1:1 追踪

> "触摸和内容应该一起移动。"—— WWDC 2018

**规则：当用户拖拽某物时，它必须粘在手指上，并且尊重用户抓取时的偏移量。**

```js
element.addEventListener('pointerdown', (e) => {
  element.setPointerCapture(e.pointerId);
  const rect = element.getBoundingClientRect();
  const grabOffsetX = e.clientX - rect.left;
  const grabOffsetY = e.clientY - rect.top;
  let velocityHistory = [];

  function onPointerMove(e) {
    const dx = e.clientX - rect.left - grabOffsetX;
    const dy = e.clientY - rect.top - grabOffsetY;
    element.style.transform = `translate(${dx}px, ${dy}px)`;
  }

  function onPointerUp(e) {
    element.removeEventListener('pointermove', onPointerMove);
    element.removeEventListener('pointerup', onPointerUp);
    const releaseVelocity = calculateVelocity(velocityHistory);
    animateSpringTo(element, targetPosition, releaseVelocity);
  }

  element.addEventListener('pointermove', onPointerMove);
  element.addEventListener('pointerup', onPointerUp);
});
```

### 10.5 中断性 —— 最重要的原则

> "思想和手势是同时发生的。"—— WWDC 2018

**这是单条最重要的交互原则。** 每个动画都必须在任何时刻可中断和可重定向。

1. **永远不要在过渡期间锁定输入。** 正在关闭的模态框，如果用户又抓住它了，应该立即跟随手指。
2. **总是从当前屏幕值开始动画，不是从目标值开始。**

```js
// 错误：从中断时的目标值开始（跳帧）
element.animate([
  { transform: `translateY(0px)` },      // ← 元素可能在 300px 的位置！
  { transform: `translateY(-500px)` }
], { duration: 400 });

// 正确：从当前屏幕值开始
const currentTransform = getComputedStyle(element).transform;
element.animate([
  { transform: currentTransform },         // ← 从实时位置开始
  { transform: `translateY(-500px)` }
], { duration: 400 });
```

3. **避免在手势驱动的内容中使用 CSS `@keyframes`。** CSS transitions 在 `transform`/`opacity` 上是可中断的（从当前值重新定位），但 `@keyframes` 不是。
4. **手势反转时，混合速度，不要硬切。** 反转点替换动画会造成"砖墙"效果。

### 10.6 使用弹簧（行为优于动画）

> "把动画想象成你和对象之间的对话，而不是界面预设的脚本。"—— WWDC 2018

**为什么弹簧优于固定时长动画：**

| 特性 | 固定时长动画 | 弹簧（Spring） |
|---|---|---|
| 可中断性 | ❌ 需要额外逻辑 | ✅ 天生支持（接受新目标即可） |
| 速度感知 | ❌ 固定速度曲线 | ✅ 物理真实的速度变化 |
| 过冲控制 | ❌ 需要手动 bounce 曲线 | ✅ 通过 damping 参数自然控制 |
| 真实感 | ❌ 可能感觉"假" | ✅ 模拟物理，感觉自然 |

**Apple 的两个参数：**

1. **Damping Ratio（阻尼比）** —— 控制过冲
   - `1.0` = 临界阻尼：无过冲，平滑收敛
   - `0.8` = 轻微过冲：略过目标再回来
   - `0` = 无阻尼：永远振荡

2. **Response（响应时间）** —— 速度感（单位：秒）
   - `0.2` = 极快
   - `0.4` = 正常 UI 速度
   - `0.8` = 慢速优雅
   - **注意：这不是"时长"** —— 弹簧没有固定时长

**弹簧参数速查表：**

| 交互场景 | Damping | Response | 效果 |
|---|---|---|---|
| 默认 UI 入场 | `1.0` | `0.3–0.4` | 平滑进入，安静专业 |
| 抽屉/面板 | `0.8` | `0.3` | 略弹跳，感觉有重量 |
| 移动/重新定位 | `1.0` | `0.4` | 精确到位，不晃动 |
| 旋转 | `0.8` | `0.4` | 轻微弹跳，物理感 |
| 动量释放 | `0.8` | `0.3–0.4` | 只在手势携带动量时弹跳 |

**铁律：只有手势携带动量时才用弹跳（damping < 1.0）。**

**CSS 近似：**

```css
:root {
  --ease-spring: cubic-bezier(0.32, 0.72, 0, 1);
  --ease-out-quart: cubic-bezier(0.25, 1, 0.5, 1);
}
```

**JS 弹簧（Motion / Framer Motion）：**

```js
import { animate } from 'motion';

// 临界阻尼
animate(el, { opacity: 1, y: 0 }, {
  type: 'spring', bounce: 0, duration: 0.4
});

// 动量交互
animate(el, { y: targetPosition }, {
  type: 'spring', bounce: 0.2, duration: 0.4,
  velocity: releaseVelocity
});
```

### 弹簧参数调优指南

在实际项目中调整弹簧参数时，使用以下系统化方法：

**第一步：确定场景类型**
- 场景是"入场/出现"还是"手势释放"？
- 入场场景：damping 总是 1.0（临界阻尼），不过冲
- 手势释放场景：damping 取决于手势是否有动量（轻弹 → 0.8，慢拖 → 1.0）

**第二步：确定响应时间**
- 元素越小/越近 → response 越小（越快）
- 元素越大/越远 → response 越大（越慢）
- 参考：按钮 0.2–0.3，面板 0.3–0.4，全屏过渡 0.4–0.5

**第三步：视觉验证**
- 动效是否太快看不见？增加 response
- 动效是否太慢显得迟钝？减少 response
- 过冲是否分散注意力？增加 damping（向 1.0 靠拢）
- 没有弹跳是否感觉死板？减少 damping（向 0.6–0.8 靠拢），但仅在手势有动量时

**典型参数组合：**

```js
// 快速按钮反馈（按压缩放）
animate(button, { scale: 0.95 }, {
  type: 'spring', bounce: 0, duration: 0.15
});

// 面板从底部升起
animate(panel, { y: [300, 0] }, {
  type: 'spring', bounce: 0.1, duration: 0.4
});

// 轻弹后归位（有速度）
animate(card, { x: 0 }, {
  type: 'spring', bounce: 0.2, duration: 0.4,
  velocity: fingerVelocity
});

// 页面过渡
animate(page, { opacity: [0, 1], x: [40, 0] }, {
  type: 'spring', bounce: 0, duration: 0.45
});
```

### 10.7 速度交接

释放前手指速度 500px/s → 释放后动画继续从 500px/s 开始，不是从 0。

```js
function animateSpringTo(element, target, velocity) {
  animate(element, { y: target }, {
    type: 'spring', bounce: 0, duration: 0.4,
    velocity: velocity
  });
}
```

### 10.8 动量投影

```js
function project(velocity, decelerationRate = 0.998) {
  return (velocity / 1000) * decelerationRate / (1 - decelerationRate);
}

const projectedEndpoint = currentPosition + project(releaseVelocity);
const target = findNearestSnapPoint(projectedEndpoint);
animateSpringTo(element, target, releaseVelocity);
```

**注意：** `v²/(2*decel)` 不是 Apple 使用的公式。使用上述指数衰减形式。

### 10.9 空间一致性

1. **相同路径进入和退出。** 从底部来，回底部去。
2. **锚定到触发来源。** 弹出框从触发它的元素处生长出来。
3. **可逆过渡镜像缓动曲线。**

```css
.sheet {
  transform: translateY(100%);
  transition: transform 0.4s var(--ease-spring);
}
.sheet.open { transform: translateY(0); }
/* 退出时自动沿相同路径 */
```

### 10.10 沿手势方向提示

让 `transform-origin` 动态设置为手势起始点。从右下角滑动 → `transform-origin: bottom right`。

### 10.11 橡皮筋效应

```js
function rubberband(overshoot, dimension, constant = 0.55) {
  return (overshoot * dimension * constant) / (dimension + constant * Math.abs(overshoot));
}
```

### 10.12 帧级流畅度

- 只动画 `transform` 和 `opacity`（合成器属性）
- `will-change` 在运动即将发生时设置，结束后移除
- `requestAnimationFrame` 是 Web 的显示同步时钟
- 不要在 rAF 循环中读取 `offsetTop`、`offsetLeft` 等布局属性

---

## 11. 交互层运动系统

> 来自 naplesblue（改编自 emilkowalski）。适用于对话框、面板、弹出框、抽屉。

### 11.1 物化效果

```css
.modal-overlay {
  position: fixed; inset: 0;
  background: rgba(0, 0, 0, 0.28);
  opacity: 0; pointer-events: none;
  transition: opacity 0.25s ease;
  z-index: 60;
}
.modal-overlay.open { opacity: 1; pointer-events: auto; }

.modal-surface {
  position: fixed; top: 50%; left: 50%;
  transform: translate(-50%, -50%) scale(0.95);
  opacity: 0;
  transition: opacity 0.4s var(--ease-spring), transform 0.4s var(--ease-spring);
  z-index: 61;
}
.modal-surface.open {
  opacity: 1; transform: translate(-50%, -50%) scale(1);
}
```

### 11.2 弹簧参数选择

| 场景 | Damping | Response | 入场 | 退出 |
|---|---|---|---|---|
| 模态对话框 | 1.0 | 0.35–0.4 | ~400ms | ~250ms |
| 底部面板 | 0.8 | 0.3 | ~350ms | ~250ms |
| 上下文菜单 | 1.0 | 0.3 | ~300ms | ~200ms |
| 提示（toast） | 1.0 | 0.3 | ~300ms | ~200ms |
| 页面过渡 | 0.8 | 0.35 | ~450ms | ~300ms |

### 11.3 中断性在 CSS 中的实现

CSS transitions 在 `transform` 和 `opacity` 上是天生可中断的——如果你在动画进行中改变属性值，浏览器自动从当前值过渡到新值。

```css
.panel {
  transform: translateX(100%);
  transition: transform 0.3s var(--ease-spring);
}
.panel.open { transform: translateX(0); }

/* 如果在关闭过程中重新点击，transition 自动从当前值（如 30%）过渡到 0% */
```

**`@keyframes` 不可用于可中断动画**——它们跳到关键帧定义位置。

---

## 12. 手势设计

### 12.1 Tap（点击）

| 属性 | 规则 |
|---|---|
| 高亮时机 | 触摸**按下**时（`pointerdown`），即时 |
| 提交时机 | 触摸**抬起**时（`pointerup`） |
| 取消方式 | 手指拖离目标再抬起 |
| 迟滞阈值 | ~10px |
| 点击区域 | ≥ 44px |

```js
button.addEventListener('pointerdown', () => {
  button.classList.add('pressed');
});
button.addEventListener('pointerup', (e) => {
  button.classList.remove('pressed');
  const rect = button.getBoundingClientRect();
  if (e.clientX >= rect.left && e.clientX <= rect.right &&
      e.clientY >= rect.top && e.clientY <= rect.bottom) {
    handleClick();
  }
});
button.addEventListener('pointerleave', () => {
  button.classList.remove('pressed');
});
```

### 12.2 为什么手势需要物理模拟

人的手指不是完美的输入设备。手指的运动有抖动、有加速减速、有细微的无意识移动。好的手势设计不是"精确跟随手指"这么简单——它需要：

1. **过滤噪声** —— 用户在尝试点击时手指有 ~1-3px 的微抖动，需要用迟滞忽略
2. **放大意图** —— 用户快速轻弹时，他们希望内容走得更远（动量投影）
3. **物理反馈** —— 拉到边界时用户期待"撞到墙"的阻力感（橡皮筋效应）
4. **可逆性** —— 用户在滑动过程中改变主意应该被尊重（中断性）

### 12.3 Drag/Swipe（拖拽/滑动）

| 属性 | 规则 |
|---|---|
| 方向锁定迟滞 | ~10px 移动后才锁定方向 |
| 追踪 | 1:1 追踪，尊重偏移 |
| 数据收集 | 最近 100ms 位置/时间历史 |

```js
let startX, startY, isDragging = false, direction;

element.addEventListener('pointerdown', (e) => {
  startX = e.clientX; startY = e.clientY;
  isDragging = false; direction = null;
});

element.addEventListener('pointermove', (e) => {
  const dx = e.clientX - startX;
  const dy = e.clientY - startY;
  const distance = Math.sqrt(dx * dx + dy * dy);

  if (!isDragging && distance > 10) {
    isDragging = true;
    direction = Math.abs(dx) > Math.abs(dy) ? 'horizontal' : 'vertical';
  }

  if (isDragging) {
    element.style.transform = direction === 'horizontal'
      ? `translateX(${dx}px)`
      : `translateY(${dy}px)`;
  }
});
```

### 12.4 并行手势识别

从第一次移动就并行检测所有可能的手势，意图明确后自信地取消输家。避免只报告最终状态的事件（如 `swipeleft`）。

### 12.5 最小化消歧延迟

只在确实有双击功能时付出 300ms 的延迟代价。

---

## 13. 减少动效与无障碍

### 13.1 为什么要为减少动效单独设计

减少动效不是"关掉动画"那么简单。前庭系统障碍（vestibular disorders）用户在看到滑动、缩放、视差动效时可能出现头晕、恶心甚至呕吐。为他们"关掉动画"确实解决了这个问题，但代价是失去了所有视觉反馈——连按钮按下、状态变化这种有意义的信息都没有了。

**正确的方式：替换，不是移除。**

- 滑动替换为交叉淡入 → 仍然传达"内容变了"
- 缩放替换为透明度变化 → 仍然传达"新元素出现了"
- 视差替换为静态层 → 仍然传达"前景和背景"
- 弹簧过冲替换为平滑收敛 → 仍然传达"到位了"

**三个独立信号：**
Apple 提供了三个独立的媒体查询，分别对应三种不同的无障碍需求。它们可能同时启用（例如一个用户可能同时需要减少动效和增加对比度），也可能只启用其中一个。必须全部独立处理。

### 13.2 三条媒体查询（全部必须处理）

**信号 1：`prefers-reduced-motion: reduce`**

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
  .sheet { transition: opacity 200ms ease; transform: none !important; }
}
```

**信号 2：`prefers-reduced-transparency: reduce`**（约 6% 用户启用）

这个信号处理玻璃/毛玻璃效果。对于某些用户（尤其是在低性能设备或需要高对比度的场景中），`backdrop-filter` 会导致可读性下降或性能问题。

```css
@media (prefers-reduced-transparency: reduce) {
  .glass, .glass-nav, .tabbar {
    background: #ffffff;
    backdrop-filter: none;
  }
  .scrim { background: rgba(0,0,0,0.5); }
}
```

**信号 3：`prefers-contrast: more`**（约 4% 用户启用）

当用户需要更高对比度时，设计系统中原本"优雅柔和"的颜色对比可能不足以满足可读性需求。

```css
@media (prefers-contrast: more) {
  .glass, .glass-nav, .tabbar {
    background: #ffffff;
    border: 1px solid rgba(0,0,0,0.35);
  }
  .hairline { border-top-color: rgba(0,0,0,0.2); }
  .text-2 { color: #1d1d1f; }
}
```

### 13.3 减少动效的设计决策表

| 动效类型 | 原始效果 | 减少动效后 | 是否能保留动效传递信息 |
|---|---|---|---|
| 面板升起 | `translateY(100%) → 0` + `0.4s ease-spring` | `opacity: 0 → 1` + `200ms ease` | ✅ 仍表明面板出现了 |
| 卡片悬浮抬升 | `translateY(-3px)` + `0.2s ease` | **完全保留**（不引起前庭反应） | ✅ 极小的尺寸变化 |
| 列表滑动进入 | `translateX(40px) → 0` + stagger | **移除** | ❌ 装饰性，不承载信息 |
| 视差滚动 | 背景层不同速度 | 静态背景 | ✅ 内容仍在，层次被简化 |
| 弹簧过冲 | damping 0.8 + response 0.4 | 临界阻尼 1.0 + 更短 | ✅ 仍传达"到位了" |
| 圆形脉冲 | `scale(1) → 1.2 → 1` 循环 | `opacity: 1 → 0.4 → 1` 循环 | ✅ 仍传达"在线" |

### 无障碍实施清单

并非 UI 的每个部分都需要相同的无障碍水平。按以下优先级处理：

| 优先级 | 元素 | 必须处理 | 建议处理 |
|---|---|---|---|
| P0 | 交互层（模态、面板、弹出框） | 三条媒体查询全部 | 减少动效下的替代动效 |
| P0 | 导航和 Tab 栏 | 减少透明度、增加对比度 | 减少动效 |
| P1 | 卡片网格、列表 | 减少动效 | 增加对比度 |
| P1 | 装饰元素（背景动画） | 直接移除 | — |
| P2 | 脉冲点、加载指示器 | 减少动效 | — |

### 13.5 其他无障碍规则

- 无全视口移动背景
- 无慢循环振荡（~0.2Hz / 每 5s）
- 无突然的亮度跳跃
- 大面积移动物体半透明化
- 大表面重新定位时淡出→移动→淡入

---

## 14. 多模态反馈

> 三条规则，**适度使用**——过度反馈会训练用户忽略一切。

**1. 因果性：** 反馈必须与原因明确关联，在因果事件时触发。

**2. 和谐性：** 视觉、声音和触觉必须在**同一帧**触发。它们之间的延迟破坏"同一事件"的错觉。

```js
element.addEventListener('click', () => {
  element.style.transform = 'scale(0.95)';
  requestAnimationFrame(() => {
    navigator.vibrate(10);
  });
});
```

**3. 效用性：** 只在值得的地方添加反馈——成功、错误、提交、归位。日常操作不需要。

---

## 15. 组件库

> 完整粘贴就绪的代码见 `components.md`，渲染效果见 `reference.html`。

### 15.1 统一面板列表（最重要的组件）

```html
<div style="background:var(--surface); border-radius:var(--r-panel);
            box-shadow:var(--sh-panel); overflow:hidden;">
  <a class="row" href="#" style="display:block; padding:16px clamp(17px,3vw,24px);
       color:var(--text); text-decoration:none;">
    <div style="display:flex; align-items:center; gap:12px;">
      <svg class="ic-row" viewBox="0 0 24 24" width="22" height="22" fill="none"
           stroke="currentColor" stroke-width="1.75" stroke-linecap="round"
           stroke-linejoin="round" style="color:var(--text-3); flex:none;">
        <rect x="3" y="6" width="18" height="13" rx="2.5"/>
        <path d="M3 10.5h18"/><circle cx="17" cy="14.5" r="1.25"/>
      </svg>
      <div style="flex:1; min-width:0;">
        <h3 style="font-size:17px; font-weight:600; letter-spacing:-0.01em;
                   line-height:1.45; margin:0;">钱包</h3>
        <p style="margin:4px 0 0; font-size:13.5px; color:var(--text-2);
                   white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
          Apple Pay · 信用卡 · 借记卡
        </p>
      </div>
      <svg viewBox="0 0 24 24" width="18" height="18" fill="none"
           stroke="currentColor" stroke-width="1.75" style="color:var(--faint); flex:none;">
        <path d="M9 6l6 6-6 6"/>
      </svg>
    </div>
  </a>
  <a class="row" href="#" style="display:block; padding:16px clamp(17px,3vw,24px);
       color:var(--text); text-decoration:none; border-top:1px solid var(--hairline);">
    <!-- 下一行 -->
  </a>
</div>

<style>
.row { transition: background 0.15s ease; }
.row:hover { background: var(--hover); }
.row + .row { border-top: 1px solid var(--hairline); }
</style>
```

### 15.2 标准卡片网格

```html
<div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(290px, 1fr));
            gap:14px; max-width:var(--max-grid); margin:0 auto; padding:0 var(--pad-x);">
  <a class="card" href="#" style="background:var(--surface); border-radius:var(--r-card);
       box-shadow:var(--sh-card); padding:18px; color:var(--text); text-decoration:none; display:block;">
    <div style="width:100%; height:140px; background:linear-gradient(135deg,#0a84ff,#5e5ce6);
                border-radius:var(--r-thumb); margin-bottom:14px;"></div>
    <h3 style="font-size:17px; font-weight:600; letter-spacing:-0.01em;
               line-height:1.45; margin:0;">卡片标题</h3>
    <p style="margin:6px 0 0; font-size:13.5px; color:var(--text-2); line-height:1.5;">
      一段简短的摘要描述。
    </p>
  </a>
</div>
<style>
.card { transition: transform 0.2s var(--ease-out-quart), box-shadow 0.2s var(--ease-out-quart); }
.card:hover { transform: translateY(-3px); box-shadow: var(--sh-lift); }
</style>
```

### 15.3 分段胶囊控件

```html
<div class="segmented" style="display:inline-flex; background:rgba(0,0,0,0.05);
     border-radius:var(--r-pill); padding:3px; gap:2px;">
  <button class="seg" data-value="list">列表</button>
  <button class="seg active" data-value="grid">网格</button>
  <button class="seg" data-value="focus">聚焦</button>
</div>

<style>
.seg {
  border:none; cursor:pointer; font-size:13px; font-weight:500;
  padding:7px 15px; border-radius:var(--r-pill);
  background:transparent; color:var(--text-2);
  transition:all 0.25s cubic-bezier(.25,.1,.25,1);
}
.seg.active {
  background:var(--surface); color:var(--text); font-weight:600;
  box-shadow:0 1px 3px rgba(0,0,0,0.12);
}
.seg:hover { color:var(--text); }
</style>

<script>
document.querySelector('.segmented').addEventListener('click', (e) => {
  const btn = e.target.closest('.seg');
  if (!btn) return;
  document.querySelectorAll('.seg').forEach(s => s.classList.remove('active'));
  btn.classList.add('active');
});
</script>
```

### 15.4 按钮

```html
<!-- 主要按钮 -->
<a class="btn-primary" href="#"
   style="display:inline-flex; align-items:center; height:44px; padding:0 22px;
          border-radius:var(--r-pill); background:var(--accent); color:#fff;
          font-size:15px; font-weight:600; text-decoration:none; gap:8px;
          transition:background 0.2s, transform 0.1s;">
  继续 →
</a>

<!-- 次要按钮 -->
<a class="btn-secondary" href="#"
   style="display:inline-flex; align-items:center; height:44px; padding:0 19px;
          border-radius:var(--r-pill); background:rgba(255,255,255,0.8);
          border:1px solid rgba(0,0,0,0.08); box-shadow:0 1px 2px rgba(0,0,0,0.05);
          color:var(--text); font-size:14px; font-weight:550; text-decoration:none;
          transition:background 0.2s, transform 0.1s;">
  取消
</a>

<style>
.btn-primary:hover { background: var(--accent-hover); }
.btn-primary:active, .btn-secondary:active { transform: scale(0.97); }
.btn-secondary:hover { background: rgba(255,255,255,0.95); }
</style>
```

### 15.5 标签/Chip

```html
<!-- 平台标签（mono，纯色背景） -->
<span style="font-family:var(--mono); font-size:10.5px; font-weight:700; color:#fff;
            background:var(--x-blue); padding:2px 7px; border-radius:var(--r-chip);">X</span>

<!-- 普通标签（灰色背景） -->
<span style="font-size:11.5px; color:var(--text-2); background:rgba(0,0,0,0.05);
            padding:3px 10px; border-radius:var(--r-pill);">一般标签</span>

<!-- 强调标签（蓝色） -->
<span style="font-size:11.5px; color:var(--accent); background:rgba(0,113,227,0.08);
            padding:3px 10px; border-radius:var(--r-pill); font-weight:550;">精选</span>

<!-- 热度标签（橙色） -->
<span style="font-size:11.5px; font-weight:650; color:var(--heat); background:var(--heat-bg);
            padding:3px 10px; border-radius:var(--r-pill);">🔥 最热</span>

<!-- 在线标签（绿色，脉冲） -->
<span style="display:inline-flex; align-items:center; gap:5px; font-size:11.5px;
            font-weight:600; color:var(--live); padding:3px 10px;">
  <span style="width:7px; height:7px; border-radius:50%; background:var(--live);
               animation:pulse-dot 2.2s ease infinite;"></span>
  LIVE
</span>

<style>
@keyframes pulse-dot {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.4; }
}
</style>
```

### 15.6 彩色 CTA + 液态玻璃

```html
<section style="position:relative; overflow:hidden; border-radius:var(--r-hero);
                padding:clamp(26px,4vw,40px); background:var(--grad-cta);
                box-shadow:var(--sh-cta);">
  <div style="position:absolute; width:260px; height:260px; border-radius:50%;
              background:rgba(255,255,255,0.18); filter:blur(46px);
              top:-80px; right:-40px; pointer-events:none;"></div>
  <div style="position:absolute; width:200px; height:200px; border-radius:50%;
              background:rgba(120,80,255,0.5); filter:blur(50px);
              bottom:-90px; left:12%; pointer-events:none;"></div>
  <div style="position:relative;">
    <h2 style="font-size:clamp(18px,3vw,24px); font-weight:700; color:#fff;
               letter-spacing:-0.02em;">CTA 标题</h2>
    <p style="margin-top:10px; font-size:14px; color:rgba(255,255,255,0.82);
              line-height:1.6; max-width:460px;">支持行。</p>
    <div style="display:flex; gap:10px; margin-top:20px; flex-wrap:wrap;">
      <a style="display:inline-flex; align-items:center; height:42px; padding:0 18px;
                border-radius:var(--r-pill); color:#fff; font-size:13.5px; font-weight:550;
                text-decoration:none; background:rgba(255,255,255,0.16);
                border:1px solid rgba(255,255,255,0.22);
                backdrop-filter:blur(8px);">玻璃按钮</a>
    </div>
  </div>
</section>
```

---

## 16. 页面模式与决策树

> 完整内容见 `patterns.md`。

### 16.1 容器选择

| 容器 | `max-width` | 适用场景 |
|---|---|---|
| 阅读列 | 720px | 文章、详情页、表单/设置 |
| 网格/密集列 | 1080px | 首页、索引/归档、仪表盘 |

共同点：居中，侧边距 22px，区块间距 `clamp(34px, 6vw, 56px)`。

### 页面节奏与布局策略

Apple 的页面布局遵循一种可预测的节奏，类似于音乐中的小节：

**节奏模式：**
1. **进入（Enter）** —— 英雄区映入眼帘，大标题和导语快速传达页面目的
2. **浏览（Scan）** —— 用户扫视内容，寻找感兴趣的部分
3. **深入（Dive）** —— 用户点击进入具体内容，面板出现或页面滚动
4. **退出（Exit）** —— 用户完成阅读或操作，返回上级或离开

**布局策略：**
- 英雄区占视口高度的 40–60%，足以建立上下文但不需要"折叠线以下"的压迫感
- 分区间距 `--sec-gap` 确保每个内容块有视觉呼吸空间
- 图片和文字交替出现，避免文字墙
- 每个布局决策都要有理由——"因为 600px 看起来差不多"不够好，使用精确 Token

### 16.2 页面原型

#### A. 详情/阅读页
```
[玻璃导航 · 返回按钮]
[英雄区: 眼部 · H1（负字间距）· 导语]
[正文: 平坦散文 —— 无卡片包装；行高 ≥ 1.85]
[元信息/来源行: 上方发丝线；署名 · 日期 · "阅读原文" · 分享]
[回到顶部 / 相关推荐 —— 克制]
```

关键：正文是**一个连续的阅读表面**——不框在卡片中。

#### B. 索引/列表页
```
[玻璃导航]
[英雄区: 章节标题 · 一行描述]
[统一面板列表，分组 → 组标签 + 发丝分隔行的面板]
["查看全部 →" 链接，安静]
```

关键：**统一面板 + 发丝线**，按日期/类别分组。

#### C. 主页/仪表盘
```
[玻璃导航 · 日期 · 操作按钮]
[英雄区: 在线眼部 · H1 · 统计行（tabular-nums）]
[封面/聚焦区块（可选）]
[主要信息流: 统一列表 —— 带分段控件切换 统一/网格/聚焦]
[次要区域: 卡片或面板]
[彩色 CTA 区块（玻璃 + 光晕）]
[订阅 / 页脚]
```

关键：主要信息流默认**统一列表**；分段控件切换模式，不三种同时显示。

#### D. 表单/设置
```
[分组面板 —— 每组 = 一块白色面板的设置行]
[行 = 标签左对齐，控件右对齐；行间发丝线；面板上方组标签]
```

### 16.3 决策树

**决策树 1：统一面板 vs 卡片网格**
```
├─ 同级行、可扫读、主要是文本 → 统一面板 + 发丝线（default）
├─ 真正独立的对象，各有图片/缩略图 → 卡片网格
└─ 不确定 → 统一面板（碎片化是更大的罪过）
```

**决策树 2：玻璃 vs 实色**
```
├─ 层叠处有重叠 → 玻璃
└─ 平面内容在页面底色上 → 实色 #fff + 柔和阴影
```

**决策树 3：彩色 vs 灰度**
```
├─ 强调色/热度/品牌/在线 → 用那个 Token
├─ 渐变 → 仅限英雄区/CTA/占位图
└─ 否则 → 灰度（字重 + 字号承载层次）
单个视图中两个强调色竞争 = 错误。每视图一个。
```

**决策树 4：添加 vs 移除**
```
├─ 承载用户需要的含义？ → 保留
└─ 存在是为了"看起来丰富/有设计感"？ → 移除
```

### 16.4 响应式

- 一次构建，使用 `clamp()`
- 断点 ~`680px`：双列→单列，隐藏次要信息，更紧凑默认

```css
@media (max-width: 680px) {
  .ds-2col { grid-template-columns: 1fr; }
  .hide-sm { display: none; }
}
```

---

## 17. App / iOS 原型壳

> 完整内容见 `app.md`。

### 17.1 导航栏风格声明

此技能涵盖 Apple 移动端导航栏的主流风格体系。请读者在实现时注意区分和遵循：

| 风格 | Apple 官方术语 | 说明 |
|---|---|---|
| **液态玻璃导航栏** | Vibrancy Effect / Liquid Glass Navigation | 导航栏采用毛玻璃（`backdrop-filter`）处理，内容在下方滚动时玻璃产生折射和色彩适应效果。这是 iOS 标配导航风格 |
| **超薄材质** | Ultra-Thin Material | Apple 材质密度体系中最轻的一级，导航栏基材使用最高透明度——`rgba(255,255,255,0.6)` + `blur()`，使导航栏"存在但不沉重" |
| **视觉效果叠加** | Visual Effect View with Blending | 导航栏不是单一矩形，而是玻璃层叠加渐变背景（`linear-gradient(180deg, ...)`），形成边缘渐隐融合的复合表面 |
| **大标题导航** | Large Title Navigation Bar | iOS 标志性模式——大尺寸粗体标题（负字距）在静止状态展示，滚动后折叠为紧凑居中标题栏 |
| **可变工具栏** | Variable Toolbar | 根据滚动位置或上下文动态显隐/变容的工具栏，共享同套 Ultra-Thin Material + Vibrancy 处理 |

典型实现使用 `nav-bar` / `lg-nav` / `lg-glass` / `nav-glass` 等 class 组合来构建层级：外层容器提供 Vibrancy 背板，内侧渐变层模拟 Visual Effect View 混合，内容槽承载实际导航控件。

> **原则：** 导航栏适用玻璃处理——因为它属于"图层真实重叠"场景（内容在固定导航栏下方滚动）。玻璃底部以发丝线或滚动边缘渐隐结束，不出现硬边框。

### 17.2 铁律

**不要手绘设备框架。** 使用以下精确值（iPhone 15 Pro / 16 / 15 逻辑点）：

```
screen (points)      393 × 852
device corner radius 55       bezel (padding) 12
Dynamic Island       125 × 37 · top 11 · centered · radius 999
safe-area top        59       safe-area bottom 34
home indicator       139 × 5  · centered · bottom 8
nav bar compact      44       large-title expanded ~96
tab bar              49 + 34 safe = 83
```

### 17.2 大标题导航（滚动折叠）

```html
<header class="nav-c" id="navc"><span class="nav-c-t">钱包</span></header>
<div class="scroll" id="scroll">
  <h1 class="lt">钱包</h1>
  <!-- 内容 -->
</div>
```
```css
.nav-c{
  position:absolute; top:59px; left:0; right:0; height:44px; z-index:50;
  display:flex; align-items:center; justify-content:center;
  background:rgba(245,245,247,.72); backdrop-filter:saturate(180%) blur(20px);
  border-bottom:1px solid transparent;
  opacity:0; transition:opacity .25s, border-color .25s; pointer-events:none;
}
.nav-c.show{ opacity:1; border-bottom-color:var(--hairline); }
.nav-c-t{ font-size:16px; font-weight:600; letter-spacing:-0.01em; }
.lt{ padding:6px 20px 10px; font-size:34px; font-weight:700; letter-spacing:-0.02em; }
```
```js
const sc=document.getElementById('scroll'), nc=document.getElementById('navc');
sc.addEventListener('scroll',()=>nc.classList.toggle('show', sc.scrollTop>44),{passive:true});
```

### 17.3 Tab 栏

- 玻璃材质，安全区域底部（`padding-bottom: 34px`）
- **恰好一个**强调 Tab
- 真实线条图标（见 §18）

### 17.4 移动端特有规则

1. **触摸目标 ≥ 44px**
2. 无 `:hover` 作为唯一反馈——使用 `:active`（`transform: scale(.98)`）
3. 使用 `env(safe-area-inset-*)`
4. **不要在列表值上按状态着色**（收入绿/支出红 = 陷阱）
5. 彩色时刻是**单一元素**
6. 底部面板从边缘升起（抓取手柄，仅顶部圆角），主页指示条 `z-index: 80` 在覆盖层之上

---

## 18. 图标层

> 完整图标集见 `icons.md`（24 格栅 Lucide 线条图标策划合集）。

### 18.1 4 条铁律

1. **`currentColor`，默认灰度 —— 只操作/激活用强调色。**
2. **图标必须赢得位置。** 纯文本设置列表没有前置图标更干净。
3. **一种描边，一个格栅，一个 viewBox。** `viewBox="0 0 24 24"`，`stroke-width: 1.75`。
4. **图标尺寸 ≠ 触摸目标。** ≥ 44px 点击区域。

### 18.2 尺寸表

| 上下文 | px | 处理方式 |
|---|---|---|
| Tab 栏 | 26 | 线条 → 填充 + 强调色（激活时） |
| 导航/工具栏操作 | 22 | 线条，灰色 |
| 列表行前置 | 20–22 | 线条，灰色 |
| 内联/元信息 | 15–16 | 线条，灰色 |
| 按钮前置 | 17–18 | 线条，匹配按钮色 |

### 18.3 核心图标集

```
chevron-right   <path d="M9 6l6 6-6 6"/>
chevron-down    <path d="M6 9l6 6 6-6"/>
arrow-left      <path d="M19 12H5"/><path d="M12 19l-7-7 7-7"/>
plus            <path d="M12 5v14"/><path d="M5 12h14"/>
x               <path d="M18 6 6 18"/><path d="M6 6l12 12"/>
check           <path d="M5 12l5 5L20 6"/>
search          <circle cx="11" cy="11" r="7"/><path d="M21 21l-4.35-4.35"/>
bell            <path d="M6 9a6 6 0 0 1 12 0c0 6 2.5 8 2.5 8h-17S6 15 6 9"/><path d="M10.3 21a1.9 1.9 0 0 0 3.4 0"/>
user            <circle cx="12" cy="8" r="4"/><path d="M4 20a8 8 0 0 1 16 0"/>
home            <path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/>
credit-card     <rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M2.5 10h19"/>
wallet          <rect x="3" y="6" width="18" height="13" rx="2.5"/><path d="M3 10.5h18"/><circle cx="17" cy="14.5" r="1.25"/>
settings        <circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/>
share (iOS)     <path d="M12 3v12"/><path d="M8 7l4-4 4 4"/><path d="M6 12v6a1.5 1.5 0 0 0 1.5 1.5h9A1.5 1.5 0 0 0 18 18v-6"/>
trash           <path d="M4 7h16"/><path d="M9 7V5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2"/><path d="M6 7l1 13a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1l1-13"/>
```

### 18.4 图标 CSS

```css
.ic { color: var(--text-3); flex: none; }
.ic.on, .btn-primary .ic, a:active .ic { color: var(--accent); }
.tab .ic { color: var(--text-3); }
.tab.on .ic { color: var(--accent); }
```

### 18.5 图标自检

- [ ] 一种描边宽度 + 24 格栅
- [ ] 灰度 `currentColor`，只操作/激活用强调色
- [ ] 没有每行一个图标的装饰
- [ ] ≥ 44px 点击区域
- [ ] 真实线条图标——不是灰色方块，不是 emoji

---

## 19. 两种工作模式

### Build（构建）—— 制作新 UI

遵循 §20 的工作流。适合设计新页面、构建组件、创建 iOS 原型。

### Review（评审）—— 审计现有 UI

遵循 §21 的工作流。适合重构现有页面、团队设计评审、品牌一致性检查。

---

## 20. Build 模式工作流

### 步骤 1：阅读 `design-system.md`

完整的视觉规范——颜色、字体、间距、圆角、阴影、玻璃配方、组件、响应式。

### 步骤 2：放入 `tokens.css`

将 `:root` 自定义属性复制到项目中。通过 `var(--…)` 引用所有值。

### 步骤 3：选择页面配方（`patterns.md`）

- 选择容器：720px 阅读 / 1080px 网格
- 选择原型：详情 / 索引 / 主页 / 表单
- 运行决策树

### 步骤 4：从 `components.md` 组合

复制经过验证的片段——玻璃导航、统一面板列表、卡片网格、分段胶囊、标签、按钮、彩色 CTA。

### 步骤 5：如果是 App / iOS 屏幕 → 阅读 `app.md`

设备框架、大标题折叠导航、Tab 栏、底部面板、安全区域、触摸目标。

### 步骤 6：如果需要图标 → 阅读 `icons.md`

线条图标层，4 条铁律，24 格栅 Lucide。

### 步骤 7：如果 UI 有交互层 → 阅读 `motion.md`

流体运动处理：指针按下反馈、弹簧缓动、相同路径、物化、可中断性、三条减少媒体查询。

### 步骤 8：对照 `reference.html` 检查

你的输出必须看起来像属于同一页面。

### 步骤 9：运行检查

- 常规自查清单（§23）
- 如有交互层 → 运动自查（§24）
- 如是 App 屏幕 → App 自查（§25）

---

## 21. Review 模式工作流

> 完整版见 `review.md`。

### 步骤 1：找到真正的视觉表面

定位 CSS/模板/组件——不是内容生成器。

### 步骤 2：清点

读取目标文件，记录每个颜色、字体、圆角、阴影、边框、间距决策。

### 步骤 3：评分

对照 `design-system.md` 在底色/表面、颜色、字体、层级、圆角/阴影、玻璃使用、响应式上评分。

### 步骤 4：优先级排序

| 级别 | 描述 |
|---|---|
| **P0** | 直接破坏审美 |
| **P1** | 不一致/漂移 |
| **P2** | 打磨 |

### 步骤 5：映射修复

每个修复映射到 Token（`tokens.css`）和组件/模式。从不说 Token 已命名的原生值。

### 步骤 6：实施并验证

对照 `reference.html`，重新渲染并截图对比。

### 输出格式

```
目标文件: theme.css
设计杠杆: 单一 CSS 文件，修复它就修复了整个站点。

| Pri | 发现 | 现在值 | → Apple 值 |
|---|---|---|---|
| P0 | body 底色 | #f7f5f0（暖米色） | #f5f5f7 冷灰色 |
| P0 | 强调色 | #ff7d4d（暖橙） | #0071e3 Apple 蓝 |
| P0 | h2 左栏 | 4px solid orange | 移除；字重+字号承载 |
| P1 | 文本 | #333 | #1d1d1f / #6e6e73 |
| P1 | hr | 2px rgba(0,0,0,.1) | 1px rgba(0,0,0,.07) |
| P2 | 圆角 | 10px | --r-thumb 12px |

最高杠杆变更: 替换 --accent 色值和 body 背景色，覆盖 ~85% 外观。
```

---

## 22. 反模式清单（Anti-slop）

### 视觉反模式

| # | 反模式 | 正确做法 |
|---|---|---|
| 1 | ❌ 碎片卡片 | 一块面板 + 发丝线 |
| 2 | ❌ 到处玻璃 | 玻璃只用于导航/覆盖层/CTA |
| 3 | ❌ 颜色做装饰 | 灰白正文，一种强调色 |
| 4 | ❌ 通用字体 | 系统 SF/PingFang 栈 |
| 5 | ❌ 暖色底色 | 冷 #f5f5f7 |
| 6 | ❌ 紫渐变在白色英雄区 | 蓝紫或蓝渐变 |
| 7 | ❌ 硬黑边框 | 发丝线或阴影 |
| 8 | ❌ 单层硬阴影 | 双层阴影（紧贴+扩散） |
| 9 | ❌ Emoji 五彩纸屑 | emoji 只在信息性使用 |
| 10 | ❌ 填充话 | 自信、专业、简洁 |
| 11 | ❌ 均匀胆小间距 | 有意空白，区块呼吸 |
| 12 | ❌ 数据填充 | 只保留有意义的数字 |
| 13 | ❌ 固定字间距 | 大字负间距，小字正或零 |

### 交互反模式

| # | 反模式 | 正确做法 |
|---|---|---|
| 14 | ❌ 不可中断动画 | CSS transitions 或弹簧 |
| 15 | ❌ 过渡锁定输入 | 永远可中断 |
| 16 | ❌ 释放时反馈 | 按下时即时高亮 |
| 17 | ❌ 无速度交接 | 继承手指速度 |
| 18 | ❌ 入口透明度动画 | 直接渲染 |
| 19 | ❌ 方向混乱 | 相同路径进入/退出 |

### 图标反模式

| # | 反模式 | 正确做法 |
|---|---|---|
| 20 | ❌ 灰色方块图标 | 真实线条图标 |
| 21 | ❌ Emoji 当图标 | Lucide 线条图标 |
| 22 | ❌ 每行一个图标 | 只对对象类型行使用 |
| 23 | ❌ 多处彩色图标 | 灰度，仅激活用强调色 |

### App 反模式

| # | 反模式 | 正确做法 |
|---|---|---|
| 24 | ❌ 手绘设备框架 | app.md 精确规范 |
| 25 | ❌ 永久分割线 | 只在滚动后显示 |
| 26 | ❌ 不透明栏 | 玻璃栏，内容在其下滚动 |
| 27 | ❌ 列表值颜色 | 灰度数值 |
| 28 | ❌ 无安全区域 | `env(safe-area-inset-*)` |
| 29 | ❌ 彩色多 Tab | 一个 Tab 强调色 |

---

## 23. 自查清单

### 表面与布局
- [ ] 页面底色是 `#f5f5f7`（冷色调）
- [ ] 内容位于 `#fff` 表面上；容器居中，侧边距 22px
- [ ] 同级同类项使用**一块面板 + 发丝分隔线**
- [ ] 布局使用 flex/grid + `gap`
- [ ] 区块间距 `clamp(34px, 6vw, 56px)`

### 玻璃
- [ ] `backdrop-filter` 只出现在导航/覆盖层/CTA 上
- [ ] 纯内容区块是实色 `#fff` + 柔和阴影
- [ ] 彩色地面上的玻璃有模糊光晕
- [ ] 粘性导航有滚动边缘效果（`.scrolled` 类）

### 字体
- [ ] 系统字体栈，没有 Inter/Roboto
- [ ] 大字标题有**负字间距**
- [ ] 长文行高 ≥ 1.85
- [ ] 数字使用 `tabular-nums`
- [ ] CJK↔Latin 之间半角空格

### 颜色
- [ ] 正文世界是灰度；颜色只作为强调色/热度/品牌/在线
- [ ] 没有有色背景、彩色左栏、多色、渐变洗
- [ ] 单个视图中最多一种强调色

### 圆角与阴影
- [ ] 圆角来自命名层级，无 ad-hoc 值
- [ ] 阴影是双层，没有单层硬投影

### 动效与无障碍
- [ ] 悬浮 = 轻柔抬升（`translateY(-2~-3px)`），0.15–0.25s
- [ ] 异步渲染内容没有透明度淡入关键帧
- [ ] 触摸目标 ≥ 44px
- [ ] `prefers-reduced-motion`、`prefers-reduced-transparency`、`prefers-contrast` 全部处理

### 克制
- [ ] 移除了可避免的噪音（额外图标、装饰 emoji、填充话）
- [ ] 图标赢得位置

### 最终
- [ ] 看起来像属于 `reference.html` 的同一页面

---

## 24. 交互层运动自查

- [ ] 指针**按下**时给出反馈（`:active` scale），即时
- [ ] 进入/退出沿**相同路径**；`transform-origin` 锚定到触发器
- [ ] 缓动使用 `--ease-spring` / `--ease-out-quart`
- [ ] 入场 ~350–450ms，退出 ~250–300ms；**不过冲**除非手势携带动量
- [ ] 玻璃表面**物化**（不透明度+缩放+模糊一起）
- [ ] 过渡期间**从不锁定输入**；CSS transition 支持自动反转
- [ ] 只动画 `transform`/`opacity`
- [ ] 三条媒体查询全部存在

---

## 25. App 自查

- [ ] 设备框架来自精确规范（岛 125×37，top 11，居中）
- [ ] 主页指示条在所有覆盖层之上（`z-index: 80`）
- [ ] 大标题滚动时折叠为紧凑玻璃栏
- [ ] Tab 栏：玻璃，安全区域底部，恰好一个强调 Tab
- [ ] 触摸目标 ≥ 44px
- [ ] 交互反馈在 `:active`，不是仅 `:hover`
- [ ] 使用 `env(safe-area-inset-*)`
- [ ] 灰度 + 一种强调色——列表值不按状态着色
- [ ] 最多一个彩色英雄区

---

## 26. 运动物理快速参考

| 需求 | 技术 | 具体值 |
|---|---|---|
| 默认 UI 弹簧 | 临界阻尼，无过冲 | `damping 1.0`, `response 0.3–0.4` |
| 动量/轻弹弹簧 | 欠阻尼，略弹跳 | `damping ~0.8`, `response 0.3–0.4` |
| 手势 → 弹簧速度 | 传递释放速度 | `gestureVelocity / (target − current)` |
| 轻弹落点 | 投影动量 | `current + (v/1000)·d/(1−d)`, `d ≈ 0.998` |
| 干净中断 | 从呈现（实时）值开始 | 读取屏幕上的 transform |
| 避免反转"砖墙" | 通过重新定位携带速度 | 混合速度的弹簧 |
| 可逆过渡 | 镜像缓动曲线 | 反向 cubic-bézier |
| 决定反转 vs 提交 | 使用速度**符号** | 在释放时 |
| 1:1 拖拽 | Pointer Events + capture | 尊重抓取偏移 |
| 反馈 | 指针按下，持续 | 绝不只在结束时 |
| 边界 | 橡皮筋 | `(o·d·0.55)/(d+0.55·\|o\|)` |
| 半透明铬 | `backdrop-filter` | 内容在其下方滚动 |
| 减少动效 | 交叉淡入 | `@media (prefers-reduced-motion)` |

---

## 27. 排版快速参考

| 需求 | 规则 | 值 |
|---|---|---|
| 大字标题追踪 | 负字间距，与尺寸成正比 | H1: `-0.03em`, H2: `-0.02em`, H3: `-0.01em` |
| 长文行高 | ≥ 1.85 | `line-height: 1.85` |
| 小字追踪 | 略正 | 12px: `+0.02em` |
| 数字 | 等宽 | `font-variant-numeric: tabular-nums` |
| 光学尺寸 | 让系统处理 | `font-optical-sizing: auto` |
| 系统字体 | 默认使用 | `--font-stack` |
| CJK↔Latin 间距 | 半角空格 | "iPhone 17 Pro 号称" |

---

### Motion 与 Framer Motion 映射速查

在 Web 项目中，最常用的弹簧库是 Motion（原 Framer Motion）。以下是将 Apple 参数映射到 Motion API 的速查表：

```js
// Apple 参数 → Motion API
// Apple: damping 1.0, response 0.4
// Motion: { type: 'spring', bounce: 0, duration: 0.4 }
//
// Apple: damping 0.8, response 0.3
// Motion: { type: 'spring', bounce: 0.2, duration: 0.3 }
//
// Apple: damping 0.6 (有意的弹跳)
// Motion: { type: 'spring', bounce: 0.4, duration: 0.4 }

// Concretely:
const appleSpring = {
  type: 'spring',
  bounce: 0,         // = damping 1.0 (临界阻尼)
  duration: 0.4      // = response 0.4
};

const momentumSpring = {
  type: 'spring',
  bounce: 0.2,       // = damping 0.8
  duration: 0.4,
  velocity: releaseVelocity
};
```

**为什么 bounce 不是直接的 damping 映射？** Motion（以及原始的 Popmotion 弹簧）使用不同的参数化方式，bounce 大致对应 `1 - damping`。damping 0.8 → bounce 0.2。这不是精确转换（底层物理模型不同），但感觉上是等效的。

## 28. 处理流程与过程

> 来自 emilkowalski，源自 WWDC 设计流程。

### 28.1 交互原型优先

规则：交互式原型胜过一百万个静态设计。

- 在最终代码前先构建可交互演示
- 使用 Motion/Framer Motion 的 spring 预设
- 在浏览器中调整弹簧参数

### 28.2 交互和视觉一起设计

> "你不应该能分辨出哪里是一个的结束和另一个的开始。"

在组件设计阶段就考虑运动。

### 28.3 真实环境测试

- 在真实设备上测试
- 用慢动作/逐帧回放检查动效
- 测试不同类型的用户

### 28.4 设计实施清单

| 阶段 | 工作 | 产出 |
|---|---|---|
| 规划 | 确定页面原型，运行决策树 | 结构草图 |
| 构建 | 放入 tokens.css，组合组件 | 功能实现 |
| 动效 | 为交互层添加流体处理 | 流畅交互 |
| 检查 | 运行自查 | 确认清单 |
| 验证 | 对照 reference.html 视觉对比 | 一致性确认 |

---

## 29. 本技能文件结构

```
moli-apple-design/
├── SKILL.md              ← 本文件：切入点 —— 哲学、工作流、反模式清单、自查
├── design-system.md      ← 完整规范：颜色、字体尺标、间距/圆角/阴影层级、玻璃配方
├── tokens.css            ← :root 自定义属性 —— 放入任何项目
├── components.md         ← 粘贴就绪的 HTML+CSS 组件
├── patterns.md           ← 页面级配方 + 决策树
├── motion.md             ← 流体交互层：弹簧、可中断性、物化、手势物理
├── app.md                ← App / iOS 壳层：设备框架、状态栏、大标题导航、Tab 栏
├── icons.md              ← 线条图标层：Lucide 内联 SVG 集（24 格栅）
├── review.md             ← 评审模式审计工作流
├── checklist.md          ← 独立的"完成"关卡
└── reference.html        ← 渲染的活体样式指南 —— 视觉基准

文件依赖关系：
  SKILL.md → 入口，引用所有其他文件
  design-system.md → tokens.css, components.md
  components.md → tokens.css
  patterns.md → components.md, design-system.md
  motion.md → tokens.css
  app.md → components.md, icons.md, motion.md
  icons.md → tokens.css
  review.md → design-system.md, checklist.md
  reference.html → 所有 CSS Token，所有组件
```

> **可移植性：** 这些文件假设**无框架**。在 React/Vue/等中，将 CSS 翻译到你的样式系统，但保持**精确的** Token 值、面板非卡片模式和玻璃只在重叠处的规则。

> **适用范围：**
> - ✅ 构建 Apple 风格的 Web 页面/组件
> - ✅ iOS/App 原型（配合 app.md）
> - ✅ 设计评审与重构
> - ❌ 非 Apple 风格的任务（游戏界面、创意品牌、暗黑设计）

---

*集成来源：naplesblue/apple-design-skill（液态玻璃视觉系统，MIT）& emilkowalski/skills apple-design（WWDC 交互哲学，MIT）。*
