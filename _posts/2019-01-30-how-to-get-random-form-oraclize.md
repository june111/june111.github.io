---
layout: post
title: '用 Oraclize 在智能合约中获得随机数'
subtitle: '智能合约中生成较安全的随机数(3)'
date: 2019-01-30
author: June
reward: 1
cover: /assets/img/post/2019-01-30/cover.jpg
tags: 区块链
---

# 用 Oraclize 在合约中获得随机数

Oraclize 提供可证明的预言机服务。可以使用 Oraclize 提供的数据源类型（URL, WolframAlpha, random），来生成随机数。

我分别用这三种数据源类型写了三个合约，做了个简单的 Dome 调取合约。[线上版本](http://blog.junezhu.top/dapp-fun-test/)效果图如下：

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-30/demo.png">
![Demo]({{site.baseurl}}/assets/img/post/2019-01-30/demo.png)
</a>

## 环境准备

1. 用 [Remix](https://remix.ethereum.org/#optimize=false)，或 [oraclize 的 IDE](http://dapps.oraclize.it/browser-solidity/)。要把编译合约的版本改为 0.4.25。

2. 把 Environment 切换到 JavaScript VM

3. 到 Settings 把 Oraclize 的插件打开

## 智能合约编写

三种方法的合约内容大同小异，以下是三种方法的对比：

### 用外部接口

速度：时快时慢，用时 00:01-2:00

可以用 Remix 部署合约

要进行真实性验证

Oraclize 关键代码
```js
bytes32 queryId =  oraclize_query("URL", "json(https://randomapi.com/api/?key=PZFO-VK8M-XV6H-H92P&ref=y5kkh9i8).results[0].numeric");
validIds[queryId] = true;
```

### 用 Oraclize 的 random 生成器

速度：用时 00:30-2:00

不能用 Remix 和 Oraclize 的 IDE 部署合约

要进行真实性验证

Oraclize 关键代码
```js
uint N = 7; // number of random bytes we want the datasource to return
uint delay = 0; // number of seconds to wait before the execution takes place
uint callbackGas = 200000; // amount of gas we want Oraclize to set for the callback function
bytes32 queryId = oraclize_newRandomDSQuery(delay, N, callbackGas); // this function internally generates the correct oraclize_query and returns its queryId
```

### 用 Oraclize 的 WolframAlpha（问人工智能）

速度：用时 00:30-2:00

可以用 Remix 部署合约

Oraclize 关键代码
```js
oraclize_query("WolframAlpha", "random number between 0 and 100");
```

---

### 参考链接

* [oraclize 文档](https://docs.oraclize.it/)