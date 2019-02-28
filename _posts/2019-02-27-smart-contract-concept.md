---
title: '开发智能合约的基本理念'
subtitle: '智能合约开发学习笔记(1)'
tags: 区块链
author: June
cover: /assets/img/post/2019-02-27/cover.png
reward: 1
layout: post
date: 2019-02-27
---

# 开发智能合约的基本理念

## 基本理念

### 开发理念

* 对可能的错误有所准备

	* 当智能合约出现错误时，停止合约，（“断路开关”）
	* 管理账户的资金风险（限制（转账）速率、最大（转账）额度）
	* 可更新的合约。有效的途径来进行bug修复和功能提升

* 谨慎发布智能合约。尽量在正式发布智能合约之前发现并修复可能的bug。

	* 从alpha版本在测试网（testnet）上发布开始便提供bug赏金计划

* 保持智能合约的简洁。复杂会增加出错的风险。

	* 确保智能合约逻辑简洁
	* 确保合约和函数模块化
	* 使用已经被广泛使用的合约或工具（比如，不要自己写一个随机数生成器）
	* 只在你系统的去中心化部分使用区块链

* 保持更新。通过下一章节所列出的资源来确保获取到最新的安全进展。

	* 在任何新的漏洞被发现时检查你的智能合约
	* 尽可能快的将使用到的库或者工具更新到最新
	* 使用最新的安全技术

* 清楚区块链的特性。尽管你先前所拥有的编程经验同样适用于以太坊开发，但这里仍然有些陷阱你需要留意：

	* 特别小心针对外部合约的调用，因为你可能执行的是一段恶意代码然后更改控制流程
	* 清楚你的public function是公开的，意味着可以被恶意调用。（在以太坊上）你的private data也是对他人可见的
	* 清楚gas的花费和区块的gas limit

### 基本权衡：简单性与复杂性

* 固化 vs 可升级
* 庞大 vs 模块化
* 重复 vs 可重用

---

### 参考链接

* [以太坊智能合约 —— 最佳安全开发指南](https://github.com/ConsenSys/smart-contract-best-practices/blob/master/README-zh.md)
* [Ethereum Smart Contract Security Best Practices](https://consensys.github.io/smart-contract-best-practices/)
