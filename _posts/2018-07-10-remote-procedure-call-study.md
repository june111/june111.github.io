---
layout: post
title: 'Ethereum JSON RPC 学习文档'
date: 2018-07-10
author: June
cover: 'https://june111.github.io/blog/assets/img/post/json-rpc.png'
tags: 技术 区块链
---

# Ethereum JSON RPC API

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Contents**

- [JSON RPC API](#json-rpc-api)
  - [JavaScript API](#javascript-api)
  - [JSON-RPC Endpoint](#json-rpc-endpoint)
    - [Go](#go)
    - [C++](#c)
    - [Python](#python)
  - [JSON-RPC support](#json-rpc-support)
  - [HEX value encoding](#hex-value-encoding)
  - [The default block parameter](#the-default-block-parameter)
  - [Curl Examples Explained](#curl-examples-explained)
  - [JSON-RPC methods](#json-rpc-methods)
  - [JSON RPC API Reference](#json-rpc-api-reference)
      - [web3_clientVersion](#web3_clientversion)
        - [Parameters](#parameters)
        - [Returns](#returns)
        - [Example](#example)
      - [web3_sha3](#web3_sha3)
        - [Parameters](#parameters-1)
        - [Returns](#returns-1)
        - [Example](#example-1)
      - [net_version](#net_version)
        - [Parameters](#parameters-2)
        - [Returns](#returns-2)
        - [Example](#example-2)
      - [net_listening](#net_listening)
        - [Parameters](#parameters-3)
        - [Returns](#returns-3)
        - [Example](#example-3)
      - [net_peerCount](#net_peercount)
        - [Parameters](#parameters-4)
        - [Returns](#returns-4)
        - [Example](#example-4)
      - [eth_protocolVersion](#eth_protocolversion)
        - [Parameters](#parameters-5)
        - [Returns](#returns-5)
        - [Example](#example-5)
      - [eth_syncing](#eth_syncing)
        - [Parameters](#parameters-6)
        - [Returns](#returns-6)
        - [Example](#example-6)
      - [eth_coinbase](#eth_coinbase)
        - [Parameters](#parameters-7)
        - [Returns](#returns-7)
        - [Example](#example-7)
      - [eth_mining](#eth_mining)
        - [Parameters](#parameters-8)
        - [Returns](#returns-8)
        - [Example](#example-8)
      - [eth_hashrate](#eth_hashrate)
        - [Parameters](#parameters-9)
        - [Returns](#returns-9)
        - [Example](#example-9)
      - [eth_gasPrice](#eth_gasprice)
        - [Parameters](#parameters-10)
        - [Returns](#returns-10)
        - [Example](#example-10)
      - [eth_accounts](#eth_accounts)
        - [Parameters](#parameters-11)
        - [Returns](#returns-11)
        - [Example](#example-11)
      - [eth_blockNumber](#eth_blocknumber)
        - [Parameters](#parameters-12)
        - [Returns](#returns-12)
        - [Example](#example-12)
      - [eth_getBalance](#eth_getbalance)
        - [Parameters](#parameters-13)
        - [Returns](#returns-13)
        - [Example](#example-13)
      - [eth_getStorageAt](#eth_getstorageat)
        - [Parameters](#parameters-14)
        - [Returns](#returns-14)
        - [Example](#example-14)
      - [eth_getTransactionCount](#eth_gettransactioncount)
        - [Parameters](#parameters-15)
        - [Returns](#returns-15)
        - [Example](#example-15)
      - [eth_getBlockTransactionCountByHash](#eth_getblocktransactioncountbyhash)
        - [Parameters](#parameters-16)
        - [Returns](#returns-16)
        - [Example](#example-16)
      - [eth_getBlockTransactionCountByNumber](#eth_getblocktransactioncountbynumber)
        - [Parameters](#parameters-17)
        - [Returns](#returns-17)
        - [Example](#example-17)
      - [eth_getUncleCountByBlockHash](#eth_getunclecountbyblockhash)
        - [Parameters](#parameters-18)
        - [Returns](#returns-18)
        - [Example](#example-18)
      - [eth_getUncleCountByBlockNumber](#eth_getunclecountbyblocknumber)
        - [Parameters](#parameters-19)
        - [Returns](#returns-19)
        - [Example](#example-19)
      - [eth_getCode](#eth_getcode)
        - [Parameters](#parameters-20)
        - [Returns](#returns-20)
        - [Example](#example-20)
      - [eth_sign](#eth_sign)
        - [Parameters](#parameters-21)
        - [Returns](#returns-21)
        - [Example](#example-21)
      - [eth_sendTransaction](#eth_sendtransaction)
        - [Parameters](#parameters-22)
        - [Returns](#returns-22)
        - [Example](#example-22)
      - [eth_sendRawTransaction](#eth_sendrawtransaction)
        - [Parameters](#parameters-23)
        - [Returns](#returns-23)
        - [Example](#example-23)
      - [eth_call](#eth_call)
        - [Parameters](#parameters-24)
        - [Returns](#returns-24)
        - [Example](#example-24)
      - [eth_estimateGas](#eth_estimategas)
        - [Parameters](#parameters-25)
        - [Returns](#returns-25)
        - [Example](#example-25)
      - [eth_getBlockByHash](#eth_getblockbyhash)
        - [Parameters](#parameters-26)
        - [Returns](#returns-26)
        - [Example](#example-26)
      - [eth_getBlockByNumber](#eth_getblockbynumber)
        - [Parameters](#parameters-27)
        - [Returns](#returns-27)
        - [Example](#example-27)
      - [eth_getTransactionByHash](#eth_gettransactionbyhash)
        - [Parameters](#parameters-28)
        - [Returns](#returns-28)
        - [Example](#example-28)
      - [eth_getTransactionByBlockHashAndIndex](#eth_gettransactionbyblockhashandindex)
        - [Parameters](#parameters-29)
        - [Returns](#returns-29)
        - [Example](#example-29)
      - [eth_getTransactionByBlockNumberAndIndex](#eth_gettransactionbyblocknumberandindex)
        - [Parameters](#parameters-30)
        - [Returns](#returns-30)
        - [Example](#example-30)
      - [eth_getTransactionReceipt](#eth_gettransactionreceipt)
        - [Parameters](#parameters-31)
        - [Returns](#returns-31)
        - [Example](#example-31)
      - [eth_getUncleByBlockHashAndIndex](#eth_getunclebyblockhashandindex)
        - [Parameters](#parameters-32)
        - [Returns](#returns-32)
        - [Example](#example-32)
      - [eth_getUncleByBlockNumberAndIndex](#eth_getunclebyblocknumberandindex)
        - [Parameters](#parameters-33)
        - [Returns](#returns-33)
        - [Example](#example-33)
      - [eth_getCompilers](#eth_getcompilers)
        - [Parameters](#parameters-34)
        - [Returns](#returns-34)
        - [Example](#example-34)
      - [eth_compileSolidity](#eth_compilesolidity)
        - [Parameters](#parameters-35)
        - [Returns](#returns-35)
        - [Example](#example-35)
      - [eth_compileLLL](#eth_compilelll)
        - [Parameters](#parameters-36)
        - [Returns](#returns-36)
        - [Example](#example-36)
      - [eth_compileSerpent](#eth_compileserpent)
        - [Parameters](#parameters-37)
        - [Returns](#returns-37)
        - [Example](#example-37)
      - [eth_newFilter](#eth_newfilter)
        - [A note on specifying topic filters:](#a-note-on-specifying-topic-filters)
        - [Parameters](#parameters-38)
        - [Returns](#returns-38)
        - [Example](#example-38)
      - [eth_newBlockFilter](#eth_newblockfilter)
        - [Parameters](#parameters-39)
        - [Returns](#returns-39)
        - [Example](#example-39)
      - [eth_newPendingTransactionFilter](#eth_newpendingtransactionfilter)
        - [Parameters](#parameters-40)
        - [Returns](#returns-40)
        - [Example](#example-40)
      - [eth_uninstallFilter](#eth_uninstallfilter)
        - [Parameters](#parameters-41)
        - [Returns](#returns-41)
        - [Example](#example-41)
      - [eth_getFilterChanges](#eth_getfilterchanges)
        - [Parameters](#parameters-42)
        - [Returns](#returns-42)
        - [Example](#example-42)
      - [eth_getFilterLogs](#eth_getfilterlogs)
        - [Parameters](#parameters-43)
        - [Returns](#returns-43)
        - [Example](#example-43)
      - [eth_getLogs](#eth_getlogs)
        - [Parameters](#parameters-44)
        - [Returns](#returns-44)
        - [Example](#example-44)
      - [eth_getWork](#eth_getwork)
        - [Parameters](#parameters-45)
        - [Returns](#returns-45)
        - [Example](#example-45)
      - [eth_submitWork](#eth_submitwork)
        - [Parameters](#parameters-46)
        - [Returns](#returns-46)
        - [Example](#example-46)
      - [eth_submitHashrate](#eth_submithashrate)
        - [Parameters](#parameters-47)
        - [Returns](#returns-47)
        - [Example](#example-47)
      - [db_putString](#db_putstring)
        - [Parameters](#parameters-48)
        - [Returns](#returns-48)
        - [Example](#example-48)
      - [db_getString](#db_getstring)
        - [Parameters](#parameters-49)
        - [Returns](#returns-49)
        - [Example](#example-49)
      - [db_putHex](#db_puthex)
        - [Parameters](#parameters-50)
        - [Returns](#returns-50)
        - [Example](#example-50)
      - [db_getHex](#db_gethex)
        - [Parameters](#parameters-51)
        - [Returns](#returns-51)
        - [Example](#example-51)
      - [shh_version](#shh_version)
        - [Parameters](#parameters-52)
        - [Returns](#returns-52)
        - [Example](#example-52)
      - [shh_post](#shh_post)
        - [Parameters](#parameters-53)
        - [Returns](#returns-53)
        - [Example](#example-53)
      - [shh_newIdentity](#shh_newidentity)
        - [Parameters](#parameters-54)
        - [Returns](#returns-54)
        - [Example](#example-54)
      - [shh_hasIdentity](#shh_hasidentity)
        - [Parameters](#parameters-55)
        - [Returns](#returns-55)
        - [Example](#example-55)
      - [shh_newGroup](#shh_newgroup)
        - [Parameters](#parameters-56)
        - [Returns](#returns-56)
        - [Example](#example-56)
      - [shh_addToGroup](#shh_addtogroup)
        - [Parameters](#parameters-57)
        - [Returns](#returns-57)
        - [Example](#example-57)
      - [shh_newFilter](#shh_newfilter)
        - [Parameters](#parameters-58)
        - [Returns](#returns-58)
        - [Example](#example-58)
      - [shh_uninstallFilter](#shh_uninstallfilter)
        - [Parameters](#parameters-59)
        - [Returns](#returns-59)
        - [Example](#example-59)
      - [shh_getFilterChanges](#shh_getfilterchanges)
        - [Parameters](#parameters-60)
        - [Returns](#returns-60)
        - [Example](#example-60)
      - [shh_getMessages](#shh_getmessages)
        - [Parameters](#parameters-61)
        - [Returns](#returns-61)
        - [Example](#example-61)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# JSON RPC API

## JSON

#### 什么是JSON
[JSON](http://json.org/)是一种轻量级数据交换格式。 

It can represent numbers, strings, ordered sequences of values, and collections of name/value pairs.


## RPC

#### 什么是rpc
RPC (Remote Procedure Call) 远程过程调用，简单说就是通过网络请求服务，不需要了解底层网络技术的协议。

#### rpc数据传递格式
rpc支持多种数据格式传递，json,xml等


## JSON-RPC

[JSON-RPC](http://www.jsonrpc.org/specification) is a stateless, light-weight remote procedure call (RPC) protocol. Primarily this specification defines several data structures and the rules around their processing. It is transport agnostic in that the concepts can be used within the same process, over sockets, over HTTP, or in many various message passing environments. It uses JSON ([RFC 4627](http://www.ietf.org/rfc/rfc4627.txt)) as data format.


## JavaScript API

To talk to an ethereum node from inside a JavaScript application use the [web3.js](https://github.com/ethereum/web3.js) library, which gives a convenient interface for the RPC methods.
See the [JavaScript API](https://github.com/ethereum/wiki/wiki/JavaScript-API) for more.


## JSON-RPC Endpoint

### Go

启动HTTP JSON-RPC
You can start the HTTP JSON-RPC with the `--rpc` flag
```bash
geth --rpc
```

修改端口号和地址
change the default port (8545) and listing address (localhost) with:

```bash
geth --rpc --rpcaddr <ip> --rpcport <portnumber>
```

如果从浏览器访问RPC，需要设置访问地址
If accessing the RPC from a browser, CORS will need to be enabled with the appropriate domain set. Otherwise, JavaScript calls are limit by the same-origin policy and requests will fail:

```bash
geth --rpc --rpccorsdomain "http://localhost:3000"
```

The JSON RPC can also be started from the [geth console](https://github.com/ethereum/go-ethereum/wiki/JavaScript-Console) using the `admin.startRPC(addr, port)` command.


## 十六进制值编码 HEX value encoding

At present there are two key datatypes that are passed over JSON: unformatted byte arrays and quantities. Both are passed with a hex encoding, however with different requirements to formatting:

When encoding **QUANTITIES** (integers, numbers): encode as hex, prefix with "0x", the most compact representation (slight exception: zero should be represented as "0x0"). 

When encoding **UNFORMATTED DATA** (byte arrays, account addresses, hashes, bytecode arrays): encode as hex, prefix with "0x", two hex digits per byte. 


## The default block parameter

The following methods have an extra default block parameter:

- [eth_getBalance](#eth_getbalance)
- [eth_getCode](#eth_getcode)
- [eth_getTransactionCount](#eth_gettransactioncount)
- [eth_getStorageAt](#eth_getstorageat)
- [eth_call](#eth_call)

When requests are made that act on the state of ethereum, the last default block parameter determines the height of the block.

The following options are possible for the defaultBlock parameter:

- `HEX String` - an integer block number
- `String "earliest"` for the earliest/genesis block
- `String "latest"` - for the latest mined block
- `String "pending"` - for the pending state/transactions

## Curl Examples Explained

(curl)[https://curl.haxx.se/ ]用于命令行或脚本来传输数据。

The curl options below might return a response where the node complains about the content type, this is because the --data option sets the content type to application/x-www-form-urlencoded . If your node does complain, manually set the header by placing -H "Content-Type: application/json" at the start of the call.

The examples also do not include the URL/IP & port combination which must be the last argument given to curl e.x. 127.0.0.1:8545

## JSON-RPC methods

* [web3_clientVersion](#web3_clientversion)
* [web3_sha3](#web3_sha3)
* [net_version](#net_version)
* [net_peerCount](#net_peercount)
* [net_listening](#net_listening)
* [eth_protocolVersion](#eth_protocolversion)
* [eth_syncing](#eth_syncing)
* [eth_coinbase](#eth_coinbase)
* [eth_mining](#eth_mining)
* [eth_hashrate](#eth_hashrate)
* [eth_gasPrice](#eth_gasprice)
* [eth_accounts](#eth_accounts)
* [eth_blockNumber](#eth_blocknumber)
* [eth_getBalance](#eth_getbalance)
* [eth_getStorageAt](#eth_getstorageat)
* [eth_getTransactionCount](#eth_gettransactioncount)
* [eth_getBlockTransactionCountByHash](#eth_getblocktransactioncountbyhash)
* [eth_getBlockTransactionCountByNumber](#eth_getblocktransactioncountbynumber)
* [eth_getUncleCountByBlockHash](#eth_getunclecountbyblockhash)
* [eth_getUncleCountByBlockNumber](#eth_getunclecountbyblocknumber)
* [eth_getCode](#eth_getcode)
* [eth_sign](#eth_sign)
* [eth_sendTransaction](#eth_sendtransaction)
* [eth_sendRawTransaction](#eth_sendrawtransaction)
* [eth_call](#eth_call)
* [eth_estimateGas](#eth_estimategas)
* [eth_getBlockByHash](#eth_getblockbyhash)
* [eth_getBlockByNumber](#eth_getblockbynumber)
* [eth_getTransactionByHash](#eth_gettransactionbyhash)
* [eth_getTransactionByBlockHashAndIndex](#eth_gettransactionbyblockhashandindex)
* [eth_getTransactionByBlockNumberAndIndex](#eth_gettransactionbyblocknumberandindex)
* [eth_getTransactionReceipt](#eth_gettransactionreceipt)
* [eth_getUncleByBlockHashAndIndex](#eth_getunclebyblockhashandindex)
* [eth_getUncleByBlockNumberAndIndex](#eth_getunclebyblocknumberandindex)
* [eth_getCompilers](#eth_getcompilers)
* [eth_compileLLL](#eth_compilelll)
* [eth_compileSolidity](#eth_compilesolidity)
* [eth_compileSerpent](#eth_compileserpent)
* [eth_newFilter](#eth_newfilter)
* [eth_newBlockFilter](#eth_newblockfilter)
* [eth_newPendingTransactionFilter](#eth_newpendingtransactionfilter)
* [eth_uninstallFilter](#eth_uninstallfilter)
* [eth_getFilterChanges](#eth_getfilterchanges)
* [eth_getFilterLogs](#eth_getfilterlogs)
* [eth_getLogs](#eth_getlogs)
* [eth_getWork](#eth_getwork)
* [eth_submitWork](#eth_submitwork)
* [eth_submitHashrate](#eth_submithashrate)
* [db_putString](#db_putstring)
* [db_getString](#db_getstring)
* [db_putHex](#db_puthex)
* [db_getHex](#db_gethex) 
* [shh_post](#shh_post)
* [shh_version](#shh_version)
* [shh_newIdentity](#shh_newidentity)
* [shh_hasIdentity](#shh_hasidentity)
* [shh_newGroup](#shh_newgroup)
* [shh_addToGroup](#shh_addtogroup)
* [shh_newFilter](#shh_newfilter)
* [shh_uninstallFilter](#shh_uninstallfilter)
* [shh_getFilterChanges](#shh_getfilterchanges)
* [shh_getMessages](#shh_getmessages)

## JSON RPC API Reference

***

练习环境
本地同步区块，端口8545

	pm2 start /Users/linktime/Documents/geth/process.json 

打开Ganache，本地私链，端口7545

#### web3_clientVersion

当前客户端版本
Returns the current client version.

##### Parameters
none

##### Returns

`String` - The current client version

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"web3_clientVersion","params":[],"id":67}'

// Result
{
  "id":67,
  "jsonrpc":"2.0",
  "result": "Mist/v0.9.3/darwin/go1.4.1"
}
```

My Example
```js
curl -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"web3_clientVersion","params":[],"id":42}' 127.0.0.1:8545

```

***

#### web3_sha3

返回给定数据的Keccak-256（不是标准化的SHA3-256）。
Returns Keccak-256 (*not* the standardized SHA3-256) of the given data.

##### Parameters

1. `DATA` - the data to convert into a SHA3 hash

```js
params: [
  "0x68656c6c6f20776f726c64"
]
```

##### Returns

`DATA` - The SHA3 result of the given string.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"web3_sha3","params":["0x68656c6c6f20776f726c64"],"id":64}'

// Result
{
  "id":64,
  "jsonrpc": "2.0",
  "result": "0xc94770007dda54cF92009BFF0dE90c06F603a09f"
}
```

My Example
```js
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"web3_sha3","params":["0x68656c6c6f20776f726c64"],"id":64}'

```


***

#### net_version
当前network id
Returns the current network id.

##### Parameters
none

##### Returns

`String` - The current network id.
- `"1"`: Ethereum Mainnet
- `"2"`: Morden Testnet  (deprecated)
- `"3"`: Ropsten Testnet
- `"4"`: Rinkeby Testnet
- `"42"`: Kovan Testnet

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"net_version","params":[],"id":67}'

// Result
{
  "id":67,
  "jsonrpc": "2.0",
  "result": "3"
}
```

My Example
```js
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"net_version","params":[],"id":67}'

```

***

#### net_listening

如果客户端正在主动侦听网络连接，则返回true。
Returns `true` if client is actively listening for network connections.

##### Parameters
none

##### Returns

`Boolean` - `true` when listening, otherwise `false`.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"net_listening","params":[],"id":67}'

// Result
{
  "id":67,
  "jsonrpc":"2.0",
  "result":true
}
```

My Example
```js
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"net_listening","params":[],"id":67}'

```

***

#### net_peerCount

Returns number of peers currently connected to the client.

##### Parameters
none

##### Returns

`QUANTITY` - integer of the number of connected peers.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"net_peerCount","params":[],"id":74}'

// Result
{
  "id":74,
  "jsonrpc": "2.0",
  "result": "0x2" // 2
}
```

My Example
```js
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"net_peerCount","params":[],"id":74}'

```

***

#### eth_protocolVersion

Returns the current ethereum protocol version.

##### Parameters
none

##### Returns

`String` - The current ethereum protocol version

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_protocolVersion","params":[],"id":67}'

// Result
{
  "id":67,
  "jsonrpc": "2.0",
  "result": "54"
}
```

My Example
```js
// Request
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"eth_protocolVersion","params":[],"id":67}'

// Result
{
	"jsonrpc": "2.0",
	"id": 67,
	"result": "0x2712"
}
```

***

#### eth_syncing

同步状态
Returns an object with data about the sync status or `false`.


##### Parameters
none

##### Returns

`Object|Boolean`, An object with sync status data or `FALSE`, when not syncing:
  - `startingBlock`: `QUANTITY` - The block at which the import started (will only be reset, after the sync reached his head)
  - `currentBlock`: `QUANTITY` - The current block, same as eth_blockNumber
  - `highestBlock`: `QUANTITY` - The estimated highest block

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_syncing","params":[],"id":1}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": {
    startingBlock: '0x384',
    currentBlock: '0x386',
    highestBlock: '0x454'
  }
}
// Or when not syncing
{
  "id":1,
  "jsonrpc": "2.0",
  "result": false
}
```

My Example
```js
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"eth_syncing","params":[],"id":1}'
```

***

#### eth_coinbase

客户端挖矿地址
Returns the client coinbase address.


##### Parameters
none

##### Returns

`DATA`, 20 bytes - the current coinbase address.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_coinbase","params":[],"id":64}'

// Result
{
  "id":64,
  "jsonrpc": "2.0",
  "result": "0xc94770007dda54cF92009BFF0dE90c06F603a09f"
}
```

My Example
```js
// Request
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"eth_coinbase","params":[],"id":64}'

// Result 没有在挖矿
{
	"jsonrpc": "2.0",
	"id": 64,
	"error": {
		"code": -32000,
		"message": "not supported"
	}
}

// Result
{
	"id": 64,
	"jsonrpc": "2.0",
	"result": "0xd7b2b8a86f677ecc13b17c383b2ef76aa4ddc151"
}
```

***

#### eth_mining

如果客户端在挖掘新区块。
Returns `true` if client is actively mining new blocks.

##### Parameters
none

##### Returns

`Boolean` - returns `true` of the client is mining, otherwise `false`.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_mining","params":[],"id":71}'

// Result
{
  "id":71,
  "jsonrpc": "2.0",
  "result": true
}

```

My Example
```js
// Request
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"eth_mining","params":[],"id":71}'

// Result 没有在挖矿
{
	"jsonrpc": "2.0",
	"id": 71,
	"result": false
}
```

***

#### eth_hashrate

Returns the number of hashes per second that the node is mining with.

##### Parameters
none

##### Returns

`QUANTITY` - number of hashes per second.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_hashrate","params":[],"id":71}'

// Result
{
  "id":71,
  "jsonrpc": "2.0",
  "result": "0x38a"
}

```

My Example
```js
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"eth_hashrate","params":[],"id":71}'
```

***

#### eth_gasPrice

当前gas的价格，单位为wei
Returns the current price per gas in wei.

##### Parameters
none

##### Returns

`QUANTITY` - integer of the current gas price in wei.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_gasPrice","params":[],"id":73}'

// Result
{
  "id":73,
  "jsonrpc": "2.0",
  "result": "0x09184e72a000" // 10000000000000
}
```

My Example
```js
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"eth_gasPrice","params":[],"id":73}'
```

***

#### eth_accounts

用户的钱包地址列表
Returns a list of addresses owned by client.

##### Parameters
none

##### Returns

`Array of DATA`, 20 Bytes - addresses owned by the client.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_accounts","params":[],"id":1}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": ["0xc94770007dda54cF92009BFF0dE90c06F603a09f"]
}
```

My Example
```js
// Request
curl -H "Content-Type: application/json" 127.0.0.1:7545 --data '{"jsonrpc":"2.0","method":"eth_accounts","params":[],"id":1}'

// Result
{
	"id": 1,
	"jsonrpc": "2.0",
	"result": ["0xd7b2b8a86f677ecc13b17c383b2ef76aa4ddc151", "0x228396a9b6e12f7d3a42514c18ffdd745cda4966", "0x2c9021bec572a3f0b40686d56567603c3baccec5", "0x53ac1fdfa77b21836c4a5185de3ea9e753b33973", "0x1a852144febcd6e6cac372654a8667728a6bf647", "0x03c99d185ad3508843d4c2a6ccb13ac4dc968259", "0x148fbf5c4270e504b6d80897e373ba8c56b16f4c", "0x91f73b31b33cc1b4cff4271f9e630389cf62af7b", "0x34d4c99a531977ce521211838a05401e13d38611", "0x7b71a1f396ab91f151c4690a356049b32dd268ff"]
}
```

***

#### eth_blockNumber

最新区块号
Returns the number of most recent block.

##### Parameters
none

##### Returns

`QUANTITY` - integer of the current block number the client is on.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":83}'

// Result
{
  "id":83,
  "jsonrpc": "2.0",
  "result": "0xc94" // 1207
}
```

My Example
```js
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":83}'
```

***

#### eth_getBalance

查询钱包余额
Returns the balance of the account of given address.

##### Parameters

1. `DATA`, 20 Bytes - address to check for balance.
2. `QUANTITY|TAG` - integer block number, or the string `"latest"`, `"earliest"` or `"pending"`, see the [default block parameter](#the-default-block-parameter)

```js
params: [
   '0xc94770007dda54cF92009BFF0dE90c06F603a09f',
   'latest'
]
```

##### Returns

`QUANTITY` - integer of the current balance in wei.


##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getBalance","params":["0xc94770007dda54cF92009BFF0dE90c06F603a09f", "latest"],"id":1}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x0234c8a3397aab58" // 158972490234375000
}
```

My Example
```js
// Request
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"eth_getBalance","params":["0x43a0603430c049e862fe4fd0985da9f9d735a138", "latest"],"id":1}'

// Result
{
	"jsonrpc": "2.0",
	"id": 1,
	"result": "0x178d133ef4d9f590"
}
```
***

#### eth_getStorageAt

返回给定地址的存储位置的值。
Returns the value from a storage position at a given address. 

##### Parameters

1. `DATA`, 20 Bytes - address of the storage.
2. `QUANTITY` - integer of the position in the storage.
3. `QUANTITY|TAG` - integer block number, or the string `"latest"`, `"earliest"` or `"pending"`, see the [default block parameter](#the-default-block-parameter)

##### Returns

`DATA` - the value at this storage position.

##### Example
Calculating the correct position depends on the storage to retrieve. Consider the following contract deployed at `0x295a70b2de5e3953354a6a8344e616ed314d7251` by address `0x391694e7e0b0cce554cb130d723a9d27458f9298`.

```
contract Storage {
    uint pos0;
    mapping(address => uint) pos1;
    
    function Storage() {
        pos0 = 1234;
        pos1[msg.sender] = 5678;
    }
}
```

Retrieving the value of pos0 is straight forward:

```js
curl -X POST --data '{"jsonrpc":"2.0", "method": "eth_getStorageAt", "params": ["0x295a70b2de5e3953354a6a8344e616ed314d7251", "0x0", "latest"], "id": 1}' localhost:8545

{"jsonrpc":"2.0","id":1,"result":"0x00000000000000000000000000000000000000000000000000000000000004d2"}
```

Retrieving an element of the map is harder. The position of an element in the map is calculated with:
```js
keccack(LeftPad32(key, 0), LeftPad32(map position, 0))
```

This means to retrieve the storage on pos1["0x391694e7e0b0cce554cb130d723a9d27458f9298"] we need to calculate the position with:
```js
keccak(decodeHex("000000000000000000000000391694e7e0b0cce554cb130d723a9d27458f9298" + "0000000000000000000000000000000000000000000000000000000000000001"))
```
The geth console which comes with the web3 library can be used to make the calculation:
```js
> var key = "000000000000000000000000391694e7e0b0cce554cb130d723a9d27458f9298" + "0000000000000000000000000000000000000000000000000000000000000001"
undefined
> web3.sha3(key, {"encoding": "hex"})
"0x6661e9d6d8b923d5bbaab1b96e1dd51ff6ea2a93520fdc9eb75d059238b8c5e9"
```
Now to fetch the storage:
```js
curl -X POST --data '{"jsonrpc":"2.0", "method": "eth_getStorageAt", "params": ["0x295a70b2de5e3953354a6a8344e616ed314d7251", "0x6661e9d6d8b923d5bbaab1b96e1dd51ff6ea2a93520fdc9eb75d059238b8c5e9", "latest"], "id": 1}' localhost:8545

{"jsonrpc":"2.0","id":1,"result":"0x000000000000000000000000000000000000000000000000000000000000162e"}

```

***

#### eth_getTransactionCount

查询该地址发送的交易数
Returns the number of transactions *sent* from an address.


##### Parameters

1. `DATA`, 20 Bytes - address.
2. `QUANTITY|TAG` - integer block number, or the string `"latest"`, `"earliest"` or `"pending"`, see the [default block parameter](#the-default-block-parameter)

```js
params: [
   '0xc94770007dda54cF92009BFF0dE90c06F603a09f',
   'latest' // state at the latest block
]
```

##### Returns

`QUANTITY` - integer of the number of transactions send from this address.


##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getTransactionCount","params":["0xc94770007dda54cF92009BFF0dE90c06F603a09f,"latest"],"id":1}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x1" // 1
}
```

My Example
```js
// Request
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"eth_getTransactionCount","params":["0x43a0603430c049e862fe4fd0985da9f9d735a138","latest"],"id":1}'

// Result
{
	"jsonrpc": "2.0",
	"id": 1,
	"result": "0x7"
}
```

***

#### eth_getBlockTransactionCountByHash

用区块哈希查询该区块的交易数
Returns the number of transactions in a block from a block matching the given block hash.


##### Parameters

1. `DATA`, 32 Bytes - hash of a block

```js
params: [
   '0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238'
]
```

##### Returns

`QUANTITY` - integer of the number of transactions in this block.


##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByHash","params":["0xc94770007dda54cF92009BFF0dE90c06F603a09f"],"id":1}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0xc" // 11
}
```
My Example
[区块信息](https://ropsten.etherscan.io/block/3599064)
```js
// Request
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByHash","params":["0x7da50ab08ebb4f7acea916a02b7d1937fb54ca42228d33210086f57975b9251a"],"id":1}'

// Result
{
	"jsonrpc": "2.0",
	"id": 1,
	"result": "0x7"
}
```
***

#### eth_getBlockTransactionCountByNumber

用区块数（Block Height）查询该区块的交易数
Returns the number of transactions in a block matching the given block number.


##### Parameters

1. `QUANTITY|TAG` - integer of a block number, or the string `"earliest"`, `"latest"` or `"pending"`, as in the [default block parameter](#the-default-block-parameter).

```js
params: [
   '0xe8', // 232
]
```

##### Returns

`QUANTITY` - integer of the number of transactions in this block.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByNumber","params":["0xe8"],"id":1}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0xa" // 10
}
```
My Example
[区块信息](https://ropsten.etherscan.io/block/3599064)
```js
// Request
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByNumber","params":["0x36ead8"],"id":1}'

// Result
{
	"jsonrpc": "2.0",
	"id": 1,
	"result": "0x31"
}
```

***

#### eth_getUncleCountByBlockHash

用block hash查询叔区块的数量
Returns the number of uncles in a block from a block matching the given block hash.

所谓“叔区块”，是指符合难度条件，但区块里的交易不被确认的区块，或叫“废块”（Stale）。比如矿工A挖到一个符合难度规定的合规区块a，而几乎同时矿工B也挖到符合标准的区块b，但由于网络延迟，区块b没有被确认，成了废块，而a成了网络共识的区块，被包括在区块链中。由于以太坊产生区块的速度比比特币产生区块的速度要快很多，因此在网络繁忙的时候，相对于比特币系统更容易出现“废块”。在比特币系统中，生产废块的矿工只能自认倒霉，是没有奖励的。而在以太坊中，产生“叔区块”的矿工和将“叔区块”包括在区块链上的矿工都能得到奖励。这样产生废块的算力也被包括进来，有效地增强了安全性，使得攻击者不容易追上一个带“叔区块”的主链。同时通过给“叔区块”奖励，也避免出现像比特币那样计算力高度集中的矿池，因为矿池相对来说不像单个挖矿节点那样容易产生废块。严格说来，“叔区块”是在当前链接区块往前推最多6个的“祖先”废块，每个区块最多能链接两个“叔区块”。

##### Parameters

1. `DATA`, 32 Bytes - hash of a block

```js
params: [
   '0xc94770007dda54cF92009BFF0dE90c06F603a09f'
]
```

##### Returns

`QUANTITY` - integer of the number of uncles in this block.


##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getUncleCountByBlockHash","params":["0xc94770007dda54cF92009BFF0dE90c06F603a09f"],"id":1}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0xc" // 1
}
```

My Example
[区块信息](https://ropsten.etherscan.io/block/3599064)
```js
// Request
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"eth_getUncleCountByBlockHash","params":["0xc94770007dda54cF92009BFF0dE90c06F603a09f"],"id":1}'

// Result
{
	"jsonrpc": "2.0",
	"id": 1,
	"result": "0x0"
}
```

***

#### eth_getUncleCountByBlockNumber

用区块数查询叔区块的数量
Returns the number of uncles in a block from a block matching the given block number.


##### Parameters

1. `QUANTITY|TAG` - integer of a block number, or the string "latest", "earliest" or "pending", see the [default block parameter](#the-default-block-parameter)

```js
params: [
   '0xe8', // 232
]
```

##### Returns

`QUANTITY` - integer of the number of uncles in this block.


##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getUncleCountByBlockNumber","params":["0xe8"],"id":1}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x1" // 1
}
```

My Example
[区块信息](https://ropsten.etherscan.io/block/3599064)
```js
// Request
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"eth_getUncleCountByBlockNumber","params":["0x36ead8"],"id":1}'

// Result
{
	"jsonrpc": "2.0",
	"id": 1,
	"result": "0x0"
}
```

***

#### eth_getCode

获取指定地址的代码
Returns code at a given address.


##### Parameters

1. `DATA`, 20 Bytes - address
2. `QUANTITY|TAG` - integer block number, or the string `"latest"`, `"earliest"` or `"pending"`, see the [default block parameter](#the-default-block-parameter)

```js
params: [
   '0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b',
   '0x2'  // 2
]
```

##### Returns

`DATA` - the code from the given address.


##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getCode","params":["0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b", "0x2"],"id":1}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x600160008035811a818181146012578301005b601b6001356025565b8060005260206000f25b600060078202905091905056"
}
```

***

#### eth_sign

使用指定帐户签名要发送的数据

The sign method calculates an Ethereum specific signature with: `sign(keccak256("\x19Ethereum Signed Message:\n" + len(message) + message)))`.

通过向消息添加前缀，可以将计算出的签名识别为以太坊特定签名。 这可以防止恶意DApp可以签署任意数据（例如交易）并使用签名来模仿受害者的滥用。
By adding a prefix to the message makes the calculated signature recognisable as an Ethereum specific signature. This prevents misuse where a malicious DApp can sign arbitrary data (e.g. transaction) and use the signature to impersonate the victim.

**Note** the address to sign with must be unlocked. 

##### Parameters
account, message

1. `DATA`, 20 Bytes - address
2. `DATA`, N Bytes - message to sign

##### Returns

`DATA`: Signature

##### Example

```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_sign","params":["0x9b2055d370f73ec7d8a03e965129118dc8f5bf83", "0xdeadbeaf"],"id":1}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0xa3f20717a250c2b0b729b7e5becbff67fdaef7e0699da4de7ca5895b02a170a12d887fd3b17bfdce3481f10bea41f45ba9f709d39ce8325427b57afcfc994cee1b"
}
```

***

#### eth_sendTransaction

若data不为空，发送一个交易到网络，或创建一个合约。
Creates new message call transaction or a contract creation, if the data field contains code.

##### Parameters

1. `Object` - The transaction object

  - `from`: `DATA`, 20 Bytes - The address the transaction is send from.
  指定的发送者的地址。如果不指定，使用eth_defaultAccount。

  - `to`: `DATA`, 20 Bytes - (optional when creating new contract) The address the transaction is directed to.
  交易消息的目标地址，如果是合约创建，则不填.

  - `gas`: `QUANTITY`  - (optional, default: 90000) Integer of the gas provided for the transaction execution. It will return unused gas.
  默认是90000，交易可使用的gas，未使用的gas会退回。

  - `gasPrice`: `QUANTITY`  - (optional, default: To-Be-Determined) Integer of the gasPrice used for each paid gas
  交易的gas价格，默认是网络gas价格的平均值。

  - `value`: `QUANTITY`  - (optional) Integer of the value sent with this transaction
  交易携带的货币量，以wei为单位。如果合约创建交易，则为初始的基金。

  - `data`: `DATA`  - The compiled code of a contract OR the hash of the invoked method signature and encoded parameters. For details see [Ethereum Contract ABI](https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI)
  或者包含相关数据的字节字符串，如果是合约创建，则是初始化要用到的代码。

  - `nonce`: `QUANTITY`  - (optional) Integer of a nonce. This allows to overwrite your own pending transactions that use the same nonce.
  整数，使用此值，可以允许你覆盖你自己的相同nonce的，正在pending中的交易。

```js
params: [{
  "from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155",
  "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567",
  "gas": "0x76c0", // 30400
  "gasPrice": "0x9184e72a000", // 10000000000000
  "value": "0x9184e72a", // 2441406250
  "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
}]
```

##### Returns

`DATA`, 32 Bytes - the transaction hash, or the zero hash if the transaction is not yet available.

Use [eth_getTransactionReceipt](#eth_gettransactionreceipt) to get the contract address, after the transaction was mined, when you created a contract.
如果交易是一个合约创建，请使用eth_getTransactionReceipt在交易完成后获取合约的地址。

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_sendTransaction","params":[{see above}],"id":1}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331"
}
```

***

#### eth_sendRawTransaction

发送一个已经签名的交易
Creates new message call transaction or a contract creation for signed transactions.

##### Parameters

具体参数见eth_sendTransaction

1. `DATA`, The signed transaction data.

```js
params: ["0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"]
```

##### Returns

`DATA`, 32 Bytes - the transaction hash, or the zero hash if the transaction is not yet available.

Use [eth_getTransactionReceipt](#eth_gettransactionreceipt) to get the contract address, after the transaction was mined, when you created a contract.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_sendRawTransaction","params":[{see above}],"id":1}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331"
}
```

***

#### eth_call

直接执行消息调用交易。但不会将数据合并区块链中（这样的调用不会修改状态）
Executes a new message call immediately without creating a transaction on the block chain.


##### Parameters

具体参数解释见eth_sendTransaction。与sendTransaction的区别在于，这里from属性是可选的

1. `Object` - The transaction call object
  - `from`: `DATA`, 20 Bytes - (optional) The address the transaction is sent from.
  - `to`: `DATA`, 20 Bytes  - The address the transaction is directed to.
  - `gas`: `QUANTITY`  - (optional) Integer of the gas provided for the transaction execution. eth_call consumes zero gas, but this parameter may be needed by some executions.
  - `gasPrice`: `QUANTITY`  - (optional) Integer of the gasPrice used for each paid gas
  - `value`: `QUANTITY`  - (optional) Integer of the value sent with this transaction
  - `data`: `DATA`  - (optional) Hash of the method signature and encoded parameters. For details see [Ethereum Contract ABI](https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI)
2. `QUANTITY|TAG` - integer block number, or the string `"latest"`, `"earliest"` or `"pending"`, see the [default block parameter](#the-default-block-parameter)

##### Returns

`DATA` - the return value of executed contract.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_call","params":[{see above}],"id":1}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x"
}
```

***

#### eth_estimateGas

生成和返回完成交易所需要的gas值
Generates and returns an estimate of how much gas is necessary to allow the transaction to complete. The transaction will not be added to the blockchain. Note that the estimate may be significantly more than the amount of gas actually used by the transaction, for a variety of reasons including EVM mechanics and node performance.

##### Parameters

同eth_call，这里所有的参数都是可选的。
See [eth_call](#eth_call) parameters, expect that all properties are optional. If no gas limit is specified geth uses the block gas limit from the pending block as an upper bound. As a result the returned estimate might not be enough to executed the call/transaction when the amount of gas is higher than the pending block gas limit.

##### Returns

`QUANTITY` - the amount of gas used.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_estimateGas","params":[{see above}],"id":1}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x5208" // 21000
}
```

***

#### eth_getBlockByHash

用哈希查询区块信息
Returns information about a block by hash.


##### Parameters

1. `DATA`, 32 Bytes - Hash of a block.
2. `Boolean` - If `true` it returns the full transaction objects, if `false` only the hashes of the transactions.
如果是true则显示transactions的所有内容，false则只显示transactions的hash数组

```js
params: [
   '0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331',
   true
]
```

##### Returns

`Object` - A block object, or `null` when no block was found:

  - `number`: `QUANTITY` - the block number. `null` when its pending block.
  - `hash`: `DATA`, 32 Bytes - hash of the block. `null` when its pending block.
  - `parentHash`: `DATA`, 32 Bytes - hash of the parent block.
  - `nonce`: `DATA`, 8 Bytes - hash of the generated proof-of-work. `null` when its pending block.
  - `sha3Uncles`: `DATA`, 32 Bytes - SHA3 of the uncles data in the block.
  - `logsBloom`: `DATA`, 256 Bytes - the bloom filter for the logs of the block. `null` when its pending block.
  - `transactionsRoot`: `DATA`, 32 Bytes - the root of the transaction trie of the block.
  - `stateRoot`: `DATA`, 32 Bytes - the root of the final state trie of the block.
  - `receiptsRoot`: `DATA`, 32 Bytes - the root of the receipts trie of the block.
  - `miner`: `DATA`, 20 Bytes - the address of the beneficiary to whom the mining rewards were given.
  - `difficulty`: `QUANTITY` - integer of the difficulty for this block.
  - `totalDifficulty`: `QUANTITY` - integer of the total difficulty of the chain until this block.
  - `extraData`: `DATA` - the "extra data" field of this block.
  - `size`: `QUANTITY` - integer the size of this block in bytes.
  - `gasLimit`: `QUANTITY` - the maximum gas allowed in this block.
  - `gasUsed`: `QUANTITY` - the total used gas by all transactions in this block.
  - `timestamp`: `QUANTITY` - the unix timestamp for when the block was collated.
  - `transactions`: `Array` - Array of transaction objects, or 32 Bytes transaction hashes depending on the last given parameter.
  - `uncles`: `Array` - Array of uncle hashes.


##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getBlockByHash","params":["0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331", true],"id":1}'

// Result
{
"id":1,
"jsonrpc":"2.0",
"result": {p
    "number": "0x1b4", // 436
    "hash": "0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331",
    "parentHash": "0x9646252be9520f6e71339a8df9c55e4d7619deeb018d2a3f2d21fc165dde5eb5",
    "nonce": "0xe04d296d2460cfb8472af2c5fd05b5a214109c25688d3704aed5484f9a7792f2",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "logsBloom": "0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331",
    "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
    "stateRoot": "0xd5855eb08b3387c0af375e9cdb6acfc05eb8f519e419b874b6ff2ffda7ed1dff",
    "miner": "0x4e65fda2159562a496f9f3522f89122a3088497a",
    "difficulty": "0x027f07", // 163591
    "totalDifficulty":  "0x027f07", // 163591
    "extraData": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "size":  "0x027f07", // 163591
    "gasLimit": "0x9f759", // 653145
    "gasUsed": "0x9f759", // 653145
    "timestamp": "0x54e34e8e" // 1424182926
    "transactions": [{...},{ ... }] 
    "uncles": ["0x1606e5...", "0xd5145a9..."]
  }
}
```

My Example
[区块信息](https://ropsten.etherscan.io/block/3599064)
```js
// Request
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"eth_getBlockByHash","params":["0x638f44f2dbaea74cd9d83ee75e791880eaf1bc4165b7f0fbb8953747fa6616c5", false],"id":1}'

```

***

#### eth_getBlockByNumber

Returns information about a block by block number.

##### Parameters

1. `QUANTITY|TAG` - integer of a block number, or the string `"earliest"`, `"latest"` or `"pending"`, as in the [default block parameter](#the-default-block-parameter).
2. `Boolean` - If `true` it returns the full transaction objects, if `false` only the hashes of the transactions.

```js
params: [
   '0x1b4', // 436
   true
]
```

##### Returns

See [eth_getBlockByHash](#eth_getblockbyhash)

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x1b4", true],"id":1}'
```

Result see [eth_getBlockByHash](#eth_getblockbyhash)

***

#### eth_getTransactionByHash

用TxHash查询交易
Returns the information about a transaction requested by transaction hash.


##### Parameters

1. `DATA`, 32 Bytes - hash of a transaction

```js
params: [
   "0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238"
]
```

##### Returns

`Object` - A transaction object, or `null` when no transaction was found:

  - `hash`: `DATA`, 32 Bytes - hash of the transaction.
  - `nonce`: `QUANTITY` - the number of transactions made by the sender prior to this one.
  - `blockHash`: `DATA`, 32 Bytes - hash of the block where this transaction was in. `null` when its pending.
  - `blockNumber`: `QUANTITY` - block number where this transaction was in. `null` when its pending.
  - `transactionIndex`: `QUANTITY` - integer of the transactions index position in the block. `null` when its pending.
  - `from`: `DATA`, 20 Bytes - address of the sender.
  - `to`: `DATA`, 20 Bytes - address of the receiver. `null` when its a contract creation transaction.
  - `value`: `QUANTITY` - value transferred in Wei.
  - `gasPrice`: `QUANTITY` - gas price provided by the sender in Wei.
  - `gas`: `QUANTITY` - gas provided by the sender.
  - `input`: `DATA` - the data send along with the transaction.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238"],"id":1}'

// Result
{
"id":1,
"jsonrpc":"2.0",
"result": {
    "hash":"0xc6ef2fc5426d6ad6fd9e2a26abeab0aa2411b7ab17f30a99d3cb96aed1d1055b",
    "nonce":"0x",
    "blockHash": "0xbeab0aa2411b7ab17f30a99d3cb9c6ef2fc5426d6ad6fd9e2a26a6aed1d1055b",
    "blockNumber": "0x15df", // 5599
    "transactionIndex":  "0x1", // 1
    "from":"0x407d73d8a49eeb85d32cf465507dd71d507100c1",
    "to":"0x85h43d8a49eeb85d32cf465507dd71d507100c1",
    "value":"0x7f110", // 520464
    "gas": "0x7f110", // 520464
    "gasPrice":"0x09184e72a000",
    "input":"0x603880600c6000396000f300603880600c6000396000f3603880600c6000396000f360",
  }
}
```


My Example
```js
// Request
curl -H "Content-Type: application/json" 192.168.50.151:8545 --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0xbf0429b9b35d36a9b080ddddc627e2bd0be53a351492ece85f3754e357a67d19"],"id":1}'

// Result
{
	"jsonrpc": "2.0",
	"id": 1,
	"result": {
		"blockHash": "0x638f44f2dbaea74cd9d83ee75e791880eaf1bc4165b7f0fbb8953747fa6616c5",
		"blockNumber": "0xaa44",
		"from": "0xadaf150b905cf5e6a778e553e15a139b6618bbb7",
		"gas": "0x15f90",
		"gasPrice": "0x4a817c800",
		"hash": "0xbf0429b9b35d36a9b080ddddc627e2bd0be53a351492ece85f3754e357a67d19",
		"input": "0x",
		"nonce": "0x2c",
		"to": "0xadd4d1d02e71c7360c53296968e59d57fd15e2ba",
		"transactionIndex": "0x0",
		"value": "0xe8d4a51000",
		"v": "0x2a",
		"r": "0x870695cb0a8f6fa104830335bbd1a75484b6e06c0468adc35f7e4f0c7edc18ee",
		"s": "0x6e5ed3e9197736f86c3ee103c6b5bb83723bceef2b0ab4186d963f34081e1fd3"
	}
}
```

***

#### eth_getTransactionByBlockHashAndIndex

用区块哈希和交易顺序查询交易
Returns information about a transaction by block hash and transaction index position.


##### Parameters

1. `DATA`, 32 Bytes - hash of a block.
2. `QUANTITY` - integer of the transaction index position.

```js
params: [
   '0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331',
   '0x0' // 0
]
```

##### Returns

See [eth_getTransactionByHash](#eth_gettransactionbyhash)

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params":["0xc6ef2fc5426d6ad6fd9e2a26abeab0aa2411b7ab17f30a99d3cb96aed1d1055b", "0x0"],"id":1}'
```

My Example
```js
curl -H "Content-Type: application/json" 192.168.50.151:8545 --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params":["0x638f44f2dbaea74cd9d83ee75e791880eaf1bc4165b7f0fbb8953747fa6616c5", "0x0"],"id":1}'
```

***

#### eth_getTransactionByBlockNumberAndIndex

用区块号和交易顺序查询交易
Returns information about a transaction by block number and transaction index position.


##### Parameters

1. `QUANTITY|TAG` - a block number, or the string `"earliest"`, `"latest"` or `"pending"`, as in the [default block parameter](#the-default-block-parameter).
2. `QUANTITY` - the transaction index position.

```js
params: [
   '0x29c', // 668
   '0x0' // 0
]
```

##### Returns

See [eth_getTransactionByHash](#eth_gettransactionbyhash)

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params":["0x29c", "0x0"],"id":1}'
```

***

#### eth_getTransactionReceipt

用TxHash查询交易
Returns the receipt of a transaction by transaction hash.

**Note** That the receipt is not available for pending transactions.


##### Parameters

1. `DATA`, 32 Bytes - hash of a transaction

```js
params: [
   '0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238'
]
```

##### Returns

`Object` - A transaction receipt object, or `null` when no receipt was found:

  - `transactionHash `: `DATA`, 32 Bytes - hash of the transaction.
  - `transactionIndex`: `QUANTITY` - integer of the transactions index position in the block.
  - `blockHash`: `DATA`, 32 Bytes - hash of the block where this transaction was in.
  - `blockNumber`: `QUANTITY` - block number where this transaction was in.
  - `from`: `DATA`, 20 Bytes - address of the sender.
  - `to`: `DATA`, 20 Bytes - address of the receiver. null when its a contract creation transaction.
  - `cumulativeGasUsed `: `QUANTITY ` - The total amount of gas used when this transaction was executed in the block.
  - `gasUsed `: `QUANTITY ` - The amount of gas used by this specific transaction alone.
  - `contractAddress `: `DATA`, 20 Bytes - The contract address created, if the transaction was a contract creation, otherwise `null`.
  - `logs`: `Array` - Array of log objects, which this transaction generated.
  - `logsBloom`: `DATA`, 256 Bytes - Bloom filter for light clients to quickly retrieve related logs.
  
It also returns _either_ :

  - `root` : `DATA` 32 bytes of post-transaction stateroot (pre Byzantium)
  - `status`: `QUANTITY` either `1` (success) or `0` (failure) 


##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params":["0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238"],"id":1}'

// Result
{
"id":1,
"jsonrpc":"2.0",
"result": {
     transactionHash: '0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238',
     transactionIndex:  '0x1', // 1
     blockNumber: '0xb', // 11
     blockHash: '0xc6ef2fc5426d6ad6fd9e2a26abeab0aa2411b7ab17f30a99d3cb96aed1d1055b',
     cumulativeGasUsed: '0x33bc', // 13244
     gasUsed: '0x4dc', // 1244
     contractAddress: '0xb60e8dd61c5d32be8058bb8eb970870f07233155', // or null, if none was created
     logs: [{
         // logs as returned by getFilterLogs, etc.
     }, ...],
     logsBloom: "0x00...0", // 256 byte bloom filter
     status: '0x1'
  }
}
```
My Example
```js
curl -H "Content-Type: application/json" 192.168.50.151:8545 --data '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params":["0xbf0429b9b35d36a9b080ddddc627e2bd0be53a351492ece85f3754e357a67d19"],"id":1}'
```

***

#### eth_getUncleByBlockHashAndIndex

Returns information about a uncle of a block by hash and uncle index position.


##### Parameters


1. `DATA`, 32 Bytes - hash a block.
2. `QUANTITY` - the uncle's index position.

```js
params: [
   '0xc6ef2fc5426d6ad6fd9e2a26abeab0aa2411b7ab17f30a99d3cb96aed1d1055b',
   '0x0' // 0
]
```

##### Returns

See [eth_getBlockByHash](#eth_getblockbyhash)

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getUncleByBlockHashAndIndex","params":["0xc6ef2fc5426d6ad6fd9e2a26abeab0aa2411b7ab17f30a99d3cb96aed1d1055b", "0x0"],"id":1}'
```

Result see [eth_getBlockByHash](#eth_getblockbyhash)

**Note**: An uncle doesn't contain individual transactions.

***

#### eth_getUncleByBlockNumberAndIndex

Returns information about a uncle of a block by number and uncle index position.


##### Parameters

1. `QUANTITY|TAG` - a block number, or the string `"earliest"`, `"latest"` or `"pending"`, as in the [default block parameter](#the-default-block-parameter).
2. `QUANTITY` - the uncle's index position.

```js
params: [
   '0x29c', // 668
   '0x0' // 0
]
```

##### Returns

See [eth_getBlockByHash](#eth_getblockbyhash)

**Note**: An uncle doesn't contain individual transactions.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getUncleByBlockNumberAndIndex","params":["0x29c", "0x0"],"id":1}'
```

Result see [eth_getBlockByHash](#eth_getblockbyhash)

***

#### eth_getCompilers（已废除）

返回可用的编译器。
Returns a list of available compilers in the client.

##### Parameters
none

##### Returns

`Array` - Array of available compilers.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getCompilers","params":[],"id":1}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": ["solidity", "lll", "serpent"]
}
```


***

#### eth_compileSolidity（已废除）

Returns compiled solidity code.

##### Parameters

1. `String` - The source code.

```js
params: [
   "contract test { function multiply(uint a) returns(uint d) {   return a * 7;   } }",
]
```

##### Returns

`DATA` - The compiled source code.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_compileSolidity","params":["contract test { function multiply(uint a) returns(uint d) {   return a * 7;   } }"],"id":1}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": {
      "code": "0x605880600c6000396000f3006000357c010000000000000000000000000000000000000000000000000000000090048063c6888fa114602e57005b603d6004803590602001506047565b8060005260206000f35b60006007820290506053565b91905056",
      "info": {
        "source": "contract test {\n   function multiply(uint a) constant returns(uint d) {\n       return a * 7;\n   }\n}\n",
        "language": "Solidity",
        "languageVersion": "0",
        "compilerVersion": "0.9.19",
        "abiDefinition": [
          {
            "constant": true,
            "inputs": [
              {
                "name": "a",
                "type": "uint256"
              }
            ],
            "name": "multiply",
            "outputs": [
              {
                "name": "d",
                "type": "uint256"
              }
            ],
            "type": "function"
          }
        ],
        "userDoc": {
          "methods": {}
        },
        "developerDoc": {
          "methods": {}
        }
      }

}
```

***

#### eth_compileLLL（已废除）

Returns compiled LLL code.

##### Parameters

1. `String` - The source code.

```js
params: [
   "(returnlll (suicide (caller)))",
]
```

##### Returns

`DATA` - The compiled source code.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_compileLLL","params":["(returnlll (suicide (caller)))"],"id":1}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x603880600c6000396000f3006001600060e060020a600035048063c6888fa114601857005b6021600435602b565b8060005260206000f35b600081600702905091905056" // the compiled source code
}
```

***

#### eth_compileSerpent（已废除）

Returns compiled serpent code.

##### Parameters

1. `String` - The source code.

```js
params: [
   "/* some serpent */",
]
```

##### Returns

`DATA` - The compiled source code.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_compileSerpent","params":["/* some serpent */"],"id":1}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x603880600c6000396000f3006001600060e060020a600035048063c6888fa114601857005b6021600435602b565b8060005260206000f35b600081600702905091905056" // the compiled source code
}
```

***

#### eth_newFilter

根据过滤器选项创建过滤器对象，以在状态更改（日志）时通知。 要检查状态是否已更改，请调用eth_getFilterChanges。
Creates a filter object, based on filter options, to notify when the state changes (logs).
To check if the state has changed, call [eth_getFilterChanges](#eth_getfilterchanges).

##### A note on specifying topic filters:
Topics are order-dependent. A transaction with a log with topics [A, B] will be matched by the following topic filters:
* `[]` "anything"
* `[A]` "A in first position (and anything after)"
* `[null, B]` "anything in first position AND B in second position (and anything after)"
* `[A, B]` "A in first position AND B in second position (and anything after)"
* `[[A, B], [A, B]]` "(A OR B) in first position AND (A OR B) in second position (and anything after)"

##### Parameters

1. `Object` - The filter options:
  - `fromBlock`: `QUANTITY|TAG` - (optional, default: `"latest"`) Integer block number, or `"latest"` for the last mined block or `"pending"`, `"earliest"` for not yet mined transactions.
  - `toBlock`: `QUANTITY|TAG` - (optional, default: `"latest"`) Integer block number, or `"latest"` for the last mined block or `"pending"`, `"earliest"` for not yet mined transactions.
  - `address`: `DATA|Array`, 20 Bytes - (optional) Contract address or a list of addresses from which logs should originate.
  - `topics`: `Array of DATA`,  - (optional) Array of 32 Bytes `DATA` topics. Topics are order-dependent. Each topic can also be an array of DATA with "or" options.

```js
params: [{
  "fromBlock": "0x1",
  "toBlock": "0x2",
  "address": "0x8888f1f195afa192cfee860698584c030f4c9db1",
  "topics": ["0x000000000000000000000000a94f5374fce5edbc8e2a8697c15331677e6ebf0b", null, ["0x000000000000000000000000a94f5374fce5edbc8e2a8697c15331677e6ebf0b", "0x0000000000000000000000000aff3454fce5edbc8cca8697c15331677e6ebccc"]]
}]
```

##### Returns

`QUANTITY` - A filter id.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_newFilter","params":[{"topics":["0x12341234"]}],"id":73}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0x1" // 1
}
```

***

#### eth_newBlockFilter

在节点中创建过滤器，以在新区块到达时通知。
Creates a filter in the node, to notify when a new block arrives.
To check if the state has changed, call [eth_getFilterChanges](#eth_getfilterchanges).

##### Parameters
None

##### Returns

`QUANTITY` - A filter id.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_newBlockFilter","params":[],"id":73}'

// Result
{
  "id":1,
  "jsonrpc":  "2.0",
  "result": "0x1" // 1
}
```

***

#### eth_newPendingTransactionFilter

在节点中创建过滤器，以通知新的待处理交易何时到达。
Creates a filter in the node, to notify when new pending transactions arrive.
To check if the state has changed, call [eth_getFilterChanges](#eth_getfilterchanges).

##### Parameters
None

##### Returns

`QUANTITY` - A filter id.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_newPendingTransactionFilter","params":[],"id":73}'

// Result
{
  "id":1,
  "jsonrpc":  "2.0",
  "result": "0x1" // 1
}
```

***

#### eth_uninstallFilter

用id卸载过滤器。不需要watch时应该调用。
Uninstalls a filter with given id. Should always be called when watch is no longer needed.
Additonally Filters timeout when they aren't requested with [eth_getFilterChanges](#eth_getfilterchanges) for a period of time.


##### Parameters

1. `QUANTITY` - The filter id.

```js
params: [
  "0xb" // 11
]
```

##### Returns

`Boolean` - `true` if the filter was successfully uninstalled, otherwise `false`.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_uninstallFilter","params":["0xb"],"id":73}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": true
}
```

***

#### eth_getFilterChanges

过滤器的轮询方法，返回自上次轮询以来发生的日志数组。
Polling method for a filter, which returns an array of logs which occurred since last poll.


##### Parameters

1. `QUANTITY` - the filter id.

```js
params: [
  "0x16" // 22
]
```

##### Returns

`Array` - Array of log objects, or an empty array if nothing has changed since last poll.

- For filters created with `eth_newBlockFilter` the return are block hashes (`DATA`, 32 Bytes), e.g. `["0x3454645634534..."]`.
- For filters created with `eth_newPendingTransactionFilter ` the return are transaction hashes (`DATA`, 32 Bytes), e.g. `["0x6345343454645..."]`.
- For filters created with `eth_newFilter` logs are objects with following params:

  - `removed`: `TAG` - `true` when the log was removed, due to a chain reorganization. `false` if its a valid log.
  - `logIndex`: `QUANTITY` - integer of the log index position in the block. `null` when its pending log.
  - `transactionIndex`: `QUANTITY` - integer of the transactions index position log was created from. `null` when its pending log.
  - `transactionHash`: `DATA`, 32 Bytes - hash of the transactions this log was created from. `null` when its pending log.
  - `blockHash`: `DATA`, 32 Bytes - hash of the block where this log was in. `null` when its pending. `null` when its pending log.
  - `blockNumber`: `QUANTITY` - the block number where this log was in. `null` when its pending. `null` when its pending log.
  - `address`: `DATA`, 20 Bytes - address from which this log originated.
  - `data`: `DATA` - contains one or more 32 Bytes non-indexed arguments of the log.
  - `topics`: `Array of DATA` - Array of 0 to 4 32 Bytes `DATA` of indexed log arguments. (In *solidity*: The first topic is the *hash* of the signature of the event (e.g. `Deposit(address,bytes32,uint256)`), except you declared the event with the `anonymous` specifier.)

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getFilterChanges","params":["0x16"],"id":73}'

// Result
{
  "id":1,
  "jsonrpc":"2.0",
  "result": [{
    "logIndex": "0x1", // 1
    "blockNumber":"0x1b4", // 436
    "blockHash": "0x8216c5785ac562ff41e2dcfdf5785ac562ff41e2dcfdf829c5a142f1fccd7d",
    "transactionHash":  "0xdf829c5a142f1fccd7d8216c5785ac562ff41e2dcfdf5785ac562ff41e2dcf",
    "transactionIndex": "0x0", // 0
    "address": "0x16c5785ac562ff41e2dcfdf829c5a142f1fccd7d",
    "data":"0x0000000000000000000000000000000000000000000000000000000000000000",
    "topics": ["0x59ebeb90bc63057b6515673c3ecf9438e5058bca0f92585014eced636878c9a5"]
    },{
      ...
    }]
}
```

***

#### eth_getFilterLogs

返回匹配具有给定id的过滤器的所有日志的数组。
Returns an array of all logs matching filter with given id.


##### Parameters

1. `QUANTITY` - The filter id.

```js
params: [
  "0x16" // 22
]
```

##### Returns

See [eth_getFilterChanges](#eth_getfilterchanges)

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getFilterLogs","params":["0x16"],"id":74}'
```

Result see [eth_getFilterChanges](#eth_getfilterchanges)

***

#### eth_getLogs

返回与给定过滤器对象匹配的所有日志的数组。
Returns an array of all logs matching a given filter object.

##### Parameters

1. `Object` - The filter options:
  - `fromBlock`: `QUANTITY|TAG` - (optional, default: `"latest"`) Integer block number, or `"latest"` for the last mined block or `"pending"`, `"earliest"` for not yet mined transactions.
  - `toBlock`: `QUANTITY|TAG` - (optional, default: `"latest"`) Integer block number, or `"latest"` for the last mined block or `"pending"`, `"earliest"` for not yet mined transactions.
  - `address`: `DATA|Array`, 20 Bytes - (optional) Contract address or a list of addresses from which logs should originate.
  - `topics`: `Array of DATA`,  - (optional) Array of 32 Bytes `DATA` topics. Topics are order-dependent. Each topic can also be an array of DATA with "or" options.
  - `blockhash`:  `DATA`, 32 Bytes - (optional, **future**) With the addition of EIP-234, `blockHash` will be a new filter option which restricts the logs returned to the single block with the 32-byte hash `blockHash`.  Using `blockHash` is equivalent to `fromBlock` = `toBlock` = the block number with hash `blockHash`.  If `blockHash` is present in in the filter criteria, then neither `fromBlock` nor `toBlock` are allowed.

```js
params: [{
  "topics": ["0x000000000000000000000000a94f5374fce5edbc8e2a8697c15331677e6ebf0b"]
}]
```

##### Returns

See [eth_getFilterChanges](#eth_getfilterchanges)

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getLogs","params":[{"topics":["0x000000000000000000000000a94f5374fce5edbc8e2a8697c15331677e6ebf0b"]}],"id":74}'
```

Result see [eth_getFilterChanges](#eth_getfilterchanges)

***

#### eth_getWork

返回当前区块的哈希
Returns the hash of the current block, the seedHash, and the boundary condition to be met ("target").

##### Parameters
none

##### Returns

`Array` - Array with the following properties:
  1. `DATA`, 32 Bytes - current block header pow-hash
  2. `DATA`, 32 Bytes - the seed hash used for the DAG.
  3. `DATA`, 32 Bytes - the boundary condition ("target"), 2^256 / difficulty.

DAG: Dagger Hashimoto是Ethereum 1.0挖掘算法的前体研究实现和规范，但它已被Ethash取代。

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getWork","params":[],"id":73}'

// Result
{
  "id":1,
  "jsonrpc":"2.0",
  "result": [
      "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
      "0x5EED00000000000000000000000000005EED0000000000000000000000000000",
      "0xd1ff1c01710000000000000000000000d1ff1c01710000000000000000000000"
    ]
}
```

My Example
```js
// Request
curl -H "Content-Type: application/json" 127.0.0.1:8545 --data '{"jsonrpc":"2.0","method":"eth_getWork","params":[],"id":73}'

// Result
{
	"jsonrpc": "2.0",
	"result": ["0xc593bc622d3575cb846641e9f984531fc51e7bac86ae5b27b6a4a1b1467981a1", "0x0000000000000000000000000000000000000000000000000000000000000000", "0x0000000040080100200400801002004008010020040080100200400801002004", "0x1"],
	"id": 73
}
```

***

#### eth_submitWork

Used for submitting a proof-of-work solution.


##### Parameters

1. `DATA`, 8 Bytes - The nonce found (64 bits)
2. `DATA`, 32 Bytes - The header's pow-hash (256 bits)
3. `DATA`, 32 Bytes - The mix digest (256 bits)

```js
params: [
  "0x0000000000000001",
  "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
  "0xD1FE5700000000000000000000000000D1FE5700000000000000000000000000"
]
```

##### Returns

`Boolean` - returns `true` if the provided solution is valid, otherwise `false`.


##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0", "method":"eth_submitWork", "params":["0x0000000000000001", "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef", "0xD1GE5700000000000000000000000000D1GE5700000000000000000000000000"],"id":73}'

// Result
{
  "id":73,
  "jsonrpc":"2.0",
  "result": true
}
```

***

#### eth_submitHashrate

Used for submitting mining hashrate.


##### Parameters

1. `Hashrate`, a hexadecimal string representation (32 bytes) of the hash rate 
2. `ID`, String - A random hexadecimal(32 bytes) ID identifying the client

```js
params: [
  "0x0000000000000000000000000000000000000000000000000000000000500000",
  "0x59daa26581d0acd1fce254fb7e85952f4c09d0915afd33d3886cd914bc7d283c"
]
```

##### Returns

`Boolean` - returns `true` if submitting went through succesfully and `false` otherwise.


##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0", "method":"eth_submitHashrate", "params":["0x0000000000000000000000000000000000000000000000000000000000500000", "0x59daa26581d0acd1fce254fb7e85952f4c09d0915afd33d3886cd914bc7d283c"],"id":73}'

// Result
{
  "id":73,
  "jsonrpc":"2.0",
  "result": true
}
```

***

#### db_putString (deprecated)

Stores a string in the local database.

**Note** this function is deprecated and will be removed in the future.

##### Parameters

1. `String` - Database name.
2. `String` - Key name.
3. `String` - String to store.

```js
params: [
  "testDB",
  "myKey",
  "myString"
]
```

##### Returns

`Boolean` - returns `true` if the value was stored, otherwise `false`.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"db_putString","params":["testDB","myKey","myString"],"id":73}'

// Result
{
  "id":1,
  "jsonrpc":"2.0",
  "result": true
}
```

***

#### db_getString (deprecated)

Returns string from the local database.

**Note** this function is deprecated and will be removed in the future.

##### Parameters

1. `String` - Database name.
2. `String` - Key name.

```js
params: [
  "testDB",
  "myKey",
]
```

##### Returns

`String` - The previously stored string.


##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"db_getString","params":["testDB","myKey"],"id":73}'

// Result
{
  "id":1,
  "jsonrpc":"2.0",
  "result": "myString"
}
```

***

#### db_putHex (deprecated)

Stores binary data in the local database.

**Note** this function is deprecated and will be removed in the future.


##### Parameters

1. `String` - Database name.
2. `String` - Key name.
3. `DATA` - The data to store.

```js
params: [
  "testDB",
  "myKey",
  "0x68656c6c6f20776f726c64"
]
```

##### Returns

`Boolean` - returns `true` if the value was stored, otherwise `false`.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"db_putHex","params":["testDB","myKey","0x68656c6c6f20776f726c64"],"id":73}'

// Result
{
  "id":1,
  "jsonrpc":"2.0",
  "result": true
}
```

***

#### db_getHex (deprecated)

Returns binary data from the local database.

**Note** this function is deprecated and will be removed in the future.


##### Parameters

1. `String` - Database name.
2. `String` - Key name.

```js
params: [
  "testDB",
  "myKey",
]
```

##### Returns

`DATA` - The previously stored data.


##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"db_getHex","params":["testDB","myKey"],"id":73}'

// Result
{
  "id":1,
  "jsonrpc":"2.0",
  "result": "0x68656c6c6f20776f726c64"
}
```

***

#### shh_version

Returns the current whisper protocol version.

Whisper协议是DApp间通信的通信协议。

##### Parameters
none

##### Returns

`String` - The current whisper protocol version

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"shh_version","params":[],"id":67}'

// Result
{
  "id":67,
  "jsonrpc": "2.0",
  "result": "2"
}
```

***

#### shh_post

Sends a whisper message.

##### Parameters

1. `Object` - The whisper post object:
  - `from`: `DATA`, 60 Bytes - (optional) The identity of the sender.
  - `to`: `DATA`, 60 Bytes - (optional) The identity of the receiver. When present whisper will encrypt the message so that only the receiver can decrypt it.
  - `topics`: `Array of DATA` - Array of `DATA` topics, for the receiver to identify messages.
  - `payload`: `DATA` - The payload of the message.
  - `priority`: `QUANTITY` - The integer of the priority in a rang from ... (?).
  - `ttl`: `QUANTITY` - integer of the time to live in seconds.

```js
params: [{
  from: "0x04f96a5e25610293e42a73908e93ccc8c4d4dc0edcfa9fa872f50cb214e08ebf61a03e245533f97284d442460f2998cd41858798ddfd4d661997d3940272b717b1",
  to: "0x3e245533f97284d442460f2998cd41858798ddf04f96a5e25610293e42a73908e93ccc8c4d4dc0edcfa9fa872f50cb214e08ebf61a0d4d661997d3940272b717b1",
  topics: ["0x776869737065722d636861742d636c69656e74", "0x4d5a695276454c39425154466b61693532"],
  payload: "0x7b2274797065223a226d6",
  priority: "0x64",
  ttl: "0x64",
}]
```

##### Returns

`Boolean` - returns `true` if the message was send, otherwise `false`.


##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"shh_post","params":[{"from":"0xc931d93e97ab07fe42d923478ba2465f2..","topics": ["0x68656c6c6f20776f726c64"],"payload":"0x68656c6c6f20776f726c64","ttl":0x64,"priority":0x64}],"id":73}'

// Result
{
  "id":1,
  "jsonrpc":"2.0",
  "result": true
}
```

***

#### shh_newIdentity

Creates new whisper identity in the client.

##### Parameters
none

##### Returns

`DATA`, 60 Bytes - the address of the new identiy.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"shh_newIdentity","params":[],"id":73}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0xc931d93e97ab07fe42d923478ba2465f283f440fd6cabea4dd7a2c807108f651b7135d1d6ca9007d5b68aa497e4619ac10aa3b27726e1863c1fd9b570d99bbaf"
}
```

***

#### shh_hasIdentity

Checks if the client hold the private keys for a given identity.


##### Parameters

1. `DATA`, 60 Bytes - The identity address to check.

```js
params: [
  "0x04f96a5e25610293e42a73908e93ccc8c4d4dc0edcfa9fa872f50cb214e08ebf61a03e245533f97284d442460f2998cd41858798ddfd4d661997d3940272b717b1"
]
```

##### Returns

`Boolean` - returns `true` if the client holds the privatekey for that identity, otherwise `false`.


##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"shh_hasIdentity","params":["0x04f96a5e25610293e42a73908e93ccc8c4d4dc0edcfa9fa872f50cb214e08ebf61a03e245533f97284d442460f2998cd41858798ddfd4d661997d3940272b717b1"],"id":73}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": true
}
```

***

#### shh_newGroup

(?)

##### Parameters
none

##### Returns

`DATA`, 60 Bytes - the address of the new group. (?)

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"shh_newGroup","params":[],"id":73}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": "0xc65f283f440fd6cabea4dd7a2c807108f651b7135d1d6ca90931d93e97ab07fe42d923478ba2407d5b68aa497e4619ac10aa3b27726e1863c1fd9b570d99bbaf"
}
```

***

#### shh_addToGroup

(?)

##### Parameters

1. `DATA`, 60 Bytes - The identity address to add to a group (?).

```js
params: [
  "0x04f96a5e25610293e42a73908e93ccc8c4d4dc0edcfa9fa872f50cb214e08ebf61a03e245533f97284d442460f2998cd41858798ddfd4d661997d3940272b717b1"
]
```

##### Returns

`Boolean` - returns `true` if the identity was successfully added to the group, otherwise `false` (?).

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"shh_addToGroup","params":["0x04f96a5e25610293e42a73908e93ccc8c4d4dc0edcfa9fa872f50cb214e08ebf61a03e245533f97284d442460f2998cd41858798ddfd4d661997d3940272b717b1"],"id":73}'

// Result
{
  "id":1,
  "jsonrpc": "2.0",
  "result": true
}
```

***

#### shh_newFilter

Creates filter to notify, when client receives whisper message matching the filter options.


##### Parameters

1. `Object` - The filter options:
  - `to`: `DATA`, 60 Bytes - (optional) Identity of the receiver. *When present it will try to decrypt any incoming message if the client holds the private key to this identity.*
  - `topics`: `Array of DATA` - Array of `DATA` topics which the incoming message's topics should match.  You can use the following combinations:
    - `[A, B] = A && B`
    - `[A, [B, C]] = A && (B || C)`
    - `[null, A, B] = ANYTHING && A && B` `null` works as a wildcard

```js
params: [{
   "topics": ['0x12341234bf4b564f'],
   "to": "0x04f96a5e25610293e42a73908e93ccc8c4d4dc0edcfa9fa872f50cb214e08ebf61a03e245533f97284d442460f2998cd41858798ddfd4d661997d3940272b717b1"
}]
```

##### Returns

`QUANTITY` - The newly created filter.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"shh_newFilter","params":[{"topics": ['0x12341234bf4b564f'],"to": "0x2341234bf4b2341234bf4b564f..."}],"id":73}'

// Result
{
  "id":1,
  "jsonrpc":"2.0",
  "result": "0x7" // 7
}
```

***

#### shh_uninstallFilter

Uninstalls a filter with given id. Should always be called when watch is no longer needed.
Additonally Filters timeout when they aren't requested with [shh_getFilterChanges](#shh_getfilterchanges) for a period of time.


##### Parameters

1. `QUANTITY` - The filter id.

```js
params: [
  "0x7" // 7
]
```

##### Returns

`Boolean` - `true` if the filter was successfully uninstalled, otherwise `false`.

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"shh_uninstallFilter","params":["0x7"],"id":73}'

// Result
{
  "id":1,
  "jsonrpc":"2.0",
  "result": true
}
```

***

#### shh_getFilterChanges

Polling method for whisper filters. Returns new messages since the last call of this method.

**Note** calling the [shh_getMessages](#shh_getmessages) method, will reset the buffer for this method, so that you won't receive duplicate messages.


##### Parameters

1. `QUANTITY` - The filter id.

```js
params: [
  "0x7" // 7
]
```

##### Returns

`Array` - Array of messages received since last poll:

  - `hash`: `DATA`, 32 Bytes (?) - The hash of the message.
  - `from`: `DATA`, 60 Bytes - The sender of the message, if a sender was specified.
  - `to`: `DATA`, 60 Bytes - The receiver of the message, if a receiver was specified.
  - `expiry`: `QUANTITY` - Integer of the time in seconds when this message should expire (?).
  - `ttl`: `QUANTITY` -  Integer of the time the message should float in the system in seconds (?).
  - `sent`: `QUANTITY` -  Integer of the unix timestamp when the message was sent.
  - `topics`: `Array of DATA` - Array of `DATA` topics the message contained.
  - `payload`: `DATA` - The payload of the message.
  - `workProved`: `QUANTITY` - Integer of the work this message required before it was send (?).

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"shh_getFilterChanges","params":["0x7"],"id":73}'

// Result
{
  "id":1,
  "jsonrpc":"2.0",
  "result": [{
    "hash": "0x33eb2da77bf3527e28f8bf493650b1879b08c4f2a362beae4ba2f71bafcd91f9",
    "from": "0x3ec052fc33..",
    "to": "0x87gdf76g8d7fgdfg...",
    "expiry": "0x54caa50a", // 1422566666
    "sent": "0x54ca9ea2", // 1422565026
    "ttl": "0x64", // 100
    "topics": ["0x6578616d"],
    "payload": "0x7b2274797065223a226d657373616765222c2263686...",
    "workProved": "0x0"
    }]
}
```

***

#### shh_getMessages

Get all messages matching a filter. Unlike `shh_getFilterChanges` this returns all messages.

##### Parameters

1. `QUANTITY` - The filter id.

```js
params: [
  "0x7" // 7
]
```

##### Returns

See [shh_getFilterChanges](#shh_getfilterchanges)

##### Example
```js
// Request
curl -X POST --data '{"jsonrpc":"2.0","method":"shh_getMessages","params":["0x7"],"id":73}'
```

Result see [shh_getFilterChanges](#shh_getfilterchanges)


参考链接
[JSON RPC wiki](https://github.com/ethereum/wiki/wiki/JSON-RPC#json-rpc-api)
