---
layout: post
title: '入门Truffle，看这篇就够了'
subtitle: '把猜一猜 DApp 加上 Truffle'
date: 2019-01-26
author: June
cover: /assets/img/post/2019-01-26/truffle-vue-dapp-demo.png
tags: 区块链
---

# 入门 Truffle，看这篇就够了

Remix 提供一个 Solidity 智能合约的开发环境，可以简易的编译、部署、执行甚至除错，适合编程经验不多的初学者。但无法做到版本控制、测试及和其他开发工具一起使用等，实际要开发 DApp 的话会比较不方便。

在这篇文章中，我们将用 Truffle 做一个 DApp。

## 准备工作

### 开发环境

检查是否具备以下工具，若都具备，可以跳过这部分，到下一步
检查
```bash
truffle version
ganache-cli --version
```

安装 Truffle 和一个以太坊的客户端，这里以 ganache-cli 为例
```bash
npm install -g truffle  # Version 3.0.5+ required.
npm install -g ganache-cli
```

## 开发

### 后端（智能合约）

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

    * 用命令行

        ```bash
        ganache-cli
        ```

    * 用 Ganache 

3. 可以修改 truffle.js (配置合约发布的环境地址)，修改RPC端口号等。

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

### 前端（用户界面）

5. 启动项目

    ```bash
    npm run start
    ```
    
6. 打包应用

    ```bash
    npm run build
    ```








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

