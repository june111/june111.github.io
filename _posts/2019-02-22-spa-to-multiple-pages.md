---
title: 'VUE 单页面改造为多页面'
subtitle: '每个页面有自己单独的路由'
tags: 前端
author: June
reward: 1
layout: post
date: 2019-02-22
---

# VUE 单页面改造为多页面

因为新页面引用的UI和旧页面的UI冲突了，新UI需要在入口引入js文件，所以改为多页面，这样就可以分开两套页面的入口html文件了。

前提：项目由 vue-cli 2.x 搭建

webpack在打包编译vue文件时，最重要的是入口和输出的配置，所以我们会主要修改这两个部分的配置。

重构过程开始～～～

## 改变目录结构

1. 在src目录下面新建views文件夹,然后在views文件夹下新建index文件夹
2. 将src目录下的main.js和App.vue移动到step1中的index文件夹下，并将main.js重命名为index.js
3. 将src目录下的router文件夹移动到step1中的index文件夹下
4. 将根目录下的index.html文件移动到step1中的index文件夹下

## 新建 test 页面

1. 在views文件夹下新建 test 文件夹
2. 在 test 文件夹下新建 assets 和 components 文件夹，新建 App.vue, dapp.html, dapp.js 文件
3. 创建文件时要注意文件夹、入口js文件、入口html文件的命名要统一

## 修改build下的配置文件

要改的文件：
* build/utils.js
* build/webpack.base.conf.js
* build/webpack.dev.conf.js
* build/webpack.prod.conf.js

### 修改 build/utils.js 文件

修改css的打包路径，以修复css背景路径错误

```js
return ExtractTextPlugin.extract({
    use: loaders,
    fallback: 'vue-style-loader',
})
```

改为

```js
return ExtractTextPlugin.extract({
    use: loaders,
    fallback: 'vue-style-loader',
    // 在这里加一行，修改公共路径前缀
    publicPath: '../../'
})
```

文件最后加上以下代码

```js

// glob是webpack安装时依赖的一个第三方模块，还模块允许你使用 *等符号, 例如lib/*.js就是获取lib文件夹下的所有js后缀名的文件
var glob = require('glob')
// 页面模板
var HtmlWebpackPlugin = require('html-webpack-plugin')
// 取得相应的页面路径，因为之前的配置，所以是src文件夹下的pages文件夹
var PAGE_PATH = path.resolve(__dirname, '../src/views')
// 用于做相应的merge处理
var merge = require('webpack-merge')

//多入口配置
// 通过glob模块读取pages文件夹下的所有对应文件夹下的js后缀文件，如果该文件存在
// 那么就作为入口处理

exports.entries = function() {
    var entryFiles = glob.sync(PAGE_PATH + '/*/*.js')
    var map = {}
    entryFiles.forEach((filePath) => {
        var filename = filePath.substring(filePath.lastIndexOf('\/') + 1, filePath.lastIndexOf('.'))
        map[filename] = ["babel-polyfill",filePath]
    })
    return map
}

//多页面输出配置
// 与上面的多页面入口配置相同，读取pages文件夹下的对应的html后缀文件，然后放入数组中
exports.htmlPlugin = function() {
    let entryHtml = glob.sync(PAGE_PATH + '/*/*.html')
    let arr = []
    entryHtml.forEach((filePath) => {
        let filename = filePath.substring(filePath.lastIndexOf('\/') + 1, filePath.lastIndexOf('.'))
        let conf = {
            // 模板来源
            template: filePath,
            // 文件名称
            filename: filename + '.html',
            // 页面模板需要加对应的js脚本，如果不加这行则每个页面都会引入所有的js脚本
            chunks: ['manifest', 'vendor', filename],
            inject: true
        }
        if (process.env.NODE_ENV === 'production') {
            conf = merge(conf, {
                minify: {
                    removeComments: true,
                    collapseWhitespace: true,
                    removeAttributeQuotes: true
                },
                chunksSortMode: 'dependency'
            })
        }
        arr.push(new HtmlWebpackPlugin(conf))
    })
    return arr
}
```

### 修改 build/webpack.base.conf.js 文件

修改入口

增加babel-polyfill主要是兼容低版本浏览器，因为Babel默认只转换新的JavaScript句法（syntax），而不转换新的API，比如Iterator、Generator、Set、Maps、Proxy、Reflect、Symbol、Promise等全局对象，以及一些定义在全局对象上的方法（比如Object.assign）都不会转码。

```js
   entry: {
     app: ["babel-polyfill", "./src/main.js"]
   },
```
改为
```js
   entry: utils.entries(),
```

### 修改 build/webpack.dev.conf.js 文件

修改 plugins 部分

注释 HtmlWebpackPlugin 相关的以下代码
```
   new HtmlWebpackPlugin({
      filename: 'index.html',
      template: 'index.html',
      inject: true,
	    favicon:path.resolve('favicon.ico')
    }),
```
在 plugins 最后加以下代码，注意中括号是 plugins 的关闭括号

```js
 new FriendlyErrorsPlugin()
  ].concat(utils.htmlPlugin())
```

### 修改 build/webpack.prod.conf.js 文件

注释以下代码
```js
new HtmlWebpackPlugin({
  filename: config.build.index,
  template: 'index.html',
  inject: true,
  minify: {
    removeComments: true,
    collapseWhitespace: true,
    removeAttributeQuotes: true
    // more options:
    // https://github.com/kangax/html-minifier#options-quick-reference
  },
  // necessary to consistently work with multiple chunks via CommonsChunkPlugin
  chunksSortMode: 'dependency'
}),
```

plugins 数组后面加以下代码
```js
.concat(utils.htmlPlugin())
```

## 修改 config 下的配置文件

### 修改 config/index.js 文件

把打包后的资源引用修改为相对路径，要改 build 属性下的 assetsPublicPath

```js
assetsPublicPath: '/',
```
改为

```js
assetsPublicPath: './',
```

在build配置项中增加目标html的输出路径及名称。

```js
index: path.resolve(__dirname, '../dist/index.html'),
test: path.resolve(__dirname, '../dist/test.html'),
```

这样，整个vue多页面配置就完成了

## 配置 history 模式的路由（坑）

有的时候出于强迫症，不能忍受hash模式下的url上存在#符号，或者是出于业务需求，url不能带#号。这个时候要考虑采用vue-router的history模式，history模式的前端配置与上文大同小异，但是由于history模式下url路径的跳转是vue-router利用h5的history API动态添加的，而手动刷新页面会导致找不到路由从而产生404错误，因此还需要对服务端进行配置

修改页面中的路由文件 router/index.js

增加两行
```js
mode: 'history',
base: '/project',
```

假设页面路径是 /test
那么访问路径是：http://localhost:8080/project/test

修改 build/webpack.dev.conf.js 文件

访问的链接，为了实现多路由

实际上，开发环境下我们访问的页面资源是被webpack管理在内存中的，webpack-dev-server作为本地服务根据url返回内存资源给浏览器从而呈现页面。但是多页面情况下如何去根据url返回对应的页面呢，答案就是配置devServer下的historyApiFallback，该配置项会传递给connect-history-api-fallback这个中间件，对request请求的url进行重定向，避免开发环境下页面404，配置如下：

```js
historyApiFallback: {
  rewrites: [
    { from: /.*/, to: path.posix.join(config.dev.assetsPublicPath, 'index.html') },
  ],
},
```
改为

```js
historyApiFallback: {
  rewrites: [
    { from: /.dapp/, to: path.posix.join(config.dev.assetsPublicPath, 'dapp.html') },
    { from: /.*/, to: path.posix.join(config.dev.assetsPublicPath, 'index.html') },
  ],
},
```

因为打包问题，history 模式的两个单独页面单独路由不行，historyApiFallback 就不改了。nginx 也配不好，坑～

最后结果是，一个页面可以用 history 模式的路由，其他页面都不用路由。

---

### 参考链接

* [vue多页面开发和打包的正确姿势](https://juejin.im/post/5a8e3f00f265da4e747fc700#heading-13)
* [基于vue-cli重构多页面脚手架](https://juejin.im/post/5a6559e55188257330610ac5)
* [vue+webpack解决css引用图片打包后找不到资源文件的问题](https://blog.csdn.net/gdut_luoyifei/article/details/79001397)
* [Vue项目编译后部署在非网站根目录的解决方案](https://juejin.im/post/5ae03b98f265da0b8e7f1251)
* [vue开发多页面应用 - hash模式和history模式](https://zhuanlan.zhihu.com/p/46964708)
