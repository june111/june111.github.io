---
title: '移动端的滚动加载'
subtitle: '用于移动端的webview'
tags: 前端
author: June
reward: 1
layout: post
date: 2019-02-20
---

# 移动端的滚动加载

记录一下经常遇到的滚动加载，滚动条一到底部就加载数据。不用组件，用vue的api

@scroll="自定义"是vue自带的浏览器滚到api

```html
<template>
  <div class="container"  @scroll="handleScroll()">
  	<div  v-for="(data,index) in data">
      <div>
        <p >订单号{{index}} : <span>201611170301</span></p>
      </div>
      <div >
        <p>顾客 : <span>张三{{index}}</span></p>
      </div>
    </div>
  </div>
</template>
 
<script>
export default {
  data() {
    return {
      data: [1,2,3,4,5,6,7,8,9,10],
      scloll:true,
      page:0,
	  pageCount:10,
    }
  },
  mounted () {
    this.handleScroll();
  },
  methods:{
    handleScroll(){
        //scrollTop为滚动条在Y轴上的滚动距离。
        //clientHeight为内容可视区域的高度。
        //scrollHeight为内容可视区域的高度加上溢出（滚动）的距离。
        if(this.$el.scrollTop+this.$el.offsetHeight>=this.$el.scrollHeight){
          this.loadmore();
          this.scloll=true;
        }else{
          this.scloll=false;
        }
    },
    loadmore() {
    	if (this.page === this.pageCount) {
            console.log('所有数据加载完毕')
            return;
        } else {
              setTimeout(() => {
		        for(var i = 0; i <10; i++) {
		          this.data.push(i);
		        }
		      }, 2000)
            console.log('单次请求数据完毕 ')
            this.page++;
        }
    
    }
  }
}
</script>

```

---

### 参考链接

* [vue滚到底部加载数据](https://blog.csdn.net/qishuixian/article/details/73008514)
