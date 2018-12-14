---
layout: post
title: '使用commitizen'
subtitle: '规范化 Git Commit message'
date: 2018-11-06
author: June
cover: 'https://june111.github.io/assets/img/post/2018-11-06/use-commitizen.png'
tags: 技术
---

# 手把手带你用 commitizen

## 安装配置

### 安装

```bash
sudo npm install -g commitizen
```

### 配置

cd到.git所在目录

```bash
commitizen init cz-conventional-changelog --save --save-exact
```

### 使用

用`git cz`命令来取代`git commit`


## Commit 内容详解

### Message 格式

一般来说，Commit Message 应包含三部分内容：Header、Body、Footer

```html
<type>(<scope>): <subject>
// 空一行
<body>
// 空一行
<footer>
```

1. Header

	Header部分应只包含一行，包括三个字段：type、scope和subject

	* type

		用于说明Commit的类型，包含以下7种类型

		feat：新功能（feature）
		fix：修补bug
		docs：文档（documentation）
		style： 格式（不影响代码运行的变动）
		refactor：重构（即不是新增功能，也不是修改bug的代码变动）
		test：增加测试
		chore：构建过程或辅助工具的变动

	* scope

		用于说明本次Commit所影响的范围，比如controller、user或者README，视项目的不同而不同

	* subject

		本次Commit目的的简短描述，一般不要超过50个字符

		规则：

		```js
		以动词开头，使用第一人称现在时，比如change，而不是changed或changes
		第一个字母小写
		结尾不加句号（.）
		```

2. Body

	对本地提交的一个详细描述

3. Footer

	Footer只用于两种情况

	* 不兼容改动

		如果当前代码与上一个版本不兼容，则 Footer 部分以 BREAKING CHANGE 开头，后面是对变动的描述、以及变动理由和迁移方法。

	* 关闭Issue

		如果当前Commit是针对某个 Issue 的提交，那么就可以在Footer中关闭这个Issue：Closes #234


## 例子

```bash
git add .
git cz
```

跟随指引写commit

```html
	Select the type of change that you're committing // type

	What is the scope of this change (e.g. component or file name) // scope

	Write a short, imperative tense description of the change // subject

	Provide a longer description of the change  // Body

	Are there any breaking changes?  // Footer 是否兼容改动

	Does this change affect any open issues?  // Footer 是否关闭Issue
```

最后push，就完成了～

```bash
git push
```

---

觉得文章不错就扫码支持一下呗～

![打赏二维码](https://june111.github.io/assets/img/post/pay-qr.jpg)

## 参考链接

* [Commit message 和 Change log 编写指南](http://www.ruanyifeng.com/blog/2016/01/commit_message_change_log.html)
