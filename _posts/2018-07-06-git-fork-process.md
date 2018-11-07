---
layout: post
title: '开发规范！Git Fork 全流程记录'
date: 2018-07-06
author: June
cover: 'https://june111.github.io/blog/assets/img/post/git-fork.png'
tags: 技术
---

# 开发规范！Git Fork 全流程记录

文章适用于团队合作的时候多个人向一个repo贡献，整理了Git从fork分支开始的过程。

1. Fork    

在github上你要贡献的repo(eg.http://github/remote/test.git)之后称上游仓库。点击fork，将上游仓库fork到你的github，之后称为远程库(eg.http://github/chercher/test.git)

2. Clone    

选择本地文件夹，之后称为本地库，克隆代码到本地
```bash
	git clone http://github/chercher/test.git
```

3. 创建dev分支

进入文件夹中，创建dev分支作为你的开发分支，当你完成了这个开发分支的时候直接将这个分支的内容push到你的远程库。一般一个分支对应一个issue，开发完毕后即可销毁

创建并切换至dev分支（相当于git branch dev + git checkout dev）
```bash
	git checkout -b dev 
```

4. 创建upstream分支

upstream分支是用于同步上游仓库的，可以同步其他人对上游仓库的更改
```bash
	git remote add upstream http://github/remote/test.git
```
查看远程分支
```bash
	git remote
```
查看具体路径
```bash
	git remote -v
```
这时候应该有origin、upstream两种分支且分别有fetch和push的路径，origin是你的远程库，upstream是你的上游仓库

tips. 如果远程分支路径出错了，替换为具体的你的出错的分支名和新的路径即可
```bash
	git remote set-url branch_name new_url 
```

5. 同步上游仓库

在提交自己的修改之前，先同步上游仓库到master

更新
```bash
	git remote update upstream
```
合并
```bash
	git rebase upstream/master
```
 
6. 修改文件push到远程库

对本地库进行修改后，添加文件到暂存区然后提交，写入相应信息。这时你的远程库将会多出一个dev分支
```bash
	git add changed_file  
	git commit -m "message" 
	git push origin dev:dev 
 ```

7. 提出pull request或merge request

这时候在你的远程库中点击create pull request，就可以等待别人review你的代码后merge入上游仓库了


8. 合并commit

一个issue有时候并不是一次commit就可以完成的，这时候就涉及到洁癖患者们用rebase合并commit的过程了

第一次commit的时候并不需要做rebase的操作，rebase是将之后的多次commit合并到之前的一个commit当中

以第二次修改为例，在commit之后进行  
```bash
	git rebase -i HEAD~2 
```
tips. 如果出现"Could not execute editor"  则设置 git config即可
```bash
	git config --global core.editor /usr/bin/vim
```
之后再执行rebase命令，可以看到这两次的提交，现在状态都是pick。只选择第一个commit为p，其他的都为s，即把新的commit并入之前的。

修改完成后写入，然后自动跳转至另一个页面修改commit的信息

之后继续按照第6步`push --force`到远程库的流程进行就可以了~

`push --force` 要慎用！！！容易出现代码事故
