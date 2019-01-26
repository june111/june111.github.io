---
layout: post
title: '入门Truffle，看这篇就够了'
subtitle: '拍卖DApp：都来拍一个属于自己的ENS吧'
date: 2019-01-25
author: June
cover: /assets/img/post/2019-01-25/truffle-vue-dapp-demo.png
tags: 区块链
---


## 拍卖 Dapp

### 设计

拍卖 DApp 允许用户注册一个“契约”token，该代币代表一些独特的资产，例如房屋，汽车，商标等。一旦token被登记，token的所有权将转移到拍卖 DApp，允许它进行拍卖。拍卖 DApp 列出了每一个已登记的token，允许其他用户进行出价。在每次拍卖期间，用户可以加入专门为该拍卖创建的聊天室。拍卖完成后，契约token所有权将转移给拍卖的获胜者。

整个拍卖的过程

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-25/auction_diagram.png">
![拍卖过程]({{site.baseurl}}/assets/img/post/2019-01-25/auction_diagram.png)
</a>

我们拍卖 DApp 的主要组成部分是：

* 实施，[ERC721](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-721.md)，不可替换代币的智能合约（`DeedRepository`）
* 实施拍卖（`AuctionRepository`）以出售"契约"的智能合约
* 使用Vue / Vuetify 作为Web前端
* web3.js库连接到以太坊链（通过MetaMask或其他客户端）
* 一个Swarm客户端，用于存储图像等资源
* 一个Whisper客户端，为所有参与者创建每个拍卖聊天室

### 后端（智能合约）

我们的拍卖 DApp 示例由两个智能合约支持，我们需要在以太坊区块链上部署这些合约以支持应用程序：`AuctionRepository` 和 `DeedRepository`。

[DeedRepository.sol](https://github.com/june111/truffle-vue-dapp-demo/blob/master/contracts/DeedRepository.sol)：在拍卖中使用的 ERC721 契约 token。这个合约是 ERC721 标准的，不可替换代币的智能合约。我们可以在拍卖 DApp 中使用这个合约去发放和跟踪 token。

[AuctionRepository.sol](https://github.com/june111/truffle-vue-dapp-demo/blob/master/contracts/AuctionRepository.sol)：实施拍卖的主要合约，此合约管理了所有拍卖的相关功能。

#### DApp 管理

如果您仔细阅读拍卖 DApp 的两个智能合约，您会注意到一些重要的事情：没有特殊的帐户或角色对 DApp 有特殊的权限。每次拍卖都有一个具有一些特殊功能的所有者，但拍卖 DApp本身没有特权用户。

这是分布式 DApp 治理权并在部署后放弃任何控制权的有意选择。相比之下，一些DApp具有一个或多个具有特殊功能的特权帐户，例如终止 DApp 合约，覆盖或更改其配置或“否决”某些操作的能力。通常，这些治理功能在 DApp 中引入，以避免由于错误而可能出现的未知问题。

治理问题是一个特别难以解决的问题，因为它代表了一把双刃剑。一方面，特权账户是危险的; 如果受到损害，他们可以破坏DApp的安全性。另一方面，没有任何特权帐户，如果发现错误，则没有恢复选项。我们已经看到这些风险在以太坊 DApps 中都有所体现。在DAO的情况下，有一些特权帐户称为“监护人”，但他们的能力非常有限。这些帐户无法阻止DAO攻击者并撤回资金。在最近的一个案例中，去中心化交易所 Bancor 经历了大规模的盗窃，因为特权管理帐户遭到了破坏。事实证明，Bancor 没有像最初假设的那样去中心化。

在构建 DApp 时，您必须决定是否要使智能合约真正独立，启动它们然后无法控制，或者创建特权帐户并冒着受到攻击的风险。任何一种选择都存在风险，但从长远来看，真正的 DApps 无法对特权帐户进行专门访问 - 这种权限不是去中心化的。

### 前端（用户界面）

一旦部署了拍卖 DApp 的合约，您就可以使用 JS 和 web3.js 或其他 web3 库与它们进行交互。但是，大多数用户需要易于使用的界面。 我们的拍卖 DApp 用户界面是使用 Vue 和 Google 的 Vuetify 构建的。

部署合同后，修改 src/config.js 中的配置，并输入 DeedRepository 和 AuctionRepository 的合约地址。 前端应用程序还需要访问提供 JSON-RPC 和 WebSockets 接口的以太坊节点。 配置前端后，在本地计算机上使用Web服务器启动它：















---

觉得文章不错就扫码支持一下呗～

![打赏二维码]({{site.baseurl}}/assets/img/post/pay-qr.jpg)

### 参考链接

* [Decentralized Applications (DApps)](https://github.com/ethereumbook/ethereumbook/blob/04f66ae45cd9405cce04a088556144be11979699/12dapps.asciidoc)
* []()
* []()
* []()
* []()
* []()
* []()

