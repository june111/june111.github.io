---
layout: post
title: 'Vue常用的传值方式'
date: 2018-11-22
author: June
cover: /assets/img/post/2018-11-22/vue-pass-value.png
tags: vue
---

# Vue常用的传值方式

Vue常用的三种传值方式有：

* 父传子

* 子传父

* 非父子传值

>引用官网的一句话：父子组件的关系可以总结为 prop 向下传递，事件向上传递。父组件通过 prop 给子组件下发数据，子组件通过事件给父组件发送消息，如下图所示：

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-22/p<=>c.png">
![父子组件通信]({{site.baseurl}}/assets/img/post/2018-11-22/p<=>c.png)
</a>

接下来，我们通过实例来看可能会更明白一些：

1. 父组件向子组件进行传值

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-22/p-c.png">
	![父组件到子组件]({{site.baseurl}}/assets/img/post/2018-11-22/p-c.png)
	</a>

	父组件：
	```html
	<template>
	  <div>
	    父组件:
	    <input type="text" v-model="name">
	    <br>
	    <br>
	    <!-- 引入子组件 -->
	    <child :inputName="name"></child>
	  </div>
	</template>
	<script>
	  import child from './child'
	  export default {
	    components: {
	      child
	    },
	    data () {
	      return {
	        name: ''
	      }
	    }
	  }
	</script>
	```
	子组件：
	```html
	<template>
	  <div>
	    子组件:
	    <span>{{inputName}}</span>
	  </div>
	</template>
	<script>
	  export default {
	    // 接受父组件的值
	    props: {
	      inputName: String,
	      required: true
	    }
	  }
	</script>
	```

2. 子组件向父组件传值

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-22/c-p.png">
	![子组件到父组件]({{site.baseurl}}/assets/img/post/2018-11-22/c-p.png)
	</a>

	子组件：
	```html
	<template>
	  <div>
	    子组件:
	    <span>{{childValue}}</span>
	    <!-- 定义一个子组件传值的方法 -->
	    <input type="button" value="点击触发" @click="childClick">
	  </div>
	</template>
	<script>
	  export default {
	    data () {
	      return {
	        childValue: '我是子组件的数据'
	      }
	    },
	    methods: {
	      childClick () {
	        // childByValue是在父组件on监听的方法
	        // 第二个参数this.childValue是需要传的值
	        this.$emit('childByValue', this.childValue)
	      }
	    }
	  }
	</script>
	```

	父组件：
	```
	<template>
	  <div>
	    父组件:
	    <span>{{name}}</span>
	    <br>
	    <br>
	    <!-- 引入子组件 定义一个on的方法监听子组件的状态-->
	    <child v-on:childByValue="childByValue"></child>
	  </div>
	</template>
	<script>
	  import child from './child'
	  export default {
	    components: {
	      child
	    },
	    data () {
	      return {
	        name: ''
	      }
	    },
	    methods: {
	      childByValue: function (childValue) {
	        // childValue就是子组件传过来的值
	        this.name = childValue
	      }
	    }
	  }
	</script>
	```

3. 非父子组件进行传值

	公共bus.js
	```js
	//bus.js
	import Vue from 'vue'
	export default new Vue()
	```
	组件A：
	```html
	<template>
	  <div>
	    A组件:
	    <span>{{elementValue}}</span>
	    <input type="button" value="点击触发" @click="elementByValue">
	  </div>
	</template>
	<script>
	  // 引入公共的bug，来做为中间传达的工具
	  import Bus from './bus.js'
	  export default {
	    data () {
	      return {
	        elementValue: 4
	      }
	    },
	    methods: {
	      elementByValue: function () {
	        Bus.$emit('val', this.elementValue)
	      }
	    }
	  }
	</script>
	```
	组件B：
	```html
	<template>
	  <div>
	    B组件:
	    <input type="button" value="点击触发" @click="getData">
	    <span>{{name}}</span>
	  </div>
	</template>
	<script>
	  import Bus from './bus.js'
	  export default {
	    data () {
	      return {
	        name: 0
	      }
	    },
	    mounted: function () {
	      var vm = this
	      // 用$on事件来接收参数
	      Bus.$on('val', (data) => {
	        console.log(data)
	        vm.name = data
	      })
	    },
	    methods: {
	      getData: function () {
	        this.name++
	      }
	    }
	  }
	</script>
	```





---

觉得文章不错就扫码支持一下呗～

![打赏二维码]({{site.baseurl}}/assets/img/post/pay-qr.jpg)

## 参考链接

* [Vue2.0的三种常用传值方式、父传子、子传父、非父子组件传值](https://blog.csdn.net/lander_xiong/article/details/79018737)
