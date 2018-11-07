---
layout: post
title: 'Mac 常用的命令'
date: 2018-06-28
author: June
cover: 'https://june111.github.io/blog/assets/img/post/mac-command.png'
tags: 技术
---

# Mac 常用的命令

修改文件夹权限

	sudo chown -R $USER 「文件夹路径」

新建文件夹

	mkdir <文件夹名称>

查看历史记录

	history

获取管理员权限
	
	sudo –s 

释放内存

	purge 

退出

	ctr+c 

系统偏好设置 -> 安全性与隐私 出现任何来源的选项
	
	sudo spctl --master-disable 

显示隐藏文件
	
	defaults write com.apple.finder AppleShowAllFiles -boolean true ; killall Finder 

隐藏隐藏文件
	
	defaults write com.apple.finder AppleShowAllFiles -boolean false ; killall Finder 

压缩文件
largefile 文件名包括后缀
500k，每卷大小
分解后文件名默认是 x* ，后缀为 2 位a-z 字母，如 aa、ab

	zip - largefile | split -b 500k

用cat命令恢复成 zip 文件
用解压软件解压file.zip.001～
	
	cat x* > file.zip.001

