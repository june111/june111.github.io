---
layout: post
title: '如何把 GitHub 中的项目部署到 GitHub Pages'
subtitle: '两步带你的项目上线'
date: 2019-02-01
author: June
tags: 前端
reward: 1
---

# 如何把 GitHub 中的项目部署到 GitHub Pages

以仓库名为 ProjectName 为例

## VUE

1. 修改路由

	打开配置路由的文件，`router/index.js`，加一行

	```js
	base: 'ProjectName/',
	```

2. 修改配置文件

	* vue-cli 2.x 创建的项目 

		修改配置文件 `config/index.js`，代码如下

		```js
		assetsRoot: path.resolve(__dirname, '../docs'),
		assetsPublicPath: '/ProjectName/',
		```

	* vue-cli 3 创建的项目 

		新建配置文件 `vue.config.js` 添加以下代码

		```js
		module.exports = {
		  baseUrl: 'ProjectName/',
		  outputDir: 'docs',
		  productionSourceMap: false,
		}
		```

## React

1. 显示配置文件

	```bash
	npm run eject
	```

2. 修改配置路径的文件 config/jest/paths.js

	```js
	module.exports = {
	...
	  appPath: resolveApp('./'),
	  appBuild: resolveApp('docs'),
	...
	};
	```


如果要部署到指定的域名，就要添加 CNAME 文件，里面写要指定的域名，再打包进 docs 即可。


---




