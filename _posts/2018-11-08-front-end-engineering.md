---
layout: post
title: '前端工程化'
subtitle: '一切都是为了提高生产率，前端工程化内容总结'
date: 2018-11-08
author: June
cover: 'https://june111.github.io/assets/img/post/2018-11-08/front-end-engineering.png'
tags: 前端
---

# 前端工程化

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-08/structure.svg">
![文章结构]({{site.baseurl}}/assets/img/post/2018-11-08/structure.svg)
</a>

## 为什么要前端工程化

提高编码、测试、维护阶段的生产效率。实现高效开发，有效协同，质量可控。

## 如何进行前端工程化

工程化，即系统化、模块化、规范化的一个过程。

前端工程化就是根据具体的业务特点，将前端的开发流程、技术、工具、经验等规范化、标准化就是前端工程化。它的目的是让前端开发能够“自成体系”，最大程度地提高前端工程师的开发效率，降低技术选型、前后端联调等带来的协调沟通成本。

下面我们来从模块化、组件化、规范化、自动化，来了解如何进行前端工程化。

### 模块化

简单来说，模块化就是将一个大文件拆分成相互依赖的小文件，再进行统一的拼装和加载。只有这样，才有多人协作的可能。

#### JS 模块化

现在ES6已经在语言层面上规定了模块系统，完全可以取代现有的CommonJS和AMD规范，而且使用起来相当简洁，并且有静态加载的特性。

* 用 Webpack+Babel 将所有模块打包成一个文件同步加载，也可以打成多个chunk异步加载

* 用 SystemJS+Babel 主要是分模块异步加载

#### CSS 模块化

* 文件拆分：

	less、sass、stylus、postCSS等预处理器

* 选择器的全局污染问题：

	CSS命名风格：BEM风格；Bootstrap风格；Semantic UI风格；NEC风格等。

* 模块化工具

	从工具层面，社区又创造出Shadow DOM、CSS in JS和CSS Modules三种解决方案。
	* Shadow DOM是WebComponents的标准。它能解决全局污染问题，但目前很多浏览器不兼容，对我们来说还很久远；
	* CSS in JS是彻底抛弃CSS，使用JS或JSON来写样式。这种方法很激进，不能利用现有的CSS技术，而且处理伪类等问题比较困难；
	* CSS Modules仍然使用CSS，只是让JS来管理依赖。它能够最大化地结合CSS生态和JS模块化能力，目前来看是最好的解决方案。Vue的scoped style也算是一种。


#### 资源模块化

Webpack的强大之处不仅仅在于它统一了JS的各种模块系统，取代了Browserify、RequireJS、SeaJS的工作。更重要的是它的万能模块加载理念，即所有的资源都可以且也应该模块化。

Webpack可以将样式文件和图片等静态资源视为模块进行打包。配合loader加载器，对资源进行处理。


###  组件化

组件化是基于模块化的，因为组件的单位可以有模板，样式加逻辑。

将你所能看见到的视图(UI)进行合理拆分得到的单元，并能让它达到可复用程度，可称之为组件。

遵循结构、表现和行为分离的原则，我把组件分为JS框架和UI框架。

#### JS框架

三分天下的Vue(118359)、React(114932)、Angular(59241)。（ps：数字为 Github Star 的数量）

#### UI框架

UI框架有很多，下面统计了21个常见的UI框架，其中Semantic Ui，Ant design，Element，iView，Vuetify，Vux，Framework 7 ，Mint UI 的Github Star过了10k。

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-08/ui-star.png">
![UI框架的Github Star]({{site.baseurl}}/assets/img/post/2018-11-08/ui-star.png)
</a>

###  规范化

为了更好的落实开发，我们要制定一些规范。

#### 编码规范

* JS使用ESLint
* CSS使用相应的Stylelint
* 使用Editorconfig，统一编辑器或ide的一些设定，如js缩进为2空格

其中编码规范最好采取ESLint和StyleLint等强制措施，配置git hooks可以实现Lint不过不能提交代码等机制，因为人是靠不住的。

#### 接口规范

接口规范包括协议规范，域名规范，版本控制规范，API路径规范，API命名规范，请求参数规范，列表请求特殊规范，返回数据规范，接口文档规范，接口管理工具。

#### 开发流程规范

项目的生命周期分为启动、实施、收尾三个过程。照产品开发流程，我把项目开发分为5个阶段。

项目启动阶段 => 需求阶段 => 设计阶段 => 开发阶段 => 测试阶段 => 上线

#### 版本控制

* 第三方库

	node module 遵循unix的思想–Do one thing and do it well，也因此单个上层的模块会依赖很多下层的模块，这可能会导致其中一个下层的模块改变，导致整个上层模块崩溃。所以package.json 里的包版本号应写死，除非因某个包有了新需求特性，再去更新。

* Git

	* 使用 Git 版本控制工具

	* 规范化 Git 工作流

	* [规范化 Git Commit message](https://june111.github.io/2018/11/06/use-commitizen.html)

		使用的 Angular 提交规范，比较合理和系统化，并且有现成配套的工具(commitizen)。不规范就不允许提交

#### 目录结构

层次清晰的目录结构，就是为了达到以下两点:

* 可读性高: 不熟悉这个项目的代码的人，一眼就能看懂目录结构，知道程序启动脚本是哪个，测试目录在哪儿，配置文件在哪儿等等。从而非常快速的了解这个项目。

* 可维护性高: 定义好组织规则后，维护者就能很明确地知道，新增的哪个文件和代码应该放在什么目录之下。这个好处是，随着时间的推移，代码/配置的规模增加，项目结构不会混乱，仍然能够组织良好。

#### 协作工具

常用的协作工具：

* 项目管理：[Trello](https://trello.com)，[@team](https://www.atteam.cn/)，[Tower](https://tower.im)，[Worktile](https://worktile.com)，[Teambition](https://www.teambition.com/)，[Asana](https://asana.com/)
* 代码仓库：[GitHub](https://github.com/)，[Gitlab](https://gitlab.com/)，[Bitbucket](https://bitbucket.org)
* 文件协作：[Google Docs](docs.google.com)，[Quip](https://quip.com/)，[Dropbox](https://www.dropbox.com/)，[石墨文档](https://shimo.im)
* 内部沟通：[Slack](www.slack.com/)，[瀑布IM](https://beta.pubu.im/)，[企业微信](https://work.weixin.qq.com/)
* 产品设计：[Mockplus](https://www.mockplus.cn/)，[Axure RP](https://www.axure.com.cn/)，[墨刀](https://modao.cc/)，[Sketch](https://www.sketchapp.com/)，[蓝湖](https://lanhuapp.com/)

#### 性能优化

性能优化的常见指标：

* 响应时间
* 吞吐量
* 并发数
* Apdex指数

###  自动化

自动化可以大大提高我们的开发效率，从重复的工作中解放出来。

#### 构建工具

构建工具的主要功能就是实现自动化处理，例如对代码进行检查、预编译、合并、压缩；生成雪碧图、sourceMap、版本管理；运行单元测试、监控等，当然有的工具还提供模块化、组件化的开发流程功能。

网上各类的构建工具非常多，有家喻户晓的 Grunt、Gulp、Webpack，也有各大公司团队开源的构建工具，这里通过 Github 的 Star 数量来简单的对比下各个工具的流行度(数据时间为2018-11-08)：

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-08/star.png">
![构建工具的 Star]({{site.baseurl}}/assets/img/post/2018-11-08/star.png)
</a>

如果把工具按类型分可以分为这三类：

* 基于任务运行的工具：  
	Grunt、Gulp
	它们会自动执行指定的任务，就像流水线，把资源放上去然后通过不同插件进行加工，它们包含活跃的社区，丰富的插件，能方便的打造各种工作流。
  
* 基于模块化打包的工具：  
	Browserify、Webpack、rollup.js
	有过 Node.js 开发经历的应该对模块很熟悉，需要引用组件直接一个 require 就 OK，这类工具就是这个模式，还可以实现按需加载、异步加载模块。

* 整合型工具：  
	Yeoman、FIS3、jdf、cooking、weflow
	使用了多种技术栈实现的脚手架工具，好处是即开即用，缺点就是它们约束了技术选型，并且学习成本相对较高。

#### 测试系统

自动化测试是是一个塔型体系。静态检查是必须的，作为团队规范存在，覆盖全部代码。UT是局部覆盖的，关注基础功能。E2E是可选的，关注主流程和回归测试。

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-08/test-sys.png">
![自动化测试体系]({{site.baseurl}}/assets/img/post/2018-11-08/test-sys.png)
</a>

静态检查 - Eslint  
Unit Test (单元测试) - [Karma](https://karma-runner.github.io/3.0/index.html)、 [Jasmine](https://jasmine.github.io/)、 [Mocha](https://mochajs.org/)、 [Chai](https://www.chaijs.com/)、 [Jest](https://jestjs.io/)、 [AVA](https://github.com/avajs/ava)  
End to End Test (端到端测试) - [Protractor](https://www.protractortest.org/#/)、 [Nightwatch](http://nightwatchjs.org/)(Angular)、 [Selenium](https://github.com/SeleniumHQ/selenium)(browser)


#### 监控系统

前端的监控系统要解决的问题是如何从用户的角度判断系统的可用性。只有用户端的可用才是真正的可用。

如果监控没有覆盖到终端，那么很可能会造成严重的幸存偏误。比如某个接口从后端的角度来看成功率接近百分之百，但事实上多数用户的请求都失败了，因为请求没有正确发到后端。

监控系统的功能分类：

* 性能监控 - 页面访问成功率，接口成功率
* 前端安全监控 - 跨站脚本攻击(XSS)，跨站点请求伪造(CSRF)，点击劫持(ClickJacking)三大前端安全问题的监控
* 错误监控 - 收集并汇总应用系统抛出的错误信息
* 业务指标监控 - 全网/业务/页面的数据表现，事件触发量

对页面错误和性能的监控是必要的，随着团队规模的不同，监控系统接入的难度不同。

其中，效率最低、准确性最差的是手动添加监控代码。这种我们放弃。

自动添加监控代码包括：

错误、性能监控脚本能够自动化添加到线上页面
错误、性能监控能够自动化获取
监控代码部署后，就通过各种手段展现、通知责任人，查看优化前后效果对比等。


#### 统计系统

统计系统和监控系统的区别在于，监控关注的是实时数据，统计关注的是全量数据，监控是为了提高团队的故障响应能力，统计是为产品与业务分析提供基础。

统计系统的功能分类：

性能统计  
访问量统计  
用户行为统计  


#### 持续集成

* 什么是持续集成

	持续集成（Continuous integration，简称CI）指的是，频繁地（一天多次）将代码集成到主干。目的是让产品可以快速迭代，同时还能保持高质量。它的核心措施是，代码集成到主干之前，必须通过自动化测试。只要有一个测试用例失败，就不能集成。

	与持续集成相关的，还有两个概念，分别是持续交付和持续部署。

	持续交付（Continuous delivery）指的是，频繁地将软件的新版本，交付给质量团队或者用户，以供评审。如果评审通过，代码就进入生产阶段。

	持续交付可以看作持续集成的下一步。它强调的是，不管怎么更新，软件是随时随地可以交付的。

	持续部署（continuous deployment）是持续交付的下一步，指的是代码通过评审以后，自动部署到生产环境。

	持续部署的目标是，代码在任何时刻都是可部署的，可以进入生产阶段。

	持续部署的前提是能自动化完成测试、构建、部署等步骤。

* 流程

	提交 => 测试（第一轮，单元测试） => 构建 => 测试（第二轮，单元测试和集成测试都会跑） => 部署 

	发生问题 => 回滚

* CI 工具

	常见的持续集成工具：

	* [Jenkins](https://jenkins.io/) 是一个用Java编写的开源的持续集成工具，提供了软件开发的持续集成服务，可监控并触发持续重复的工作，具有开源，支持多平台和插件扩展，安装简单，界面化管理等特点。  
	* [Docker](https://www.docker.com/) docker通过内核虚拟化技术（namespace及cgroups等）来提供容器的资源隔离与安全保障等，由于docker通过操作系统层的虚拟化实现隔离，所以docker容器在运行时，不需要类似虚拟机额外的操作系统开销，提供资源利用率。
	* [kubernetes(k8s)](https://kubernetes.io/)   是一个自动化部署、伸缩和操作应用程序容器的开源平台。
	* [Travis CI](https://travis-ci.org/)   在软件开发领域中的一个在线的，分布式的持续集成服务，用来构建及测试在GitHub托管的代码。
	* [Circle CI](https://circleci.com/) 是一个强大的持续集成与部署服务, 支持 Ruby, Python, Node.js, Java, and PHP 等语言。  
	* [Codeship](https://codeship.com/) 是一个本地的持续集成解决方案。它有两种不同的版本：基本版和专业版。在基本版中提供了安装即用的持续集成服务但是不能够支持Docker，它的主要用途就是通过UI来进行应用的构建等操作。专业版本提供了更灵活的功能以及Docker支持。  
	* [Strider CD](http://strider-cd.github.io/) 是一个开源的持续集成和部署平台，使用Javascript Node.js和MongoDB架构，BSD许可证，概念上类似Travis 和 Jenkins，Strider是易设置使用和定制的。  


## 实践前端工程化

接下来就要上点私货了。

### 技术选型

技术选型原则：

* 匹配业务场景，快速实现核心业务。尽量不重复造轮子。
* 尽可能少的引入和业务原型实现无关的技术。
* 拥有强大社区支撑的开源技术。遇到问题时可以搜索，提问，看源码。
* 团队最擅长和可以驾驭的。

基于技术选型的原则，我的技术选型如下：

* 编程语言：ES6
* JS工具库：Echarts
* 前端 MVC 框架：Vue (上手难度低，社区活跃)
* UI 框架：Element (组件比较全，适合项目的需求)
* node中间层：koa2（Express 原班人马基于 ES7 新特性重新开发的框架）
* 模块化，打包，自动化构建：Webpack ()
* 包管理工具：npm/yarn ()
* 后台进程管理 pm2 ()
* 测试工具：Karma + Mocha + chai (Karma，Mocha 社区成熟，配置灵活；chai )
* 前端监控：Sentry (有开发者免费模式，异常信息符合需要)
* 持续集成：Docker + Travis-CI + Codecov ()
* 接口管理：Swagger (UI界面漂亮，支持在线测试)


### 项目配置

TODO

<!-- 

	https://juejin.im/entry/58febab1b123db6e95a978c6
* 模块化

	Webpack+Babel
	css预处理 sass
	BEM风格
	CSS Modules Vue的scoped style

* 规范化

流程规范
目录结构
编码规范

JavaScript Standard Style Guide，stylelint
		
接口规范
性能优化
版本控制

* 自动化

前端安全监控
统计系统
 -->




---

写文不容易，且看且珍惜。觉得文章不错就扫码支持一下呗～

![打赏二维码](https://june111.github.io/assets/img/post/pay-qr.jpg)

## 参考链接

* [谁能介绍下web前端工程化？ 赵雨森的回答](https://link.juejin.im/?target=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F24558375)
* [前端项目架构小结](https://juejin.im/entry/58febab1b123db6e95a978c6)
* [前端工程化概述](https://juejin.im/post/5ac9c6f451882555677ed301)
* [前端工程化实践：大前端的转变之路](https://zhuanlan.zhihu.com/p/28769103)
* [前端工程化简介 #114](https://github.com/hoperyy/blog/issues/114)
* [前端工程化开发方案app-proto](https://tech.meituan.com/tech_salon_13_app_proto.html)
* [21 Top Vue.js UI Libraries For Your App](https://hackernoon.com/21-top-vue-js-ui-libraries-for-your-app-4556e5a9060e)
* [前端工程化——构建工具选型](https://www.jianshu.com/p/3e8941eda2dd)
* [前端技术体系大局观](https://zhuanlan.zhihu.com/p/23185351)
* [持续集成是什么？](http://www.ruanyifeng.com/blog/2015/09/continuous-integration.html)
* [九款优秀的企业项目协作工具推荐](https://zhuanlan.zhihu.com/p/28941055)
* [效率为王！11款最高效的团队协作工具](http://www.woshipm.com/pmd/190054.html)
* [技术选型的艺术](https://juejin.im/entry/5ae9ce7751882567113b04ef)
* [创业公司或新项目如何做技术选型
](https://segmentfault.com/a/1190000011810796)
* []()
* []()
* []()
* []()