---
title: 'SNS｜产品拆解（5/100）'
subtitle: '注册一个「链上身份」要花多少钱？带你看懂 SNS 的收费、租金、代币机制'
tags: 产品经理
author: June
cover: /assets/img/post/2025-07-05/cover.jpg
reward: 1
layout: post
date: 2025-07-05
---

# SNS｜产品拆解（5/100）

## 1 产品名称

**SNS（Solana Name Service）**

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2025-07-05/logo.jpg">
![logo]({{site.baseurl}}/assets/img/post/2025-07-05/logo.jpg)
</a>

---

## 2 简介

### 2.1 一句话介绍产品

**Solana 链上的钱包域名系统，是 Solana 版本的 DNS（域名解析系统），让钱包地址变得更易记并且赋予社交属性。**

### 2.2 产品融资情况

**SNS 由 Bonfida 团队主导**，Bonfida 旗下包括链上永续合约 DEX、Solana 域名服务（SNS）、加密消息协议、NFT 市场以及链上交易机器人。

**在种子轮融资中，Bonfida 共募得 450 万美元，用于支持产品开发和生态建设。**

Bonfida 生态内的代币 **\$FIDA** 用于多种功能，包括：**回购与销毁机制、Bonfida 生态内所有产品的交易媒介、链上质押和治理**。

2024 年 7 月 15 日，Bonfida 宣布将 Solana 域名服务品牌正式更名为 SNS，定位为支持所有 Solana 用户链上身份的核心基础设施，并以更中立、开放的姿态服务整个生态。

---

## 3 产品定位

SNS 的核心价值是 **「钱包地址人性化 + 链上身份标识 + 社交货币」。**

### 3.1 钱包地址人性化

在没有 SNS 域名之前，用户只能使用冗长、复杂、几乎无法记忆的钱包地址，如：

```
CUYfv2MEizxmTYRPN32M6CxL6s6woaFufPSoeZ46jMiA
```

这种复杂性直接导致：

* 每次转账都需要复制粘贴，且需**多次核对，极易发生误转**
* 许多人在高额转账前，都会先尝试小额（例如 1 USDC）转账验证

有了 SNS 域名后，用户可以将钱包地址映射为一个可读性极强的域名（如 `june.sol`），不仅**易于记忆、降低错误率，还提升整体转账体验，极大增强用户信任感**。

### 3.2 链上身份标识

SNS 域名除了作为钱包地址映射之外，还能充当用户的 **链上身份标签**，具体表现为：

* 可在 NFT 市场、链游、DAO 等平台中直接展示
* 绑定个性化社交信息（例如 IPFS 链接、X（Twitter）账号等）
* 长远来看，可逐步形成 **Web3 世界的 DID（去中心化身份）入口**

### 3.3 社交货币

在链上社交场景里，一个简洁好记、有辨识度的域名（例如 punk.sol、ape.sol、vitalik.sol）不仅能彰显个性，还有 **「社交货币」的象征意义**。

比如，在群聊或活动中，用户仅凭域名就能被快速识别、获得话题关注，特别适合 Web3 圈层中强调身份与声誉的用户群体。

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2025-07-05/junesol.png">
![logo]({{site.baseurl}}/assets/img/post/2025-07-05/junesol.png)
</a>

---

## 4 核心功能

**域名购买流程示意图**

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2025-07-05/flow.png">
![flow]({{site.baseurl}}/assets/img/post/2025-07-05/flow.png)
</a>

---

## 5 商业模式

### 5.1 代币经济学

2025 年 5 月，SNS 公布代币经济模型，\$SNS 总发行量为 100 亿枚，分配如下：

* 40% 用于现有 .sol 域名持有者、社区用户及合作伙伴
* 20% 预留用于未来社区激励与生态扩展
* 26.25% 用于生态增长，4 年线性解锁
* 5% 作为流动性支持
* 8.75% 分配给核心贡献者（锁仓 4 年）

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2025-07-05/token.jpg">
![token]({{site.baseurl}}/assets/img/post/2025-07-05/token.jpg)
</a>

### 5.2 注册费用与租金机制

当你在 SNS 上购买域名，支付的 SOL 主要包含两块：

#### 1 注册费（Registration fee）

真正用来支付域名注册的费用。

* 1 字符域名：\$750
* 2 字符域名：\$700
* 3 字符域名：\$640
* 4 字符域名：\$160
* 5+ 字符域名：\$20

#### 2 租金抵押（Rent）

按照 Solana 链的账户存储需求预存押金（如 0.0032 SOL），保障账户长期有效，避免被链上「回收」。

在 Solana 上，账户不是免费无限存在的，每个账户包含一定量的数据，需要链上存储空间，如：

* 域名字符串（如 `june.sol`）
* 所有者（Owner）
* 解析地址（比如钱包地址）
* 其他元数据（比如 IPFS link、社交信息等）

链上的存储空间是有限资源，**为了防止链上被垃圾数据占满，Solana 设计了租金机制**，保证：

* 真正需要长期存储的数据有人付费维持
* 不再需要的账户可以被「回收」，释放存储资源

例如，买 `0xjune.sol`，其中 \$20 是注册费，0.0032 SOL 是租金。

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2025-07-05/0xjune.jpg">
![0xjune]({{site.baseurl}}/assets/img/post/2025-07-05/0xjune.jpg)
</a>

### 5.3 产品基础数据

根据官方数据，SNS **近 30 天**（2025 年 6 月至 7 月初）的表现如下：

* 一级注册交易总额（Aggregate volume, registrations）：约 **\$93,970.49（约 33,809 个域名注册）**
* 二级市场成交总额（Aggregate volume, sales）：约 **\$56,685.91（约 1,888 个域名成交）**
* 总成交额（Aggregate volume, all）：约 **\$150,656.44（总交易域名数约 35,697 个）**

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2025-07-05/Volume-registrations.png">
![Volume-registrations]({{site.baseurl}}/assets/img/post/2025-07-05/Volume-registrations.png)
</a>

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2025-07-05/Volume-sales.png">
![Volume-sales]({{site.baseurl}}/assets/img/post/2025-07-05/Volume-sales.png)
</a>

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2025-07-05/Volume-all.png">
![Volume-all]({{site.baseurl}}/assets/img/post/2025-07-05/Volume-all.png)
</a>

再来看更短周期的**近 7 天**（2025 年 7 月）数据，能更直观地反映近期热度与活跃度：

* 新注册域名数量：**超 10,000 个**
* 独立持有人数：**超过 5,000 个，表明用户群体正在快速增长**
* 一级注册成交额：**超 \$20,000，验证域名注册持续受到用户需求支撑**

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2025-07-05/7day.jpg">
![7天数据]({{site.baseurl}}/assets/img/post/2025-07-05/7day.jpg)
</a>

这组数据表明 SNS 在 Solana 生态中逐步形成了**稳定的用户基础**，并具备较好的交易活跃度及二级市场流动性。相比传统 Web2 域名注册服务，**SNS 的注册成本低、去中心化特性强，更易形成投机价值与社交属性的叠加效应。**

数据来源：[SNS 官方数据统计](https://v1.sns.id/stats)

### 5.4 平台收入模型

#### 5.4.1 在二级市场（sns.id）

* **使用 Maker-Taker 费用模型**

  * **Maker（做市商）**：提供流动性的人，比如先挂出域名出售（让别人来买）
  * **Taker（吃单者）**：吃掉流动性的人，比如直接买走域名，或者直接接受别人的挂单
* Maker（挂单方）费率为负，甚至可获得平台返佣（最高返佣 0.5%）
* Taker（接单方）支付手续费（1% \~ 3.5%，根据持有 \$FIDA 数量分级）
* 平台收益 = Taker 手续费 - Maker 返佣

**不同情况对应谁是 Maker、谁是 Taker**

| 交易类型               | Maker | Taker |
|------------------------|-------|-------|
| 固定价格挂单（fixed price） | 卖家  | 买家  |
| 主动报价（unsolicited offers） | 买家  | 卖家  |
| 类别报价（category offers） | 买家  | 卖家  |

例子：

Alice 挂一个域名 2 SOL，Bob 直接买走，Alice = Maker，Bob = Taker

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2025-07-05/example.png">
![交易域名]({{site.baseurl}}/assets/img/post/2025-07-05/example.png)
</a>

**费用标准（Fee Tier）**

平台会根据用户持有的 **\$FIDA** 代币数量来区分费用等级（Tier）。

| 等级（Tier） | 最少持有 $FIDA 数量 | Maker 费率 (%) | Taker 费率 (%) |
|--------------|---------------------|----------------|----------------|
| 0            | 0                   | 0              | 3.5            |
| 1            | 1,000               | 0              | 3              |
| 2            | 10,000              | -0.25          | 2              |
| 3            | 40,000              | -0.3           | 1.3            |
| 4            | 60,000              | -0.5           | 1              |

**Maker 费率为负数，意味着什么？**

当 **Maker 费率是负数（比如 -0.25%）**，代表平台不仅不收 Maker 手续费，还会给 Maker 一笔返佣奖励。

举个例子，若交易额是 2 SOL，-0.25% 意味着平台会给 Maker 回赠 0.005 SOL。

#### 5.4.2 点对点交易（P2P）私下成交

**固定手续费 0.02 SOL，由发起方支付。**

#### 5.4.3 近 30 天平台综合收益预估

为了更准确评估平台的整体盈利能力，我们将平台的收益来源分为两大部分：**一级注册交易收入和二级市场交易收入，并分别进行详细测算和汇总。**

---

**（1）一级注册交易收入**

一级注册交易指的是用户在平台上首次注册域名所支付的官方注册费用，这部分收入全部归平台所有。

根据官网公开数据显示，过去 30 天内，**一级注册交易总收入为 \$93,970.49。**

---

**（2）二级市场交易收入**

二级市场交易收入来自于用户之间的域名买卖，平台通过向成交订单收取手续费来获利。同时，对于部分活跃 Maker，平台还会根据一定规则进行手续费返佣。

* 总成交额：\$56,685.91
* 平均 Taker 手续费率：取区间 1% \~ 3.5% 的中间值，保守假设为 2%
* 平均 Maker 返佣率：保守假设为 0.3%

据此，平台在**二级市场的净收益率**可粗略计算为：

净收益率 = 平均 Taker 手续费率 − 平均 Maker 返佣率
```
= 2% − 0.3%
 = 1.7%
```

接着，计算平台在**二级市场的净收益金额**：

净收益金额 = 总成交额 × 净收益率
```
 = $56,685.91 × 1.7%
 = $963.66
```

---

**（3）平台总收益（近 30 天）**

总收益 = 一级注册收入 + 二级市场净收益

```
= $93,970.49 + $963.66
 ≈ $94,934.15
```

为保持测算的谨慎性，上述结果属于保守估计。

结合过去 30 天的数据，平台的**收入以一级注册交易为主要来源，占比超过 99%。总收入为 $94,934.15。**

---

## 6 市场竞争与合作生态

### 6.1 SNS 和 Ethereum ENS 的比较

| 项目       | Solana SNS         | Ethereum ENS       |
|------------|--------------------|--------------------|
| 费用机制   | 注册费 + Rent 租金 | 注册费 + 每年续费  |
| 是否需要续费 | 不需要             | 需要按年续费       |
| 空间管理方式 | 链上账户存储租金抵押保证持续存在 | 通过续费控制，过期可被抢注 |

### 6.2 生态合作伙伴

域名系统在链上的推广不仅是「技术实现」问题，**更重要的是「生态合作」**。

**为什么合作项目的数量很关键？**

一个域名系统如果只有自己定义的命名规则，但没有其他项目支持解析、显示和调用，**那么用户注册域名后也无法在其他场景中被识别，实际价值会大打折扣**。

**SNS 的生态策略：**

* SNS 在 2022 年后积极与 Phantom、Solflare 等主流钱包以及各大 DeFi、NFT 平台深度合作
* 每一个合作项目，都需在前端与后端中同时**集成 SNS 域名的识别和解析逻辑，支持用户输入域名后自动解析到钱包地址**
* 除钱包外，SNS 还逐步打入 DAO、链游、社交协议，强化域名在**多场景下的使用体验**

截至 2025 年 6 月，SNS 已经完成了与 100+ 个 Solana 项目的集成。

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2025-07-05/eco.png">
![合作生态]({{site.baseurl}}/assets/img/post/2025-07-05/eco.png)
</a>

---

## 7 总结与思考

1. SNS 并不仅仅是一个「简化钱包地址」的工具，更是 Solana 生态的身份基石。它让用户**拥有可读性更高、易传播、更有社交属性的钱包域名**，同时还能与钱包、NFT、DeFi、DAO、GameFi 等场景高度融合，极大提升链上操作的可用性与趣味性。

2. 从**用户体验**角度看，SNS 有效解决了转**账恐惧、地址混淆、重复验证**等传统链上痛点，为「链上身份」构建提供了入口。

3. 从**商业模式**看，通过**注册费用、二级市场手续费、P2P 交易**等收入渠道，既覆盖运营成本，也为生态激励留出空间。

4. **不过，未来仍存在一些挑战和风险，包括：**

   * **链稳定性依赖**：Solana 若发生长时间宕机或性能问题，会直接影响域名解析
   * **市场竞争**：其他多链域名项目也在快速发展，能否保持合作优势和技术领先是关键

总的来看，SNS 既是当前 Solana **用户提升体验的重要工具**，也是未来链上身份经济的**重要基础设施**。

---

### 参考内容

* [Solana 上的一站式商店 — Bonfida 了解一下](https://medium.com/the-oasians/solana%E4%B8%8A%E7%9A%84%E4%B8%80%E7%AB%99%E5%BC%8F%E5%95%86%E5%BA%97-bonfida-%E4%BA%86%E8%A7%A3%E4%B8%80%E4%B8%8B-62d3197674fe)
* [SNS 官方文档](https://docs.sns.id/collection/tokenomics/sns-token)
* [SNS 官方数据统计](https://v1.sns.id/stats)

