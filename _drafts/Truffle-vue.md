---
layout: post
title: '入门Truffle，看这篇就够了'
subtitle: '拍卖DApp：都来拍一个属于自己的ENS吧'
date: 2019-01-25
author: June
cover: /assets/img/post/2019-01-25/truffle-vue-dapp-demo.png
tags: 区块链
---

# 入门 Truffle，看这篇就够了

Remix 提供一个 Solidity 智能合约的开发环境，可以简易的编译、部署、执行甚至除错，适合编程经验不多的初学者。但无法做到版本控制、测试及和其他开发工具一起使用等，实际要开发 DApp 的话会比较不方便。

在这篇文章中，我们将用 Truffle 做一个 DApp。

## 准备工作

### 开发环境

检查是否具备以下工具，若都具备，可以跳过这部分，到下一步

安装 Truffle 和一个以台坊的客户端，这里以 EthereumJS TestRPC 为例
```bash
sudo npm install -g truffle  # Version 3.0.5+ required.
sudo npm install -g ethereumjs-testrpc
```

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

部署合同后，config.js中的前端配置，并在部署时输入DeedRepository和AuctionRepository合同的地址。 前端应用程序还需要访问提供JSON-RPC和WebSockets接口的以太坊节点。 配置前端后，在本地计算机上使用Web服务器启动它：








## 开发

### Truffle

Truffle是自動化從合約的編譯(truffle compile)到部署合約(truffle deploy)再到app建置(truffle build)的過程。其中不含鏈的建置和操作，所以要搭配Ganache(或用client software自建一個節點並開放rpc)才能完成。

1. 初始化 Truffle-vue 项目 (Truffle v5.0.2)
    ```bash
    truffle unbox wespr/truffle-vue
    ```

    truffle-vue 内置的 Migrations.sol 版本低，要修改 [Migrations.sol](https://github.com/june111/truffle-vue-dapp-demo/blob/master/contracts/Migrations.sol)。

2. 編譯合約 
    ```bash
    truffle compile
    ```
    sol合约存在contracts文件夹，truffle要求合約名稱和檔案名稱要一致。
    編譯完後的執行檔(.js檔)會放在/build/contracts資料夾裡。

3. 开启以太坊客户端的本地环境

    * 用 testrpc

        ```bash
        testrpc
        ```

    * 用 Ganache 

3. 用 Ganache 的话，要修改 truffle.js (配置合约发布的环境地址)，把端口号改成7545。

4. 部署合約

    migrate 会执行 migrations 文件夹，js文件开头必須是数字 (truffle 会按照这顺序执行，数字后的名称可任意指定)。truffle 要求第一个执行的必須是部署一個 Migrations 合约(如果有 init，contracts 文件夹中会有一个 Migrations.sol )才能开始 migrate。

    修改 migrations 文件夹中的 [2_deploy_contracts.js](https://github.com/june111/truffle-vue-dapp-demo/blob/master/migrations/2_deploy_contracts.js)

    部署合約

    ```bash
    truffle migrate
    ```

    執行過的migration檔不會再執行，如果有更改過已經執行過的migration檔，要在migrate指令加上--reset，它會重新部署一次：

    ```bash
    truffle migrate --reset
    ```

    还可以指定要部署的网络

    ```bash
    truffle migrate --network ropsten
    ```

5. 启动项目

    ```bash
    npm run start
    ```
    
6. 打包应用

    ```bash
    npm run build
    ```


    ```bash
    npm install --save vuetify moment
    ```





## 完善UI

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

