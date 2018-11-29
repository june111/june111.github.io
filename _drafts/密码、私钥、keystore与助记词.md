---
layout: post
title: '密码、私钥、keystore与助记词之间的关系'
date: 2018-11-27
author: June
cover: /assets/img/post/2018-11-27/front-end-build-tool.png
tags: 前端
---

# 密码、私钥、keystore与助记词之间的关系

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-27/structure.svg">
![文章结构]({{site.baseurl}}/assets/img/post/2018-11-27/structure.svg)
</a>

## 理解密码、私钥、keystore与助记词

1. 密码
	密码不是私钥，密码可以进行修改或重置。它主要用途有两个，一是转账时候的支付密码，二是用 keystore 导入钱包时需要输入的密码，用于解锁keystore。

	在钱包应用程序中，创建账号时需要设定一个密码，这个密码一般要求不少于 8 个字符，为了安全，密码最好设置复杂一点。

2. 私钥
	私钥由64位长度的十六进制的字符组成，比如：`0xE4356E49C88C8B7AB370AF7D5C0C54F0261AAA006F6BDE09CD4745CF54E0115A`，一个账户只有一个私钥且不能修改，谁拥有私钥就能够掌控该账号的数字货币。通常一个钱包中私钥和公钥是成对出现的，有了私钥，我们就可以通过一定的算法生成公钥，再通过公钥经过一定的算法生成地址，这一过程都是不可逆的，是如何生成的？我们在上一章节中有详细的说明。私钥一定要妥善保管，若被泄漏别人可以通过私钥解锁账号转出你的该账号的数字货币。

	在钱包应用程序中，解锁账号后可以导出私钥。

3. Keystore
	因为私钥不利于记忆，容易被盗，因此有了Keystore。Keystore常见于以太坊钱包，它并不是私钥，而是将私钥以加密的方式保存为一份 JSON 文件，这份 JSON 文件就是 keystore，所以它就是加密后的私钥。但是Keystore必须配合钱包密码才能使用该账号，所以只有Keystore文件，并不能掌控账号。对于助记词和私钥就不一样了，只要知道助记词或者私钥就能掌控该账号了。

	在应用程序中，可以实现解锁账号后生成Keystore文件，支持的钱包有MetaMask、Mist等。

4. 助记词
	私钥是64位长度的十六进制的字符，不利于记录且容易记错，所以用算法将一串随机数转化为了一串12 ~ 24个容易记住的单词，方便保存记录。所以有的同学有了下面的结论：

	* 助记词是私钥的另一种表现形式。
	* 还有同学说助记词=私钥，这是不正确的说法，通过助记词可以获取相关联的多个私钥，但是通过其中一个私钥是不能获取助记词的，因此助记词≠私钥。
	
	目前只有少数钱包应用程序支持导出助记词，如MetaMask等。通过助记词导入账号也只有少数钱包应用程序支持，如MyEtherWallet、imToken等。

### BIP
要弄清楚助记词与私钥的关系，得清楚BIP协议，是Bitcoin Improvement Proposals的缩写，意思是Bitcoin 的改进建议，用于提出 Bitcoin 的新功能或改进措施。BIP协议衍生了很多的版本，主要有BIP32、BIP39、BIP44。

#### BIP32

BIP32是 HD钱包的核心提案，通过种子来生成主私钥，然后派生海量的子私钥和地址，种子是一串很长的随机数。

#### BIP39

由于种子是一串很长的随机数，不利于记录，所以我们用算法将种子转化为一串12 ~ 24个的单词，方便保存记录，这就是BIP39，它扩展了 HD钱包种子的生成算法。

#### BIP44

BIP44 是在 BIP32 和 BIP43 的基础上增加多币种，提出的层次结构非常全面，它允许处理多个币种，多个帐户，每个帐户有数百万个地址。

在BIP32路径中定义以下5个级别：

	m/purpse'/coin_type'/account'/change/address_index

* purpose：在BIP43之后建议将常数设置为44'。表示根据BIP44规范使用该节点的子树。
* Coin_type：币种，代表一个主节点（种子）可用于无限数量的独立加密币，如比特币，Litecoin或Namecoin。此级别为每个加密币创建一个单独的子树，避免重用已经在其它链上存在的地址。开发人员可以为他们的项目注册未使用的号码。
* Account：账户，此级别为了设置独立的用户身份可以将所有币种放在一个的帐户中，从0开始按顺序递增。
* Change：常量0用于外部链，常量1用于内部链，外部链用于钱包在外部用于接收和付款。内部链用于在钱包外部不可见的地址，如返回交易变更。
* Address_index：地址索引，按顺序递增的方式从索引0开始编号。

BIP44的规则使得 HD钱包非常强大，用户只需要保存一个种子，就能控制所有币种，所有账户的钱包，因此由BIP39 生成的助记词非常重要，所以一定安全妥善保管，那么会不会被破解呢？如果一个 HD 钱包助记词是 12 个单词，一共有 2048 个单词可能性，那么随机的生成的助记词所有可能性大概是5e+39，因此几乎不可能被破解。

#### HD钱包
通过BIP协议生成账号的钱包叫做HD钱包。这个HD钱包，并不是Hardware Wallet硬件钱包，这里的 HD 是Hierarchical Deterministic的缩写，意思是分层确定性，所以HD钱包的全称为比特币分成确定性钱包 。

#### 以太坊对BIP的支持
BIP是用于提出 Bitcoin 的新功能或改进措施，那么对于以太坊来说如何支持呢？

* 以太坊在[EIPs/issues/84](https://github.com/ethereum/EIPs/issues/84)中讨论，是否遵循 BIP32 和 BIP44，社区里提出来很多有意思的观点，比特币是基于 UTXO 的，所以可以使用 HD 钱包（BIP32）为每个交易分配一个新地址，以保护您的隐私。然而，以太坊是基于帐户，每个帐户都有一个地址，BIP 是比特币的提案，而且比特币的数据结构的设计是围绕改变地址的想法构建的，BIP 的一些提案可能并不适合以太坊。以太坊的模式和比特币UTXO 不同，以太坊转账不能改变地址，如果在以太坊上实现 UTXO ，用户还必须签名两个交易以将余额的一部分发送到一个地址，将余额的一部分发送到第二个地址 - 这将使成本增加一倍，而且第二个交易可能不会在同一个区块中，当然以太坊也可以通过智能合约的方式实现。另外，以太坊目前官方钱包采用 KDF 的形式，也就是我们常说的 Keystore 的形式。

* 以太坊在[EIPs/issues/85](https://github.com/ethereum/EIPs/issues/85)中讨论，以太坊社区似乎也采用了 BIP32 的做法，提议 HD 路径为 : m/44'/60'/0'/0/n，n 是第 n 次生成地址。目前以太坊客户端实现了BIP32的客户端有：Jaxx, Metamask, Exodus, imToken, TREZOR (ETH) & Digital Bitbox。

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-27/process.svg">
![从助记词到地址]({{site.baseurl}}/assets/img/post/2018-11-27/process.svg)
</a>

## 密码、私钥、keystore与助记词的关系

它们关系可以用下面的图来表述。

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-27/relationship.png">
![文章结构]({{site.baseurl}}/assets/img/post/2018-11-27/relationship.png)
</a>

## 钱包的核心：私钥

基于以上的分析，我们对以太坊钱包的账号系统有了一个很好的认识，那么我们在使用钱包的过程中，该如何保管自己的钱包呢？主要包含以下几种方式：

* 私钥（Private Key）
* Keystore+密码（Keystore+Password）
* 助记词（Mnemonic code）

通过以上三种中的一种方式都可以解锁账号，然后掌控它，所以对于每种方式中的数据都必须妥善包括，如有泄漏，请尽快转移数字资产。

我们可以得到以下总结：

* 通过私钥+密码可以生成keystore，即加密私钥；
* 通过keystore+密码可以获取私钥，即解密keystore。
* 通过助记词根据不同的路径获取不同的私钥，即使用HD钱包将助记词转化成种子来生成主私钥，然后派生海量的子私钥和地址。

可以看出这几种方式的核心其实都是为了获得私钥，然后去解锁账号，因此钱包的核心功能是私钥的创建、存储和使用。

---

觉得文章不错就扫码支持一下呗～

![打赏二维码]({{site.baseurl}}/assets/img/post/pay-qr.jpg)

### 参考链接


* [密码、私钥、keystore与助记词之间的爱恨情仇](http://chaindesk.cn/columninfo.html?id=6&dirId=1)
* [](https://web3js.readthedocs.io/en/1.0/web3-eth-accounts.html)
* [](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki)
* [](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki)
* [](https://github.com/ethereum/EIPs/issues/84)
* [](https://github.com/ethereum/EIPs/issues/85)
* []()
* []()
