---
layout: post
title: '以太坊智能合约随机数的生成方法'
subtitle: '智能合约中生成较安全的随机数(1)'
date: 2019-01-28
author: June
reward: 1
tags: 区块链
---

# 以太坊智能合约随机数的生成方法

**在区块链领域需要记住一些权衡和关键点。**

1. 用户做出的任何可以影响结果的决定，都会给该用户带来的优势。例子包括：

	1. 使用blockhash，timestamp或其他矿工定义的值。 请记住，矿工可以选择是否发布一个区块，因此他们可以假设每个区块有一次机会获得奖金。
	2. 任何用户提交的随机数。 即使用户预先提交了一个号码，他们也可以选择是否显示该号码。

2. 公众可以看到合约里的一切。

	* 这意味着在开奖之前都不应该生成该号码。

3. EVM不会超越物理计算机。

	合约生成的任何数字可能在该块出块之前已知。要在数字的生成和使用之间留出时间。

## 不安全的数据来源

随机数，即不可预测的数，所有可预测的数据来源都是不可靠的，如区块变量

1. block.coinbase 表示当前区块的矿工地址
2. block.difficulty 表示当前区块的挖掘难度
3. block.gaslimit 区块内交易的最大限制燃气消耗量
4. block.number 表示当前区块高度
5. block.timestamp 表示当前区块挖掘时间

接下来说一下较安全伪随机数的产生方法

## oraclize

* 一个可证明的诚实的预言机服务，可以让智能合约访问互联网
* 考虑一个提供打赌的智能合约。 用户调用打赌的接口，这个接口会把用户的请求存储起来，然后调用Oracle随机数生成服务。 然后通过Oracle回调服务，判断随机数是否大于某个值，如果成立，那么用户成功，否则用户失败。

## RANDAO

* 一个生成以太坊随机数的去中心化组织

## Signidice

1. 玩家通过调用智能合约进行下注。
2. 庄家看到赌注，用私钥将之签名，然后将签名发送给智能合约。
3. 智能合约使用公钥验证此签名。
4. 此签名则能够用于生成随机数。

## Commit–reveal approach

1. ”提交”阶段 : 一方提交加密内容给向智能合约。
2. ”揭示”阶段 : 一方宣布明文种子，智能合约验证它们的正确性，并使用此种子生成随机数。

---



### 参考链接

* [以太坊随机数生成方式](https://github.com/ZtesoftCS/go-ethereum-code-analysis/blob/master/%E4%BB%A5%E5%A4%AA%E5%9D%8A%E9%9A%8F%E6%9C%BA%E6%95%B0%E7%94%9F%E6%88%90%E6%96%B9%E5%BC%8F.md)
* [randao/README](https://github.com/randao/randao/blob/master/README.md)
* [以太坊智能合约中随机数预测](https://www.freebuf.com/vuls/179173.html)
* [How can I securely generate a random number in my smart contract?](https://ethereum.stackexchange.com/questions/191/how-can-i-securely-generate-a-random-number-in-my-smart-contract)



