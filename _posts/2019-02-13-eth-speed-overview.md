---
title: '区块链扩展性问题概述'
subtitle: '主要谈谈扩容解决方案'
tags: 前端
author: June
cover: /assets/img/post/2019-02-13/cover.png
reward: 1
layout: post
date: 2019-02-13
---

# 区块链扩展性问题概述

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-02-13/structure.svg">
![文章结构]({{site.baseurl}}/assets/img/post/2019-02-13/structure.svg)
</a>

## 基础概念

### PoW（工作量证明，Proof of Work）

PoW，就是大家熟悉的挖矿，通过数学运算，计算出一个满足规则的随机数，即获得本次记账权，发出本轮需要记录的数据，全网其它节点验证后一起存储。

使用者：Bitcoin、Ethereum、Litecoin等。

### PoS（权益证明，Proof of Stake）

PoS，Pow的一种升级共识机制；根据每个节点所占代币的比例和时间；等比例的降低挖矿难度，从而加快找随机数的速度。

使用者：Ethereum（即将推出）、Peercoin、Nxt

### DPoS（委托权益证明，Delegated Proof-of-Stake）

DPoS 原理是让每一个持有比特股的人进行投票，由此产生101位代表, 我们可以将其理解为101个超级节点或者矿池，而这101个超级节点彼此的权利是完全相等的。

使用者：BitShares、Steemit、EOS、Lisk、Ark

### TPS

TPS，就是“系统每秒钟能够处理的业务数量”，通俗的定义，就是“系统的吞吐量”。

TPS = 并发数/平均响应时间

对于比特币而言，并发数就是一个区块链里包含的数据大小，目前一个区块的大小是2118。

平均响应时间就是打包一个区块的时间，也就是10分钟，600秒。

那么比特币的TPS=2118÷600=3.53

## 区块链的TPS

下表是比特币，以太坊，EOS，Fabric 的 TPS 对比：

|||共识|区块大小|出块时间|确认时间|每区块交易数量|TPS|
|:--|:--|:--- |:---|:--|:--|:--|:--|
|公链|比特币|POW|1M|10分钟 |60分钟|1500-2000笔|4|
| |以太坊|POW|2KB以下|15秒|3分钟|70笔交易|20|
| |EOS 2.0|DPOS| |0.5秒|1秒||百万TPS|
|联盟链|Fabric|Kafka|64M|可配置|可配置|可配置|商业级TPS|

## 为什么区块链的可扩展性这么差呢？

区块链是去中心化的账本技术，需要保证开放性、自治性、不可篡改等特性。去中心化是指使用分布式核算和存储，不存在中心化的硬件或管理机构，任意节点的权利和义务都是均等的，系统中的数据块由整个系统中具有维护功能的节点来共同维护。也就是说，系统中任意节点都需要对交易数据进行全量计算和存储。因此，区块链是没有可扩展性的，即系统的总体性能受限于单个节点的性能上限，即使加入了大量节点，系统的总体性能也无法提升。

可扩展性是传统分布式系统的基本特性，但区块链由于去中心化的要求，可扩展性却难以满足。业界总结了一个三元悖论描述去中心化与可扩展性之间的矛盾，它尚未被严格证明，只能被称为猜想，但实际系统设计过程中却能感觉到时时受其挑战：

去中心化(Decentralization)，安全性(Security)和可扩展性(Scalability)这三个属性，区块链系统无法同时满足，最多只能三选其二。

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-02-13/reason.jpeg">
![速度慢的原因]({{site.baseurl}}/assets/img/post/2019-02-13/reason.jpeg)
</a>

上图演示了区块链如何在这三个因素之间作选择及对应的策略，例如若要满足安全性与去中心化，则需要所有节点参与共识、计算、全量存储，但由此带来的问题是失去可扩展性，也就是系统的总体性能无法随着节点的增多而提升；若要满足可扩展性与安全性，则需要中心化管理，需要保证参与共识的节点是可信的；若要满足可扩展性与去中心化，则采用分散存储、计算的策略，不做全量共识，则攻击网络的难度降低，安全性难以保证。

## 扩容解决方案

借鉴计算机网络分层管理、各层标准化设计的思想，将区块链与传统互联网 OSI 模型结合，建立区块链技术可扩展方案分层模型三个一级层级：Layer 0 层数据传输层，Layer 1 层 On-Chain 公链自身（底层账本）层和 Layer 2 层 Off-Chain 扩展性（应用扩展）层。

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-02-13/layers.png">
![区块链分层研究构架图]({{site.baseurl}}/assets/img/post/2019-02-13/layers.png)
</a>

### 第一层（layer 1）

第一层扩容技术，即改进区块链自身，把区块链自身变的更快、容量变的更大。其实，区块链是一个项目，它本身是由很多个部分组成的。由下往上分别是P2P的网络、共识机制、虚拟机、区块链的编程语言，每一部分都有很大的发展和改进的空间。

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-02-13/layer1.png">
![第一层]({{site.baseurl}}/assets/img/post/2019-02-13/layer1.png)
</a>

在第一层的改进方案中，最引人瞩目的就是分片这块的内容。

#### 分片（Sharding）

分片（Sharding）是以太坊正在开发中的，一种链上扩容技术，旨在提升协议基础层的容量。

总体思路是每个节点只处理一部分交易，比如一部分账户发起的交易，从而减轻节点的计算和存储负担。

其大致设计思路是：将区块链网络中的每个区块变为一个子区块链，子区块链中可以容纳若干（目前为100个）打包了交易数据的Collation（大概可以称为“校验块”，为了在分片的情景中将其与区块的概念区分开），这些Collation最终组成一个在主链上区块；因为这些Collation是整体作为区块存在的，所以其数据必定是全部由某个特定的矿工所打包生成，本质上和现有协议中的区块没有区别，所以不再需要增加额外的网络确认。这样，每个区块的交易容量就大概扩大了100倍；而且这种设计还有利于未来的继续扩展。

关于分片的开发进度，以太坊 2.0 中提到了一个基于 POS 共识机制的信标链（英文叫 beacon chain，在第四阶段，也就是全面实现 Casper 的阶段，这个信标链会被合并到以太坊主链中），和以太坊主链绑定在一起。每一个信标链的区块，必须指定一个最近的主链区块。这个信标区块是否从属于标准链（canonical chain）的一部分，则取决于信标区块对应的主链区块是否属于标准链的一部分。

### 第二层（layer 2）

第二层扩容技术，目的是把计算移到链下。怎么来理解第二层扩容技术呢? 举一个例子，最近有一个比较火的云斗龙区块链游戏，游戏玩家通过让龙去战斗，让龙升级，然后得奖金。龙的整个战斗过程，如果放到链上，玩家在玩游戏的时候就需要很多的燃料费，并且还要花时间等交易的确定，游戏体验非常不好。因此使用第二层扩容技术，把战斗过程放到链下，最后只把结果给存到链上，这样就会大大改善游戏的体验。这就是第二层技术的一个基本思路。

#### 侧链

这里举一个简单的应用场景，帮助大家理解侧链。假设你们公司有一百个员工，因为需要协同工作等原因，员工之间可以通过发一点比特币作为回报，但是你不想每一笔交易都发到链上，而是希望员工之间可以自由的进行交易，同时速度也非常的快。基于这种场景，一种非常直接的交易方式就是所谓的侧链。

首先，你们公司得有自己的一个区块链，然后决定矿工以及服务器的数量。假设我是公司里的一名员工，需要先把比特币存进多重签名钱包里面，这个多重签名钱包需要矿工的签名同意，才能使用里面的资金。所以，员工第一步就是把钱存到这个钱包里面，由矿工签名，签完名之后员工自己在这个公司里面就有了一个钱包。通过这种方式，员工就把主链上的币转到侧链上。而侧链上支撑的功能和主链是一样的，可以交易，所以交易速度就可以更快。而侧链是公司自己跑的，也不会收取你的手续费。

显然，对于用户来说，侧链的优势很明显。不过，因为侧链只是在公司内部跑，服务器比较少，会不会很容易受到黑客攻击呢? 其实，这也是传统侧链的问题，很可能矿工把你的资产给偷走了，这就需要你信任矿工。这里会产生信任问题。

Cosmos 和 Polkadot 是运用了侧链技术的项目。

* Cosmos

	[Cosmos](https://cosmos.network/) 的目的是解决区块链交互操作和可扩展性问题，其区块链间通讯协议可以实现区块链的互联，支持不同区块链之间的资产转移。

	进度：[Cosmos Network](https://github.com/cosmos/ethermint) 还在研发中

* Polkadot

	[Polkadot](https://polkadot.network/) 是一种异构多链交互架构，可以使定制的侧链与公共区块链连接。使用 Polkadot，各种区块链能够以安全和去信任的方式在彼此之间发送和接收消息。

	进度：[Polkadot Network](https://github.com/polkadot-js/apps) 还在研发中

#### Plasma：把数据放在链外

是一种链下扩容解决方案。Plasma 项目将区块链设计为树状结构，使用大量“子区块链”来分担主链上的数据储存量，每个子链都能处理和维护它自己的转账记录，同时使用特定技术实现“主链”与“子链”的连接，由主链维护其安全性，主链只需在子链中出现争议时才进行计算，从而实现最优化交易处理速度和效率。如果子链上的节点愿意，它们也可以提交转账信息并输出他们的转账记录到主链。

该方案允许每个 Plasma 链都可以有自己的标准，也即不同子链可以支持有不同需求的交易(如私有链)，且所有交易都处在同样安全的生态系统内。

Plasma 也存在一些问题，第一个是你只能用来做资产交易;第二个问题是需要等待在链上确认交易;第三个想要确保你的资产安全，你需要一直监视主链，你如果没有监视，你的资产还是可能会被偷走。

运用 Plasma 开发的项目有 OmiseGO 和 Loom Network。

* OmiseGO

	[OmiseGO](https://omisego.network/) ，OMG 网络，是基于 POS，使用了 Plasma 架构的区块链。

	进度：[Omise 商户平台](https://www.omise.co/developers) 已上线，类似 PayPal

* Loom Network

	[Loom](https://loomx.io/) 是一个以太坊的区块链应用平台。

	进度：[Loom SDk](https://loomx.io/developers/docs/en/intro-loom-sdk.html) 已上线

#### 状态通道（State Channels）

相对于Plasma只能用来做资产交易这个痛点，状态通道可以通过写一个智能合约，可以让你在链下执行任意程序。不过，发起一笔交易时，状态通道首先要在链上创造一个多重签订合约;接下来，是在链下接受这笔交易或者状态的更新，每一笔交易多重合约里面所有人都要签名;而合约发布最终的更新，会检查所有人是否都签名了。

但是，状态通道还是有些问题，一个最明显的问题就是用户的数量需要固定，假如用户不固定的，毫无安全性可言。第二个问题是每一笔交易都需要所有人签名，比如玩一个游戏，每一笔交易都需要几千人签名，这笔交易就行不通了。第三个问题你还是需要监视主链，比如想让一些老的交易退出来，你自己需要用更新的交易去挑战之前的老交易。

以下是运用了状态通道技术的项目：

* Lightning Network（闪电网络）

	[Lightning Network](https://lightning.network/) 是一种支付协议，在基于区块链的加密货币中（如比特币）运行。 它支持参与节点之间的快速交易，并被吹捧为比特币可扩展性问题的解决方案。 它具有点对点系统，可通过双向支付渠道网络进行加密货币的微支付，而无需委托资金保管。

	进度：[Lightning Network Daemon (LND)](https://github.com/lightningnetwork/lnd) 已上线

* Raiden（雷电网络）：把一部分交易放在链外

	[雷电网络（Raiden Network）](https://raiden.network/) 是一种利用链下支付通道网络实现以太坊扩容的技术。该项目始于2015年，与比特币上的闪电网络原理类似，雷电技术把以太坊区块上的绝大多数交易转移至链外处理，允许用户通过私下交换转账签名信息实现交易，从而大幅度增加交易处理速度。

	雷电网络方案的主要好处是，能大幅降低每笔交易的燃料费用，但它也主要适用于经常性小额支付场景。

	进度：[Red Eyes](https://github.com/raiden-network/raiden/releases/tag/v0.100.1) 已上线

* Celer Network

	[Celer Network](https://www.celer.network/) 是一个互联网规模，无需信任，保护隐私的平台，每个人都可以快速构建，运营和使用高度可扩展的分散式应用程序。 它不是一个独立的区块链，而是一个在现有和未来区块链之上运行的通用网络系统。 它通过创新脱链扩展技术和激励一致的加密经济学提供前所未有的性能和灵活性。

	进度：[cPilot SDK](https://celer-network.github.io/docs/guide?utm_source=website&utm_medium=organic&utm_campaign=cn) 还在研发中

* [Counterfactual](https://counterfactual.com/) 是一个能在以太坊上推行使用状态通道的框架。由 L4 团队开发。

	进度：[Counterfactual](http://github.com/counterfactual) 还在研发中

* [Funfair](https://funfair.io/) 是去中心化赌博平台。

	进度：Fate channels，已上线，但没有放出开发者文档链接

* [Horizon Games](https://horizongames.net/) 是视频游戏平台，

	进度：[Arcadeum](https://arcadeum.net/) 已上线，[GitHub](https://github.com/horizon-games/arcadeum)；[skyweaver](https://skyweaver.net/) 已上线

* [Spankchain](https://spankchain.com/) 是基于区块链的支付处理器和直播视频流平台。关注的是成人娱乐产业。用的是one-way payment channels
	
	进度：[成人视频直播网站](https://beta.spankchain.com/) 已上线

#### 十倍协议（tenfold protocol）

[十倍协议（tenfold protocol）](https://tenfoldprotocol.io/) 是区块链初创企业 Binary Mint 发布的一项新型扩容方案，它用于安全地维持一个链下状态机，同时能在链上读取其状态。

首先你在链上锁定资产，在链下将交易通过P2P网络广播给验证者，这些验证者可以通过一个去中心化的文件系统，去下载应用的本身。比如，每个验证者都会在本地跑一套云斗龙这款游戏，链下的交易是通过P2P广播的，每一个验证者都可以知道云斗龙的情况。

和所有的系统一样，十倍协议也有问题。假如你买超过50%的经济体，确实可以攻击这个系统;另外需要解决怎么样激励验证者。

相关实现：[云斗龙（Hyper Dragons）](http://hyperdragons.alfakingdom.com/)，已上线

#### Truebit

[Truebit](http://truebit.io/) 是一种帮助以太坊在链下进行繁重或者复杂 运算的技术。它对于提高以太坊区块链的总交易通量更有效，这使得它与状态通道和 Plasma 不一样。

进度：[Truebit](https://github.com/TrueBitFoundation/truebit-os) 还在研发中

### 总结

综上，一般开发者可以用的平台，似乎只有 Loom。我去试一下，再来发使用体验。

---

### 参考链接

* [TPS:如何正确认识区块链上的TPS吞吐量](https://www.bitguai.com/xueyuan/rumen/25168.html)
* [一文读懂11个主流共识算法, 彻底搞懂PoS,PoW,dPoW,PBFT,dBFT这些究竟是什么鬼](https://www.tuoniaox.com/news/p-287193.html)
* [10分钟搞懂区块链扩容，4个解决方案拿走不谢](http://www.btb8.com/rookie/1809/14041.html)
* [【火币区块链产业专题报告】区块链技术可扩展方案分层模型](https://research.huobi.cn/detail/35)
* [都说百万TPS：EOS、迅雷链、以太坊，谁才是区块链3.0的领航者？](https://cloud.tencent.com/developer/article/1151194)
* [Making Sense of Ethereum’s Layer 2 Scaling Solutions: State Channels, Plasma, and Truebit](https://medium.com/l4-media/making-sense-of-ethereums-layer-2-scaling-solutions-state-channels-plasma-and-truebit-22cb40dcc2f4)
* [深度拆解以太坊八大扩容路，V神选择了最难的那条！](https://wallstreetcn.com/articles/3414335)
* [区块链的可扩展性问题及解决方案对比](https://www.odaily.com/post/5134016)
