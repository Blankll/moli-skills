#!/usr/bin/env python3
"""moli-write-check — 自媒体文案合规检测(确定性词库匹配层)

纯标准库实现,零第三方依赖。加载 references/wordlists/ 下的 TSV 词库,
对文案做 L1(广告法极限词)/ L2(平台违禁词)匹配,输出定位、分级与替换建议。
L3(上下文风险)由 Agent 按 instructions 工作流另行判断,本脚本不负责。

用法:
    python3 detect.py --file article.md --platform xiaohongshu
    python3 detect.py --text "全网第一的神仙水" --format json
    pbpaste | python3 detect.py                 # 从管道读入
    python3 detect.py --file copy.md --platform all

退出码: 0=未命中, 1=有命中, 2=参数/词库错误
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

WORDLISTS_DIR = Path(__file__).resolve().parent.parent / "references" / "wordlists"
AD_LAW = "advertising-law"
PLATFORMS = ("xiaohongshu", "wechat", "douyin")
SEVERITY_ORDER = {"block": 0, "risk": 1, "caution": 2}
SEVERITY_LABEL = {
    "block": "违规(必改)",
    "risk": "高风险(建议修改)",
    "caution": "谨慎(结合语境判断)",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="自媒体文案合规检测(词库匹配层)")
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--file", help="待检测文案文件路径")
    source.add_argument("--text", help="待检测文案(直接传入字符串)")
    parser.add_argument(
        "--platform",
        action="append",
        choices=PLATFORMS + ("all",),
        help="目标平台,可重复传入;缺省为 all(三个平台全部加载)",
    )
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument(
        "--wordlists-dir", type=Path, default=WORDLISTS_DIR, help="词库目录"
    )
    args = parser.parse_args()

    if not args.file and not args.text:
        if sys.stdin.isatty():
            parser.error("需要 --file、--text 或 stdin 输入文案")
        args.text = sys.stdin.read()
    return args


def load_terms(wordlists_dir: Path, platforms: list[str]) -> dict[str, dict]:
    """加载广告法层 + 平台层词库;平台层条目优先于通用层(更具体)。"""
    terms: dict[str, dict] = {}
    layers = [(AD_LAW, "通用")] + [(p, p) for p in platforms]
    for name, label in layers:
        path = wordlists_dir / f"{name}.tsv"
        if not path.exists():
            if label != "通用":  # 平台词库缺失属配置问题
                print(f"警告: 词库缺失 {path}", file=sys.stderr)
            continue
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            term = parts[0].strip()
            if not term:
                continue
            severity = parts[2].strip().lower() if len(parts) > 2 else "risk"
            terms[term] = {
                "category": parts[1].strip() if len(parts) > 1 else "未分类",
                "severity": severity if severity in SEVERITY_ORDER else "risk",
                "suggestion": parts[3].strip() if len(parts) > 3 else "",
                "source": label,
            }
    return terms


def build_pattern(terms: dict[str, dict]) -> re.Pattern:
    # 按长度降序排列候选词,保证同一位置优先命中最长词条
    alternation = "|".join(
        re.escape(t) for t in sorted(terms, key=len, reverse=True)
    )
    return re.compile(alternation, re.IGNORECASE)


def line_bounds(text: str, start: int, end: int) -> tuple[int, int, int, str]:
    """返回 (行号, 列号, 所在行原文, 所在行原文结束偏移)。"""
    line_start = text.rfind("\n", 0, start) + 1
    line_end = text.find("\n", end)
    if line_end == -1:
        line_end = len(text)
    lineno = text.count("\n", 0, start) + 1
    col = start - line_start + 1
    return lineno, col, text[line_start:line_end], line_end


def find_hits(text: str, terms: dict[str, dict]) -> list[dict]:
    pattern = build_pattern(terms)
    hits = []
    for m in pattern.finditer(text):
        term = m.group(0)
        info = terms[term]
        lineno, col, line_text, _ = line_bounds(text, m.start(), m.end())
        rel = m.start() - (text.rfind("\n", 0, m.start()) + 1)
        highlighted = line_text[:rel] + "「" + term + "」" + line_text[rel + len(term):]
        hits.append(
            {
                "term": term,
                "category": info["category"],
                "severity": info["severity"],
                "source": info["source"],
                "suggestion": info["suggestion"],
                "line": lineno,
                "col": col,
                "excerpt": highlighted,
            }
        )
    return hits


def render_text(hits: list[dict], platforms: list[str]) -> str:
    lines = []
    scanned = "、".join(platforms) if platforms else "仅广告法通用层"
    lines.append(f"合规检测 — 目标平台: {scanned}")
    if not hits:
        lines.append("✅ 未命中词库词条。注意:词库只覆盖词面风险,医疗宣称、")
        lines.append("   收益承诺、软广标注等上下文风险仍需 Agent 按 L3 清单复查。")
        return "\n".join(lines)

    counts = {s: 0 for s in SEVERITY_ORDER}
    for h in hits:
        counts[h["severity"]] += 1
    lines.append(
        f"命中 {len(hits)} 处:违规 {counts['block']} / 高风险 {counts['risk']} / 谨慎 {counts['caution']}\n"
    )
    for severity in SEVERITY_ORDER:
        group = [h for h in hits if h["severity"] == severity]
        if not group:
            continue
        lines.append(f"━━ {SEVERITY_LABEL[severity]} ━━")
        for h in group:
            lines.append(
                f"  L{h['line']}:{h['col']} 「{h['term']}」[{h['category']}|{h['source']}]"
            )
            lines.append(f"    原文: {h['excerpt']}")
            if h["suggestion"]:
                lines.append(f"    建议: {h['suggestion']}")
        lines.append("")
    return "\n".join(lines).rstrip()


def main() -> int:
    args = parse_args()

    platforms: list[str] = []
    if args.platform:
        if "all" in args.platform:
            platforms = list(PLATFORMS)
        else:
            platforms = sorted(set(args.platform), key=PLATFORMS.index)
    else:
        platforms = list(PLATFORMS)

    text = Path(args.file).read_text(encoding="utf-8") if args.file else args.text
    if not text or not text.strip():
        print("错误: 待检测文案为空", file=sys.stderr)
        return 2

    terms = load_terms(args.wordlists_dir, platforms)
    if not terms:
        print(f"错误: 词库为空({args.wordlists_dir})", file=sys.stderr)
        return 2

    hits = find_hits(text, terms)
    hits.sort(key=lambda h: (SEVERITY_ORDER[h["severity"]], h["line"], h["col"]))

    if args.format == "json":
        counts = {s: sum(1 for h in hits if h["severity"] == s) for s in SEVERITY_ORDER}
        print(
            json.dumps(
                {
                    "platforms": platforms,
                    "summary": {"total": len(hits), **counts},
                    "hits": hits,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(render_text(hits, platforms))

    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
