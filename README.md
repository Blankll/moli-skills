# 墨吏 Skills

墨吏（moli）是一款面向中文场景的 AI 文书技能集。**任何 agent 都能用。**

## 技能清单

| 技能 | 说明 | 状态 |
|---|---|---|
| `moli-apple-design` | Apple 设计语言 — 液态玻璃视觉系统 + 流体交互哲学 | ✅ |
| `moli-cn-copyright` | AI 自动分析项目代码，生成全套软著申请材料 | ✅ |
| `moli-write-check` | 自媒体文案合规检测与改写（敏感词/违禁词/限流词） | ✅ |
| `moli-cn-patent` | 专利申请材料生成 | 🔜 |
| `moli-write-polish` | 文章润色 | 🔜 |

## 安装

告诉你的 agent：

```
帮我安装 https://github.com/geek-fun/moli-skills
```

任何 agent 都会读取本说明，自动完成。也可手动：

```bash
curl -sSL https://raw.githubusercontent.com/geek-fun/moli-skills/master/install.sh | bash
```

Windows（以管理员身份运行 PowerShell）：

```powershell
iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/geek-fun/moli-skills/master/install.ps1'))
```

### 各平台适配

安装后，各平台自动注册：

| Agent | 位置 | 说明 |
|---|---|---|
| OpenCode | `~/.config/opencode/skills/moli-apple-design/` | `/moli-apple-design` |
| Claude Code | `~/.claude/plugins/moli-skills/` | 运行 `claude --plugin ~/.claude/plugins/moli-skills` |
| Cursor / Windsurf | `cursor/rules/` | 复制 `.cursor/rules/moli-apple-design.mdc` |

## 使用：Apple 设计系统

```
/moli-apple-design  → 构建 Apple 风格页面或设计评审
```

触发后，Agent 会进入 Build（新设计）或 Review（审查现有 UI）模式，加载液态玻璃设计系统（tokens、组件、模式）+ 流体交互哲学（弹簧动效、手势物理、中断响应）。

## 使用：软著申请

安装完成后，直接输入命令：

| 命令 | 功能 | 适用平台 |
|---|---|---|
| `/moli-apple-design` | Apple 设计系统 — 构建/评审 | OpenCode |
| `/moli-cn-copyright` | 生成软著材料 | OpenCode / Claude Code |
| `/moli-cn-copyright-validate` | 验证已生成的材料 | OpenCode |
| `/moli-update` | 检查并升级到最新版本 | OpenCode |
| `/moli-write-check` | 敏感词/违禁词检测 + 合规改写 | OpenCode / Claude Code |
| `/moli-skills:validate` | 验证已生成的材料 | Claude Code |

### 工作流

```
/moli-cn-copyright                  → 生成材料到 docs/moli/copyright-v1/
        ↓
你补充截图、修改内容
        ↓
/moli-cn-copyright-validate        → 33 条规则检查 → 自动修复 → ✅ 通过
```

### 完整流程

```
① setup check   → 检查环境
② source scan   → 读源码、理解功能
③ ask unclear   → 最多问 3 个问题
④ generate      → 输出 docs/moli/copyright-v1/
⑤ review        → 你补充截图、修改内容
⑥ validate      → 你告诉 AI"帮我验证"，AI 自动检查
⑦ fix           → AI 修复问题，直到全部通过 ✅
```

### 输出

```
docs/moli/
├── copyright-v1/
│   ├── 正式资料/
│   │   ├── xxx_V1.0_源代码.pdf      ← 直接上传版权中心
│   │   └── xxx_V1.0_操作手册.docx   ← 截图后转PDF
│   └── 验证报告.md
├── copyright-v2/                    ← 修订版
├── 修订历史.md
└── copyright-latest -> copyright-v2
```

## 常见问题

### 安装后 `/moli-cn-copyright` 不可用？
确保 install.sh 已执行。手动检查：`ls ~/.agents/skills/moli-cn-copyright/SKILL.md` 应存在。如不存在，重新运行 install.sh。

### 生成 PDF 中文显示为方框/乱码？
系统缺少中文字体。macOS 自带 Songti 字体，无需操作。Linux 需安装：`sudo apt install fonts-wqy-zenhei`。Windows 自带宋体。

### Python 依赖安装失败？
```bash
pip install python-docx
```
如果权限不足，加 `--user` 或使用虚拟环境。

### Agent 说找不到 `MOLI_SKILLS_DIR`？
运行 `source ~/.zshrc` 或重启终端。或手动设置：`export MOLI_SKILLS_DIR="$HOME/.moli-skills"`。

### 验证报告全是 ❌？
检查材料目录是否正确：`--workdir` 应指向包含 PDF 和 DOCX 的 `正式资料/` 目录。

## 架构

## 架构

```
moli-skills/
├── instructions/           ← 共享工作流（所有 agent 可读）
│   ├── moli-apple-design.md
│   └── moli-cn-copyright.md
├── opencode/               ← OpenCode 适配层
│   ├── SKILL.md
│   └── moli-apple-design.md
├── claude/                 ← Claude Code 适配层
│   ├── .claude-plugin/
│   │   └── plugin.json
│   └── skills/
│       ├── copyright/
│       │   └── SKILL.md
│       └── validate/
├── cursor/                 ← Cursor / Windsurf 适配层
│   └── rules/
│       ├── moli-apple-design.mdc
│       └── moli-cn-copyright.mdc
├── moli-apple-design/      ← Apple 设计系统（视觉 + 动效）
│   ├── SKILL.md
│   ├── design-system.md
│   ├── tokens.css
│   ├── components.md
│   ├── patterns.md
│   ├── motion.md
│   ├── app.md
│   ├── icons.md
│   ├── review.md
│   ├── checklist.md
│   └── reference.html
├── moli-cn-copyright/      ← 核心脚本与规范
│   ├── scripts/
│   ├── references/
│   └── vendor/
├── moli-write-check/  ← 合规词库 + 检测脚本
│   ├── scripts/
│   └── references/wordlists/
├── ARCHITECTURE.md
├── cli.py
└── install.sh
```

## 许可证

Apache 2.0 © 2026 WENTSEN (Kunming) Technology Co., Ltd.
