---
layout: post
title: '以太坊智能合约随机数的生成方法'
date: 2019-01-28
author: June
cover: /assets/img/post/2019-01-28/eth-random-number-generation.png
tags: 区块链
---

# 以太坊智能合约随机数的生成方法

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

觉得文章不错就扫码支持一下呗～

![打赏二维码]({{site.baseurl}}/assets/img/post/pay-qr.jpg)

### 参考链接

* [以太坊随机数生成方式](https://github.com/ZtesoftCS/go-ethereum-code-analysis/blob/master/%E4%BB%A5%E5%A4%AA%E5%9D%8A%E9%9A%8F%E6%9C%BA%E6%95%B0%E7%94%9F%E6%88%90%E6%96%B9%E5%BC%8F.md)
* [randao/README](https://github.com/randao/randao/blob/master/README.md)
* [以太坊智能合约中随机数预测](https://www.freebuf.com/vuls/179173.html)
* [How can I securely generate a random number in my smart contract?](https://ethereum.stackexchange.com/questions/191/how-can-i-securely-generate-a-random-number-in-my-smart-contract)



