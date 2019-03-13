---
layout: post
title: '简说 callback，async/await 和 promise'
subtitle: 'callback，async/await 和 promise 怎么用'
date: 2019-03-12
author: June
cover: /assets/img/post/2019-03-12/front-end-build-tool.png
reward: 1
tags: 前端
---

# 简说 callback，async/await 和 promise


http://www.ruanyifeng.com/blog/2015/05/async.html


https://segmentfault.com/a/1190000007535316

https://segmentfault.com/a/1190000017224799?utm_source=tag-newest

https://codeburst.io/javascript-es-2017-learn-async-await-by-example-48acc58bad65

## callback


await 只能出现在 async 函数中

JavaScript 的 async/await 实现，离不开 Promise


## 例子

配合[在线例子](https://codepen.io/june111/pen/VRrxpE)可以更好地理解

前置数据
```js
const posts = [
    { title: 'one' },
    { title: 'two' }
]

function getPost() {
    setTimeout(() => {
        let output = ''
        posts.forEach((post, index) => {
            output += `<li>${post.title}</li>`
        })
        document.body.innerHTML = output
    }, 1000)
}
```

### callback

```js
/**
 * callback
 */

function createAPost(post, callback) {
    setTimeout(() => {
        posts.push(post)
        callback()
    }, 2000)
}

createAPost({ title: 'callback' }, getPost)
```

### Promise
```js
/**
 * Promise
 */

function createPost(post) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {

            const err = false

            if (!err) {
                posts.push(post)
                resolve()
            } else {
                reject('Error!!!')
            }
          
        }, 2000)
    })
}
createPost({ title: 'Promise' })
    .then(getPost)
    .catch(err => console.log(err))
```


```js
/**
 * Promise.all
 */
const promise1 = Promise.resolve('hello')
const promise2 = 13
const promise3 = new Promise((resolve, reject) => {
    setTimeout(resolve, 2000, 'bye')
})

Promise.all([promise1, promise2, promise3]).then(val => {
    posts.push({ title: val })
})
```

### async/await

```js
/**
 * Async/Await
 */
async function init() {
    // await createPost({ title: 'Async/Await' })

    // ----- 处理错误 -----
    try {
        await createPost({ title: 'Async/Await' })
    } catch (error) {
        console.log(error);
    }
    getPost()
}
init()
```

### fetch

```js
// async/await/fetch
async function fetchUsers() {
    const res = await fetch('http://jsonplaceholder.typicode.com/users')
    const data = await res.json()
    console.log(data)
}

fetchUsers()
// (10) [{…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}, {…}]
```

### 简洁代码
```js
/**
 * Promise/Async/Await
 */
function getAllPost() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            let data = { title: 'Promise/Async/Await' }
            resolve(data)
        })
    })
}

async function initPost() {

    // getAllPost().then((data) => {
    //     posts.push(data)
    // })

    // ---- 简化版 -----
    const data = await getAllPost()
    posts.push(data)
}
initPost()
```

async/await 的优势在于处理 then 链

```js
function doubleAfter2Seconds(x) {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(x * 2);
    }, 2000);
  });
}

// ----- then 链 -----

function addPromise(x){
  return new Promise(resolve => {
    doubleAfter2Seconds(10).then((a) => {
      doubleAfter2Seconds(20).then((b) => {
        doubleAfter2Seconds(30).then((c) => {
          resolve(x + a + b + c);
        })
      })
    })
  });
}

addPromise(10).then((sum) => {
  console.log(sum);
});

// ----- 简化版 -----

async function addAsync(x) {
  const a = await doubleAfter2Seconds(10);
  const b = await doubleAfter2Seconds(20);
  const c = await doubleAfter2Seconds(30);
  return x + a + b + c;
}

addAsync(10).then((sum) => {
  console.log(sum);
});
```

---

### 参考链接

* [JavaScript ES 2017: Learn Async/Await by Example](https://codeburst.io/javascript-es-2017-learn-async-await-by-example-48acc58bad65)
* [理解 async/await](https://segmentfault.com/a/1190000010244279)
* []()
* []()
* []()
* []()




