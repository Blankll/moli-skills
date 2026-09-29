---
name: moli-write-check
description: 自媒体文案合规检测与改写。用户提到"敏感词"、"违禁词"、"合规检测"、"限流词"、"文案合规"、"发布前检查"、"小红书违禁词"、"公众号敏感词"时使用。本地词库检测广告法极限词与小红书/公众号/抖音平台违禁词,AI 上下文风险判断,输出合规报告与改写稿。
version: 1.0.0
---

# moli-write-check

完整工作流见 `instructions/moli-write-check.md`,读取后按步骤执行。

## 工作流

1. **setup check** — 检查 Python 3.10+(脚本零第三方依赖)
2. **intake** — 确认文案与目标平台(未说明则默认全平台,不追问)
3. **detect** — 运行词库检测(L1 广告法极限词 / L2 平台违禁词)
4. **context review** — Agent 按 L3 清单判断医疗/金融/软广标注等上下文风险
5. **report** — 输出合规报告 → `docs/moli/compliance-v1/report.md`
6. **rewrite** — 用户确认后生成合规改写稿,逐处附理由
7. **re-check** — 改写稿重跑检测,block/risk 清零才算通过
8. **deliver** — 告知报告与改写稿路径、遗留 caution 项

## 检测脚本

```bash
python3 "$MOLI_SKILLS_DIR/moli-write-check/scripts/detect.py" --file <文案> --platform all
```

## 安装

```bash
git clone --depth=1 https://github.com/geek-fun/moli-skills.git ~/.moli-skills
export MOLI_SKILLS_DIR="$HOME/.moli-skills"
```
