#!/usr/bin/env python3
"""import_wordlist.py — 外部词库导入辅助(词面对齐,定级交给人/Agent)

从纯文本词表(一行一词,支持 # 注释与顿号/逗号分隔)读入,与
references/wordlists/ 现有 TSV 全量去重,输出尚未覆盖的"待审词"草稿 TSV
——逐条补全 类别/严重度/替换建议 后,再复制进对应平台词库。

本脚本刻意不自动定级、不直接修改词库:同一词在不同平台/语境下风险不同,
机器只能对齐词面,定级与改写建议必须经过人或 Agent 复核。

用法:
    python3 import_wordlist.py --source banned-words.txt --platform xiaohongshu
    python3 import_wordlist.py --source a.txt --source b.txt --format json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

WORDLISTS_DIR = Path(__file__).resolve().parent.parent / "references" / "wordlists"
PLATFORMS = ("advertising-law", "xiaohongshu", "wechat", "douyin")
# 行内可能出现这些分隔符时按多词拆分(词表来源格式不统一)
INLINE_SEPARATORS = re.compile(r"[、,，;；\s]+")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="外部词表 → 待审词草稿(与现有词库去重)")
    parser.add_argument("--source", action="append", required=True, help="源词表文件,可重复")
    parser.add_argument(
        "--platform", choices=PLATFORMS, required=True,
        help="目标词库(决定草稿头注释;去重仍针对全部现有词库)",
    )
    parser.add_argument("--format", choices=("tsv", "json"), default="tsv")
    parser.add_argument("--wordlists-dir", type=Path, default=WORDLISTS_DIR)
    return parser.parse_args()


def load_existing(wordlists_dir: Path) -> dict[str, str]:
    """已收录词 → 所在词库名(小写规范化,拉丁词忽略大小写)。"""
    existing: dict[str, str] = {}
    for name in PLATFORMS:
        path = wordlists_dir / f"{name}.tsv"
        if not path.exists():
            continue
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            existing.setdefault(line.split("\t")[0].strip().lower(), name)
    return existing


def read_source(path: Path) -> list[str]:
    words: list[str] = []
    seen: set[str] = set()
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        for part in INLINE_SEPARATORS.split(line):
            word = part.strip()
            if not word:
                continue
            key = word.lower()
            if key not in seen:
                seen.add(key)
                words.append(word)
    return words


def main() -> int:
    args = parse_args()
    existing = load_existing(args.wordlists_dir)

    pending: list[dict] = []
    for src in args.source:
        path = Path(src)
        if not path.exists():
            print(f"警告: 源文件不存在 {path}", file=sys.stderr)
            continue
        for word in read_source(path):
            if word.lower() in existing:
                continue
            existing[word.lower()] = "(本次导入)"
            pending.append({"word": word, "source": path.name})

    if args.format == "json":
        print(json.dumps({"platform": args.platform, "pending": pending}, ensure_ascii=False, indent=2))
        return 0

    print(
        f"# 待审词草稿 — 目标词库: {args.platform}.tsv | 生成: {date.today().isoformat()}\n"
        f"# 来源: {', '.join(Path(s).name for s in args.source)}\n"
        f"# 共 {len(pending)} 词未收录。逐条补全后复制进 {args.platform}.tsv;\n"
        f"# 与营销合规无关的审核类词(暴恐/色情/违法工具等)直接删除,不要入库。\n"
        f"词\t类别\t严重度\t替换建议"
    )
    for item in pending:
        print(f"{item['word']}\t\t\t")
    return 0


if __name__ == "__main__":
    sys.exit(main())
