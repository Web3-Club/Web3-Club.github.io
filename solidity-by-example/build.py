#!/usr/bin/env python3
"""Generate a Solidity-by-Example-styled static site from the Chinese translation."""

from __future__ import annotations

import base64
import html
import re
from pathlib import Path

SRC = Path("/Users/yanbo/WritersideProjects/solidity-by-example_Chinese")
OUT = Path(__file__).resolve().parent

PAGES = [
    # slug, title, source, category
    ("hello-world", "Hello World", "01 Hello World.md", "基础"),
    ("first-app", "第一个应用", "02 第一个应用.md", "基础"),
    ("primitives", "基本数据类型", "03 基本数据类型.md", "基础"),
    ("variables", "变量", "04 变量.md", "基础"),
    ("constants", "常量", "05 常量.md", "基础"),
    ("immutable", "不可变", "06 不可变.md", "基础"),
    ("state-variables", "读写状态变量", "07 读写状态变量.md", "基础"),
    ("ether-units", "以太币和 Wei", "08 以太币和Wei.md", "基础"),
    ("gas", "Gas 与 Gas Price", "09 Gas费.md", "基础"),
    ("if-else", "条件判断", "10 条件判断.md", "基础"),
    ("loop", "循环语句", "11 循环语句.md", "基础"),
    ("mapping", "映射", "12 映射.md", "基础"),
    ("array", "数组", "13 数组.md", "基础"),
    ("enum", "枚举", "14 枚举.md", "基础"),
    ("user-defined-value-types", "用户自定义值类型", "15 用户自定义值类型.md", "基础"),
    ("structs", "结构体", "16 结构体.md", "基础"),
    ("data-locations", "数据位置", "17 数据位置.md", "基础"),
    ("transient-storage", "瞬时存储", "18 瞬时存储.md", "基础"),
    ("function", "函数", "19 函数.md", "基础"),
    ("view-and-pure-functions", "View 和 Pure 函数", "20 View和Pure函数.md", "基础"),
    ("error", "错误或异常", "21 错误或异常.md", "基础"),
    ("function-modifier", "函数修饰符", "22 函数修饰符.md", "基础"),
    ("events", "事件", "23 事件.md", "基础"),
    ("events-advanced", "高级事件", "24 高级事件.md", "基础"),
    ("constructor", "构造函数", "25 构造函数.md", "基础"),
    ("inheritance", "继承", "26 继承.md", "基础"),
    ("shadowing-inherited-state-variables", "继承状态变量的屏蔽", "27 继承状态变量的屏蔽.md", "基础"),
    ("super", "调用父合约", "28 调用父合约.md", "基础"),
    ("visibility", "可见性", "29 可见性.md", "基础"),
    ("interface", "接口", "30 接口.md", "基础"),
    ("payable", "Payable", "31 Payable 函数.md", "基础"),
    ("sending-ether", "发送以太币", "32 发送以太币.md", "基础"),
    ("fallback", "回退函数", "33 回退函数.md", "基础"),
    ("call", "Call", "34 Call.md", "基础"),
    ("delegatecall", "Delegatecall", "35 Delegatecall.md", "基础"),
    ("function-selector", "函数选择器", "36 函数选择器.md", "基础"),
    ("calling-contract", "调用其他合约", "37 调用其他合约.md", "基础"),
    ("new-contract", "从合约创建合约", "38 从合约创建合约.md", "基础"),
    ("try-catch", "Try / Catch", "39 Try Catch.md", "基础"),
    ("import", "导入", "40 导入.md", "基础"),
    ("library", "库", "41 库.md", "基础"),
    ("abi-encode", "ABI 编码", "42 ABI 编码.md", "基础"),
    ("abi-decode", "ABI 解码", "43 ABI 解码.md", "基础"),
    ("hashing", "Keccak256 哈希", "44 Keccak256 哈希.md", "基础"),
    ("signature", "验证签名", "45 验证签名.md", "基础"),
    ("gas-golf", "Gas 优化", "46 Gas 优化.md", "基础"),
    ("bitwise", "位运算", "47 位运算.md", "基础"),
    ("unchecked-math", "Unchecked Math", "48 Unchecked Math.md", "基础"),
    ("assembly-variable", "汇编变量", "49 汇编变量.md", "基础"),
    ("assembly-if", "汇编条件语句", "50 汇编条件语句.md", "基础"),
    ("assembly-loop", "汇编循环", "51 汇编循环.md", "基础"),
    ("assembly-error", "汇编错误", "52 汇编错误.md", "基础"),
    ("assembly-math", "汇编数学运算", "53 汇编数学运算.md", "基础"),
    ("app/ether-wallet", "以太钱包", "Unit2 应用/以太钱包.md", "应用"),
    ("app/multi-sig-wallet", "多签钱包", "Unit2 应用/多签钱包.md", "应用"),
    ("app/merkle-tree", "默克尔树", "Unit2 应用/默克尔树.md", "应用"),
    ("app/iterable-mapping", "可迭代映射", "Unit2 应用/可迭代映射.md", "应用"),
    ("app/erc20", "ERC20", "Unit2 应用/ERC20.md", "应用"),
    ("app/erc721", "ERC721", "Unit2 应用/ERC721.md", "应用"),
    ("app/erc1155", "ERC1155", "Unit2 应用/ERC1155.md", "应用"),
    ("app/gasless-token-transfer", "无 Gas 代币转账", "Unit2 应用/无Gas代币转账.md", "应用"),
    ("app/simple-bytecode-contract", "简单字节码合约", "Unit2 应用/简单字节码合约.md", "应用"),
    ("app/create2", "使用 Create2 预计算合约地址", "Unit2 应用/使用Create2预计算合约地址.md", "应用"),
    ("app/minimal-proxy", "最小代理合约", "Unit2 应用/最小代理合约.md", "应用"),
    ("app/upgradeable-proxy", "可升级代理", "Unit2 应用/可升级代理.md", "应用"),
    ("app/deploy-any-contract", "部署任意合约", "Unit2 应用/部署任意合约.md", "应用"),
    ("app/write-to-any-slot", "写入任意存储槽", "Unit2 应用/写入任意存储槽.md", "应用"),
    ("app/uni-directional-payment-channel", "单向支付渠道", "Unit2 应用/单向支付渠道.md", "应用"),
    ("app/bi-directional-payment-channel", "双向支付渠道", "Unit2 应用/双向支付渠道.md", "应用"),
    ("app/english-auction", "英式拍卖", "Unit2 应用/英式拍卖.md", "应用"),
    ("app/dutch-auction", "荷兰式拍卖", "Unit2 应用/荷兰式拍卖.md", "应用"),
    ("app/crowd-fund", "众筹基金", "Unit2 应用/众筹基金.md", "应用"),
    ("app/multi-call", "多调用", "Unit2 应用/多调用.md", "应用"),
    ("app/multi-delegatecall", "多委托调用", "Unit2 应用/多委托调用.md", "应用"),
    ("app/time-lock", "定时锁", "Unit2 应用/定时锁.md", "应用"),
    ("app/assembly-bin-exp", "汇编中的二进制求幂", "Unit2 应用/汇编中的二进制求幂.md", "应用"),
    ("app/airdrop", "默克尔空投", "Unit2 应用/默克尔空投.md", "应用"),
    ("hacks/re-entrancy", "重入攻击", "Unit5 黑客攻击及预防/重入攻击.md", "黑客攻击"),
    ("hacks/overflow", "算术溢出与下溢", "Unit5 黑客攻击及预防/算术溢出.md", "黑客攻击"),
    ("hacks/self-destruct", "自毁函数", "Unit5 黑客攻击及预防/自毁函数.md", "黑客攻击"),
    ("hacks/accessing-private-data", "访问私有数据", "Unit5 黑客攻击及预防/访问私有数据.md", "黑客攻击"),
    ("hacks/delegatecall", "Delegatecall 攻击", "Unit5 黑客攻击及预防/delegatecall.md", "黑客攻击"),
    ("hacks/randomness", "随机数预测", "Unit5 黑客攻击及预防/随机数预测.md", "黑客攻击"),
    ("hacks/denial-of-service", "拒绝服务攻击", "Unit5 黑客攻击及预防/拒绝服务攻击.md", "黑客攻击"),
    ("hacks/phishing-with-tx-origin", "tx.origin 钓鱼", "Unit5 黑客攻击及预防/tx.origin钓鱼.md", "黑客攻击"),
    ("hacks/hiding-malicious-code-with-external-contract", "使用外部合约隐藏恶意代码", "Unit5 黑客攻击及预防/使用外部合约隐藏恶意代码.md", "黑客攻击"),
    ("hacks/honeypot", "蜜罐", "Unit5 黑客攻击及预防/蜜罐.md", "黑客攻击"),
    ("hacks/front-running", "抢跑", "Unit5 黑客攻击及预防/抢跑.md", "黑客攻击"),
    ("hacks/block-timestamp-manipulation", "区块时间戳操纵", "Unit5 黑客攻击及预防/区块时间戳操纵.md", "黑客攻击"),
    ("hacks/signature-replay", "签名重放", "Unit5 黑客攻击及预防/签名重放.md", "黑客攻击"),
    ("hacks/contract-size", "绕过合约大小检查", "Unit5 黑客攻击及预防/绕过extcodesize.md", "黑客攻击"),
    ("hacks/deploy-different-contracts-same-address", "在同一地址部署不同合约", "Unit5 黑客攻击及预防/在同一个地址部署不同的合约.md", "黑客攻击"),
    ("hacks/vault-inflation", "金库通货膨胀攻击", "Unit5 黑客攻击及预防/金库通货膨胀攻击.md", "黑客攻击"),
    ("hacks/weth-permit", "WETH Permit", "Unit5 黑客攻击及预防/WETH Permit.md", "黑客攻击"),
    ("hacks/63-64-gas-rule", "63 / 64 Gas 规则", "Unit5 黑客攻击及预防/63-64 Gas规则.md", "黑客攻击"),
    ("evm/storage", "EVM 存储布局", "Unit6 EVM/存储布局.md", "EVM"),
    ("evm/memory", "EVM 内存布局", "Unit6 EVM/内存布局.md", "EVM"),
    ("tests/echidna", "Echidna", "Unit3 测试/使用Echidna进行智能合约测试.md", "测试"),
    ("foundry/basic", "Foundry 基础", "Unit7 Foundry/01 基础.md", "Foundry"),
    ("foundry/auth", "授权", "Unit7 Foundry/02 授权.md", "Foundry"),
    ("foundry/error", "错误", "Unit7 Foundry/03 错误.md", "Foundry"),
    ("foundry/event", "事件", "Unit7 Foundry/04 事件.md", "Foundry"),
    ("foundry/send", "发送", "Unit7 Foundry/05 发送.md", "Foundry"),
    ("foundry/time", "时间", "Unit7 Foundry/06 时间.md", "Foundry"),
    ("foundry/sign", "签名", "Unit7 Foundry/07 签名.md", "Foundry"),
    ("foundry/label", "标签", "Unit7 Foundry/08 标签.md", "Foundry"),
    ("foundry/mock-call", "Mock Call", "Unit7 Foundry/09 Mock Call.md", "Foundry"),
    ("foundry/vm-store", "Store", "Unit7 Foundry/10 Store.md", "Foundry"),
    ("defi/uniswap-v2", "Uniswap V2 Swap", "Unit4 DeFi/01 Uniswap V2 Swap.md", "DeFi"),
    ("defi/uniswap-v2-add-remove-liquidity", "Uniswap V2 添加与移除流动性", "Unit4 DeFi/02 Uniswap V2 Add Remove Liquidity.md", "DeFi"),
    ("defi/uniswap-v2-optimal-one-sided-supply", "Uniswap V2 最优单边供给", "Unit4 DeFi/03 Uniswap V2 Optimal One Sided Supply.md", "DeFi"),
    ("defi/uniswap-v2-flash-swap", "Uniswap V2 Flash Swap", "Unit4 DeFi/04 Uniswap V2 Flash Swap.md", "DeFi"),
    ("defi/uniswap-v3-swap", "Uniswap V3 Swap", "Unit4 DeFi/05 Uniswap V3 Swap.md", "DeFi"),
    ("defi/uniswap-v3-liquidity", "Uniswap V3 流动性", "Unit4 DeFi/06 Uniswap V3 Liquidity.md", "DeFi"),
    ("defi/uniswap-v3-flash", "Uniswap V3 闪电贷", "Unit4 DeFi/07 Uniswap V3 Flash Loan.md", "DeFi"),
    ("defi/uniswap-v3-flash-swap", "Uniswap V3 Flash Swap 套利", "Unit4 DeFi/08 Uniswap V3 Flash Swap Arbitrage.md", "DeFi"),
    ("defi/uniswap-v4-swap", "Uniswap V4 Swap", "Unit4 DeFi/09 Uniswap V4 Swap.md", "DeFi"),
    ("defi/uniswap-v4-flash", "Uniswap V4 闪电贷", "Unit4 DeFi/10 Uniswap V4 Flash Loan.md", "DeFi"),
    ("defi/uniswap-v4-limit-order", "Uniswap V4 限价单", "Unit4 DeFi/11 Uniswap V4 Limit Order.md", "DeFi"),
    ("defi/chainlink-price-oracle", "Chainlink 价格预言机", "Unit4 DeFi/12 Chainlink Price Oracle.md", "DeFi"),
    ("defi/chronicle-price-oracle", "Chronicle 价格预言机", "Unit4 DeFi/13 Chronicle Price Oracle.md", "DeFi"),
    ("defi/dai-proxy", "DAI Proxy", "Unit4 DeFi/14 DAI Proxy.md", "DeFi"),
    ("defi/staking-rewards", "质押奖励", "Unit4 DeFi/15 Staking Rewards.md", "DeFi"),
    ("defi/discrete-staking-rewards", "离散质押奖励", "Unit4 DeFi/16 Discrete Staking Rewards.md", "DeFi"),
    ("defi/vault", "Vault", "Unit4 DeFi/17 Vault.md", "DeFi"),
    ("defi/token-lock", "Token Lock", "Unit4 DeFi/18 Token Lock.md", "DeFi"),
    ("defi/constant-sum-amm", "恒定和 AMM", "Unit4 DeFi/19 Constant Sum AMM.md", "DeFi"),
    ("defi/constant-product-amm", "恒定乘积 AMM", "Unit4 DeFi/20 Constant Product AMM.md", "DeFi"),
    ("defi/stable-swap-amm", "Stable Swap AMM", "Unit4 DeFi/21 Stable Swap AMM.md", "DeFi"),
]

CATEGORY_ORDER = ["基础", "应用", "黑客攻击", "EVM", "测试", "Foundry", "DeFi"]
NAV_LABEL = {
    "基础": "Basic",
    "应用": "Applications",
    "黑客攻击": "Hacks",
    "EVM": "EVM",
    "测试": "Tests",
    "Foundry": "Foundry",
    "DeFi": "DeFi",
}

SOLIDITY_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1300 1300" width="30" height="30" class="logo" data-logo>
  <path opacity="0.45" d="M773.772 253.308 643.068 485.61H381.842l130.614-232.302h261.316"/>
  <path opacity="0.6" d="M643.068 485.61h261.318L773.772 253.308H512.456L643.068 485.61z"/>
  <path opacity="0.8" d="M512.456 717.822 643.068 485.61 512.456 253.308 381.842 485.61l130.614 232.212z"/>
  <path opacity="0.45" d="m513.721 1066.275 130.704-232.303h261.318l-130.705 232.303H513.721"/>
  <path opacity="0.6" d="M644.424 833.973H383.107l130.613 232.303h261.317L644.424 833.973z"/>
  <path opacity="0.8" d="M775.038 601.761 644.424 833.973l130.614 232.303 130.704-232.303-130.704-232.212z"/>
</svg>"""

HAMBURGER = """<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20" stroke-width="2" stroke="currentColor" width="20" height="20">
  <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"/>
</svg>"""

DARK_ICON = """<svg data-icon="dark" xmlns="http://www.w3.org/2000/svg" fill="#fff" viewBox="0 0 438.277 438.277" width="20" height="20"><path d="M428.756 300.104c-.664-3.81-2.334-7.047-4.996-9.713-5.9-5.903-12.752-7.142-20.554-3.716-20.937 9.708-42.641 14.558-65.097 14.558-28.171 0-54.152-6.94-77.943-20.838-23.791-13.894-42.631-32.736-56.525-56.53-13.899-23.793-20.844-49.773-20.844-77.945 0-21.888 4.333-42.683 12.991-62.384 8.66-19.7 21.176-36.973 37.543-51.82 6.283-5.898 7.713-12.752 4.287-20.557-3.236-7.801-9.041-11.511-17.415-11.132-29.121 1.141-56.72 7.664-82.797 19.556C111.33 31.478 88.917 47.13 70.168 66.548c-18.747 19.414-33.595 42.399-44.54 68.95-10.942 26.553-16.416 54.39-16.416 83.511 0 29.694 5.806 58.054 17.416 85.082 11.613 27.028 27.218 50.344 46.824 69.949 19.604 19.599 42.92 35.207 69.951 46.822 27.028 11.607 55.384 17.415 85.075 17.415 42.64 0 81.987-11.563 118.054-34.69 36.069-23.124 63.05-54.006 80.944-92.645 1.524-3.423 1.951-7.036 1.28-10.838z"/></svg>"""

LIGHT_ICON = """<svg data-icon="light" hidden xmlns="http://www.w3.org/2000/svg" viewBox="0 0 302.4 302.4" width="20" height="20"><circle cx="151.2" cy="151.2" r="48" fill="none" stroke="#252519" stroke-width="16"/><g stroke="#252519" stroke-width="12" stroke-linecap="round"><path d="M151.2 20 v32M151.2 250 v32M20 151.2 h32M250 151.2 h32M55 55 l22 22M225 225 l22 22M55 247 l22 -22M225 77 l22 -22"/></g></svg>"""

SEARCH_ICON = """<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" width="18" height="18"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"/></svg>"""


def asset_prefix(slug: str | None) -> str:
    if slug is None:
        return "./"
    return "../" * (slug.count("/") + 1)


def page_href(from_slug: str | None, to_slug: str) -> str:
    prefix = asset_prefix(from_slug)
    return f"{prefix}{to_slug}/"


def home_href(from_slug: str | None) -> str:
    return asset_prefix(from_slug)


def remix_url(code: str) -> str:
    b64 = base64.b64encode(code.encode("utf-8")).decode("ascii")
    return f"https://remix.ethereum.org/?#code={b64}"


def strip_md(text: str) -> str:
    text = re.sub(r"^---\s*\n## 关注我们[\s\S]*", "", text).strip()
    text = re.sub(r"\n---\s*\n## 关注我们[\s\S]*", "", text).strip()
    return text


def inline_md(text: str) -> str:
    parts: list[str] = []
    i = 0
    pattern = re.compile(
        r"(`[^`]+`)|(\*\*[^*]+\*\*)|(\[[^\]]+\]\([^)]+\))"
    )
    for m in pattern.finditer(text):
        if m.start() > i:
            parts.append(html.escape(text[i : m.start()]))
        token = m.group(0)
        if token.startswith("`"):
            parts.append(f"<code>{html.escape(token[1:-1])}</code>")
        elif token.startswith("**"):
            parts.append(f"<strong>{html.escape(token[2:-2])}</strong>")
        else:
            label, url = re.match(r"\[([^\]]+)\]\(([^)]+)\)", token).groups()
            parts.append(f'<a href="{html.escape(url, quote=True)}">{html.escape(label)}</a>')
        i = m.end()
    parts.append(html.escape(text[i:]))
    return "".join(parts)


def md_to_html(md: str) -> tuple[str, list[tuple[str, str]]]:
    codes: list[tuple[str, str]] = []

    def save_code(m: re.Match) -> str:
        lang = (m.group(1) or "").strip() or "plaintext"
        code = m.group(2).replace("\r\n", "\n")
        if code.endswith("\n"):
            code = code[:-1]
        codes.append((lang, code))
        return f"\n\n%%CODE{len(codes) - 1}%%\n\n"

    md = re.sub(r"```([^\n]*)\n(.*?)```", save_code, md, flags=re.S)

    lines = md.split("\n")
    out: list[str] = []
    para: list[str] = []
    list_buf: list[str] = []
    list_ordered = False

    def flush_para() -> None:
        nonlocal para
        if para:
            out.append("<p>" + "<br>\n".join(inline_md(x) for x in para) + "</p>")
            para = []

    def flush_list() -> None:
        nonlocal list_buf, list_ordered
        if list_buf:
            tag = "ol" if list_ordered else "ul"
            items = "".join(f"<li>{inline_md(x)}</li>" for x in list_buf)
            out.append(f"<{tag}>{items}</{tag}>")
            list_buf = []

    for raw in lines:
        line = raw.rstrip()
        code_m = re.fullmatch(r"%%CODE(\d+)%%", line.strip())
        if code_m:
            flush_para()
            flush_list()
            idx = int(code_m.group(1))
            lang, code = codes[idx]
            cls = "language-solidity" if lang in ("solidity", "sol") else f"language-{html.escape(lang)}"
            out.append(
                f'<pre><code class="{cls}">{html.escape(code)}</code></pre>'
            )
            continue
        if not line.strip():
            flush_para()
            flush_list()
            continue
        if re.match(r"^#{1,6} ", line):
            flush_para()
            flush_list()
            hashes, rest = line.split(" ", 1)
            level = min(len(hashes), 6)
            if level == 1:
                continue
            out.append(f"<h{level}>{inline_md(rest)}</h{level}>")
            continue
        ol = re.match(r"^(\d+)\.\s+(.*)$", line)
        ul = re.match(r"^[-*]\s+(.*)$", line)
        if ol:
            flush_para()
            if list_buf and not list_ordered:
                flush_list()
            list_ordered = True
            list_buf.append(ol.group(2))
            continue
        if ul:
            flush_para()
            if list_buf and list_ordered:
                flush_list()
            list_ordered = False
            list_buf.append(ul.group(1))
            continue
        flush_list()
        para.append(line)
    flush_para()
    flush_list()
    solidity_codes = [(lang, code) for lang, code in codes if lang in ("solidity", "sol", "")]
    return "\n".join(out), solidity_codes


def nav_html(current: str | None, from_slug: str | None) -> str:
    chunks = ['<h3 class="nav-category">Basic</h3>']
    last_cat = None
    for slug, title, _src, cat in PAGES:
        label = NAV_LABEL[cat]
        if cat != last_cat:
            if cat != "基础":
                chunks.append(f'<h3 class="nav-title">{html.escape(label)}</h3>')
            chunks.append('<ul class="nav-list">')
            last_cat = cat
        cls = "nav-item-active" if slug == current else "nav-item"
        href = page_href(from_slug, slug)
        chunks.append(
            f'<li class="{cls}"><a class="nav-link" href="{href}">{html.escape(title)}</a></li>'
        )
        nxt = None
        idx = next(i for i, p in enumerate(PAGES) if p[0] == slug)
        if idx + 1 >= len(PAGES) or PAGES[idx + 1][3] != cat:
            chunks.append("</ul>")
    return "\n".join(chunks)


def chrome(title: str, body: str, slug: str | None) -> str:
    prefix = asset_prefix(slug)
    home = home_href(slug)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} | Solidity by Example | 0.8.26</title>
  <meta name="description" content="Solidity by Example 简体中文译本，对照 solidity-by-example.org v0.8.26。">
  <link rel="stylesheet" href="{prefix}css/app.css">
</head>
<body class="light">
  <div class="layout">
    <aside class="side-nav">
      {nav_html(slug, slug)}
    </aside>
    <div class="main">
      <header class="header">
        <button class="hamburger" data-toggle-nav aria-label="菜单">{HAMBURGER}</button>
        <div class="header-center">
          <div class="header-center-inner">
            <a href="{home}">{SOLIDITY_SVG}</a>
            <h3><a href="{home}">Solidity by Example</a></h3>
          </div>
          <div class="zh-badge">中文译本 · Web3-Club</div>
        </div>
        <button class="mode-btn" data-toggle-theme aria-label="切换主题">{DARK_ICON}{LIGHT_ICON}</button>
      </header>
      <div class="children">
        {body}
        <footer class="footer">
          <div class="footer-row"><a href="https://github.com/Web3-Club/Solidity-by-example_Chinese" target="_blank" rel="noreferrer">中文翻译源码</a></div>
          <div class="footer-row"><a href="https://solidity-by-example.org/" target="_blank" rel="noreferrer">英文原站 solidity-by-example.org</a></div>
          <div class="footer-row">
            <a href="https://github.com/Web3-Club" target="_blank" rel="noreferrer">Web3-Club</a>
            <div class="bar">|</div>
            <a href="https://twitter.com/Web3ClubCN" target="_blank" rel="noreferrer">Twitter</a>
          </div>
          <div class="footer-row">v 0.8.26</div>
        </footer>
      </div>
    </div>
  </div>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/solidity.min.js"></script>
  <script src="{prefix}js/app.js"></script>
  <script>
    document.querySelectorAll("[data-logo]").forEach(function (el) {{
      function paint() {{
        el.setAttribute("fill", document.body.classList.contains("dark") ? "rgb(0, 255, 0)" : "currentColor");
      }}
      paint();
      new MutationObserver(paint).observe(document.body, {{ attributes: true, attributeFilter: ["class"] }});
    }});
  </script>
</body>
</html>
"""


def home_body() -> str:
    groups: dict[str, list[tuple[str, str]]] = {c: [] for c in CATEGORY_ORDER}
    for slug, title, _src, cat in PAGES:
        groups[cat].append((slug, title))
    parts = [
        '<div class="home">',
        '<h1 class="home-header"><a href="./">Solidity by Example</a></h1>',
        '<div class="sub-header">v 0.8.26 · 简体中文译本</div>',
        "<p>用简单示例学习 <a href=\"https://solidity.readthedocs.io\" target=\"_blank\" rel=\"noreferrer\">Solidity</a>。<br>对照 <a href=\"https://solidity-by-example.org/\" target=\"_blank\" rel=\"noreferrer\">solidity-by-example.org</a> 翻译。</p>",
        '<div class="updates">由 <a href="https://github.com/Web3-Club/Solidity-by-example_Chinese" target="_blank" rel="noreferrer">Web3-Club</a> 维护</div>',
        f'<div class="search"><div class="search-bar">{SEARCH_ICON}<input data-search type="search" placeholder="Search..."></div></div>',
    ]
    first = True
    for cat in CATEGORY_ORDER:
        if not first:
            parts.append(f'<h3 class="category">{html.escape(NAV_LABEL[cat])}</h3>')
        first = False
        parts.append("<ul>")
        for slug, title in groups[cat]:
            hay = f"{title} {slug} {NAV_LABEL[cat]}"
            parts.append(
                f'<li class="list-item" data-route="{html.escape(hay)}"><a href="./{slug}/">{html.escape(title)}</a></li>'
            )
        parts.append("</ul>")
    parts.append("</div>")
    return "\n".join(parts)


def article_body(idx: int, html_body: str, codes: list[tuple[str, str]], en_url: str) -> str:
    slug, title, _src, _cat = PAGES[idx]
    prev = PAGES[idx - 1] if idx > 0 else None
    nxt = PAGES[idx + 1] if idx + 1 < len(PAGES) else None
    prev_html = (
        f'<a href="{page_href(slug, prev[0])}">&lt; {html.escape(prev[1])}</a>' if prev else "<span></span>"
    )
    next_html = (
        f'<a href="{page_href(slug, nxt[0])}">{html.escape(nxt[1])} &gt;</a>' if nxt else "<span></span>"
    )
    remix_items = []
    for i, (lang, code) in enumerate(codes):
        if lang not in ("solidity", "sol", ""):
            continue
        name = f"Example{i + 1}.sol" if len(codes) > 1 else "Example.sol"
        remix_items.append(
            f'<li><a href="{html.escape(remix_url(code), quote=True)}" target="_blank" rel="noreferrer">{html.escape(name)}</a></li>'
        )
    remix = ""
    if remix_items:
        remix = "<h3>Try on Remix</h3><ul>" + "".join(remix_items) + "</ul>"
    return f"""
    <article class="article">
      <div class="article-content">
        <h2>{html.escape(title)}</h2>
        <div class="en-link">英文原页：<a href="{html.escape(en_url, quote=True)}" target="_blank" rel="noreferrer">{html.escape(en_url)}</a></div>
        {html_body}
        <div class="prev-next">{prev_html}{next_html}</div>
        {remix}
      </div>
    </article>
    """


def main() -> None:
    missing = []
    (OUT / "index.html").write_text(
        chrome("Solidity by Example 中文", home_body(), None).replace(
            "Solidity by Example 中文 | Solidity by Example | 0.8.26",
            "Solidity by Example | 0.8.26",
        ),
        encoding="utf-8",
    )
    for i, (slug, title, src, _cat) in enumerate(PAGES):
        path = SRC / src
        if not path.exists():
            missing.append(src)
            continue
        raw = strip_md(path.read_text(encoding="utf-8"))
        body_md = re.sub(r"^# .*\n+", "", raw, count=1)
        en = ""
        m = re.search(r"对应英文原页：(\S+)", body_md)
        if m:
            en = m.group(1)
            body_md = re.sub(r"^对应英文原页：\S+\n+", "", body_md)
        html_body, codes = md_to_html(body_md.strip())
        page_dir = OUT / slug
        page_dir.mkdir(parents=True, exist_ok=True)
        (page_dir / "index.html").write_text(
            chrome(title, article_body(i, html_body, codes, en), slug),
            encoding="utf-8",
        )
    if missing:
        raise SystemExit("missing sources:\n" + "\n".join(missing))
    print(f"wrote {len(PAGES) + 1} pages to {OUT}")


if __name__ == "__main__":
    main()
