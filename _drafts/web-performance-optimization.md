---
layout: post
title: 'web性能优化'
date: 2018-11-03
author: June
cover: 'https://june111.github.io/assets/img/post/browser-compatibility.png'
tags: 前端
---

# web性能优化

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-03/structure.svg">
![文章结构]({{site.baseurl}}/assets/img/post/2018-11-03/structure.svg)
</a>


https://juejin.im/post/5b0b7d74518825158e173a0c

https://tech.meituan.com/performance_tunning.html

https://www.cnblogs.com/xybaby/p/9055734.html

https://www.w3ctech.com/topic/2089

## 为什么要做性能优化

一切都是为了提升用户体验。在求快的时代，网站的响应速度十分重要，如果打开网站速度太慢，用户会选择关闭，而不是无止境地等待。

## 如何进行性能优化

把雅虎 14 条优化原则，《高性能网站建设指南》以及《高性能网站建设进阶指南》中提到的优化点做一次梳理，如果按照优化方向分类可以得到这样一张表格：

|优化方向|优化手段|
|:----|:------- |
|请求数量|合并脚本和样式表，CSS Sprites，拆分初始化负载，划分主域|
|请求带宽|开启 GZip，精简 JavaScript，移除重复脚本，图像优化|
|缓存利用|使用 CDN，使用外部 JavaScript 和 CSS，添加 Expires 头，减少 DNS 查找，配置 ETag，使 Ajax 可缓存|
|页面结构|将样式表放在顶部，将脚本放在底部，尽早刷新文档的输出|
|代码校验|避免重定向，避免 CSS 表达式|

### 工业化流程

一般网站开发都会进行优化的地方，也是已经成熟应用到实际生产中的优化手段：

|优化手段||
|:----|:------- |
|CSS Sprites|把所有小图标放在一张图上，通过背景定位展示图标|
|划分主域|通过“查找 - 替换”，把资源分到不同的域名上|
|开启 GZip|开启服务端的 Gzip 压缩|
|精简 javascript|yui compressor、webpack等打包压缩工具|
|图像优化|用图片压缩工具|
|使用 CDN|使用 CDN 加速服务|
|使用外部 JavaScript 和 CSS|引用第三方库的时候，用他们提供的cdn链接|
|减少 DNS 查找|减少唯一主机名的数量；当页面的组件量比较多的时候，可以考虑将组件分别放到至少2-4个主机名|
|避免重定向|写href属性的时候，使用最完整的地址；如果涉及到从测试环境到生产环境的迁移，建议通过DNS中的CNAME的机制来定义别名，而不是强制地重定向来实现|
|避免 CSS 表达式|避免用CSS动态设置CSS属性，可以用JS代为设置|
|添加 Expires 头，配置 ETag|使用webpack打包，生成的文件都带有hash，可以解决资源缓存的问题|

我们把以上这些已经成熟应用到实际生产中的优化手段去除掉，留下那些还没有很好实现的优化原则，再来回顾一下之前的性能优化分类:

|优化方向|优化手段|
|:----|:-----|
|请求数量|合并脚本和样式表，拆分初始化负载|
|请求带宽|移除重复脚本|
|缓存利用|使 Ajax 可缓存|
|页面结构|将样式表放在顶部，将脚本放在底部，尽早刷新文档的输出|

下面就来说说这些大多数团队没能很好解决的问题吧。

### 有待工业化

静态资源管理与模板框架

解决：合并脚本和样式表

在大型 web 应用，这种方式有一些非常严重的缺陷


<!-- todo -->
https://juejin.im/post/5a966bd16fb9a0635172a50a

http://fex.baidu.com/blog/2014/03/fis-optimize/

https://www.cnblogs.com/dojo-lzz/p/4591446.html

http://taligarsiel.com/Projects/howbrowserswork1.htm

https://github.com/berwin/Blog/issues/23

https://www.jianshu.com/p/9a47f45064af

https://blog.csdn.net/ahuan08/article/details/59481859

https://www.cnblogs.com/sunshineliulu/p/7509810.html

http://blog.oneapm.com/apm-tech/340.html

http://www.10tiao.com/html/148/201603/402847065/1.html

解决：拆分初始化负载

解决：移除重复脚本



解决：将样式表放在顶部，将脚本放在底部



解决：尽早刷新文档的输出

待解决：使 Ajax 可缓存

真正可缓存的 Ajax 在现实开发中比较少见

## 性能好的网站
### 性能指标

响应时间-页面响应时间分布-DNS、TCP耗时
吞吐量
并发数
Apdex指数

### 性能测试

介绍测试工具

1. [Google PageSpeed Insights](http://developers.google.com/speed/pagespeed/insights/)

网页。网站速度和性能测试，通过分析网页内容来为开发者提供提升网站加载速的建议。PageSpeed 的测试包含移动设备和桌面设备两方面，使您的网页在所有设备上都能快速加载。

2. [Yslow](http://yslow.org/)

chrome扩展应用。YSlow 基于一组高性能网页规则来给你提供建议，如何优化可以让网站更快。

3. [Pingdom](https://tools.pingdom.com/)

网页。帮助用户确定网站加载时间并生成大量的报告，例如页面大小、浏览器缓存、性能等级等。它允许您跟踪性能历史和从不同的地理位置进行测试。在线检查网站每个元素的加载速度，生成非常详细的测试报告，帮助你轻松优化网站。

3. [Load Impact](https://loadimpact.com/)

网页。进行负载测试和性能测试。选择一个全球的负荷区，然后测试模拟客户、带宽、数据接受、每秒的请求等等。该工具显示一个漂亮的图表来测量加载时间。


3. [Show Slow](https://github.com/sergeychernyshev/showslow/wiki)

一个开源工具，帮助你监控各种网站性能指标。能够测试网站在 YSlow，Page Speed，WebPageTest 和 dynaTrace AJAX Edition 中的情况。


3. [GT Matrix](https://gtmetrix.com/)

网页。帮助你开发更快速，高效以及用户体验良好的网站。GTmetrix 结合了最流行的 Firefox 的性能组件 YSlow 和谷歌网页速度测试工具。 Gtmetrix 给目标网站评分并提供改进网站存在的问题的建议。


3. [WebPage Test](https://www.webpagetest.org/)

网页。可以运行简单的测试或执行先进的测试包括多级事务、视频捕捉、内容阻塞等。你的结果将提供丰富的诊断信息，包括资源加载瀑布图，页面速度优化检查和改进的建议。

3. [Rapid Search Metrics](https://www.searchmetrics.com/essentials/)

网页。用于做 SEO 搜索引擎优化和速度测试和分析，数据包括网站的平均速度、数据量，非HTML加载时间等等。

3. [Host Tracker](https://www.host-tracker.com/)

网页。可通过来自全球的超过 95% 的节点对网站进行模拟测试，包括错误报告通知到手机，支持HEAD/POST/GET 等方法以及 CGI 脚本操作。

3. [Webo Software](http://www.webogroup.com/corporate/test-speed/?utm_source=webo.name&utm_medium=internal&utm_campaign=webo.name.top&url=www.webogroup.com)

网页。Webo 软件对网站进行性能测试后，将测试结果通过 email 发送给你，同时它也建议什么时候需要提升网站速度、带宽等信息。

3. [Web Page Analyzer](http://www.websiteoptimization.com/services/analyze/)

网页。Web Page Analyzer 可让用户测试网站速度以提升性能，同时可计算网页大小、复杂度和下载时间。


3. [WebToolHub](https://www.webtoolhub.com/)

[测试](http://www.webtoolhub.com/tn561353-website-speed-test.aspx)
网页。网站测试的一个精巧的工具，包括两种测试模式：简单和高级.

简单模式显示网站的加载时间以及各个地方的访问速度，而高级模式还包括每个元素的加载时间。

3. [sitespeed](http://sitespeed.me/en/)

网页。测试每个地区的网页加载速度，页面大小等。

3. [OctaGate](http://www.octagate.com/service/SiteTimer/)

允许你监视用户打开你网站中一个或多个网页的时间。

3. [Web Polygraph](http://www.web-polygraph.org/)

一个用于测试WEB性能的工具，这个工具是很多公司的标准测试工具，包括微软在分析其软件性能的时候，也是使用这个工具做为基准工具的。很多招聘测试员的广告中都注明需要熟练掌握这个测试工具。

3. [OpenSTA](http://opensta.org/)

一个免费的、开放源代码的web性能测试工具，能录制功能非常强大的脚本过程，执行性能测试。例如虚拟多个不同的用户同时登陆被测试网站。其还能对录制的测试脚本进行,按指定的语法进行编辑。在录制完测试脚本后，可以对测试脚本进行编辑，以便进行特定的性能指标分析。其较为丰富的图形化测试结果大大提高了测试报告的可阅读性。OpenSTA 基于CORBA 的结构体系，它通过虚拟一个proxy，使用其专用的脚本控制语言，记录通过proxy 的一切HTTP/S traffic。通过分析OpenSTA的性能指标收集器收集的各项性能指标，以及HTTP 数据，对系统的性能进行分析。

3. []()
3. []()
3. []()
3. []()
3. []()




---

觉得文章不错就扫码支持一下呗～

![打赏二维码](https://june111.github.io/assets/img/post/pay-qr.jpg)



参考链接
1. [前端工程与性能优化](http://fex.baidu.com/blog/2014/03/fis-optimize/)
2. [分享18个常用的网站性能测试工具](https://cloud.tencent.com/info/7c8ea638a8764b6bbf4fd56d7493a67c.html)
3. [五款资深高效的开源Web性能测试工具](https://blog.csdn.net/u012572955/article/details/52238811)
4. []()

