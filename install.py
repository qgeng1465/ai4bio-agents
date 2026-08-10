#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI 智能体一键安装器
====================
把本仓库 agents/ 目录下的智能体安装到 AI 助手的全局 agents 目录，
安装后即可在任意 AI 编程助手会话中用 @智能体名 调用。

用法:
    python install.py                # 安装全部
    python install.py --list         # 仅列出可用智能体
    python install.py --target <目录> # 指定安装目录
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path


def default_target() -> Path:
    """AI 助手全局 agents 目录（跨平台）。"""
    return Path(os.path.expanduser("~")) / ".claude" / "agents"


def main():
    ap = argparse.ArgumentParser(description="AI 智能体一键安装器")
    ap.add_argument("--target", default=None, help="安装目录（默认自动定位全局 agents 目录）")
    ap.add_argument("--list", action="store_true", help="仅列出可用智能体")
    args = ap.parse_args()

    src = Path(__file__).resolve().parent / "agents"
    if args.list:
        files = sorted(src.glob("*.md"))
        print(f"本仓库共 {len(files)} 个智能体：")
        for f in files:
            print(f"  @{f.stem}")
        return

    target = Path(os.path.expanduser(args.target)) if args.target else default_target()
    target.mkdir(parents=True, exist_ok=True)
    count = 0
    for f in sorted(src.glob("*.md")):
        shutil.copy2(f, target / f.name)
        print(f"  [✓] @{f.stem}  ->  {target / f.name}")
        count += 1
    print(f"\n安装完成：共 {count} 个智能体 -> {target}")
    if count:
        print("用法：在任意 AI 编程助手会话输入 @智能体名 即可调用。")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\n已取消")
