---
layout: post
title: 'web 异常监控(Sentry + VUE)'
date: 2018-12-15
author: June
cover: /assets/img/post/2018-12-15/cover.png
reward: 1
tags: 前端
---

# 异常监控(Sentry + VUE)

选用sentry的原因，功能较完善，免费。

所有发给Sentry的异常都会被捕获到如下的特征信息，其中包括：

环境;浏览器;操作系统;触发异常的路径;异常发生的条件;软件的发布信息;异常严重性;服务器名称;最后一次出现的时间点;受异常活跃用户数;错误类型(HTTP错误、500和404);已经发生异常的次数;是否已经解决。

## Sentry 配置全过程

安装
```bash
npm i @sentry/browser
```

配置
```js 
import * as Sentry from '@sentry/browser'

Sentry.init({
  dsn: 'your DSN',
  integrations: [new Sentry.Integrations.Vue({ Vue })]
})

```

这里的DSN指的是Sentry为每个项目配置的用来接入服务的链接，有些类似于git服务。每个DSN由以下六个部分组成：

>{PROTOCOL}://{PUBLIC_KEY}:{SECRET_KEY}@{HOST}/{PATH}{PROJECT_ID}

可以在Sentry的项目设置中获得

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-15/sentry.png">
![DSN的获得]({{site.baseurl}}/assets/img/post/2018-12-15/sentry.png)
</a>

## 废弃版

以下版本已被废弃，但很多文章仍是旧版本的实现，特此提醒。

安装
```bash
npm i raven-js
```

配置
```js 
//测试错误获取
import Raven from 'raven-js';
import RavenVue from 'raven-js/plugins/vue';
Vue.prototype.$Raven = Raven; //设置全局变量
Raven
  .config('your DSN')
  .addPlugin(RavenVue, Vue)   
  .install();
```
---



### 参考链接

* [sentry vue](https://docs.sentry.io/platforms/javascript/vue/)
* [Vue.js (2.0) 已废弃](https://docs.sentry.io/clients/javascript/integrations/vue/)
* [前端代码错误日志监控——Sentry](http://www.yaya12.com/archives/866)

