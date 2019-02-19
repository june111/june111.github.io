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

Loom Network的基本构建块是一个SDK，允许开发人员快速构建自己的区块链，而无需了解区块链基础设施。 可以把它想象成“构建自己的区块链”生成器。

### 什么是 DAppChains

DAppChain是一个特定于应用程序的侧链，在这种情况下，它与主链（以太坊）并行运行。 它的规则集是根据用例定制的，其安全性由主链的一致性算法维护。

开发人员将能够使用Loom的软件开发工具包（SDK）为DAppChain创建基础。

然后，他们可以专注于编写应用程序逻辑，同时为他们处理所有区块链逻辑。

Loom Network 通过将主链负责的计算转移到 DAppChains 上，来实现扩展，同时允许在区块链上安全地运行 DApp。

### 什么是 Plasma

Plasma 允许用户将他们的数字资产安全地转移到以太坊主网的侧链上，而无需信任侧链的一致性算法。

通过在我们的 DAppChains 上实施 Plasma，我们可以确保资产所有者更好的安全性，并允许在侧链上运行更多关键操作。

### 什么是 Plasma Cash

Plasma Cash 允许用户安全地将诸如令牌之类的资产转移到侧链上。

它通过将您存入的令牌与唯一的序列号相关联来实现此目的。 令牌是不可替代的，并且具有自己的交易历史。 这样可以在硬币历史上进行更紧凑的校样，并可以进行零确认交易。

因此，交换和游戏可以从中受益，因为它们可以在有效的侧链上运行，并且在黑客或欺诈的情况下，用户可以通过等离子出口回收其在以太坊主链上的资金或稀有收藏品。



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

* [DAppChains: Scaling Ethereum DApps Through Sidechains](https://medium.com/loom-network/dappchains-scaling-ethereum-dapps-through-sidechains-f99e51fff447)
* [Plasma on Loom Network DAppChains: Scalable DApps With Ethereum-Secured Assets](https://medium.com/loom-network/loom-network-plasma-5e86caaadef2)
* [Everything You Need to Know About Loom Network, All in One Place (Updated Regularly)](https://medium.com/loom-network/everything-you-need-to-know-about-loom-network-all-in-one-place-updated-regularly-64742bd839fe)
* []()
* []()
* []()