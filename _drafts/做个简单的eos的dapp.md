---
layout: post
title: ''
subtitle: ''
date: 2019-02-04
author: June
reward: 1
cover: /assets/img/post/2019-02-04/front-end-build-tool.png
tags: 前端
---

# 

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-02-03/structure.svg">
![文章结构]({{site.baseurl}}/assets/img/post/2019-02-03/structure.svg)
</a>

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-02-03/stack.png">
![交互的模块]({{site.baseurl}}/assets/img/post/2019-02-03/stack.png)
</a>

## 开发环境

1. Brew/Git/Boost

	具体[安装教程](https://medium.com/@imeosone/one-how-to-build-an-eos-development-environment-using-mac-ubuntu-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8mac-ubuntu%E6%90%AD%E5%BB%BAeos%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83-cfc5620fe506)就不写这了

2. 安装 EOS 依赖

	```bash
	brew tap eosio/eosio
	brew install eosio
	```

3. 启动节点

	启动钱包

	```bash
	keosd &
	```

	启动节点nodeos

	```bash
	nodeos -e -p eosio \
	--plugin eosio::producer_plugin \
	--plugin eosio::chain_api_plugin \
	--plugin eosio::http_plugin \
	--plugin eosio::history_plugin \
	--plugin eosio::history_api_plugin \
	--access-control-allow-origin='*' \
	--contracts-console \
	--http-validate-host=false \
	--verbose-http-errors \
	--filter-on='*' >> nodeos.log 2>&1 &
	```

	检查安装

	```bash
	tail -f nodeos.log # 查看是否出块
	cleos wallet list # 查看钱包列表
	curl http://localhost:8888/v1/chain/get_info # 区块信息
	```

4. 安装 CDT (Contract Development Toolkit)

	```bash
	brew tap eosio/eosio.cdt
	brew install eosio.cdt
	```

5. 创建开发者钱包

	创建
	```bash
	cleos wallet create --to-console
	```

	打开
	```bash
	cleos wallet open # 打开
	cleos wallet list # 列出列表
	```

	解锁
	```bash
	cleos wallet unlock
	```

	创建私钥
	```bash
	cleos wallet create_key
	```

	导入key
	```bash
	cleos wallet import
	```


6. 创建测试账户

	 创建测试账户
	```bash
	cleos create account eosio bob YOUR_PUBLIC_KEY 
	cleos create account eosio alice YOUR_PUBLIC_KEY
	```

	公钥

	```bash
	cleos get account bob
	```
## 
## 
## 
## 

---

### 参考链接

* [eos.io 文档](https://developers.eos.io/eosio-home/docs/introduction)
* []()
* []()
* []()
* []()
* []()
* []()


[Why Developers Should Build on EOS](https://medium.com/@eosgo/why-developers-should-build-on-eos-dd534ce456e7)
[ONE — -How to Build an EOS Development Environment Using Mac/Ubuntu / 如何使用Mac/Ubuntu搭建EOS开发环境](https://medium.com/@imeosone/one-how-to-build-an-eos-development-environment-using-mac-ubuntu-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8mac-ubuntu%E6%90%AD%E5%BB%BAeos%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83-cfc5620fe506)
[EOS DAPP合约开发之DICE游戏 二](https://www.chaindesk.cn/witbook/37/528)
[dice.cpp](https://github.com/EOSIO/eos/blob/v1.3.0/contracts/dice/dice.cpp)
[eosjs](https://github.com/eosio/eosjs)

[Top Dapp tutorials Series](https://medium.com/coinmonks/top-dapp-tutorial-serie)