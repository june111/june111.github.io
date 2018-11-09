---
layout: post
title: '前端构建工具'
date: 2018-11-09
author: June
cover: /assets/img/post/2018-11-09/front-end-build-tool.png
tags: 前端
---

# 前端构建工具分析

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-09/structure.svg">
![文章结构]({{site.baseurl}}/assets/img/post/2018-11-09/structure.svg)
</a>

## 为什么要使用构建工具

提高开发效率，用代码代替重复的劳动。

## 构建工具对比分析

构建就是把源代码转换成发布到线上的可执行 JavaScrip、CSS、HTML 代码，包括如下内容。

代码转换：TypeScript 编译成 JavaScript、SCSS 编译成 CSS 等。
文件优化：压缩 JavaScript、CSS、HTML 代码，压缩合并图片等。
代码分割：提取多个页面的公共代码、提取首屏不需要执行部分的代码让其异步加载。
模块合并：在采用模块化的项目里会有很多个模块和文件，需要构建功能把模块分类合并成一个文件。
自动刷新：监听本地源代码的变化，自动重新构建、刷新浏览器。
代码校验：在代码被提交到仓库前需要校验代码是否符合规范，以及单元测试是否通过。
自动发布：更新完代码后，自动构建出线上发布代码并传输给发布系统。
构建其实是工程化、自动化思想在前端开发中的体现，把一系列流程用代码去实现，让代码自动化地执行这一系列复杂的流程。 构建给前端开发注入了更大的活力，解放了我们的生产力。

历史上先后出现一系列构建工具，它们各有其优缺点。由于前端工程师很熟悉 JavaScript ，Node.js 又可以胜任所有构建需求，所以大多数构建工具都是用 Node.js 开发的。

我按功能把这些工具分为四类，分别是安装，任务运行，模块化，集成解决方案。

### 安装

* NPM

	* 简介    
		[NPM](https://www.npmjs.com/)  即：npm package manager ，是一种重用其他开发人员的代码的方法，也是一种与他人共享代码的方式，并且可以很容易地管理不同版本的代码。是目前JS最流行的包管理工具,也是Node.js能够如此成功的主要原因之一。通过 npm 可以安装、共享、分发代码,管理项目依赖关系。

	* 优点
		* 社区成熟
		* 透过冗馀安装来解决套件相依性问题。如果要安装套件 A 和套件 B，而两者都相依于套件 C，则 npm 会在套件 A 和套件 B 的 node_modules 资料夹内同时安装套件 C。换句话说，套件 C 被安装了两次。这种设计的好处是不会有相依性问题。

	* 缺点
		* 同样的套件会被安装多次，当有需要编译的套件被冗馀安装多次时，更新会变得很缓慢，幸好绝大多数的套件都不需要编译。
		* 权限问题。安装、移除和更新套件的时候，可能会需要 root 权限。可以透过 sudo 执行 npm 指令，或者是切换使用者到 root。

* Yarn

	* 简介    
		[yarn](https://www.yarnpkg.com/en/) 是facebook发布的新一代包管理工具，旨在解决以往使用 npm 作为包管理会遇到的一些问题。

	* 优点

		* 并行安装速度快 
		* 安装版本统一
		* 更好的语义化

	* 缺点
		* 对于私有 npm 包的支持有限

* Bower

	* 简介  
		[Bower](https://bower.io/)  是 twitter 推出的一款包管理工具，基于nodejs的模块化思想，把功能分散到各个模块中，让模块和模块之间存在联系，通过 Bower 来管理模块间的这种联系。 为模块的安装、升级和删除，提供一种统一的、可维护的管理模式。

	* 优点
		* 展现客户端的依赖关系
		* 让升级变得简单。假设某个库的新版本发布了一个重要的安全修补程序，为了安装新版本，你只需要运行一个命令，bower会自动更新所有有关新版本的依赖关系。

	* 缺点
		* 未注册的软件包往往包含冗余的非生产环境的代码，有时甚至需要手动构建。

### 任务运行

* Npm Script

	* 简介  
		[Npm Script](https://docs.npmjs.com/misc/scripts) 是一个任务执行者。Npm 是在安装 Node.js 时附带的包管理器，Npm Script 则是 Npm 内置的一个功能，允许在 package.json 文件里面使用 scripts 字段定义任务。

	* 优点
		* 内置，无须安装其他依赖

	* 缺点
		* 功能太简单，虽然提供了 pre 和 post 两个钩子，但不能方便地管理多个任务之间的依赖。

* Grunt

	* 简介  
		[Grunt](https://gruntjs.com/)老牌的构建工具。现在已基本不用了，简单说一下。Grunt 和 Npm Scripts 类似，也是一个任务执行者。Grunt 有大量现成的插件封装了常见任务，也能管理任务之间的依赖关系，自动化地执行依赖任务，每个任务的具体执行代码和依赖关系写在配置文件 gruntfile.js 里。

	* 优点
		* 配置驱动
		* 灵活，它只负责执行我们定义好的任务
		* 大量可复用插件封装好了常见的构建任务

	* 缺点
		* 也是配置驱动，当任务非常多的情况下，试图用配置完成所有事简直就是个灾难；再就是它的 I/O 操作也是个弊病，它的每一次任务都需要从磁盘中读取文件，处理完后再写入到磁盘。当资源文件较多，任务较复杂的时候性能就是个问题了。
		* 集成度不高，要写很多配置后才可以用，无法做到开箱即用。

* Gulp

	* 简介  
		[Gulp](https://www.gulpjs.com.cn/) 是一个基于流的自动化构建工具。除了可以管理任务和执行任务，还支持监听文件、读写文件。引入了流（Stream）的概念，同时提供了一系列常用插件去处理流，流可以在插件之间传递。也就是说一次 I/O 可以处理多个任务。

	* 优点
		* 代码驱动
		* 好用又不失灵活，既可以单独完成构建，也可以和其他工具搭配使用。

	* 缺点
		* 和Grunt 类似。集成度不高，要写很多配置后才可以用，无法做到开箱即用。

	可以将Gulp 看做是 Grunt 的加强版。相对于 Grunt ，Gulp 增加了文件监听、读写文件、流式处理的功能。

### 模块化

* Webpack

	* 简介  
		[Webpack](https://webpack.js.org/) 目前最热门的前端资源模块化管理和打包工具。

	* 优点
		* 把一切都视为模块：不管是 CSS、JS、Image 还是 HTML 都可以互相引用，通过定义 entry.js，对所有依赖的文件进行跟踪，将各个模块通过 loader 和 plugins 处理，然后打包在一起。
		* 按需加载：打包过程中 Webpack 通过 Code Splitting 功能将文件分为多个 chunks，还可以将重复的部分单独提取出来作为 commonChunk，从而实现按需加载。
		* 专注于处理模块化的项目，能做到开箱即用、一步到位
		* 可通过 Plugin 扩展，完整好用又不失灵活性
		* 使用场景不局限于Web开发
		* 社区庞大活跃，经常引入紧跟时代发展的新特性，能为大多数场景找到已有的开源扩展
		* 良好的开发体验


	* 缺点
		* 上手比较难：官方文档混乱、配置复杂、难以调试（Webpack2 已经好了很多）对于新手而言需要经历踩坑的过程；
		* 对于 Server 端渲染的多页应用有点力不从心：Webpack 的最初设计就是针对 SPA，所以在处理 Server 端渲染的多页应用时，不管你如何 chunk，总不能真正达到按需加载的地步，往往要去考虑如何提取公共文件才能达到最优状态。
		* 只能用于采用模块化开发的项目。

	适合配合 React.js、Vue.js 构建单页面应用以及需要多人合作的大型项目，在规范流程都已约定好的情况下往往能极大的提升开发效率与开发体验。

* Browserify

	* 简介  
		[Browserify](http://browserify.org/) 是一个供浏览器环境使用的模块打包工具，像在node环境一样，也是通过require('modules')来组织模块之间的引用和依赖，既可以引用npm中的模块，也可以引用自己写的模块，然后打包成js文件，再在页面中通过`<script>`标签加载。

	* 优点
		* 可以使开发前端组件就像开发node后端一样—-使用require引入依赖（无缝使用了node模块系统的优点）
		* 所有浏览器本身都支持这种方法，并且不需要服务器端工具。

	* 缺点
		* 没有开箱即用的方法

* Rollup

	* 简介  
		[Rollup](https://www.rollupjs.com/guide/zh) 一个和 Webpack 很类似但专注于ES6的模块打包工具。由于 Rollup 的使用方法和 Webpakc 差不多，所以这里就不详细介绍如何使用 Rollup 了，而是详细说明他们的差别：

		* Rollup 是在Webpack 流行后出现的替代品；
		* Rollup 生态链不完善，体验还不如Webpack；
		* Rollup 的功能不如 Webpack 完善，但其配置和使用更简单；

	* 优点
		* 能对es6的源码进行Tree Shaking(简单介绍剔除无效代码，稍微详细点就是可以去除已经被定义却没被使用的代码并进行Scope Hoisting(作用域提升)，以减小输出文件的大小和提升运行性能。)然而 Rollup 的这些亮点随后就被 Webpack 模仿和实现了。
		* Rollup 在用于打包JavaScript库时比 Webpack 更有优势，因为其打包出来的代码更小、更快。

	* 缺点
		* 插件库比较少，社区不够活跃
		* 功能不够完善，在很多场景下都找不到现成的解决方案。

* Cooking

	* 简介  
		[cooking](http://elemefe.github.io/cooking/) 是饿了么前端团队开发的，目标是将你从繁琐的构建配置中解放出来，同时还省去每个项目都要安装一堆开发依赖的麻烦。基于 webapck 但更友好的配置项、易用的扩展配置机制，让你专注项目忘掉配置。

	* 优点
		* 配置简单

	* 缺点
		* 不够灵活

### 集成解决方案

* Yeoman

	* 简介  
		[Yeoman](http://yeoman.io/) 是Google的团队和外部贡献者团队合作开发的，他的目标是通过Grunt（一个用于开发任务自动化的命令行工具）和Bower（一个HTML、CSS、Javascript和图片等前端资源的包管理器）的包装为开发者创建一个易用的工作流。

	* 优点
		* 很适合Angularjs (1.x) 的项目
		* 官方教程很棒很易懂
		* 用户社区大，所以相关教学和模块很丰富
		* 你能想到的主流工具基本都集成了
		* 搭建自定义度不错，SASS/LESS， Gulp/Grunt都支持

	* 缺点
		* 缺少中文文档
		* 依赖会自动使用谷歌的cdn

* FIS3

	* 简介  
		[FIS3](http://fis.baidu.com/) 是一个来自百度的构建工具。相对于 Grunt、Gulp 这些只提供了基本功能的工具。Fis3集成了开发者常用的构建功能。

	* 优点
		* 集成了各种Web开发所需的构建功能，配置简单，开箱即用。

	* 缺点
		* 目前官方已经不再更新和维护，不支持最新版本的Node。

	FIS3是一种专注于Web开发的完整解决方案，如果将Grunt、Gulp比作汽车的发动机，那么FIS3则就是一辆完整的汽车。

* Weflow

	[weflow](https://weflow.io/) 是腾讯的一个前端开发工作流GUI工具。

* JDF

	[JDF](https://github.com/putaoshu/jdf) 是京东前端开发集成解决方案(Jingdong front-end integrated solution) 目的是合理、快速和高效的解决前端开发中的工程和项目问题

## 搭建项目实践

[详细教程]()


---

觉得文章不错就扫码支持一下呗～

![打赏二维码](https://june111.github.io/assets/img/post/pay-qr.jpg)

## 参考链接

* [前端工程化——构建工具选型](https://www.jianshu.com/p/3e8941eda2dd)
* [前端构建工具整理](https://www.imooc.com/article/66984)
* [前端构建工具发展及其比较](https://juejin.im/entry/5ae5c8c9f265da0b9f400d8e)
* [前端构建工具的区别与联系](https://segmentfault.com/a/1190000008443074)
* [《深入浅出Webpack》](http://webpack.wuhaolin.cn/)
* [NPM - Node Package Manager](https://www.openfoundry.org/tw/tech-column/8537-npm-node-package-manager)
* [Yeoman自动构建js项目](http://blog.fens.me/nodejs-yeoman-intro/)
