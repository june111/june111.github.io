---
layout: post
title: '浏览器兼容性问题的解决参考方案'
date: 2018-10-25
author: June
cover: 'https://june111.github.io/blog/assets/img/post/browser-compatibility.png'
tags: 前端
---

# 浏览器兼容性问题的解决参考方案

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-10-25/structure.svg">
![文章结构]({{site.baseurl}}/assets/img/post/2018-10-25/structure.svg)
</a>

## 兼容性问题出现的原因

### 为什么要解决兼容性问题

为了提升用户体验。无论用户用什么浏览器来查看我们的网站或者登陆我们的系统，都应该是统一的显示效果。

### 为什么不同的浏览器会产生差异

因为浏览器种类多，而渲染引擎(Rendering Engine)不尽相同。

#### 渲染引擎(Rendering Engine)

渲染引擎(Rendering Engine)，我们一般称为“浏览器内核”。

常见的浏览器内核可以分四种：Trident、Gecko、Blink、Webkit

主流浏览器及其内核：

|浏览器|内核|
|:------|:------|
|IE浏览器|	Trident内核，也成为IE内核|
|Chrome浏览器|	Webkit内核，现在是Blink内核|
|Firefox浏览器|	Gecko内核，俗称Firefox内核|
|Safari浏览器|	Webkit内核|
|Opera浏览器|	最初是自己的Presto内核，后来加入谷歌大军，从Webkit又到了Blink内核；|
|360浏览器|	IE+Chrome双内核|
|猎豹浏览器|	IE+Chrome双内核|
|百度浏览器|	IE内核|
|QQ浏览器|	Trident（兼容模式）+Webkit（高速模式）|

## 兼容性问题的分类

网页由html，css，js组成，下面就从这三方面阐述对应的兼容性问题和解决方法。

### 页面

#### html5shiv.js

解决 ie9 以下浏览器对 html5 新增标签不识别的问题。
```html
<!--[if lt IE 9]>
<script type="text/javascript" src="https://cdn.bootcss.com/html5shiv/3.7.3/html5shiv.min.js"></script>
<![endif]-->
```
#### picturefill.js

解决 IE 9 10 11 等浏览器不支持 `<picture>` 标签的问题
```html
<script src="https://cdn.bootcss.com/picturefill/3.0.3/picturefill.min.js"></script>
```

### 样式

#### 双核浏览器的内核控制问题

解决 双核浏览器优先使用webkit内核 
```html
	<meta name="renderer" content="webkit">
```

#### 常用的第三方库

样式问题纷繁复杂，站在巨人的肩膀上，引用一些第三方库可以加快开发速度

##### Normalize.css

解决不同浏览器的默认样式存在差异的问题

Normalize.css，文件体积小，在默认的HTML元素样式上提供了跨浏览器的高度一致性。支持包括手机浏览器在内的超多浏览器。

直接用 `<script>` 引入
```html
<link href="https://cdn.bootcss.com/normalize/8.0.0/normalize.min.css" rel="stylesheet">
```

NPM
```bash
npm install normalize.css
```
main.js 导入
```js
import 'normalize.css/normalize.css' // A modern alternative to CSS resets
```
##### autoprefixer

解决 浏览器 CSS 缺少兼容前缀的问题。

现在vue的脚手架都带有这个，不用自己安装配置了。

浏览器内核与前缀的对应关系：

|内核|浏览器|前缀|
|:---|:---|:---|
|Trident|IE浏览器|-ms|
|Gecko|Firefox|	-moz|
|Presto	|Opera|	-o|
|Webkit	|Chrome和Safari|	-webkit|

#### 解决IE兼容性问题

##### respond.js

解决 ie9 以下浏览器不支持 CSS3 Media Query 的问题。
```html
<!--[if lt IE 9]>
<script src="https://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
<![endif]-->
```
##### X-UA-Compatible（不建议）

解决 兼容所有旧版IE

生效前提：如果安装了 Google Chrome Frame （谷歌浏览器內嵌框架）则使用谷歌浏览器内核模式，否则使用最新的IE模式
```html
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
```
##### 解决 IE9 以下浏览器不能使用 opacity
```css
opacity: 0.5;
filter: alpha(opacity = 50);
filter: progid:DXImageTransform.Microsoft.Alpha(style = 0, opacity = 50);
```
##### IE6双边距问题

在 IE6中设置了float , 同时又设置margin , 就会出现边距问题

解决 设置display:inline

##### IE6、IE7中标签的高度问题

当标签的高度设置小于10px，在IE6、IE7中会超出自己设置的高度

解决 超出高度的标签设置overflow:hidden,或者设置line-height的值小于你的设置高度

##### IE6、IE7中overflow的溢出问题

两个块级元素，父元素设置了overflow:auto；子元素设置了position:relative ;且高度大于父元素，在IE6、IE7会被隐藏而不是溢出

解决 父级元素设置position:relative


### 交互

#### 语言兼容性的问题

解决 兼容es6及以上的js语言版本

一句话，Using Babel。

#### DOM 事件处理程序的兼容
```js
var eventshiv = {
    // event兼容
    getEvent: function(event) {
        return event ? event : window.event;
    },

    // type兼容
    getType: function(event) {
        return event.type;
    },

    // target兼容
    getTarget: function(event) {
        return event.target ? event.target : event.srcelem;
    },

    // 添加事件句柄
    addHandler: function(elem, type, listener) {
        if (elem.addEventListener) {
            elem.addEventListener(type, listener, false);
        } else if (elem.attachEvent) {
            elem.attachEvent('on' + type, listener);
        } else {
            // 在这里由于.与'on'字符串不能链接，只能用 []
            elem['on' + type] = listener;
        }
    },

    // 移除事件句柄
    removeHandler: function(elem, type, listener) {
        if (elem.removeEventListener) {
            elem.removeEventListener(type, listener, false);
        } else if (elem.detachEvent) {
            elem.detachEvent('on' + type, listener);
        } else {
            elem['on' + type] = null;
        }
    },

    // 添加事件代理
    addAgent: function (elem, type, agent, listener) {
        elem.addEventListener(type, function (e) {
            if (e.target.matches(agent)) {
                listener.call(e.target, e); // this 指向 e.target
            }
        });
    },

    // 取消默认行为
    preventDefault: function(event) {
        if (event.preventDefault) {
            event.preventDefault();
        } else {
            event.returnValue = false;
        }
    },

    // 阻止事件冒泡
    stopPropagation: function(event) {
        if (event.stopPropagation) {
            event.stopPropagation();
        } else {
            event.cancelBubble = true;
        }
    }
};
```
#### 事件兼容的问题

解决 封装一个适配器的方法，过滤事件句柄绑定、移除、冒泡阻止以及默认事件行为处理
```js
 var  helper = {}

 //绑定事件
 helper.on = function(target, type, handler) {
 	if(target.addEventListener) {
 		target.addEventListener(type, handler, false);
 	} else {
 		target.attachEvent("on" + type,
 			function(event) {
 				return handler.call(target, event);
 		    }, false);
 	}
 };

 //取消事件监听
 helper.remove = function(target, type, handler) {
 	if(target.removeEventListener) {
 		target.removeEventListener(type, handler);
 	} else {
 		target.detachEvent("on" + type,
 	    function(event) {
 			return handler.call(target, event);
 		}, true);
     }
 };
```

#### 获取 scrollTop的问题

解决 scrollTop兼容非chrome浏览器
```js
var scrollTop = document.documentElement.scrollTop||document.body.scrollTop;
```
### 浏览器 hack

#### 快速判断 IE 浏览器版本
```html
<!--[if IE 8]> ie8 <![endif]-->
```
#####  IE 条件注释
```html
<!--[if lt IE 9]> XXX <![endif]-->
```
操作符及其含义：

|操作符|含义|
|:---|:---|
|lt|小于|
|gt|大于|
|lte|小于等于|
|gte|不小于|
|!|不等于|

#### 判断是否是 Safari 浏览器
```js
 /* Safari */
 var isSafari = /a/.__proto__=='//';
```
#### 判断是否是 Chrome 浏览器
```js
 /* Chrome */
 var isChrome = Boolean(window.chrome);
```

## 如何检查兼容性问题

### 浏览器兼容性测试工具

为了跨平台使用，只列举几个常见的在线工具。

* [browserling](https://www.browserling.com ) 收费

可以选择运行的windows版本和浏览器种类及版本，模拟浏览器的环境，在线浏览页面，免费版的只能看3分钟。

* [Browser Sandbox](https://turbo.net/browsers) 收费

在新页面打开模拟浏览器环境的网站，自行用网站打开要测试的网站。用户体验比browserling好一些。

* [Browsera](http://www.browsera.com/ ) 收费

Browsera 可以测试和报告在您的网站上的跨浏览器布局的差异和脚本错误。仅仅截取每一个特定的页面，你必须具体再分析才行。

* [browserstack](https://www.browserstack.com ) 收费

提供实时的，基于Web的浏览器测试的能力。

* [crossbrowsertesting](https://crossbrowsertesting.com/ ) 收费

允许用户与超过100分辨率/浏览器/操作系统组合，测试他们的网站。

* [saucelabs](https://saucelabs.com/ )  收费

不是简单地把你的网站在不同的浏览器进行截图，而是室可以让你记录你网站的实时测试效果

* [browsershots](http://browsershots.org/ ) 免费／收费

Browsershots是一个免费开源的在线Web应用程序，可以为你设计的网页在不同的操作系统和浏览器中进行屏幕截图。（ps.收费的可以加快排队速度。)

ps：这些在线测试工具大多是付费的，而且体验不好。

---

觉得文章不错就扫码支持一下呗～

![打赏二维码](https://june111.github.io/blog/assets/img/post/pay-qr.jpg)

参考链接
1. [浏览器兼容性问题解决方案 · 总结](https://juejin.im/post/59a3f2fe6fb9a0249471cbb4)
2. [如何机智地回答浏览器兼容性问题](https://juejin.im/post/5b3da006e51d4518f140edb2)
3. [WEB前端开发人员须知的常见浏览器兼容问题及解决技巧](https://blog.csdn.net/xustart7720/article/details/73604651/)
4. [最全整理浏览器兼容性问题与解决方案](https://blog.csdn.net/weixin_38536027/article/details/79375411)
5. [js兼容性问题总结](https://www.cnblogs.com/yufann/p/Browser1.html )