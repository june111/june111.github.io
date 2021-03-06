---
layout: post
title: 'Markdown常用语法规则'
date: 2018-06-20
author: June
cover: 'https://june111.github.io/assets/img/post/2018-06-20/computer.png'
tags: 技术
---


# Markdown常用语法规则

## 标题
```md
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
```

## 换行
有时候单个换行符，会没有显示的效果，虽然markdown是换行，但是html却是一行的。
这时在换行的时候在行尾加2个空格，就可以解决了。

## 文本样式
```md
**加粗**
*斜体*
~~删除线~~
`底纹`
```
效果：
**加粗**
*斜体*
~~删除线~~
`底纹`

## 列表
#### 无序列表
* 1
* 2
	* 2.1
		* 2.1.1	

#### 有序列表
1. 1
2. 2
	1. 2.1
		1. 2.1.1

#### 有序+无序
* 一
	1. 1.1
* 二
	1. 2.1
		1. 2.1.1

## 引用
只要在文本内容之前加 「 > （大于号）」 即可将文本变成引用文本

>引用的内容

## 图片与链接
* 图片
```md
![图片描述](链接的地址)
```

<!-- ![文章的cover](http://on2171g4d.bkt.clouddn.com/jekyll-banner.png) -->

* 链接
```md
[文本内容](链接的地址)
```

[文章的cover](http://on2171g4d.bkt.clouddn.com/jekyll-banner.png)

## 水平线
三个「 - 」或「 * 」都可以画出一条水平分割线。建议用*

---

***	

## 代码框
两对「 ``` 」包裹
代码前加四个空格键
代码前加一个 tab 键

报错时可以在前后加上
```
{% raw %}
{% endraw %}
```

若要使添加的代码块高亮，将代码语言的名称添加到紧随反引号之后：

```javascript
var a = 1+2;
 ``` 

## 表格
画出来！

Name | Academy | score 
- | :-: | -: 
Harry Potter | Gryffindor| 90 
Hermione Granger | Gryffindor | 100 
Draco Malfoy | Slytherin | 90

## 引号
在网页上写文章建议使用直角引号『「」』。

## 锚点
```md
[说明文字](#列表)
```
[到列表去](#列表)

## 脚注
```md
脚注总是成对出现的，「 [^1] 」作为标记，可以点击跳至末尾注解。
「 [^1]: 」填写注解，不论写在什么位置，都会出现在文章的末尾。
```

这个要注解[^1]

[^1]:注解的具体内容


***

*了解更多：
[Markdown 语法说明 (简体中文版)](http://wowubuntu.com/markdown/)
[Github 中 Markdown 锚点链接如何写](https://my.oschina.net/antsky/blog/1475173)*

