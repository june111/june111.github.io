---
title: 'vue 根据窗口宽度改变UI组件'
subtitle: 'debounce & throttling'
tags: 前端
author: June
reward: 1
layout: post
date: 2019-05-14
---

# vue 根据窗口宽度改变UI组件

```bash
npm i lodash
```

`layout.vue`

```html
<template>
  <div>
    <router-view></router-view>
  </div>
</template>
<script>
import _ from 'lodash'

const { body } = document
const WIDTH = 992 // refer to Bootstrap's responsive design

export default {
  name: 'layout',
  mounted() {
    window.addEventListener('resize', this.onWindowResize)
  },
  destroyed() {
    window.removeEventListener('resize', this.onWindowResize)
  },
  methods: {
    isMobile() {
      const rect = body.getBoundingClientRect()
      return rect.width - 1 < WIDTH
    },
    resizeHandler() {
      if (!document.hidden) {
        const isMobile = this.isMobile()
        this.$store.dispatch('toggleDevice', isMobile ? 'mobile' : 'desktop')
      }
    },
    onWindowResize: _.debounce(function() {
      this.resizeHandler()
    }, 400) // delay 100ms between resize events
  }
}
</script>
```

`store/index.js`

```js
import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
export default new Vuex.Store({
  state: {
    device: 'desktop',
  },

  mutations: {
    TOGGLE_DEVICE: (state, device) => {
      state.device = device
    },
  },
  actions: {
    toggleDevice({
      commit
    }, device) {
      commit('TOGGLE_DEVICE', device)
    },
  },
})
```

---

### 参考链接

* [Improve Your App Performance with Event Debouncing](https://tahazsh.com/vuebyte-debounce-event)
* [PanJiaChen/vue-element-admin](https://github.com/PanJiaChen/vue-element-admin/blob/26d0f40df21fa5e5583a20cb3df14ae9d475bb3c/src/layout/mixin/ResizeHandler.js)
