---
title: 'Loom 做一个dapp'
subtitle: ''
tags: 前端
author: June
cover: /assets/img/post/2019-02-02/cover.png
reward: 1
layout: post
date: 2019-02-02
---

# 

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-02-02/structure.svg">
![文章结构]({{site.baseurl}}/assets/img/post/2019-02-02/structure.svg)
</a>

## 开发环境

安装 Loom 并设置开发环境

在我们的系统上安装 Loom 二进制文件，这样我们就可以有一个本地链来测试。

```bash
curl https://raw.githubusercontent.com/loomnetwork/loom-sdk-documentation/master/scripts/get_loom.sh | sh && chmod +x loom
```

初始化 genesis 文件和 chaindata 目录

```bash
./loom init
```

启动我们的链

```bash
./loom run
```

默认情况下，该链在端口46657上运行，如果我们愿意，可以使用提供的区块浏览器实时查看交易：

[https://blockexplorer.loomx.io/](https://blockexplorer.loomx.io/)

会出现报错，忽略就可以了，因为现在是在单个节点上运行
```bash
E[14026-02-14|09:48:04.964] Couldn't connect to any seeds                module=p2p
```

生成密钥
```bash
./loom genkey -k priv_key -a pub_key
```

结果

```bash
local address: 0xa887dB52e0dA5B32D7423A95D21e5d11b5D50989
local address base64: qIfbUuDaWzLXQjqV0h5dEbXVCYk=
```

这一步会在你包含密钥的目录中创建 priv_key 和 pub_key 文件。 请注意，它将以编码格式保存你的密钥，并且我们需要访问它输出的原始公钥，因此请确保将本地地址公钥输出保存在某处，以便我们以后可以轻松访问它。

MyToken Contract Address: 0x04aed4899e1514e9ebd3b1ea19d845d60f9eab95
MyCoin Contract Address: 0x60ab575af210cc952999976854e938447e919871


---

### 参考链接

* []()
* []()
* []()
* []()
* []()
* []()