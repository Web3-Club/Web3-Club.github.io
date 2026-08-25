# Solidity by Example 中文

对照 [solidity-by-example.org](https://solidity-by-example.org/) **v 0.8.26** 的简体中文译本。

用简单示例学习 [Solidity](https://solidity.readthedocs.io)。左侧目录可浏览全部章节。

共 **129** 篇。翻译仓库：[Web3-Club/Solidity-by-example_Chinese](https://github.com/Web3-Club/Solidity-by-example_Chinese)。

也可使用更接近英文原站的独立页面：[原站风格阅读](/solidity-by-example/)。

## Basic

- [Hello World](hello-world.md)
- [第一个应用](first-app.md)
- [基本数据类型](primitives.md)
- [变量](variables.md)
- [常量](constants.md)
- [不可变](immutable.md)
- [读写状态变量](state-variables.md)
- [以太币和 Wei](ether-units.md)
- [Gas 与 Gas Price](gas.md)
- [条件判断](if-else.md)
- [循环语句](loop.md)
- [映射](mapping.md)
- [数组](array.md)
- [枚举](enum.md)
- [用户自定义值类型](user-defined-value-types.md)
- [结构体](structs.md)
- [数据位置](data-locations.md)
- [瞬时存储](transient-storage.md)
- [函数](function.md)
- [View 和 Pure 函数](view-and-pure-functions.md)
- [错误或异常](error.md)
- [函数修饰符](function-modifier.md)
- [事件](events.md)
- [高级事件](events-advanced.md)
- [构造函数](constructor.md)
- [继承](inheritance.md)
- [继承状态变量的屏蔽](shadowing-inherited-state-variables.md)
- [调用父合约](super.md)
- [可见性](visibility.md)
- [接口](interface.md)
- [Payable](payable.md)
- [发送以太币](sending-ether.md)
- [回退函数](fallback.md)
- [Call](call.md)
- [Delegatecall](delegatecall.md)
- [函数选择器](function-selector.md)
- [调用其他合约](calling-contract.md)
- [从合约创建合约](new-contract.md)
- [Try / Catch](try-catch.md)
- [导入](import.md)
- [库](library.md)
- [ABI 编码](abi-encode.md)
- [ABI 解码](abi-decode.md)
- [Keccak256 哈希](hashing.md)
- [验证签名](signature.md)
- [Gas 优化](gas-golf.md)
- [位运算](bitwise.md)
- [Unchecked Math](unchecked-math.md)
- [汇编变量](assembly-variable.md)
- [汇编条件语句](assembly-if.md)
- [汇编循环](assembly-loop.md)
- [汇编错误](assembly-error.md)
- [汇编数学运算](assembly-math.md)

## Applications

- [以太钱包](app/ether-wallet.md)
- [多签钱包](app/multi-sig-wallet.md)
- [默克尔树](app/merkle-tree.md)
- [可迭代映射](app/iterable-mapping.md)
- [ERC20](app/erc20.md)
- [ERC721](app/erc721.md)
- [ERC1155](app/erc1155.md)
- [无 Gas 代币转账](app/gasless-token-transfer.md)
- [简单字节码合约](app/simple-bytecode-contract.md)
- [使用 Create2 预计算合约地址](app/create2.md)
- [最小代理合约](app/minimal-proxy.md)
- [可升级代理](app/upgradeable-proxy.md)
- [部署任意合约](app/deploy-any-contract.md)
- [写入任意存储槽](app/write-to-any-slot.md)
- [单向支付渠道](app/uni-directional-payment-channel.md)
- [双向支付渠道](app/bi-directional-payment-channel.md)
- [英式拍卖](app/english-auction.md)
- [荷兰式拍卖](app/dutch-auction.md)
- [众筹基金](app/crowd-fund.md)
- [多调用](app/multi-call.md)
- [多委托调用](app/multi-delegatecall.md)
- [定时锁](app/time-lock.md)
- [汇编中的二进制求幂](app/assembly-bin-exp.md)
- [默克尔空投](app/airdrop.md)

## Hacks

- [重入攻击](hacks/re-entrancy.md)
- [算术溢出与下溢](hacks/overflow.md)
- [自毁函数](hacks/self-destruct.md)
- [访问私有数据](hacks/accessing-private-data.md)
- [Delegatecall 攻击](hacks/delegatecall.md)
- [随机数预测](hacks/randomness.md)
- [拒绝服务攻击](hacks/denial-of-service.md)
- [tx.origin 钓鱼](hacks/phishing-with-tx-origin.md)
- [使用外部合约隐藏恶意代码](hacks/hiding-malicious-code-with-external-contract.md)
- [蜜罐](hacks/honeypot.md)
- [抢跑](hacks/front-running.md)
- [区块时间戳操纵](hacks/block-timestamp-manipulation.md)
- [签名重放](hacks/signature-replay.md)
- [绕过合约大小检查](hacks/contract-size.md)
- [在同一地址部署不同合约](hacks/deploy-different-contracts-same-address.md)
- [金库通货膨胀攻击](hacks/vault-inflation.md)
- [WETH Permit](hacks/weth-permit.md)
- [63 / 64 Gas 规则](hacks/63-64-gas-rule.md)

## EVM

- [EVM 存储布局](evm/storage.md)
- [EVM 内存布局](evm/memory.md)

## Tests

- [Echidna](tests/echidna.md)

## Foundry

- [Foundry 基础](foundry/basic.md)
- [授权](foundry/auth.md)
- [错误](foundry/error.md)
- [事件](foundry/event.md)
- [发送](foundry/send.md)
- [时间](foundry/time.md)
- [签名](foundry/sign.md)
- [标签](foundry/label.md)
- [Mock Call](foundry/mock-call.md)
- [Store](foundry/vm-store.md)

## DeFi

- [Uniswap V2 Swap](defi/uniswap-v2.md)
- [Uniswap V2 添加与移除流动性](defi/uniswap-v2-add-remove-liquidity.md)
- [Uniswap V2 最优单边供给](defi/uniswap-v2-optimal-one-sided-supply.md)
- [Uniswap V2 Flash Swap](defi/uniswap-v2-flash-swap.md)
- [Uniswap V3 Swap](defi/uniswap-v3-swap.md)
- [Uniswap V3 流动性](defi/uniswap-v3-liquidity.md)
- [Uniswap V3 闪电贷](defi/uniswap-v3-flash.md)
- [Uniswap V3 Flash Swap 套利](defi/uniswap-v3-flash-swap.md)
- [Uniswap V4 Swap](defi/uniswap-v4-swap.md)
- [Uniswap V4 闪电贷](defi/uniswap-v4-flash.md)
- [Uniswap V4 限价单](defi/uniswap-v4-limit-order.md)
- [Chainlink 价格预言机](defi/chainlink-price-oracle.md)
- [Chronicle 价格预言机](defi/chronicle-price-oracle.md)
- [DAI Proxy](defi/dai-proxy.md)
- [质押奖励](defi/staking-rewards.md)
- [离散质押奖励](defi/discrete-staking-rewards.md)
- [Vault](defi/vault.md)
- [Token Lock](defi/token-lock.md)
- [恒定和 AMM](defi/constant-sum-amm.md)
- [恒定乘积 AMM](defi/constant-product-amm.md)
- [Stable Swap AMM](defi/stable-swap-amm.md)

## 关注我们

[Yanbo的Twitter](https://x.com/Yanbo2004)｜[Web3Club的Twitter](https://twitter.com/Web3ClubCN)

[加入我们](https://github.com/Web3-Club/Intro./blob/main/Join%20club.md)
