---
layout: post
title: '常用Git命令总结'
date: 2018-06-29
author: June
cover: 'https://june111.github.io/assets/img/post/2018-06-29/git-command.png'
tags: 技术
---

# 常用Git命令总结

## Command line instructions

### git clone
```bash
	git clone <版本库的网址> <本地目录名>
	git clone -b gzy http://120.79.161.66:90/pandara/pandara-web.git
```
### git remote

为了便于管理，Git要求每个远程主机都必须指定一个主机名。git remote命令就用于管理主机名。

列出所有远程主机
```bash
	git remote
```
查看git路径。参看远程仓库(主机)的网址。
```bash
	git remote -v
```
添加远程仓库地址
```bash
git remote add  origin git@120.79.161.66:Ethworld/ethis-web.git
```
修改远程仓库地址
```bash
	git remote set-url origin http://120.79.161.66:90/pandara/pandara-web.git
```
更新远程分支列表
```bash
	git remote update origin --prune
```

### git fetch

将某个远程主机的更新，全部取回本地。
```bash
	git fetch <远程主机名>
```
取回特定分支的更新
```bash
	git fetch 远程主机名/分支名
```
### git pull

拉代码
```bash
	git pull <远程主机名> <远程分支名>:<本地分支名>
	git pull origin june
```

### git push

推送到june
```bash
	git push <远程主机名> <本地分支名>:<远程分支名>
	git push origin june
```

-u选项指定一个默认主机，这样后面就可以不加任何参数使用git push。
```bash
	git push -u origin master
```
### git branch

查看当前分支
```bash
	git branch
```

查看所有远程分支
```bash
	git branch -a
```
查看远程分支
```bash
	git branch -r
```
删除本地分支
```bash
	git branch -d <分支名>
```
删除远程分支
```bash
	git branch -r -d <远程主机名>/<分支名>
```
在origin/master的基础上，创建一个新分支。
```bash
	git checkout -b newBrach origin/master
```
手动建立追踪关系。更改默认分支。指定master分支追踪origin/next分支
```bash
	git branch --set-upstream master origin/next
	// Branch 'master' set up to track remote branch 'master' from 'origin'.
```
查询默认分支
```bash	
	git config --get branch.master.remote
```
切换分支
```bash
	git checkout <分支名>
```
合并分支
```bash	
	git merge <分支名>
```
添加文件
```bash
	git add <file>
```
提交更新
```bash
	git commit
	git commit –m’xxx’
```
检查
```bash
	git status
```
检查配置信息
```bash	
	git config --list
```
查看日志
```bash
	git log
```

利用 SSH 完成 Git 与 GitHub 的绑定

生成ssh
```bash
	ssh-keygen -t rsa -C 'xxx@xxx.com' 
```
然后一路回车(-C 参数是你的邮箱地址)
输入保存key的文件名，密码（可选）

前往`~/.ssh	` 把key复制，粘贴到Gitlab的ssh中


## 附：初始化项目的官方指南

Git global setup
```bash
	git config --global user.name "June"
	git config --global user.email "june@linktimetech.com"
```
Create a new repository
```bash
	git clone http://120.79.161.66:90/web/edcon.git
	cd edcon
	touch README.md
	git add README.md
	git commit -m "add README"
	git push -u origin master
```
Existing folder or Git repository
```bash
	cd existing_folder
	git init
	git remote add origin http://120.79.161.66:90/web/edcon.git
	git add .
	git commit
	git push -u origin master
```


## 参考链接
1. [git官方指南](https://git-scm.com/book/zh/v2/)
2. [Git远程操作详解](http://www.ruanyifeng.com/blog/2014/06/git_remote.html)
