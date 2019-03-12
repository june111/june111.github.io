---
layout: post
title: '简说 callback，async/await 和 promise'
subtitle: 'callback，async/await 和 promise 原理'
date: 2019-03-12
author: June
cover: /assets/img/post/2019-03-12/front-end-build-tool.png
reward: 1
tags: 前端
---

# async/await 和 promise

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-03-12/structure.svg">
![文章结构]({{site.baseurl}}/assets/img/post/2019-03-12/structure.svg)
</a>
     

https://segmentfault.com/a/1190000010244279

http://www.ruanyifeng.com/blog/2015/05/async.html

https://segmentfault.com/a/1190000012806637

https://segmentfault.com/a/1190000007535316

https://segmentfault.com/a/1190000017224799?utm_source=tag-newest

https://codeburst.io/javascript-es-2017-learn-async-await-by-example-48acc58bad65

## 原理

## 例子

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
            posts.push(post)

            const err = false

            if (!err) {
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
    await createPost({ title: 'Async/Await' })
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
更明显的例子
```js
function doubleAfter2Seconds(x) {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(x * 2);
    }, 2000);
  });
}

// ---- 一直then -----

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

// ---- 简化版 -----

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

* [](https://codeburst.io/javascript-es-2017-learn-async-await-by-example-48acc58bad65)
* []()
* []()
* []()
* []()
* []()




