---
title: ''
subtitle: ''
tags: 效率
author: June
cover: /assets/img/post/2019-02-02/cover.png
reward: 1
layout: post
date: 2020-03-15
---

# 

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2019-02-02/structure.svg">
![文章结构]({{site.baseurl}}/assets/img/post/2019-02-02/structure.svg)
</a>

原理
利用网页结构，遍历网页数据

## 准备：

基础知识：python语法，html

工具：
Python 3.x
Google-chrome browser

开发环境：
```bash
pip3 install requests
pip3 install beautifulsoup4
```

## 实操

### 找可用的代理

If you don't have proxies at hand, you can [fetch some proxies](https://github.com/stamparm/fetch-some-proxies).

切入文件夹，执行文件
```bash
python3 fetch.py 
```

要看运气，有时候可能一个都找不到

选个 latency 低的，http://51.158.108.135:8811

关闭terminal，退出程序

### 找要的网页内容


### Export to Excel CSV

```py
import csv
```





---

### 参考链接

* [Beautiful Soup: Build a Web Scraper With Python](https://realpython.com/beautiful-soup-web-scraper-python/)
* [How to get info/data from blocked web sites with BeautifulSoup?](https://stackoverflow.com/questions/54051830/how-to-get-info-data-from-blocked-web-sites-with-beautifulsoup)
* [Beautiful Soup 4.4.0 文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)
* [How to scrape websites with Python and BeautifulSoup](https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe/)
* [python-requests](https://2.python-requests.org/en/v2.8.1/user/quickstart/)
* [CSV File Reading and Writing](https://docs.python.org/3.4/library/csv.html)