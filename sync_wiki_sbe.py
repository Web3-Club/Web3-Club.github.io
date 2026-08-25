#!/usr/bin/env python3
"""Copy Chinese translations into the docsify wiki tree and rebuild sidebar."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = Path("/Users/yanbo/WritersideProjects/solidity-by-example_Chinese")
DST = ROOT / "post" / "solidity-by-example"

spec = importlib.util.spec_from_file_location("sbe_build", ROOT / "solidity-by-example" / "build.py")
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)
PAGES = mod.PAGES
CATEGORY_ORDER = mod.CATEGORY_ORDER
NAV_LABEL = mod.NAV_LABEL


def copy_pages() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    missing = []
    for slug, _title, src, _cat in PAGES:
        path = SRC / src
        if not path.exists():
            missing.append(src)
            continue
        dest = DST / f"{slug}.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    if missing:
        raise SystemExit("missing:\n" + "\n".join(missing))


def write_intro() -> None:
    groups = {c: [] for c in CATEGORY_ORDER}
    for slug, title, _src, cat in PAGES:
        groups[cat].append((slug, title))
    lines = [
        "# Solidity by Example 中文",
        "",
        "对照 [solidity-by-example.org](https://solidity-by-example.org/) **v 0.8.26** 的简体中文译本。",
        "",
        "用简单示例学习 [Solidity](https://solidity.readthedocs.io)。左侧目录可浏览全部章节。",
        "",
        f"共 **{len(PAGES)}** 篇。翻译仓库：[Web3-Club/Solidity-by-example_Chinese](https://github.com/Web3-Club/Solidity-by-example_Chinese)。",
        "",
        "也可使用更接近英文原站的独立页面：[原站风格阅读](/solidity-by-example/)。",
        "",
    ]
    for cat in CATEGORY_ORDER:
        lines.append(f"## {NAV_LABEL[cat]}")
        lines.append("")
        for slug, title in groups[cat]:
            lines.append(f"- [{title}]({slug}.md)")
        lines.append("")
    lines.extend(
        [
            "## 关注我们",
            "",
            "[Yanbo的Twitter](https://x.com/Yanbo2004)｜[Web3Club的Twitter](https://twitter.com/Web3ClubCN)",
            "",
            "[加入我们](https://github.com/Web3-Club/Intro./blob/main/Join%20club.md)",
            "",
        ]
    )
    (DST / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_sidebar() -> None:
    lines = [
        "* [Introduction](README.md)",
        "",
        "---",
        "",
        "* Solidity by Example 中文",
        "  * [简介](post/solidity-by-example/README.md)",
    ]
    last = None
    for slug, title, _src, cat in PAGES:
        if cat != last:
            lines.append(f"  * {NAV_LABEL[cat]}")
            last = cat
        lines.append(f"    * [{title}](post/solidity-by-example/{slug}.md)")
    lines.extend(
        [
            "",
            "---",
            "",
            "* 区块链",
            "  * [区块链介绍](post/区块链/介绍.md)",
            "",
            "---",
            "",
            "* sui",
            "  * [sui介绍](post/sui公链/sui介绍.md)",
            "",
            "---",
            "",
            "* **友链**",
            "* [hello-ctf](http://ctf.probius.xyz/)",
            "",
        ]
    )
    (ROOT / "sidebar.md").write_text("\n".join(lines), encoding="utf-8")


def write_wiki_readme() -> None:
    (ROOT / "README.md").write_text(
        """# Web3club Wiki

这里是 Web3-Club 的公开 wiki。

## Solidity by Example 中文

对照 [solidity-by-example.org](https://solidity-by-example.org/) v0.8.26，全部章节已放入本 wiki，可直接浏览。

- [从目录开始阅读](post/solidity-by-example/README.md)
- [原站风格页面](/solidity-by-example/)
- [翻译仓库](https://github.com/Web3-Club/Solidity-by-example_Chinese)
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    copy_pages()
    write_intro()
    write_sidebar()
    write_wiki_readme()
    print(f"synced {len(PAGES)} pages into {DST}")
