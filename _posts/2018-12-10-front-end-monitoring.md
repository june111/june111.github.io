---
layout: post
title: '前端监控'
date: 2018-12-10
author: June
cover: /assets/img/post/2018-12-10/front-end-monitoring.png
tags: 前端
---

# 前端监控

先上文章结构图～

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-10/structure.svg">
![文章结构]({{site.baseurl}}/assets/img/post/2018-12-10/structure.svg)
</a>

## 前端监控的目的

随着前后端分离，监控也可以分为前后端，前端监控与后端监控的关注不同。

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-10/focus.png">
![前端监控关注]({{site.baseurl}}/assets/img/post/2018-12-10/focus.png)
</a>

其实很多公司都有这个方面的尝试，包括一些开源的解决方案，比如腾讯的badjs，淘宝的JSTracker，阿里巴巴的FdSafe，支付宝的saijs，国外的sentry和对应的前端sdk ravenjs，包括对应的TraceKit，当你真正开始要动手做的时候，一大堆已有的解决方案其实早在3-4年前就已经被人提出，实现和应用了。

### 为什么要做前端监控

都知道监控的重要性，我觉得关键目的有三：

1. 获取用户体验相关的数据。
2. 当客户端出现故障时，能第一时间通知到前端负责人，定位故障，及时止损。
3. 获取用户行为以及跟踪产品在用户端的使用情况，并以监控数据为基础，指明产品优化的方向。

这三条分布对应监控内容的三个方面：性能监控、异常监控和用户行为监控。

### 监控什么

#### 性能监控

指标

* 白屏时间；
* 首屏时间（不同用户，不同机型和不同系统下的首屏加载时间）；
* 主要内容可见时间 FMP(first meaning paint)
* 页面渲染时间
* 用户可交互时间；
* 页面交互动画完成时间
* 总下载时间（静态资源整体下载时间）；
* TCP连接时间；
* HTTP响应时间；

#### 异常监控

指标

* Javascript的异常监控
* 样式丢失的异常监控
* 静态资源加载异常

#### 用户行为监控

指标

* PV/UV: PV (page view)，即页面浏览量或点击量。UV:指访问某个站点或点击某条新闻的不同IP地址的人数
* 用户在每一个页面的停留时间
* 用户通过什么入口来访问该网页
* 用户在相应的页面中触发的行为

## 如何进行前端监控

### 日志采集

收集异常日志，先在本地做一定的处理，采取一定的方案上报到服务器。

#### 采集内容

当异常出现的时候，我们需要知道异常的具体信息，根据异常的具体信息来决定采用什么样的解决方案。在采集异常信息时，可以遵循4W原则：

WHO did WHAT and get WHICH exception in WHICH environment?

1. 用户信息

	出现异常时该用户的信息，例如该用户在当前时刻的状态、权限等，以及需要区分用户可多终端登录时，异常对应的是哪一个终端。

2. 行为信息

	用户进行什么操作时产生了异常：所在的界面路径；执行了什么操作；操作时使用了哪些数据；当时的API吐了什么数据给客户端；如果是提交操作，提交了什么数据；上一个路径；上一个行为日志记录ID等。

3. 异常信息

	产生异常的代码信息：用户操作的DOM元素节点；异常级别；异常类型；异常描述；代码stack信息等。

4. 环境信息

	网络环境；设备型号和标识码；操作系统版本；客户端版本；API接口版本等。


#### 采集性能指标

白屏时间；HTTP响应时间；TCP连接时间；页面渲染时间；用户可交互时间(用户等待页面可用的时间)；页面交互动画完成时间；总下载时间（静态资源整体下载时间）；主要内容可见时间 FMP (first meaning paint)，可以直接使用window.performance接口获取

只是这里的首屏时间，不是真正的首屏时间，只是个接近值。
我觉得比较合理的实现是`加载最慢的图片的时间点 - performance.timing.navigationStart;` 这个要配合具体的业务写，就不上code了。

```js
handleAddListener('load', getTiming)

function handleAddListener(type, fn) {
    if (window.addEventListener) {
        window.addEventListener(type, fn)
    } else {
        window.attachEvent('on' + type, fn)
    }
}

function getTiming() {
    try {
        let time = performance.timing;
        let timingObj = {};

        let loadTime = (time.loadEventEnd - time.loadEventStart) / 1000;

        if (loadTime < 0) {
            setTimeout(function() {
                getTiming();
            }, 200);
            return;
        }

        timingObj['白屏时间'] = (time.domLoading - time.fetchStart) / 1000;

        timingObj['重定向时间'] = (time.redirectEnd - time.redirectStart) / 1000;

        timingObj['DNS解析时间'] = (time.domainLookupEnd - time.domainLookupStart) / 1000;

        timingObj['TCP完成握手时间'] = (time.connectEnd - time.connectStart) / 1000;

        timingObj['HTTP请求响应完成时间'] = (time.responseEnd - time.requestStart) / 1000;

        timingObj['DOM开始加载前所花费时间'] = (time.responseEnd - time.navigationStart) / 1000;

        timingObj['DOM加载完成时间'] = (time.domComplete - time.domLoading) / 1000;

        timingObj['DOM结构解析完成时间'] = (time.domInteractive - time.domLoading) / 1000;

        timingObj['脚本加载时间'] = (time.domContentLoadedEventEnd - time.domContentLoadedEventStart) / 1000;

        timingObj['伪首屏时间,页面加载完成的时间，用户等待页面可用的时间'] = (time.loadEventEnd - time.navigationStart) / 1000;

        timingObj['onload事件时间(页面交互动画完成时间)'] = (time.loadEventEnd - time.loadEventStart) / 1000;

        timingObj['总下载时间（静态资源整体下载时间）'] = (+new Date() - time.navigationStart) / 1000;

        timingObj['页面完全加载时间'] = (timingObj['重定向时间'] + timingObj['DNS解析时间'] + timingObj['TCP完成握手时间'] + timingObj['HTTP请求响应完成时间'] + timingObj['DOM结构解析完成时间'] + timingObj['DOM加载完成时间']);

        for (let item in timingObj) {
            console.log(item + ":" + timingObj[item] + '毫秒(ms)');
        }


    } catch (e) {
        console.log('error: ', e)
    }
}

let client = function() {

    //呈现引擎
    let engine = {
        ie: 0,
        gecko: 0,
        webkit: 0,
        khtml: 0,
        opera: 0,

        //完整的版本号
        ver: null
    };

    //浏览器
    let browser = {

        //主要的浏览器
        ie: 0,
        firefox: 0,
        safari: 0,
        konq: 0,
        opera: 0,
        chrome: 0,

        //具体版本号
        ver: null
    };

    //平台/设备/操作系统
    let system = {
        win: false,
        mac: false,
        x11: false,

        //移动设备
        iphone: false,
        ipod: false,
        ipad: false,
        ios: false,
        android: false,
        nokiaN: false,
        winMobile: false,

        //游戏系统
        wii: false,
        ps: false
    };

    //给上面的属性对象赋值(具体的检测方法实现)
    //检测呈现引擎和浏览器
    let ua = navigator.userAgent;
    if (window.opera) {
        engine.ver = browser.ver = window.opera.version();
        engine.opera = browser.opera = parseFloat(engine.ver);
    } else if (/AppleWebKit\/(\S+)/.test(ua)) {
        engine.ver = RegExp["$1"];
        engine.webkit = parseFloat(engine.ver);

        //确定是 Chrome or Safari
        if (/Chrome\/(\S+)/.test(ua)) {
            browser.ver = RegExp["$1"];
            browser.chrome = parseFloat(browser.ver);
        } else if (/Version\/(\S+)/.test(ua)) {
            browser.ver = RegExp["$1"];
            browser.safari = parseFloat(browser.ver);
        } else {
            //近似地确定版本号
            let safariVersion = 1;
            if (engine.webkit < 100) {
                safariVersion = 1;
            } else if (engine.webkit < 312) {
                safariVersion = 1.2;
            } else if (engine.webkit < 412) {
                safariVersion = 1.3;
            } else {
                safariVersion = 2;
            }

            browser.safari = browser.ver = safariVersion;
        }
    } else if (/KHTML\/(\S+)/.test(ua) || /Konqueror\/([^;]+)/.test(ua)) {
        engine.ver = browser.ver = RegExp["$1"];
        engine.khtml = browser.konq = parseFloat(engine.ver);
    } else if (/rv:([^\)]+)\) Gecko\/\d{8}/.test(ua)) {
        engine.ver = RegExp["$1"];
        engine.gecko = parseFloat(engine.ver);

        //确定是不是 Firefox
        if (/Firefox\/(\S+)/.test(ua)) {
            browser.ver = RegExp["$1"];
            browser.firefox = parseFloat(browser.ver);
        }
    } else if (/MSIE ([^;]+)/.test(ua)) {
        engine.ver = browser.ver = RegExp["$1"];
        engine.ie = browser.ie = parseFloat(engine.ver);
    }

    //检测浏览器
    browser.ie = engine.ie;
    browser.opera = engine.opera;


    //检测平台
    let p = navigator.platform;
    system.win = p.indexOf("Win") == 0;
    system.mac = p.indexOf("Mac") == 0;
    system.x11 = (p == "X11") || (p.indexOf("Linux") == 0);

    //检测 windows 操作系统
    if (system.win) {
        if (/Win(?:dows )?([^do]{2})\s?(\d+\.\d+)?/.test(ua)) {
            if (RegExp["$1"] == "NT") {
                switch (RegExp["$2"]) {
                    case "5.0":
                        system.win = "2000";
                        break;
                    case "5.1":
                        system.win = "XP";
                        break;
                    case "6.0":
                        system.win = "Vista";
                        break;
                    case "6.1":
                        system.win = "7";
                        break;
                    default:
                        system.win = "NT";
                        break;
                }
            } else if (RegExp["$1"] == "9x") {
                system.win = "ME";
            } else {
                system.win = RegExp["$1"];
            }
        }
    }

    //移动设备
    system.iphone = ua.indexOf("iPhone") > -1;
    system.ipod = ua.indexOf("iPod") > -1;
    system.ipad = ua.indexOf("iPad") > -1;
    system.nokiaN = ua.indexOf("NokiaN") > -1;

    //windows mobile
    if (system.win == "CE") {
        system.winMobile = system.win;
    } else if (system.win == "Ph") {
        if (/Windows Phone OS (\d+.\d+)/.test(ua)) {;
            system.win = "Phone";
            system.winMobile = parseFloat(RegExp["$1"]);
        }
    }


    //检测 iOS 版本
    if (system.mac && ua.indexOf("Mobile") > -1) {
        if (/CPU (?:iPhone )?OS (\d+_\d+)/.test(ua)) {
            system.ios = parseFloat(RegExp.$1.replace("_", "."));
        } else {
            system.ios = 2; //can't really detect - so guess
        }
    }

    //检测 Android 版本
    if (/Android (\d+\.\d+)/.test(ua)) {
        system.android = parseFloat(RegExp.$1);
    }

    //游戏系统
    system.wii = ua.indexOf("Wii") > -1;
    system.ps = /playstation/i.test(ua);

    //返回这些对象
    return {
        engine: engine,
        browser: browser,
        system: system
    };
}

function filterData(data) {

    for (const key in data) {
        // 去除对象内多余的数据
        if (data[key] === 0 || data[key] === false) delete data[key]
    }
}

// 过滤无效数据

let clientInfo = client()

filterData(clientInfo.browser)
filterData(clientInfo.engine)
filterData(clientInfo.system)

let envObj = {}

envObj['浏览器信息'] = Object.keys(clientInfo.browser)[0] + ' ' + clientInfo.browser.ver
envObj['浏览器引擎'] = Object.keys(clientInfo.engine)[0] + ' ' + clientInfo.engine.ver
envObj['系统'] = Object.keys(clientInfo.system)[0]

for (let item in envObj) {
    console.log(item + ": " + envObj[item])
}
```

#### 采集异常指标

* try-catch 异常处理

	try-catch 在我们的代码中经常见到，通过给代码块进行 try-catch 进行包装后，当代码块发生出错时 catch 将能捕捉到错误的信息，页面也将可以继续执行。

	但是 try-catch 处理异常的能力有限，只能捕获捉到运行时非异步错误，对于语法错误和异步错误就显得无能为力，捕捉不到。

	示例：运行时错误
	```js
	try {
	  error    // 未定义变量 
	} catch(e) {
	  console.log('我知道错误了');
	  console.log(e);
	}
	```

	然而对于语法错误和异步错误就捕捉不到了。

	一般语法错误在编辑器就会体现出来，常表现的错误信息为： Uncaught SyntaxError: Invalid or unexpected token xxx 这样。但是这种错误会直接抛出异常，常使程序崩溃，一般在编码时候容易观察得到。

	特点：

	* 无法捕捉到语法错误，只能捕捉运行时错误；
	* 可以拿到出错的信息，堆栈，出错的文件、行号、列号；
	* 需要借助工具把所有的function块以及文件块加入try,catch，可以在这个阶段打入更多的静态信息。

* window.onerror 异常处理

	这个偶尔会被try catch影响

	window.onerror 捕获异常能力比 try-catch 稍微强点，无论是异步还是非异步错误，onerror 都能捕获到运行时错误。

	示例：运行时同步错误
	```js
	/**
	 * @param {String}  msg    错误信息
	 * @param {String}  url    出错文件
	 * @param {Number}  row    行号
	 * @param {Number}  col    列号
	 * @param {Object}  error  错误详细信息
	 */
	 window.onerror = function (msg, url, row, col, error) {
	  console.log('我知道错误了');
	  console.log({
	    msg,  url,  row, col, error
	  })
	  return true;
	};
	error;
	```

	示例：异步错误
	```js
	window.onerror = function (msg, url, row, col, error) {
	  console.log('我知道异步错误了');
	  console.log({
	    msg,  url,  row, col, error
	  })
	  return true;
	};
	setTimeout(() => {
	  error;
	});
	```

	然而 window.onerror 对于语法错误还是无能为力，所以我们在写代码的时候要尽可能避免语法错误的，不过一般这样的错误会使得整个页面崩溃，还是比较容易能够察觉到的。

	在实际的使用过程中，onerror 主要是来捕获预料之外的错误，而 try-catch 则是用来在可预见情况下监控特定的错误，两者结合使用更加高效。

	需要注意的是，window.onerror 函数只有在返回 true 的时候，异常才不会向上抛出，否则即使是知道异常的发生控制台还是会显示 Uncaught Error: xxxxx。

	关于 window.onerror 还有两点需要值得注意

	* 对于 onerror 这种全局捕获，最好写在所有 JS 脚本的前面，因为你无法保证你写的代码是否出错，如果写在后面，一旦发生错误的话是不会被 onerror 捕获到的。
	* 另外 onerror 是无法捕获到网络异常的错误。

	由于网络请求异常不会事件冒泡，因此必须在捕获阶段将其捕捉到才行，但是这种方式虽然可以捕捉到网络请求的异常，但是无法判断 HTTP 的状态是 404 还是其他比如 500 等等，所以还需要配合服务端日志才进行排查分析才可以。
	```html
	<script>
	window.addEventListener('error', (msg, url, row, col, error) => {
	  console.log('我知道 404 错误了');
	  console.log(
	    msg, url, row, col, error
	  );
	  return true;
	}, true);
	</script>
	<img src="./404.png" alt="">
	```

	这点知识还是需要知道，要不然用户访问网站，图片 CDN 无法服务，图片加载不出来而开发人员没有察觉就尴尬了。

	当你的页面有使用 iframe 的时候，你需要对你引入的 iframe 做异常监控的处理，否则一旦你引入的 iframe 页面出现了问题，你的主站显示不出来，而你却浑然不知。

	首先需要强调，父窗口直接使用 window.onerror 是无法直接捕获，如果你想要捕获 iframe 的异常的话，有分好几种情况。

	如果你的 iframe 页面和你的主站是同域名的话，直接给 iframe 添加 onerror 事件即可。
	```html
	<iframe src="./iframe.html" frameborder="0"></iframe>
	<script>
	  window.frames[0].onerror = function (msg, url, row, col, error) {
	    console.log('我知道 iframe 的错误了，也知道错误信息');
	    console.log({
	      msg,  url,  row, col, error
	    })
	    return true;
	  };
	</script>
	```

	如果你嵌入的 iframe 页面和你的主站不是同个域名的，但是 iframe 内容不属于第三方，是你可以控制的，那么可以通过与 iframe 通信的方式将异常信息抛给主站接收。与 iframe 通信的方式有很多，常用的如：postMessage，hash 或者 name 字段跨域等等。

	如果是非同域且网站不受自己控制的话，除了通过控制台看到详细的错误信息外，没办法捕获，这是出于安全性的考虑，你引入了一个百度首页，人家页面报出的错误凭啥让你去监控呢，这会引出很多安全性的问题。

	特点

	* 可以捕捉语法错误，也可以捕捉运行时错误；
	* 可以拿到出错的信息，堆栈，出错的文件、行号、列号；
	* 只要在当前页面执行的js脚本出错都会捕捉到，例如：浏览器插件的javascript、或者flash抛出的异常等。
	* 跨域的资源需要特殊头部支持。

	完整方案
	```js
	window.onerror = function(msg,url,line,col,error){
    //没有URL不上报！上报也不知道错误
	    if (msg != "Script error." && !url){
	        return true;
	    }
	    //采用异步的方式
	    //我遇到过在window.onunload进行ajax的堵塞上报
	    //由于客户端强制关闭webview导致这次堵塞上报有Network Error
	    //我猜测这里window.onerror的执行流在关闭前是必然执行的
	    //而离开文章之后的上报对于业务来说是可丢失的
	    //所以我把这里的执行流放到异步事件去执行
	    //脚本的异常数降低了10倍
	    setTimeout(function(){
	        var data = {};
	        //不一定所有浏览器都支持col参数
	        col = col || (window.event && window.event.errorCharacter) || 0;
	        data.url = url;
	        data.line = line;
	        data.col = col;
	        if (!!error && !!error.stack){
	            //如果浏览器有堆栈信息
	            //直接使用
	            data.msg = error.stack.toString();
	        }else if (!!arguments.callee){
	            //尝试通过callee拿堆栈信息
	            var ext = [];
	            var f = arguments.callee.caller, c = 3;
	            //这里只拿三层堆栈信息
	            while (f && (--c>0)) {
	               ext.push(f.toString());
	               if (f  === f.caller) {
	                    break;//如果有环
	               }
	               f = f.caller;
	            }
	            ext = ext.join(",");
	            data.msg = ext;
	        }
	        //把data上报到后台！
	    },0);
	    return true;
	};
	```

* Promise 错误

	通过 Promise 可以帮助我们解决异步回调地狱的问题，但是一旦 Promise 实例抛出异常而你没有用 catch 去捕获的话，onerror 或 try-catch 也无能为力，无法捕捉到错误。

	虽然在写 Promise 实例的时候养成最后写上 catch 函数是个好习惯，但是代码写多了就容易糊涂，忘记写 catch。

	所以如果你的应用用到很多的 Promise 实例的话，特别是你在一些基于 promise 的异步库比如 axios 等一定要小心，因为你不知道什么时候这些异步请求会抛出异常而你并没有处理它，所以你最好添加一个 Promise 全局异常捕获事件 unhandledrejection。
	```js
	window.addEventListener("unhandledrejection", function(e){
	  e.preventDefault()
	  console.log('我知道 promise 的错误了');
	  console.log(e.reason);
	  return true;
	});
	Promise.reject('promise error');
	new Promise((resolve, reject) => {
	  reject('promise error');
	});
	new Promise((resolve) => {
	  resolve();
	}).then(() => {
	  throw 'promise error'
	});
	```

* 使用框架的能力采集错误

	AngularJS 的 `ErrorHandler` , Vue 的 `Vue.config.errorHandler`, React 16 的 `componentDidCatch` 。

* 压缩代码如何定位到脚本异常位置（source map）

	1. 利用 sourcemap 定位到错误代码的具体位置

	2. 另外也可以通过在打包的时候，在每个合并的文件之间添加几行空格，并相应加上一些注释，这样在定位问题的时候很容易可以知道是哪个文件报的错误，然后再通过一些关键词的搜索，可以快速地定位到问题的所在位置。

	以webpack为例，webpack 的 config 文件：
	```js
    devtool: '#cheap-source-map'
	```

#### 采集用户行为指标

如果第三方平台可以满足需求，就用第三方平台吧，可以减少开发工作量。在入口添加一段代码就可以了。

统计系统:仅能呈现问题，告诉你数据是什么

|名称|特点|缺点|
|:--|:--|:--|
|百度统计|别人家都看不到百度的关键词流量情况，百度统计可以看到，所以这个工具在做百度投放优化上，必用。免费。|百度的维度之间的交叉，太差。自定义性，不行。功能全面性还有所欠缺，没有归因，没有电商设置等。|
|友盟+|免费。国内最大的移动应用统计分析平台|并非企业级网站分析工具，是个人站长时代的产品。功能较为有限。|
|腾讯分析|最初腾讯分析是建立在Discuz内置网站统计工具上，每一个disucz论坛都会有腾讯分析工具，由于discuz是主流的论坛建站程序所以腾讯结合市面上的统计工具与论坛大数据的分析在网站统计工具上进行了很好的整合||
|Ptengine|易用性在目前的工具中出类拔萃，热图功能极为强大|付费。功能全面性有待提高，目前没有归因，没有电商设置。自定义能力、路径、转化等，均不可与GA相比。|
|51la|免费，易获取|并非企业级网站分析工具，是个人站长时代的产品。功能较为有限。|

分析系统:不但能呈现问题，还能进一步深入分析，在告诉你数据是什么的同时，还能告诉你数据为什么会这样

|名称|特点|缺点|
|:--|:--|:--|
|Google Analytics|免费提供。GA最实用的功能是细分功能，今天细分功能进一步强大，并且GA推出并不断完善了路径分析能力、用户行为回放、自定义变量（维度和指标）、数据的输入输出（透过上传或者API）等等。GA已经逐渐从一款单纯的网站分析工具过渡为网站的用户行为数据中心。|如果不能科学上网，不能打开她的界面。但是，收集数据的Javascript代码并没有被墙，数据可以正常收集，你只是不能打开报告界面。当然，GA服务器不在国内，有丢包，20%以内，也听说更严重的丢包，但我不能证实。另外，尽管异步载入代码，在网络出现问题的时候，据称仍可能会导致页面一直显示在加载的问题（虽然我没有遇到过）。|
|Adobe Analytics|AA是功能和自定义能力最为强大的网站分析工具|AA需要强大的本地客户支持。如果没有官方的帮助，你想自己配置AA，死了这条心。如果没有配置好AA，功能基本上跟自己开发一个流量计数器差不多。|
|Webtrends|在国内没有太多业务。产品同样需要配置，这一点与AA类似，但是（个人感觉）易用性比AA更弱。|需要非常专业的配置才能发挥作用，所以门槛很高（与AA类似），缺乏国内支援，缺乏知识分享的社区，且在国内已经越来越不主流|
|Piwik|一个PHP和MySQL的开放源代码的Web统计软件， 它给你一些关于你的网站的实用统计报告，比如网页浏览人数， 访问最多的页面， 搜索引擎关键词等等。||
|Mixpanel|精准控制， 准确的发送数据，可以自定义事件、属性，传递丰富的数据到服务端|埋点代价比较大，每一个控件的埋点都需要添加相应的代码，不仅工作量大，而且限定了必须是技术人员才能完成；其次是更新的代价比较大，每一次更新埋点方案，都必须改代码|
|Web Dissector|Web Dissector是国内为数不多的提供企业级网站用户行为数据分析的工具。功能比较丰富，且也能提供较为灵活的配置。另外像归因分析这类较为复杂的流量分析功能，WD也提供|WD并不是类似于GA这样的“大众工具”，而是如Omniture这样的企业级工具，这注定了WD的门槛较高|
|GrowingIO|企业无需在网站或app中埋点，即可获取并分析全面、实时的用户行为数据，以优化产品体验，实现精益化运营，用数据驱动用户和营收的增长。||

### 日志存储

后端接收前端上报的异常日志，经过一定处理，按照一定的存储方案存储。

#### 异常监控上报

监控拿到报错信息之后，接下来就需要将捕捉到的错误信息发送到信息收集平台上，常用的发送形式主要有两种:

* 通过 Ajax 发送数据
* 动态创建 img 标签的形式

实例 - 动态创建 img 标签进行上报
```js
function report(error) {
  var reportUrl = 'http://xxxx/report';
  new Image().src = reportUrl + 'error=' + error;
}
```

#### 前端错误日志

日志服务进入数据处理流程之前要进行采样率控制。

如果你的网站访问量很大，假如网页的 PV 有 1kw，那么一个必然的错误发送的信息就有 1kw 条，我们可以给网站设置一个采集率：
```js
Reporter.send = function(data) {
  // 只采集 30%
  if(Math.random() < 0.3) {
    send(data)      // 上报错误信息
  }
}
```

这个采集率可以通过具体实际的情况来设定，方法多样化，可以使用一个随机数，也可以具体根据用户的某些特征来进行判定。

### 统计与分析

分析分为机器自动分析和人工分析。

机器自动分析，通过预设的条件和算法，对存储的日志信息进行统计和筛选，发现问题，触发报警。

人工分析，通过提供一个可视化的数据面板，让系统用户可以看到具体的日志数据，根据信息，发现异常问题根源。

均值与分布

均值与分布是数据处理中最常见的两种方式。因为它能直观的表示指标的趋势与分布状况，方便进行评估、瓶颈发现与告警。处理过程中应去除异常值，例如明显超过阈值的脏数据等。

耗时的评估中，有很多这方面的研究数据。例如有人提出三个基本的时间范围：

* 0.1秒 : 0.1 秒是用户感知的最小粒度，在这个时间范围内完成的操作被认为是流畅没有延迟的
* 1.0秒 : 1.0 秒内完成的响应认为不会干扰用户的思维流。尽管用户能感觉到延迟，但 0.1 秒 -1.0 秒内完成的操作并不需要给出明显 loading 提示
* 10秒 : 达到 10 秒用户将无法保持注意力，很可能选择离开做其他事情

我们根据业界的一些调研，结合不同指标的特点，制定了指标的分布评估区间。如下图所示：

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-10/speed.png">
![页面速度]({{site.baseurl}}/assets/img/post/2018-12-10/speed.png)
</a>

评估区间的制定方便我们了解当前性能状况，同时对性能趋势波动做出反应。


### 报告和警告

分为告警和预警。

告警按照一定的级别自动报警，通过设定的渠道，按照一定的触发规则进行。

预警则在异常发生前，提前预判，给出警告。

规则报警的问题，监控平台可以引入一些简单的数学模型来解决时序数据的异常识别工作。以最常见的高斯分布（正态分布）为例，利用 3-sigma 原则可以快速判断某一时刻的报错数是否满足概率分布，继而可以产生报警。

## 监控实战

为了方便，性能监控、异常监控和用户行为监控都用第三方的服务。

### 性能监控(Google PageSpeed Insights)

用[Google PageSpeed Insights](http://developers.google.com/speed/pagespeed/insights/)进行网站打开速度测试。按照优化建议来调优。

### 异常监控(Sentry + VUE)

文章篇幅缘故，这部分内容请看：[异常监控(Sentry + VUE)](https://june111.github.io/2018/12/17/unusual-monitoring)

### 用户行为监控(Google Analytics)

用 [Google Analytics](https://analytics.google.com/analytics/web/) 进行数据统计与分析。

GA 会生成一段代码：全局网站代码 (gtag.js)，请复制此代码，并将其作为第一个项目粘贴到您要跟踪的每个网页的 <HEAD> 标记中。如果您的网页上已经有全局网站代码，则只需将以下代码段中的 config 行添加到现有的全局网站代码。

然后检测是否安装成功，成功后就可以在GA看到数据了。

---

觉得文章不错就扫码支持一下呗～

![打赏二维码](https://june111.github.io/assets/img/post/pay-qr.jpg)

## 参考链接

* [2017前端监控系统探索总结](https://juejin.im/post/5a3e121451882533f01ec66d)
* [别再让你的web页面在用户浏览器端裸奔](http://www.aliued.com/?p=4162)
* [把前端监控做到极致](https://zhuanlan.zhihu.com/p/32262716)
* [前端监控和前端埋点方案设计](https://github.com/forthealllight/blog/issues/23)
* [GMTC 大前端时代前端监控的最佳实践](http://jm.taobao.org/2018/06/29/大前端时代前端监控的最佳实践)
* [前端异常监控解决方案研究](https://cdc.tencent.com/2018/09/13/frontend-exception-monitor-research/)
* [前端性能监控：window.performance](https://www.cnblogs.com/libin-1/p/6501951.html)
* [W3C Navigation Timing](https://www.w3.org/TR/navigation-timing/)
* [Web 性能优化-首屏和白屏时间](https://lz5z.com/Web性能优化-首屏和白屏时间/)
* [关于首屏时间采集自动化的解决方案](https://cloud.tencent.com/developer/article/1061844)
* [7 天打造前端性能监控系统 ](http://fex.baidu.com/blog/2014/05/build-performance-monitor-in-7-days/)
* [前端异常监控平台对比](https://www.jianshu.com/p/900e638648a7)
* [前端代码异常监控实战](https://github.com/happylindz/blog/issues/5)
* [前端代码异常监控](http://rapheal.sinaapp.com/2014/11/06/javascript-error-monitor/)
* [站长统计、百度统计、腾讯统计、Google Analytics 哪一统计的数据相对准确些？](https://www.zhihu.com/question/19955915)
* [中国互联网数据分析行业生态：网站分析工具全解析](https://36kr.com/p/5118546.html)
* [高逼格运营必备的8个数据分析工具 让你告别初级运营](https://zhuanlan.zhihu.com/p/33733252)
* [帮你确定应用程序异常的四款在线跟踪服务](http://mobile.51cto.com/hot-564045.htm)
