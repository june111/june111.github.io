
# 测试


测试分类
<!-- todo -->
[高流量网站如何做出高性能？](http://blog.oneapm.com/apm-tech/340.html)

* 性能测试

lighthouse
安装
```bash
npm install -g lighthouse
```
使用 
```bash
lighthouse https://mobile.twitter.com/home
```

* 负载测试

3. [Pylot]()

Pylot是一款开源的测试web service性能和扩展性的工具，它运行HTTP 负载测试，这对容量计划，确定基准点，分析以及系统调优都很有用处。Pylot产生并发负载（HTTP Requests），检验服务器响应，以及产生带有metrics的报表。通过GUI或者shell/console来执行和监视test suites。

3. [Multi-Mechanize](https://pypi.org/project/multi-mechanize/)

是一个网站性能和负载测试的开源框架。 它允许你编写Python脚本来生成对一个网站或Web服务的负载。

3. [Apache JMeter](http://jmeter.apache.org/)

Apache JMeter是一款Java平台的开源测试工具，专门为运行和服务器装载测试而设计的、100％的纯Java桌面运行程序。原先它是为Web/HTTP测试而设计的，但是它已经扩展以支持各种各样的测试模块。它和用于HTTP和SQL数据库（使用JDBC）的模块一起运送。它可以用来测试静止资料库或者活动资料库中的服务器的运行情况，可以用来模拟对服务器或者网络系统加以重负荷以测试它的抵抗力，或者用来分析不同负荷类型下的所有运行情况。它也提供了一个可替换的界面用来定制数据显示，测试同步及测试的创建和执行。

3. [Grinder](http://grinder.sourceforge.net/)

Grinder是一个开源的JVM负载测试框架，它通过很多负载注射器来为分布式测试提供了便利。 支持用于执行测试脚本的Jython脚本引擎HTTP测试可通过HTTP代理进行管理。根据项目网站的说法，Grinder的 主要目标用户是“理解他们所测代码的人——Grinder不仅仅是带有一组相关响应时间的‘黑盒’测试。由于测试过程可以进行编码——而不是简单地脚本 化，所以程序员能测试应用中内部的各个层次，而不仅仅是通过用户界面测试响应时间。


3. [Web Capacity Analysis Tool (WCAT)](https://www.iis.net/downloads/community/2007/05/wcat-63-x86)

这是一种轻量级负载生成实用工具，不仅能够重现对 Web 服务器（或负载平衡服务器场）的脚本 HTTP 请求，同时还可以收集性能统计数据供日后分析之用。WCAT 是多线程应用程序，并且支持从单个源控制多个负载测试客户端，因此您可以模拟数千个并发用户。该实用工具利用您的旧机器作为测试客户端，其中每个测试客户端又可以产生多个虚拟客户端（最大数量取决于客户端机器的网络适配器和其他硬件）。您可以选择使用 HTTP 1.0 还是 HTTP 1.1 请求，以及是否使用 SSL。并且，如果测试方案需要，您还可以使用脚本执行的基本或 NTLM 身份验证来访问站点的受限部分。（如果您的站点使用 cookie、表单或基于会话的身份验证，那您可以创建正确的 GET 或 POST 请求来对测试用户进行身份验证。）WCAT 还可管理您站点可能设置的任何 cookie，所以配置文件和会话信息将永久保存。

3. [fwptt](http://fwptt.sourceforge.net/index.html)

一个用来进行WEB应用负载测试的工具。它可以记录一般的请求，也可以记录Ajax请求。它可以用来测试 asp.net， jsp， php 或是其它的Web应用。

3. [http_load](http://www.acme.com/software/http_load/)

http_load 以并行复用的方式运行，用以测试web服务器的吞吐量与负载。但是它不同于大多数压力测试工具，它可以以一个单一的进程运行，一般不会把客户机搞死。可以可以测试HTTPS类的网站请求。

3. []()



3. []()
3. []()
3. []()

* 压力测试

3. [Load UI](https://www.soapui.org/professional/loadui-pro.html)

Load UI是一款开源的压力测试工具，它可以与soapUI紧密集成，高效执行各种功能/性能测试。它也是一款非常灵活且交互性很强的负载测试工具。在测试期间，它还允许创建、配置和更新测试。与此同时，它还使用高度图形化接口，使得测试变得很简单而且运行迅速。

3. [Siege](https://siege.org/)

Siege是一个开源的压力测试和评测工具，开发者可以用它测试高负荷加载下应用程序代码，也可以根据配置对一个Web站点进行多用户的并发访问，记录每个用户所有请求过程的相应时间，并在一定数量的并发访问下重复进行。

3. [JCrawler](http://jcrawler.sourceforge.net/)

一个开源( CPL) 的WEB应用压力测试工具。通过其名字，你就可以知道这是一个用Java写的像网页爬虫一样的工具。只要你给其几个URL，它就可以开始爬过去了，它用一种特殊的方式来产生你WEB应用的负载。这个工具可以用来测试搜索引擎对你站点产生的负载。当然，其还有另一功能，你可以建立你的网站地图和再点击一下，将自动提交Sitemap给前5名的搜索引擎！


3. []()
3. []()

* 稳定性测试
<!-- todo -->
看这个文章 [淘宝团队是如何进行稳定性测试的？](https://testerhome.com/topics/12475)

3. []()
3. []()
3. []()
3. []()
3. []()


---

觉得文章不错就扫码支持一下呗～

![打赏二维码](https://june111.github.io/assets/img/post/pay-qr.jpg)



参考链接
1. [五款资深高效的开源Web性能测试工具](https://blog.csdn.net/u012572955/article/details/52238811)
2. [十个免费的WEB压力测试工具](https://coolshell.cn/articles/2589.html)
3. [淘宝团队是如何进行稳定性测试的？](https://testerhome.com/topics/12475)


