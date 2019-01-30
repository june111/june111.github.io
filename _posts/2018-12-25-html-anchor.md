---
layout: post
title: '解决HTML锚点定位偏移最有效快捷的方法'
date: 2018-12-25
author: June
cover: /assets/img/post/2018-12-25/html-anchor.png
reward: 1
tags: 前端
---

# 解决HTML锚点定位偏移最有效快捷的方法

在锚定的内容前加一个暗锚
```html
<a class="target-fix" id="article"></a>
<artivle>主体内容...</article>
```

将锚点进行偏移，并隐藏占位：
```css
.target-fix {
    position: relative;
    top: -44px; // 偏移值
    display: block;
    height: 0;
    overflow: hidden;
}
```

点击锚点，就可以到达锚定的内容了
```html
<a href="#article"></a>
```




