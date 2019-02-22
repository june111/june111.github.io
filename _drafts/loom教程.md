---
title: 'Loom 做一个dapp'
subtitle: ''
tags: 前端
author: June
cover: /assets/img/post/2019-02-02/cover.png
reward: 1
layout: post
date: 2019-02-02
---

# 

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-02-02/structure.svg">
![文章结构]({{site.baseurl}}/assets/img/post/2019-02-02/structure.svg)
</a>

## loom 基础

### 什么是 Loom SDK

Loom Network 的核心产品是一款 SDK，可以让开发者快速构建自己的区块链，而无需了解区块链基础架构。把它想成是一个“构建你自己的区块链”的生成器。

### 什么是 DAppChains

DAppChain 是一个特定于应用程序的侧链，平行于主链运行，在这种情况下，主链就是以太坊。 它的规则集是基于用例自定义的，其安全性由主链的共识算法维护。

开发人员将能够使用 Loom 的软件开发工具包（SDK）为一个 DApp 链生成基础。

然后，他们可以专注于编写应用程序逻辑，SDK 会帮他们处理所有区块链逻辑。

Loom Network 通过将主链的计算卸载到 DApp 链上，有助于扩展，同时仍然允许在安全的区块链上运行的 DApp 的存在。

### 什么是 Plasma

Plasma 让用户可以将他们的数字资产从以太坊主网安全地转移到侧链上，而无需信任侧链的共识算法。

通过在我们的 DApp 链上实施 Plasma，我们能确保资产所有者有更好的安全性，并允许在侧链上运行更多的关键操作。

### 什么是 Plasma Cash

Plasma Cash 使用户能够安全地将代币等资产转移到侧链上。Plasma Cash 通过将你存储在侧链上的代币与一个独一无二的序列号关联来实现此目的。 代币是不可替代的，并具有自己的交易历史记录。 这让币历史上的证明更简洁以及提供了“零确认”交易的可能性。

因此，交易所和游戏可以从中受益，因为它们可以在一条高效的侧链上进行操作。并且在遭遇黑客攻击和诈欺的情况下，用户可以通过 Plasma 出口，在以太坊主链上收回其资金或稀有收藏品。

### 什么是 LOOM Token

LOOM 代币用于Loom Network提供的所有产品和服务。

用处：

* 开发者：锁定 & 支付代币将 DApp 运行在 ZombieChain 僵尸链（及其他未来推出的共享链）上
* 开发者：Loom SDK 的企业支持
* 用户：“僵尸战场”游戏会员福利
* 用户：访问Loom转移网关
* 开发者：Loom SDK许可证等级 & 运行节点

### PlasmaChain

用于在侧链和以太坊主网之间进行交易的受Plasma Cash支持的枢纽。

之前叫做ZombieChain，后来我们将其重新构建、重新命名为PlasmaChain并发布。

作为中心枢纽，它充当多个侧链和以太坊之间的桥梁，PlasmaChain将成为我们愿景中最重要的组成部分之一

## 开发环境

安装 Loom 并设置开发环境

在我们的系统上安装 Loom 二进制文件，这样我们就可以有一个本地链来测试。

```bash
curl https://raw.githubusercontent.com/loomnetwork/loom-sdk-documentation/master/scripts/get_loom.sh | sh && chmod +x loom
```

初始化 genesis 文件和 chaindata 目录

```bash
./loom init
```

启动我们的链

```bash
./loom run
```

默认情况下，该链在端口46657上运行，如果我们愿意，可以使用提供的区块浏览器实时查看交易：

[https://blockexplorer.loomx.io/](https://blockexplorer.loomx.io/)

会出现报错，忽略就可以了，因为现在是在单个节点上运行
```bash
E[14026-02-14|09:48:04.964] Couldn't connect to any seeds                module=p2p
```

生成密钥
```bash
./loom genkey -k priv_key -a pub_key
```

结果

```bash
local address: 0x662ec5C2d4FaDb8cc9459D28986F5aA891bC23C0
local address base64: Zi7FwtT624zJRZ0omG9aqJG8I8A=
```

这一步会在你包含密钥的目录中创建 priv_key 和 pub_key 文件。 请注意，它将以编码格式保存你的密钥，并且我们需要访问它输出的原始公钥，因此请确保将本地地址公钥输出保存在某处，以便我们以后可以轻松访问它。

MyToken Contract Address: 0x04aed4899e1514e9ebd3b1ea19d845d60f9eab95
MyCoin Contract Address: 0x60ab575af210cc952999976854e938447e919871

```bash
cd truffle-dappchain-example
```


```bash
# copy the private key generated earlier to the root directory of the example repo
cp ../priv_key extdev_private_key
```

yarn deploy:reset

yarn serve

部署到 loom 测试网络
yarn deploy:extdev

部署到 rinkeby 测试网络

生成地址：
生成私钥：
yarn gen:rinkeby-key

获取地址：
cat rinkeby_account 
结果：
0x949BFAA842A1fca61C0fb03d61A93fB3c4d7f4eC

往这个地址转些eth，以便部署合约

设置Infura API key
export INFURA_API_KEY=323e44018f994f0c97025d409eb79344

部署合约
```bash
yarn deploy:rinkeby
```

修改 contract.js

```js
...
this.client = new Client(
      'default',
      'ws://127.0.0.1:46658/websocket',
      'ws://127.0.0.1:46658/queryws',
    )
...
this.currentNetwork = SimpleStore.networks[4]
```
https://loomx.io/developers/docs/en/extdev-transfer-gateway.html#5-token-transfer

https://github.com/loomnetwork/dashboard/blob/5904223f26dc0796c07ab6f41de8871ea4974594/src/store/dappChainStore.js

---

### 参考链接

* [DApp链：通过侧链扩展以太坊DApp](https://medium.com/loom-network-chinese/dapp%E9%93%BE-%E9%80%9A%E8%BF%87%E4%BE%A7%E9%93%BE%E6%89%A9%E5%B1%95%E4%BB%A5%E5%A4%AA%E5%9D%8Adapps-1f7648f117a6)
* [Plasma on Loom Network DAppChains: Scalable DApps With Ethereum-Secured Assets](https://medium.com/loom-network/loom-network-plasma-5e86caaadef2)
* [Everything You Need to Know About Loom Network, All in One Place (Updated Regularly)](https://medium.com/loom-network/everything-you-need-to-know-about-loom-network-all-in-one-place-updated-regularly-64742bd839fe)
* [LOOM代币FAQ－你的问题，我们有答案！](https://medium.com/loom-network-chinese/loom%E4%BB%A3%E5%B8%81faq-%E4%BD%A0%E7%9A%84%E9%97%AE%E9%A2%98-%E6%88%91%E4%BB%AC%E6%9C%89%E7%AD%94%E6%A1%88-3eb8e8f5bf31)
* []()
* []()