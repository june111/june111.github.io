---
layout: post
title: 'Mac上使用 nvm 管理 node 版本'
date: 2019-01-25
author: June
cover: /assets/img/post/2019-01-25/using-nvm-at-mac.png
tags: 前端
---

# Mac上使用 nvm 管理 node 版本

## 卸载已安装到全局的 node/npm

删除下已安装的 node 和全局 node 模块：
```bash
#查看已经安装在全局的模块，以便删除这些全局模块后再按照不同的 node 版本重新进行全局安装
npm ls -g --depth=0

#删除全局 node_modules 目录
sudo rm -rf /usr/local/lib/node_modules

#删除 node
sudo rm /usr/local/bin/node

#删除全局 node 模块注册的软链
cd  /usr/local/bin && ls -l | grep "../lib/node_modules/" | awk '{print $9}'| xargs rm
```

## 安装 nvm

```bash
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash
```
配一下环境变量

编辑.bash_profile文件，没有的话就新建一个，命令都是：

```bash
vi ~/.bash_profile
```

然后将以下代码复制进去，保存退出(esc 然后:wq 保存退出)

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
```

然后 source 一下 .bash_profile

```bash
source ~/.bash_profile
```

## 使用nvm

```bash
nvm install stable # 安装最新稳定版 node
nvm install 8.15 # 安装 8.15.0 版本
```

## 切换版本

```bash
nvm use 8 # 切换至 8.15.0 版本
```
---
### 参考链接

* [Mac上使用nvm管理node版本](https://www.jianshu.com/p/04d31f6c22bd)
