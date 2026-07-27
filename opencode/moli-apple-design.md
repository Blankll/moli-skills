---
name: moli-apple-design
description: Apple 设计语言 — 构建 Apple 风格页面/组件、iOS 原型、设计评审。结合液态玻璃视觉系统（灰白底、统一白色表面、克制玻璃）与流体交互哲学（弹簧动效、手势物理、中断响应）。用户提到"苹果风"、"Apple 设计"、"液态玻璃"、"iOS原型"、"Apple风格UI"时使用。
license: Apache-2.0
compatibility: opencode
metadata:
  author: Integrated from naplesblue/apple-design-skill & emilkowalski/skills apple-design
  version: "1.0.0"
  category: design
---

# moli-apple-design

完整工作流见 `instructions/moli-apple-design.md`，读取后按步骤执行。

## 工作流

1. **理解设计需求** — 确认是新构建还是现有设计评审
2. **加载视觉系统** — 应用 tokens.css、组件、模式
3. **流体交互处理** — 若含交互层，应用弹簧动效、材质化、可中断性
4. **iOS 屏幕处理** — 使用 app.md 移动端外壳配合 Lucide 线性图标
5. **最终检查** — 对照 reference.html 运行 checklist

## 安装

```bash
git clone --depth=1 https://github.com/geek-fun/moli-skills.git ~/.moli-skills
export MOLI_SKILLS_DIR="$HOME/.moli-skills"
```

## 更新

告知用户：`/moli-update` 检查并升级到最新版本。
