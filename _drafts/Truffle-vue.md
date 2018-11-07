---
layout: post
title: '入门Truffle，看这篇就够了'
date: 2018-06-30
author: June
cover: 'https://june111.github.io/assets/img/post/started-dapp.png'
tags: 技术 区块链
---

# 入门Truffle，看这篇就够了



## 准备工作


#### 开发环境

检查是否具备以下工具，若都具备，可以跳过这部分，到下一步

Truffle

安装 Truffle

    sudo npm install -g truffle




## 区块链开发环境



#### Truffle

Truffle是自動化從合約的編譯(truffle compile)到部署合約(truffle deploy)再到app建置(truffle build)的過程。其中不含鏈的建置和操作，所以要搭配Ganache(或用client software自建一個節點並開放rpc)才能完成。

1. 初始化Truffle-vue项目(Truffle v4.1.13)
```
truffle unbox wespr/truffle-vue
```
把Casino.sol 放入contracts文件夹

这个项目的truffle版本很低，要修改Migrations.sol，这里用的是truffle init 里面的Migrations.sol

2. 編譯合約
```
    truffle compile
```
sol合約會存在contracts資料夾裡，truffle要求合約名稱和檔案名稱要一致。
編譯完後的執行檔(.js檔)會放在/build/contracts資料夾裡。

3. 修改 truffle.js
配置链接合约发布的环境地址

```
    module.exports = {
        networks: {
            development: {
                host: "localhost",
                port: 7545,
                network_id: "*" // 匹配任何network id
            }
        }
    };
```

4. 部署合約

migrate會執行migration資料夾裡的js檔，js檔名開頭必須是數字(truffle會按照這順序執行，數字後的名稱可任意指定)。truffle要求第一個執行的必須是部署一個Migrations合約(如果有init，contracts資料夾裡會有一個Migrations.sol)才能開始migrate。

在 migrations 文件夹中创建文件 2_casino.js

    var Casino = artifacts.require("./Casino.sol");
    module.exports = function(deployer) {
        deployer.deploy(Casino, 1000000, 80); //第一個參數為合約名稱，如果合約constructor有參數則加在其後
    };

部署合約

    truffle migrate


執行過的migration檔不會再執行，如果有更改過已經執行過的migration檔，要在migrate指令加上--reset，它會重新部署一次：

    truffle migrate --reset

还可以指定要部署的网络

    truffle migrate --network ropsten



5. 启动项目

    npm run start
    
6. 打包

    npm run build


Remix 提供一個 Solidity 智能合约的开发环境，可以简易的编译、部署、执行甚至除错，时候编程经验不多的初学者。但無法做到版本控制、測試及和其他開發工具一起使用等，實際要開發 DApp 的話會比較不方便。






## 完善UI

## 参考链接
1. []()
2. []()
3. []()
4. []()
5. []()


