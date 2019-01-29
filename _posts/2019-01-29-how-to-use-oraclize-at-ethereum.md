---
layout: post
title: '如何在智能合约中使用 Oraclize 调取外部接口'
subtitle: 'Oraclize 在以太坊中的应用'
date: 2019-01-29
author: June
cover: /assets/img/post/2019-01-29/how-to-use-oraclize-at-ethereum.png
tags: 区块链
---

# 如何在智能合约中使用 Oraclize 调取外部接口

### 目录 

* [基本概念](#基本概念)

	* [请求的构成](#请求的构成)
	* [数据源类型](#数据源类型)
	* [查询](#查询)
	* [查询](#查询)
	* [解析助手](#解析助手)
	* [真实性证明](#真实性证明)
	* [数据隐私](#数据隐私)

* [与以太坊智能合约进行交互](#与以太坊智能合约进行交互)

	* [编写智能合约](#编写智能合约)
	* [部署并测试合约](#部署并测试合约)

## 基本概念

### 请求的构成

通过 HTTP API 完成对 Oraclize 数据的有效请求应指定以下参数：

* 数据源类型
* 查询 (query)
* 真实性证明（可选）

### 数据源类型

数据源是受信任的数据提供者。它可以是网站或 Web API，如路透社，Weather.com，BBC.com，或在硬件强制的可信执行环境（TEE）上运行的安全应用程序，也可以是在云中运行的可审计，锁定的虚拟机实例供应商。 Oraclize 目前提供以下类型的本机数据源：

* URL：允许访问任何网页或HTTP API
	
	`HTTP GET request`

	假如 oraclize_query 函式只有一个 arg 传入参数的时候，服务会用 HTTP GET 的方式来取得资料。

	```js
	oraclize_query(
	    "URL",
	    "https://www.therocktrading.com/api/ticker/ETHEUR"
    )
	```

	`HTTP POST request`
	
	假如 oraclize_query 函式只有第二个 arg 传入参数的时候，服务则会用 HTTP POST 的方式来取得资料。

	```js
	oraclize_query(
	    "URL",
	    "json(https://shapeshift.io/sendamount).success.deposit",
	    '{
	        "pair":"eth_btc",
	        "amount":"1",
	        "withdrawal":"1AAcCo21EUc1jbocjssSQDzLna9Vem2UN5"
	    }'
	)
	```

	如果我们只需要一个值，可以搭配 Parsing Helper 函式，将资料先过滤过后，才送回我们的智能合约。

* WolframAlpha：允许对 WolframAlpha 计算引擎进行本机访问
	
	WolframAlpha 是一个使用 AI 技术的线上自动问答系统，你只要传入问题，它就会回传答案给你。问题的范围非常广泛，从最基本的天气、微积分、统计学，甚至连地球科学的问题，它都可以回应你。

	```js
	oraclize_query("WolframAlpha", "random number between 0 and 100");
	```

	>WolframAlpha 官網：https://www.wolframalpha.com/ wiki：https://zh.wikipedia.org/wiki/Wolfram_Alpha

* IPFS：提供对存储在IPFS文件中的内容的访问

	IPFS (InterPlanetary File System) 是一個 P2P 的分散式檔案系統。因為區塊鏈儲存資料非常昂貴，所以你可以上傳檔案到 IPFS 後，將 IPFS 給你的 hash 值存入區塊鏈中。

	```js
	oraclize_query("IPFS", "QmdEJwJG1T9rzHvBD8i69HHuJaRgXRKEQCP7Bh1BVttZbU");
	```

* random：提供来自在Ledger Nano S上运行的安全应用程序的随机字节。

	使用算法是 Oraclize 自创的，可以配合一些博彩类智能合约使用

* 计算：提供任意计算的结果

另外，还有一些元数据源，例如：

* 嵌套：启用不同类型的数据源的结合，或使用一个数据源发出多个请求的，并返回唯一的结果
* identity：返回查询
* 解密：解密以Oraclize私钥加密的字符串

### 查询

一个查询是一个参数数组，需要对其进行评估才能完成特定的数据源类型请求：`query：[parameter_1，parameters_2，...]`;

第一个参数是主要参数，通常是强制性的。 例如，对于URL数据源类型，第一个参数是资源所在的预期URL。 如果仅存在第一个参数，则URL数据源假定请求了HTTP GET。 第二个参数是可选的，应该包含HTTP POST请求的数据有效负载。

可能需要解析查询的中间结果：例如，在JSON API响应中提取精确字段。 因此，查询还可以指定要应用的解析助手。

### 解析助手

Oraclize 提供 XML, JSON, XHTML and a binary parser helpers. 例子:

* JSON解析：从Kraken API中提取最后价格字段，查询第一个参数 `json(https://api.kraken.com/0/public/Ticker?pair=ETHUSD).result.XETHZUSD.c.0`
* HTML Parser：对于HTML抓取非常有用。 可以将所需的 XPATH 指定为 `xpath(..)` 的参数，如示例所示：`html(https://twitter.com/oraclizeit/status/671316655893561344).xpath(//*[contains(@class, 'tweet-text')]/text()).`。
* 二进制助手：使用 `slice(offset,length)` 运算符，对于提取二进制中间结果的一部分非常有用。 第一个参数是预期的偏移量，而第二个参数是返回的片段的长度。 例如，`binary(https://www.sk.ee/crls/esteid/esteid2015.crl).slice(0,300)` 返回链接证书吊销列表的第一个证书的原始字节。
二进制助手必须与 `slic()` 一起使用，并且只接受原始二进制输入


### 真实性证明

Oraclize旨在充当不受信任的中间人。 可选地，对Oraclize的请求可以指定真实性证明。 

### 数据隐私

某些情况，例如公链上的智能合约，可能需要一定程度的隐私来保护数据免受公众监督。 开发人员可以通过使用Oraclize公钥加密整个查询或其某些参数来进行加密的Oraclize查询。 

## 与以太坊智能合约进行交互

Oraclize与以太坊智能合约之间的交互是异步的。任何数据请求都包含两个步骤：

1. 在最常见的情况下，执行智能合约功能的交易由用户广播。该函数包含一个特殊指令，该指令调用了 `oraclize_query`  (从 `oraclizeAPI` 合约继承而来)，Oraclize 会持续监控 `oraclize_query` 所触发的事件，即数据请求。

2. 根据此类请求的参数，Oraclize将获取或计算结果，构建，签名和广播携带结果的事件。在默认配置中，这个事件将执行`__callback` ，该函数应由其开发人员置于智能合约中：因此，此事件在文档中称为Oraclize回调事件。

如前面部分所述，Oraclize的一个基本特征是将数据返回到智能合约的能力以及一个或多个数据真实性证明。生成真实性证明是可选的，它是合同范围的设置，必须由智能合约开发人员在启动数据请求之前进行配置。 Oraclize始终建议使用真实性证明进行生产部署。

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-29/query_flow.png">
![流程]({{site.baseurl}}/assets/img/post/2019-01-29/query_flow.png)
</a>

### 编写智能合约

测试 Oraclize query 工具：[http://app.oraclize.it/home/test_query](http://app.oraclize.it/home/test_query)

1. 导入 `oraclizeAPI`

	```js
	import "github.com/oraclize/ethereum-api/oraclizeAPI_0.4.sol";
	```

2. 继承 `usingOraclize` 合约

	```js
	contract ExampleContract is usingOraclize
	```

3. 调用 `oraclize_query`

	在使用预设 gas 参数的情况下，合约的第一个呼叫 Oraclize 的 request，将不会被收费。如果连续发送多笔 request，将会被收费来支付 callback transaction 的费用。会自动从 contract 的帐户中扣钱，若 contract 中没有足够的金钱，request 将会 fail 并且 Oraclize 不会回传任何数据。

	[https://api.gdax.com/products/ETH-USD/ticker](https://api.gdax.com/products/ETH-USD/ticker) API 回传值如下：

	```json
	{
	    "trade_id": 44625542,
	    "price": "104.04000000",
	    "size": "1.25986581",
	    "time": "2019-01-29T01:35:49.298Z",
	    "bid": "104.04",
	    "ask": "104.05",
	    "volume": "176877.30304853"
	}
	```

	结合 Parsing Helper

	把 url 用 () 包住，然后再指定用哪种 parser helper，这里使用的是 json 格式。

	```js
	oraclize_query(
	  "URL", 
	  "json(https://api.gdax.com/products/ETH-USD/ticker).price");
	```

4. 使用回调事件

	`__callback` 函数名称是固定的，不能取别的名字，在函数内的第一行需要先验证，调用此函数的来源真的是从 oraclize 主机，不接受来路不明丢过来的值。result 就是从外部取得的值，

	```js
	function __callback(string result) public {
	  if (msg.sender != oraclize_cbAddress()) revert();
	  // 略
	}
	```

5. 完整例子

	```js
	pragma solidity ^0.4.25;
	// Step 1: 导入 oraclize
	import "github.com/oraclize/ethereum-api/oraclizeAPI_0.4.sol";

	// Step 2: 继承 usingOraclize 合约
	contract ExampleContract is usingOraclize {

	  string public ETHUSD;

	  function updatePrice() public payable {
	    // Step 3: 调用 oraclize_query 
	    oraclize_query(
	      "URL", 
	      "json(https://api.gdax.com/products/ETH-USD/ticker).price"
	    );
	  }
	  
	  // Step 4: 使用 `__callback` 
	  function __callback(string result) public {
	    if (msg.sender != oraclize_cbAddress()) revert();
	    ETHUSD = result;
	  }
	}
	```

### 使用 Oraclize 插件

这个插件可以让你方便地看到回传的结果。

1. 切换环境。

	使用 Oraclize 插件，要把运行环境切换到 `JavaScript VM` ,

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-29/env.png">
	![切换环境]({{site.baseurl}}/assets/img/post/2019-01-29/env.png)
	</a>

2. 打开插件。
	
	在 Remix ([http://remix.ethereum.org/](http://remix.ethereum.org/)) 的 Settings 标签页，点击 Oraclize 按钮，即可打开插件。

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-29/btn.png">
	![Oraclize 按钮]({{site.baseurl}}/assets/img/post/2019-01-29/btn.png)
	</a>

### 部署并测试合约

1. 部署合约

	选择 `ExampleContract` 合约，然后点击 Deploy。部署成功后， Deployed Contracts 中会显示该合约部署的地址和合约的功能。

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-29/deploy.png">
	![Deploy]({{site.baseurl}}/assets/img/post/2019-01-29/deploy.png)
	</a>

2. 请求数据

	使用合约中的 `updatePrice` 发出请求

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-29/request.png">
	![请求数据]({{site.baseurl}}/assets/img/post/2019-01-29/request.png)
	</a>

3. 得到回传数据

	需要等待一会才会得到回传数据，得到数据后，result 会自动显示出来。

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-01-29/callback.png">
	![得到回传数据]({{site.baseurl}}/assets/img/post/2019-01-29/callback.png)
	</a>



---

觉得文章不错就扫码支持一下呗～

![打赏二维码]({{site.baseurl}}/assets/img/post/pay-qr.jpg)

### 参考链接

* [oraclize 文档](https://docs.oraclize.it/)
* [介紹 Oraclize 與資料來源](https://github.com/alincode/30-days-smart-contract/blob/847906b9d549d9854f3a9c70f1a970b742113bb2/25_oraclize_data_source.md)
* [Oraclize request](https://github.com/alincode/30-days-smart-contract/blob/847906b9d549d9854f3a9c70f1a970b742113bb2/26_oraclize_query.md)
* [Oraclize 可靠證明](https://github.com/alincode/30-days-smart-contract/blob/847906b9d549d9854f3a9c70f1a970b742113bb2/27_oraclize_proof.md)
* [Oraclize 的 computation 資料來源](https://github.com/alincode/30-days-smart-contract/blob/847906b9d549d9854f3a9c70f1a970b742113bb2/28_orazlize_computation.md)
