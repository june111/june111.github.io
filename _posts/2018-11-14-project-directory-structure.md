---
layout: post
title: '项目目录结构规范'
date: 2018-11-14
author: June
cover: /assets/img/post/2018-11-14/project-directory-structure.png
tags: 前端
---

# 项目目录结构规范

## 建目录需要遵循的原则

### 结构清晰

项目的目录结构的分层要有章可循，看完目录后，可以让人大致掌握项目的结构。

### 可读性

文件的命名要简洁，有习惯性缩写的单词必须采用容易理解的缩写。且文件名必须一律小写。

### 组件粒度

通常我们在 components 目录放组件，组件不宜划分太细。

>在组件化的应用中，组件树的层级不宜过深，从根节点算起，应当尽可能控制在3到5层内，如果层级太多的话，会造成组件通讯和数据传递的负担。

组件的划分还需要兼顾移除成本最小化，即减少耦合。

## 搭建目录结构

不管大型还是小型项目，清晰的目录结构是开发过程的好的开始。以我常用的web项目为例，搭建一下目录结构。

```html
Project
    ├── node_modules      		// npm上的第三方资源
	├── build					// 构建相关
		├── config				// 配置相关
		├── webpack.config.js   // webpack 配置文件 
    ├── src 					// 开发时源文件
        ├── api	       			// 所有请求
        ├── components    		// 存放自己实现的组件
        	├── foo        		// 组件 foo
	            ├── css      	// 组件 foo 的样式 
	            ├── js       	// 组件 foo 的逻辑 
	            ├── tpl     	// 组件 foo 的模板 
	            ├── index.js    // 组件 foo 的入口 
        ├── filters       		// 存放自己实现的 filter
        ├── directives    		// 存放自己实现的 directives
        ├── static        		// 存放非组件资源
        ├── util 		 		// 全局公用方法
		├── router       		// 本地路由配置 
			├── modules			
			├── index.js 			
		├── store 				// 全局 store管理
			├── modules			
			├── getters.js 			
			├── index.js 			
		├── pages				// 存放页面
			├── dashboard      	
				├── a.vue  		
				├── index.vue 	
		├── main.js             // 入口文件 加载组件 初始化等
		├── app.vue             // 入口页面
	├── test 					// 测试用例
		├── mock               	// 假数据目录 
    ├── dep           			// 存放不在npm上的第三方资源
	├── doc 					// 存放项目文档
	├── dist               		// 编译输出目录，即发布目录 
	├── .babelrc                // babel-loader 配置
	├── .eslintrc.js            // eslint 配置项
	├── .gitignore              // git 忽略项
	├── .travis.yml             // 自动化CI配置
	├── package.json          	// 项目配置 
	├── README.md             	// 项目说明
```

这是个经典的前端项目目录结构，项目目结构在一定程度上约定了开发规范。业务开发的同学只需关注src目录即可，开发时尽可能最小化模块粒度，这是异步加载的需要。

## 常用目录

根目录下，一级目录的目录结构按照 `职能` 进行划分。根据`业务逻辑`划分src目录结构。

src 目录用于存放开发时源文件。  
dist 目录用于存放编译输出的文件。  
dep 目录用于存放项目引入依赖的第三方包。  
tool 目录用于存放开发时或构建阶段使用的工具。  
build 目录用于存放打包相关的配置文件。  
test 目录用于存放测试用例以及开发阶段的模拟数据。  
doc 目录用于存放项目文档。项目文档可能是开发者维护的文档，也可能是通过工具生成的文档。  
entry 目录用于存放项目的页面入口文件，通常是上线后可被直接访问的静态页面。  

如果项目规模较大，涉及多个团队协作，还可以将具有相关业务功能的页面组织在一起，形成一个子系统，进一步将整个站点拆分出多个子系统来分配给不同团队维护。


---

觉得文章不错就扫码支持一下呗～

![打赏二维码](https://june111.github.io/assets/img/post/pay-qr.jpg)

## 参考链接

* [告别刀耕火种:浅谈VisMooc的前端工程化](http://chenzhutian.org/blog/2016/%E6%B5%85%E8%B0%88VisMooc%E7%9A%84%E5%89%8D%E7%AB%AF%E5%B7%A5%E7%A8%8B%E5%8C%96/)
* [前端工程——基础篇 #10](https://github.com/fouber/blog/issues/10#)
* [项目目录结构规范](https://github.com/ecomfe/spec/blob/master/directory.md)
* [Web应用组件化的权衡 #22](https://github.com/xufei/blog/issues/22)
* [组件化架构漫谈](https://www.jianshu.com/p/67a6004f6930)
