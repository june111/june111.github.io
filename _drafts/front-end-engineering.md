---
layout: post
title: '前端工程化'
subtitle:'一切都是为了提高生产率'
date: 2018-11-08
author: June
cover: 'https://june111.github.io/blog/assets/img/post/2018-11-08/front-end-engineering.png'
tags: 前端
---

# 前端工程化

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-08/structure.svg">
![文章结构]({{site.baseurl}}/assets/img/post/2018-11-08/structure.svg)
</a>

## 为什么要前端工程化

提高编码、测试、维护阶段的生产效率。实现高效开发，有效协同，质量可控。

## 如何进行前端工程化

工程化，即系统化、模块化、规范化的一个过程。前端工程化就是根据具体的业务特点，将前端的开发流程、技术、工具、经验等规范化、标准化就是前端工程化。它的目的是让前端开发能够“自成体系”，最大程度地提高前端工程师的开发效率，降低技术选型、前后端联调等带来的协调沟通成本。下面我们来从模块化、组件化、规范化、自动化，来了解如何进行前端工程化。

### 模块化

在语言层面上，对代码的拆分

简单来说，模块化就是将一个大文件拆分成相互依赖的小文件，再进行统一的拼装和加载。只有这样，才有多人协作的可能。

#### JS 模块化

现在ES6已经在语言层面上规定了模块系统，完全可以取代现有的CommonJS和AMD规范，而且使用起来相当简洁，并且有静态加载的特性。

* 用 Webpack+Babel 将所有模块打包成一个文件同步加载，也可以打成多个chunk异步加载；

* 用 SystemJS+Babel 主要是分模块异步加载；

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

Webpack将样式文件和图片等静态资源视为模块进行打包。配合loader加载器，对资源进行处理。


###  组件化

将你所能看见到的视图(UI)进行合理拆分得到的单元，并能让它达到可复用程度，可称之为组件。

组件化是基于模块化的，因为组件的单位可以有模板，样式加逻辑。

遵循结构、表现和行为分离的原则，

三分天下的JS框架: React、Vue、Angular

UI框架：

将数据层分离管理: redux、mbox

###  规范化

为了更好的落实开发，可以制定一些规范

#### 编码规范

* js使用eslint，目前采用 google 的 javascript style guide
* css使用相应的stylelint
* 使用editorconfig，统一编辑器或ide的一些设定，如js缩进为2空格

其中编码规范最好采取ESLint和StyleLint等强制措施，配置git hooks可以实现Lint不过不能提交代码等机制，因为人是靠不住的。

#### 接口规范

采用 restful 风格，接口描述使用swagger

对于某些接口返回状态码还是中文结果，前端应尽量不让去判断状态，只作显示

#### 开发流程规范

使用敏捷，增强开发进度管理和控制
应对各项风险，需求变更等
code review 机制
UAT 提升发布的需求的质量

#### 版本控制

node module 遵循unix的思想–do one thing and do it well，也因此单个上层的模块会依赖很多下层的模块，这可能会导致其中一个下层的模块改变，导致整个上层模块崩溃。

package.json 里的包版本号应写死，除非因某个包有了新需求特性，再去更新


#### Git

* 使用 Git 版本控制工具

* 规范化 Git 工作流

成熟的 Git 分支开发流程

Git分支管理

创建 merge request，code review 完毕之后方可合并代码

* 规范化 Git Commit message

使用的 Angular 提交规范，比较合理和系统化，并且有现成配套的工具(commitizen)。不规范就不允许提交





#### 目录结构

架构	

文件名一律小写
采用就近原则

#### 协作工具

这里指的是协作工具的采用

任务分配，trello/gitlab todo
代码仓库，gitlab
文档，gitlab wiki/trello
产品设计，sketch画图，inDesign写文档

#### 性能优化

#### 其他

* 开发环境。 推荐 unix，与部署环境统一，且前端许多工具对unix系友好
* codereview
* [中文技术文档的写作规范](https://github.com/ruanyf/document-style-guide)

###  自动化

#### 环境控制

使用docker自动化部署，集群使用 kubernetes(k8s)

#### 构建工具

浏览器自动刷新，热加载
编译中间语言，如 es6/7，sass
js、css的压缩及混肴
压缩图片，一定大小内使用base64
根据文件内容生成哈希值，实现缓存控制
实现按需加载，见模块化部分
umd 打包

图标合并
不要再用PS拼雪碧图了，统一走Webpack吧；
不要再用Icomoon了，统一走Webpack吧。

使用前端构建工具
gulp、grunt、Broccoli

javascript 编译工具
Babel、Browserify、Webpack

使用CI集成工具
jenkins、Travis CI

使用脚手架工具
yeoman、create-app

工具层面
预编译，包括es6/7语法转译、css预编译器处理、spirit图片生成；
依赖打包；
资源嵌入；
文件压缩；
hash指纹；
代码审查；
模板构建。

平台层面
文件监听，动态编译；
mock server。livereload



#### 持续化集成

gitlab/git hook 实现 hook
jenkin/gitlab ci执行相应的构建脚本，并订阅构建结果
将构建结果打包，交给运维部署

#### 项目徽章

无论是开源项目还是私有项目都可以使用徽章查看状态

travis/circle，持续集成
codacy，代码审查
npm，提供版本号，下载量等
开源许可，一般采用 mit
codecov，代码覆盖率检测
saucellabs，跨浏览器集成测试

#### 测试

采用tdd的编程思想，引入单元测试
karma + mocha + chai、jest、ava

使用各种调试工具
web devtools、finddle

本地开发阶段进行自动化测试

通过工具，将本地复杂的测试准备工作自动化，以便于在本地进行自动化测试。

线上部署阶段进行自动化测试

线上部署阶段，很容易进行自动化测试的中心化管理，如果有项目没有写测试用例，中心化平台可以做各种操作，如暂停部署等。

本地开发和线上部署两个阶段的自动化测试，需要有机结合起来，保证测试环境的一致性。

#### 监控

* 错误与性能监控

对页面错误和性能的监控是必要的，随着团队规模的不同，监控系统接入的难度不同。

其中，效率最低、准确性最差的是手动添加监控代码。这种我们放弃。

自动添加监控代码包括：

错误、性能监控脚本能够自动化添加到线上页面
错误、性能监控能够自动化获取
监控代码部署后，就通过各种手段展现、通知责任人，查看优化前后效果对比等。

性能监控系统需要的功能

数据可视化
可以查看：全网/业务/页面 的数据表现
可以查询任意时间段的数据
可以查看表现变化情况（趋势）
秒开率计算算法符合逻辑
展示首屏网络传输各个时刻的状态（转场、查询缓存、dns 解析、建立 tcp 连接等）
找出瓶颈页面
20%、80% 的页面处于哪个时间区间
找到处于某个时间区间的有哪些页面，以及各种网络信息
消息通知
线上性能表现差时，通过消息通知责任人优化，精确到页面
工具推荐：

自动获取前端首屏时间：https://github.com/hoperyy/auto-compute-first-screen-time

* 前端安全监控





## 实践前端工程化

### 技术选型

基于以上工程化流程，技术选型如下：

基础库 vue
node中间层 koa
css预处理 sass
日志收集 sentry
前端测试框架 jasmine
构建工具 webpack/rollup
调试工具 chrome/ide/vue-dev-tools
后台进程管理 pm2
包管理工具 npm/yarn
前后端通信 json-rpc/swagger/graphql(查询)

### 项目配置

css


















---

觉得文章不错就扫码支持一下呗～

![打赏二维码](https://june111.github.io/blog/assets/img/post/pay-qr.jpg)

## 参考链接

* [谁能介绍下web前端工程化？ 赵雨森的回答](https://link.juejin.im/?target=https%3A%2F%2Fwww.zhihu.com%2Fquestion%2F24558375)
* [前端项目架构小结](https://juejin.im/entry/58febab1b123db6e95a978c6)
* [前端工程化概述](https://juejin.im/post/5ac9c6f451882555677ed301)
* [前端工程化实践：大前端的转变之路](https://zhuanlan.zhihu.com/p/28769103)
* [前端工程化简介 #114](https://github.com/hoperyy/blog/issues/114)
* [前端工程化开发方案app-proto]https://tech.meituan.com/tech_salon_13_app_proto.html)
* []()
* []()
* []()
* []()
* []()
* []()
* []()