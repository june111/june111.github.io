---
layout: post
title: '入门dAPP，看这篇就够了'
date: 2018-07-07
author: June
cover: 'https://june111.github.io/assets/img/post/2018-07-07/started-dapp.png'
tags: 技术 区块链
---

# 入门dAPP，看这篇就够了

网上有很多关于智能合约的教程，但是简单易懂的很少，最近写了一个dAPP的demo，踩了很多坑，官方文档不是最新的，很多问题搜不到解决方法，要看源码才能解决问题，故萌生了写这个教程的念头。

**网上教程大多都是基于metamask，在测试链进行合约部署和调用的，除了metamask，我还会介绍如何在没有metamask的情况下，进行合约调用。Enjoy～**

`技术栈：Vuejs+Web3js`

dAPP的最终效果如图：

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/vue-dapp.png">
![dAPP]({{site.baseurl}}/assets/img/post/2018-06-30/vue-dapp.png)
</a>



## 准备工作

#### 基础概念

* 智能合约：指一种计算机协议，这类协议一旦制
定和部署就能实现自我执行（self-executing）和自我
验证（self-verifying），而且不再需要人为的干预。
一种以信息化方式传播、验证或者执行合约的计算机协议，能够允许在没有第三方的情况下进行可信的交易，并且这些交易是无法被追踪、同时也是不可逆的。

* Solidity：以太坊的软件开发语言之一，内置了Serpent的
所有特性，但是语法类似于JavaScript。专门用于编写智能合约。

* dAPP(Distributed applications)：由智能合约和客户端代码构成，智能逻辑运行在区块链上，客户端代码运行在
浏览器里。

#### 开发环境

检查是否具备以下工具，若都具备，可以跳过这部分，到下一步

1. nodeJS 和 NPM
2. 以太坊客户端 Geth
3. pm2
4. vue-cli

nodeJS 和 NPM [安装指导](https://nodejs.org/zh-cn/)

可以输入以下指令，看是否正确安装
```bash
node -v
npm -v
```

Geth安装
```bash
brew tap ethereum/ethereum
brew install ethereum
```

pm2安装

```bash
sudo npm i -g pm2
```

脚手架 vue-cli
```bash
npm i vue-cli -g
```


## Metamask
用 [MetaMask](https://metamask.io/) 作为以太坊钱包。如果没有安装MetaMask，需要在chrome应用商店或[官网](https://metamask.io/)进行下载安装。
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/get-metamask.png">
![在Google应用商店下载metamask插件]({{site.baseurl}}/assets/img/post/2018-06-30/get-metamask.png)
</a>

初次打开，需要同意协议，把协议拉到最后，Accept按钮才会亮起来。有3个协议需要同意。
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/metamask01.png">
![同意协议]({{site.baseurl}}/assets/img/post/2018-06-30/metamask01.png)
</a>

输入密码创建一个账户,创建成功后，要把seed word保存下来。seed word可以用于恢复账户或在其他地方导入这个账户。
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/metamask02.png">
![创建账户]({{site.baseurl}}/assets/img/post/2018-06-30/metamask02.png)
</a>
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/metamask03.png">
![创建账户成功]({{site.baseurl}}/assets/img/post/2018-06-30/metamask03.png)
</a>

切换到测试网络Ropsten Test Net
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/metamask04.png">
![切换网络]({{site.baseurl}}/assets/img/post/2018-06-30/metamask04.png)
</a>

点击buy，到 Ropsten Test Faucet 
要一些测试用的ETH。记得不能贪多哦，这个demo，要5个就够了。（不用科学上网也可以）
因为网络问题，有时候点了之后会没有反馈，等一会儿就好了。
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/metamask05.png">
![]({{site.baseurl}}/assets/img/post/2018-06-30/metamask05.png)
</a>

然后打开Metamask，余额为5ETH，Metamask准备完成！
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/metamask06.png">
![]({{site.baseurl}}/assets/img/post/2018-06-30/metamask06.png)
</a>



## 区块链开发环境

#### Ganache

本来想用 Ganache 搭个本地私有链，但是发现和测试网络的环境不一致，有些在本地私有链可以实现的功能，到测试网络就不行了。所以我把测试网络的节点同步到了本地，希望能最大程度地还原测试网络的环境。

Ganache 是以太访可视化私有链，在本地使用内存模拟的以太坊环境。每次执行它都会帮你创建十组帐号且裡面都有充足的ether让你做测试，自动挖矿(每个transaction执行都是即时的），但缺点是把所有东西都存在内存里而不是写在硬碟裡，所以关掉之后，将丢失以前的状态，所有链的资料(帐户余额、合约等)都会消失，因此比较适合用来快速测试你的智能合约的功能。

下载之后，运行Ganache，默认会在7545端口上运行一个私有链。如果想要远程访问Ganache，将127.0.0.1设置成对外的IP地址即可。
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/ganache.png">
![私有链准备完成]({{site.baseurl}}/assets/img/post/2018-06-30/ganache.png)
</a>

对 Ganache 感兴趣的话，可以[下载](https://github.com/trufflesuite/ganache/releases)一个看看。

Ganache 的 node 和 npm 的最低版本要求：npm v5.3.0，node v8.3.0。

#### pm2

创建配置文件 process.json

其中<目录>要填放区块数据的目录路径
```json
    [
      {
        "name"              : "geth",
        "script"            : "geth",
        "args"              : "--testnet --rpc --rpcaddr 0.0.0.0 --rpccorsdomain '*' --syncmode 'light' --maxpeers 100 --cache 1024 --datadir <目录>",
        "log_date_format"   : "YYYY-MM-DD HH:mm Z",
        "merge_logs"        : false,
        "watch"             : false,
        "max_restarts"      : 10,
        "exec_interpreter"  : "none",
        "exec_mode"         : "fork_mode"
      }      
    ]  
```
同步区块
```bash
    pm2 start <process.json文件的路径>
```



## 编写智能合约
本教程不以写合约为重点，故省去写合约的细节，如果你对编写智能合约感兴趣的话，可以去学习一下Solidity，写出属于自己的智能合约～ 在智能合约的世界，限制你的只有你的想象...



## 测试合约
我们用 [Remix](https://remix.ethereum.org/) 来测试和部署合约。Remix 提供一個 Solidity 智能合约的开发环境，可以简易的编译、部署、执行甚至除错，时候编程经验不多的初学者。

进入Remix，新建合约文件Casino.sol，把合约复制粘贴一下
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-01.png">
![新建合约文件Casino.sol]({{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-01.png)
</a>

在Remix环境 Settings 选项卡中，选择版本0.4.21
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-02.png">
![选择Solidity编译器的版本]({{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-02.png)
</a>

切换到 Compile 选项卡，点击Start to compile，有时候会因为环境问题，一直在loading，这时候用一下科学上网就可以了。
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-03.png">
![合约编译完成]({{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-03.png)
</a>



## 部署合约

切换到 run 选项卡，简单介绍一下 Environment 的三个选项

* Javascript VM：简单的Javascript虚拟机环境，纯粹练习智能合约编写的时候可以选择。
* Injected Web3：连接到嵌入到页面的Web3，比如连接到 MetaMask。
* Web3 Provider：连接到自定义的节点。

#### 部署到测试网络Ropsten
确认metamask中的网络环境是Ropsten。run 选项卡的 Environment 选择 Injected Web3，Value(转到合约中的币) 填 **3 ether**，Deplog 的参数填 1000000,80，然后点击Deploy，metamask弹出确认交易的窗口，点确定。
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-04.png">
![部署合约到Ropsten]({{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-04.png)
</a>

注意如果用的是Metamask的新UI，要设置Gas，新UI默认的Gas是0。旧UI默认的Gas是1Gwei。图中是没有设置Gas的，会报错。
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-041.png">
![]({{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-041.png)
</a>

部署成功，返回Txhash
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-05.png">
![部署成功]({{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-05.png)
</a>

区块打包成功，得到合约地址
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-06.png">
![打包成功]({{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-06.png)
</a>
```js
    Contract address ＝ '0x34e97414cD12fE1b3d96B1C9ca6e437aC5FcfdB9'
```
切换到 Compile 选项卡，点击 Details，出来一个窗口，第四个块就是ABI
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-07.png">
![ABI]({{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-07.png)
</a>

```js
    ABI = [
        {
          "constant": false,
          "inputs": [{
            "name": "_number",
            "type": "uint256"
          }],
          "name": "bet",
          "outputs": [],
          "payable": true,
          "stateMutability": "payable",
          "type": "function"
        },
        {
          "constant": false,
          "inputs": [],
          "name": "kill",
          "outputs": [],
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "function"
        },
        {
          "anonymous": false,
          "inputs": [{
              "indexed": false,
              "name": "_status",
              "type": "bool"
            },
            {
              "indexed": false,
              "name": "_amount",
              "type": "uint256"
            }
          ],
          "name": "Won",
          "type": "event"
        },
        {
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "fallback"
        },
        {
          "inputs": [{
              "name": "_minBet",
              "type": "uint256"
            },
            {
              "name": "_houseEdge",
              "type": "uint256"
            }
          ],
          "payable": true,
          "stateMutability": "payable",
          "type": "constructor"
        },
        {
          "constant": true,
          "inputs": [],
          "name": "checkContractBalance",
          "outputs": [{
            "name": "",
            "type": "uint256"
          }],
          "payable": false,
          "stateMutability": "view",
          "type": "function"
        },
        {
          "constant": true,
          "inputs": [],
          "name": "houseEdge",
          "outputs": [{
            "name": "",
            "type": "uint256"
          }],
          "payable": false,
          "stateMutability": "view",
          "type": "function"
        }
      ]
```

#### 部署到本地私有链（如果用Ganache，可以看一下这步，不用的话就跳过吧）
run 选项卡的 Environment 选择 Web3 Provider，并输入我们的测试链的地址 http://127.0.0.1:7545 ，Value 填 **3 ether**，Deplog 的参数填 1000000,80，然后点击Deploy。

打包成功，得到合约地址
```js
    Contract address ＝ '0x34e97414cD12fE1b3d96B1C9ca6e437aC5FcfdB9'
```
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-08.png">
![打包成功]({{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-08.png)
</a>

可以到Ganache看一下区块

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-09.png">
![Ganache区块]({{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-09.png)
</a>

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-10.png">
![Ganache区块1]({{site.baseurl}}/assets/img/post/2018-06-30/deploy-casino-10.png)
</a>

*ABI和上面的相同*

**要记下这里拿到的ABI和Contract address，后面会用到**



## 创建项目
打开终端输入

```
 vue init webpack vue-dapp
```

一路enter到底，项目就建好了。
```bash
    ? Project name vue-dapp
    ? Project description A Vue.js project
    ? Author June 
    ? Vue build standalone
    ? Install vue-router? Yes
    ? Use ESLint to lint your code? No
    ? Set up unit tests No
    ? Setup e2e tests with Nightwatch? No
    ? Should we run `npm install` for you after the project has been created? (recom
    mended) npm
```

#### 安装依赖

mac 可能会遇到权限问题，不能添加文件，或要输入密码才能新建文件夹，我们可以输入以下命令来解决这个问题
```bash
sudo chown -R $USER 「项目文件夹路径」
```

```bash
cd vue-dapp
npm i web3@0.14.0 ethereumjs-abi ethereumjs-tx
```

1. web3

web3需要指定安装0.14.0的版本，因为1.0.0版本还没稳定，而且与MetaMask有点兼容性问题。

[Web3.js](https://github.com/ethereum/web3.js)是以太坊官方的Javascript API，里面封装了以太坊的 JSON RPC API ，提供了一系列与区块链交互的 Javascript 对象和函数，包括查看网络状态，查看本地账户、查看交易和区块、发送交易、编译/部署智能合约、调用智能合约等，其中最重要的就是与智能合约交互的 API。实际上就是一个库的集合，主要包括下面几个库：

* web3-eth 用来与以太坊区块链和智能合约交互
* web3-shh 用来控制whisper协议与p2p通信以及广播
* web3-bzz 用来与swarm协议交互
* web3-utils 包含了一些Dapp开发有用的功能

2. abi

 ABI(Application Binary Interface) 是一种与 Ethereum 生态系统中合约交互的标准方法。我们可以使用 ABI 从区块链外部调用合约（DApp）提供的服务，也可以在合约中调用其他合约的函数。
 [ethereumjs-abi](https://github.com/ethereumjs/ethereumjs-abi)

3. tx
 [ethereumjs-tx](https://github.com/ethereumjs/ethereumjs-tx) 是用于创建，操作和签署以太坊交易的库

## Vue

#### 运行项目
```bash
npm run dev
```

若显示出vue的初始页面，说明项目创建成功，可正常运行。
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/vue-init.png">
![初始页面]({{site.baseurl}}/assets/img/post/2018-06-30/vue-init.png)
</a>

#### 完善项目结构

添加文件夹 contracts，再把合约 Casino.sol 放进去

src/components 中添加文件 casino-dapp.vue

删除文件 HelloWorld.vue

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-06-30/vue-project-structure.png">
![项目结构]({{site.baseurl}}/assets/img/post/2018-06-30/vue-project-structure.png)
</a>

#### 修改几个文件

App.vue
删除logo图片和样式

```js
    <template>
      <div id="app">
        <router-view/>
      </div>
    </template>
    <script>
    export default {
      name: 'App'
    }
    </script>
```
router/index.js
导入和挂载组件
```js
    import Vue from 'vue'
    import Router from 'vue-router'
    import Casino from '@/components/casino-dapp'
    Vue.use(Router)
    export default new Router({
      routes: [
        {
          path: '/',
          name: 'casino-dapp',
          component: Casino
        }
      ]
    })
```



## 实例化Web3

casino-dapp.vue

`目标：导入web3，第一行显示欢迎语，第二行显示web3当前所在的网络`

若Metamask打开，则显示Welcome to the Metamask，若没有Metamask，且正在运行Ganache，则显示Welcome to the Ganache Blockchain
```js
    <template>
      <div>
        <h1>Welcome to the <span v-if="isMetamask">Metamask</span></h1>
        <h2>{{network}}</h2>
      </div>
    </template>
    <script>
    import Web3 from 'web3'
    export default {
      created() {
        this.getWeb3()
      },
      data() {
        return {
          //初始化web3
          web3: undefined,
          isMetamask: false,
          network: '',
        }
      },
      methods: {
        getWeb3() {
          if (typeof web3 !== 'undefined') {
            this.web3 = new Web3(web3.currentProvider);
            this.isMetamask = true
          } else {
            // set the provider you want from Web3.providers
            // 后面涉及到合约event，故不能用Infura
            // this.web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:7545")); //本地ganache
            this.web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545")); //本地同步的测试网络的节点
            this.isMetamask = false
          }
          console.log('Get Web3!')
          this.showNetwork()
        },
        showNetwork() {
          const NETWORKS = {
            '1': 'Main Net',
            '2': 'Deprecated Morden test network',
            '3': 'Ropsten test network',
            '4': 'Rinkeby test network',
            '42': 'Kovan test network',
            '4447': 'Truffle Develop Network',
            '5777': 'Ganache Blockchain'
          }
          var version = this.web3.version.network;
          this.network = NETWORKS[version]
        }
      }
    }
    </script>
```



## 实例化智能合约

casino-dapp.vue

`目标：实例化智能合约`

ABI和contractAddr是合约部署成功后得到的信息，我们在[部署合约](#部署合约)那步已经拿到了。
```js
    created() {
        ...
        this.setContract()
    },
    data() {
         return {
             ...
             //合约提供的数据
             ABI: null,
             contractAddr: '',
             //实例化合约
             casinoContract: undefined,
             casino: undefined,
         }
     },
     methods: {
        getWeb3() {
          this.ABI = [{
              "constant": false,
              "inputs": [{
                "name": "_number",
                "type": "uint256"
              }],
              "name": "bet",
              "outputs": [],
              "payable": true,
              "stateMutability": "payable",
              "type": "function"
            },
            {
              "constant": false,
              "inputs": [],
              "name": "kill",
              "outputs": [],
              "payable": false,
              "stateMutability": "nonpayable",
              "type": "function"
            },
            {
              "anonymous": false,
              "inputs": [{
                  "indexed": false,
                  "name": "_status",
                  "type": "bool"
                },
                {
                  "indexed": false,
                  "name": "_amount",
                  "type": "uint256"
                }
              ],
              "name": "Won",
              "type": "event"
            },
            {
              "payable": false,
              "stateMutability": "nonpayable",
              "type": "fallback"
            },
            {
              "inputs": [{
                  "name": "_minBet",
                  "type": "uint256"
                },
                {
                  "name": "_houseEdge",
                  "type": "uint256"
                }
              ],
              "payable": true,
              "stateMutability": "payable",
              "type": "constructor"
            },
            {
              "constant": true,
              "inputs": [],
              "name": "checkContractBalance",
              "outputs": [{
                "name": "",
                "type": "uint256"
              }],
              "payable": false,
              "stateMutability": "view",
              "type": "function"
            },
            {
              "constant": true,
              "inputs": [],
              "name": "houseEdge",
              "outputs": [{
                "name": "",
                "type": "uint256"
              }],
              "payable": false,
              "stateMutability": "view",
              "type": "function"
            }
          ]
          this.contractAddr = '0x34e97414cD12fE1b3d96B1C9ca6e437aC5FcfdB9' 
        ...
        },
        ...
        setContract() {
          this.casinoContract = this.web3.eth.contract(this.ABI);
          this.casino = this.casinoContract.at(this.contractAddr);
          console.log('Set Contract!')
        }
     }
```
## 与智能合约交互

要调取合約，至少需要：

* 合約地址，例如：0x34e97414cD12fE1b3d96B1C9ca6e437aC5FcfdB9
* 要调取的 function signature，这里我们用 abi 进行函数签名。

另外在 Remix 的 compile 选项卡中的Details，可以看到合约信息，第八块是对应的 function signature。

casino-dapp.vue

导入abi
```js
    import abi from 'ethereumjs-abi'
```
#### 查询合约信息

如果要调用的 function 只是查询，而不是更新合约的状态，可以用 eth.call

其中 params 的值包含：

* "to"：合約地址
* "data"：丟給合约的參數。由三個部分組成：0x、d667dcd7和一個 32 bytes 的參數
* "latest"，代表使用最新的區塊鏈資料

`目标：查询houseEdge`

casino-dapp.vue
```html
    <p>houseEdge: <span>{{odds}}</span></p>
```
```js
    mounted() {
        ...
        this.checkHouseEdge()
    },
    data() {
        return {
          ...
          odds: null,
        }
    },
    methods: {
        ...
        checkHouseEdge() {
          //不能这样调合约方法，本地的私链会成功，但测试网络失败
          // this.casino.houseEdge();
          // function signature
          var encoded = '0x' + abi.methodID('houseEdge', []).toString('hex')
          //调用合约方法
          this.web3.eth.call({
            to: this.contractAddr,
            data: encoded
          }, (error, result) => {
            if (!error) {
              console.log(result);
              this.odds = parseInt(result, 16);
            } else
              console.error(error);
          });
        },
    }
```


#### 更新合约的状态

如果要更新合约的状态，就需要发送 transaction，要发送 transaction 就需要钱包中的 private key 來 sign transaction 和提供 Ether 做手续费

先写界面和样式

```html
    <template>
      <div class="casino">
        <h1>Welcome to the <span v-if="isMetamask">Metamask</span></h1>
        <h2>{{network}}</h2>
        <h1>Welcome to the Casino</h1> 下注:
        <input v-model="amount" placeholder="0">Ether
        <h4>猜数字（1～10）</h4>
        <ul>
          <li v-on:click="clickNumber">1</li>
          <li v-on:click="clickNumber">2</li>
          <li v-on:click="clickNumber">3</li>
          <li v-on:click="clickNumber">4</li>
          <li v-on:click="clickNumber">5</li>
          <li v-on:click="clickNumber">6</li>
          <li v-on:click="clickNumber">7</li>
          <li v-on:click="clickNumber">8</li>
          <li v-on:click="clickNumber">9</li>
          <li v-on:click="clickNumber">10</li>
        </ul>
        <img v-if="pending" id="loader" src="https://loading.io/spinners/double-ring/lg.double-ring-spinner.gif" />
        <div class="event" v-if="winEvent">
          <p v-if="winEvent._status" id="has-won">
            不得了了, 中奖 {{winEvent._amount}} ETH
          </p>
          <p v-else id="has-lost">
            没中诶，再接再厉吧
          </p>
        </div>
      </div>
    </template>
    <style scoped>
        .casino {
          margin-top: 50px;
          text-align: center;
          max-width: 1000px;
        }
        .networkBtn,
        .network {
          position: absolute;
          right: 10px;
        }
          top: 75px;
        }
        .network p {
          margin: 0;
        }
        #loader {
          width: 150px;
        }
        input {
          width: 45px;
        }
        ul {
          margin: 40px;
          list-style-type: none;
          display: grid;
          grid-template-columns: repeat(5, 1fr);
          grid-column-gap: 110px;
          grid-row-gap: 35px;
        }
        li {
          padding: 20px;
          margin-right: 5px;
          border-radius: 50%;
          cursor: pointer;
          background-color: #fff;
          border: -2px solid #bf0d9b;
          color: #bbb6b6;
          /*box-shadow: 3px 5px #bf0d9b;*/
          border: 1px solid #bbb6b6;
        }
        li:hover {
          background-color: rgb(244, 198, 20);
          color: white;
          box-shadow: 0px 0px rgb(244, 198, 20);
          border: none;
        }
        li:active {
          opacity: 0.7;
        }
        * {
          color: #444444;
        }
        #has-won {
          color: green;
        }
        #has-lost {
          color: red;
        }
    </style>
```
```js
    data() {
        return {
          ...
          amount: null,
          pending: false,
          winEvent: null
        }
    },
    methods: {
        ...
        clickNumber(event) {}
    }
```

敲黑板！下面我会分别介绍如何用 Metamask ，和不用 Metamask 来发送 transaction。

1. 用Metamask
```js
   clickNumber(event) {
      this.winEvent = null
      this.pending = true
      this.casino.bet(event.target.innerHTML, {
        gas: 300000, //Gas Limit
        gasPrice: this.web3.toWei('0.000000001', 'ether'), // 1 Gwei
        value: this.web3.toWei(this.amount, 'ether'),
        from: this.web3.eth.coinbase
      }, (err, result, data) => {
        if (err) {
          this.pending = false
          console.log(err)
        } else {
          console.log('result', result)
          //捕捉 event
          let Won = this.casino.Won()
          Won.watch((err, result) => {
            if (err) {
              this.pending = false
              console.error(err)
            } else {
              this.pending = false
              console.log(result)
              this.winEvent = result.args
              this.winEvent._amount = parseInt(result.args._amount, 10) / Math.pow(10, 18);
              this.checkCasinoBalance()
              // 停止捕捉
              Won.stopWatching();
            }
          })
        }
      })
    }
```

2. 不用 Metamask

使用 web3.eth.sendRawTransaction。

RPC 和 web3.js 提供的 SendTransaction 都是連到一節點，使用節點中的帳戶 sign 過再發送。而如果要用自己的帳戶就要用 sendRawTransaction，也就是說要自己建立 transaction、自己 sign 過，再透過 sendRawTransaction 發送。


rawTx 中包含：

* nonce：紀錄目前帳戶送出的交易數，用來避免 replay attack，每次送要加 1。可以用 RPC eth_getTransactionCount 查詢目前帳戶的 nonce。也可以用 Etherscan 查，但 Etherscan 顯示的 No Of Transactions 會包含送出去但沒有成功的交易，所以會不準
* gasPrice：每一计算步骤需要支付矿工的燃料的价格。一般用 1 Gwei（= 1000000000 = 0x3B9ACA00）
* gasLimit：gaslimit 估算可參考 使用ethereum browser計算gas cost
* to：合約地址
* value：要送的 Ether 數量，因為只是要呼叫合約所以設 0
* data：丟給合約的參數。由三個部分組成：0x、60fe47b1和一個 32 bytes 的參數 000000000000000000000000000000000000000000000000000000000000000a(也就是我要更新的值，這邊設 10)

顺便说一下gas
* gas：以太坊上的每笔交易都会被收取一定数量的燃料Gas，设置Gas的目的是限制交易执行所需的工作量，同时为交易的执行支付费用。

导入ethereumjs-tx
```js
    import EthereumTx from 'ethereumjs-tx'
```
data加上钱包信息
```js
    myAddress: '0x43a0603430c049e862fe4fd0985da9f9d735a138',
    myPrivateKey: '3b7525aeaad45f9eaa26406d0df55f9bd10f49b7ea55b5e1909aad4704f8a799',
```
methods 加上。。。todo

```js
    clickNumber(event) {
      this.winEvent = null
      this.pending = true
      const privateKey = Buffer.from(this.myPrivateKey, 'hex')
      var encoded = '0x' + abi.simpleEncode("bet(uint256)", event.target.innerHTML).toString('hex')
      this.getNonce().then(web3Nonce => {
        // gas,gasPrice,value 单位是wei
        const txParams = {
          nonce: web3Nonce,
          gas: this.web3.fromDecimal('300000'), //十进制数字或者十进制字符串转为十六进制
          gasPrice: this.web3.fromDecimal('1000000'), //0.001 Gwei
          value: this.web3.fromDecimal(this.web3.toWei(this.amount, 'ether')),
          to: this.contractAddr,
          from: this.myAddress,
          data: encoded,
          // EIP 155 chainId - mainnet: 1, ropsten: 3
          chainId: 3
        }
        const tx = new EthereumTx(txParams)
        tx.sign(privateKey)
        const serializedTx = tx.serialize()
        this.web3.eth.sendRawTransaction('0x' + serializedTx.toString('hex'), (err, result, data) => {
          if (err) {
            this.pending = false
            console.error(err)
          } else {
            console.log('result', result)
            //捕捉 event
            let Won = this.casino.Won()
            Won.watch((err, result) => {
              console.log('result', result)
              if (err) {
                this.pending = false
                console.error(err)
              } else {
                this.pending = false
                console.log(result)
                this.winEvent = result.args
                this.winEvent._amount = parseInt(result.args._amount, 10) / Math.pow(10, 18);
                this.checkCasinoBalance()
                // 停止捕捉
                Won.stopWatching();
              }
            })
          }
        });
      })
    },
    getNonce() {
      return new Promise((resolve, reject) => {
        this.web3.eth.getTransactionCount(this.myAddress, (error, result) => {
          if (!error) {
            let nonce = '0x' + result.toString(16)
            resolve(nonce)
          } else {
            console.error(error);
          }
        })
      })
    }
```


## 完善UI

`目标：把网络状态隐藏起来，点击按钮时才显示`

```html
    <button @click="checkNetwork" class="networkBtn">Network</button>
    <div v-if="showEnv" class="network">
      <p>Welcome to the <span v-if="isMetamask">Metamask</span></p>
      <p>{{network}}</p>
    </div>
```
data 加
```js
      showEnv: false,
```
methods 加
```js
    checkNetwork() {
      this.showEnv ? this.showEnv = false : this.showEnv = true
    },
```


`目标：显示合约，钱包的余额和钱包的地址`
```html
    <p>奖池：<span>{{contractBalance}}</span> ETH</p>
    <p>账户：<span>{{myAddress}}</span></p>
    <p>余额：<span>{{accountBalance}}</span> ETH</p>
```
```js
    mounted() {
        ...
        this.checkCasinoBalance()
        this.getAccount()
    },
    mounted() {
        this.checkCasinoBalance()
        this.getAccount()
    },
    data() {
        return {
          ...
          accountBalance: null,
          contractBalance: null,
        }
    },
    methods: {
        ...
        getAccount() {
          if (this.isMetamask) {
            //设置账户
            this.web3.eth.accounts[0] ? this.myAddress = this.web3.eth.accounts[0] : alert('请检查账户是否登录')
          } else {
            this.web3.eth.accounts[0] = this.myAddress
          }
          this.web3.eth.getBalance(this.myAddress, (error, result) => {
            if (!error) {
              console.log(result);
              this.accountBalance = parseInt(result, 10) / Math.pow(10, 18);
            } else {
              console.error(error);
            }
          });
        },
        checkCasinoBalance() {
          this.web3.eth.getBalance(this.contractAddr, (error, result) => {
            if (!error) {
              console.log(result);
              this.contractBalance = parseInt(result, 10) / Math.pow(10, 18);
            } else {
              console.error(error);
            }
          });
        },
    }
```
`目标：显示下注的数字，开奖的数字，限制一些`  。。。todo
```html
      <p>您猜的是：<span>{{chooseNum}}</span></p>
      <p>开奖：中奖数字为<span>{{luckyNum}}</span></p>
```
data 加
```js
      chooseNum: null,
      luckyNum: null,
```
修改clickNumber
```js
    clickNumber(event) {
      this.chooseNum = event.target.innerHTML
      let pay = this.amount * (100 - this.odds) / 10
      this.amount <= 0 ? alert('下注太少了，不行啊') : ''
      this.contractBalance < pay ? alert('奖池钱不够啊，赌少一点钱呗') : ''
      if (this.contractBalance > pay && this.amount > 0) {
        this.winEvent = null
        this.pending = true
        if (this.isMetamask) {
          this.casino.bet(event.target.innerHTML, {
            gas: 300000, //Gas Limit
            gasPrice: this.web3.toWei('0.000000001', 'ether'), // 1 Gwei
            value: this.web3.toWei(this.amount, 'ether'),
            from: this.web3.eth.coinbase
          }, (err, result, data) => {
            if (err) {
              this.pending = false
              console.log(err)
            } else {
              console.log('result', result)
              //捕捉 event
              let Won = this.casino.Won()
              Won.watch((err, result) => {
                if (err) {
                  this.pending = false
                  console.error(err)
                } else {
                  this.pending = false
                  console.log(result)
                  let winningNumber = result.blockNumber % 10 + 1 // % 取余数
                  this.luckyNum = winningNumber
                  this.winEvent = result.args
                  this.winEvent._amount = parseInt(result.args._amount, 10) / Math.pow(10, 18);
                  this.checkCasinoBalance()
                  // 停止捕捉
                  Won.stopWatching();
                }
              })
            }
          })
        } else {
          const privateKey = Buffer.from(this.myPrivateKey, 'hex')
          var encoded = '0x' + abi.simpleEncode("bet(uint256)", event.target.innerHTML).toString('hex')
          this.getNonce().then(web3Nonce => {
            // gas,gasPrice,value 单位是wei
            const txParams = {
              nonce: web3Nonce,
              gas: this.web3.fromDecimal('300000'), //十进制数字或者十进制字符串转为十六进制
              gasPrice: this.web3.fromDecimal('1000000'), //0.001 Gwei
              value: this.web3.fromDecimal(this.web3.toWei(this.amount, 'ether')),
              to: this.contractAddr,
              from: this.myAddress,
              data: encoded,
              // EIP 155 chainId - mainnet: 1, ropsten: 3
              chainId: 3
            }
            const tx = new EthereumTx(txParams)
            tx.sign(privateKey)
            const serializedTx = tx.serialize()
            this.web3.eth.sendRawTransaction('0x' + serializedTx.toString('hex'), (err, result, data) => {
              if (err) {
                this.pending = false
                console.error(err)
              } else {
                console.log('result', result)
                //捕捉 event
                let Won = this.casino.Won()
                Won.watch((err, result) => {
                  console.log('result', result)
                  if (err) {
                    this.pending = false
                    console.error(err)
                  } else {
                    this.pending = false
                    console.log(result)
                    let winningNumber = result.blockNumber % 10 + 1 // % 取余数
                    this.luckyNum = winningNumber
                    this.winEvent = result.args
                    this.winEvent._amount = parseInt(result.args._amount, 10) / Math.pow(10, 18);
                    this.checkCasinoBalance()
                    // 停止捕捉
                    Won.stopWatching();
                  }
                })
              }
            });
          })
        }
      }
    },
```

---

觉得文章不错就扫码支持一下呗～

![打赏二维码](https://june111.github.io/assets/img/post/pay-qr.jpg)

## 参考链接
1. [本教程的完整Demo](https://github.com/june111/vue-dapp-demo)
2. [Web3 JavaScript API](https://github.com/ethereum/wiki/wiki/JavaScript-API)
3. [ethereumjs-tx](https://github.com/ethereumjs/ethereumjs-tx)
4. [MetaMask FAQ](https://github.com/MetaMask/faq)


