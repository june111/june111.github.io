---
layout: post
title: '用 Github Pages && Jekyll 搭建博客'
subtitle: '手把手带你搭建自己的博客'
date: 2018-12-17
author: June
cover: /assets/img/post/2018-12-17/cover.png
tags: 前端
---

# Github Pages && Jekyll

## Github Pages

1. 登陆Github，创建仓库

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-17/create.png">
	![创建仓库]({{site.baseurl}}/assets/img/post/2018-12-17/create.png)
	</a>

2. 克隆仓库到本地
	```bash
	git clone https://github.com/username/username.github.io
	```

3. 写个 Hello World

	进入项目文件夹，添加index.html文件
	```bash
	cd username.github.io
	echo "Hello World" > index.html
	```

4. 推送

	添加文件，提交，推送到仓库
	```bash
	git add --all
	git commit -m "Initial commit"
	git push -u origin master
	```

5. 完成

	打开网址 https://username.github.io 就可以看到之前提交的 Hello World 了

## Jekyll

1. 安装Ruby

	MacBook 自带 Ruby，但是版本较低，一般都需要升级

	```bash
	# 安装 RVM
	curl -sSL https://get.rvm.io | bash -s stable
	# 载入 RVM 环境
	source ~/.rvm/scripts/rvm
	# 修改 RVM 下载 Ruby 的源，到 Ruby China 的镜像
	echo "ruby_url=https://cache.ruby-china.org/pub/ruby" > ~/.rvm/user/db
	# 检查一下是否安装正确
	rvm -v
	# 安装 ruby
	rvm install 2.4.0
	```

2. 安装 Jekyll 和 bundler gems
	```bash
	gem install jekyll bundler
	```

	如果报错 ` Unable to download data from https://ruby.taobao.org/` 
	要删除原gem源
	```bash
	sudo gem sources --remove https://ruby.taobao.org/
	```

	再添加新的，如果这个失效了，则在[官网](https://ruby-china.org/)找新的。
	```bash
	gem source -a https://gems.ruby-china.com
	```

	看下有没添加成功
	```bash
	gem sources -l
	```

3. 创建一个 jekyll 项目，假设名字为 myblog
	```bash
	jekyll new myblog
	```

4. 进入项目
	```bash
	cd myblog
	```

5. 在本地运行项目
	```bash
	bundle exec jekyll serve
	```

	用浏览器打开 http://localhost:4000，看到默认页，说明项目可以跑起来了

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-17/run.png">
	![运行项目]({{site.baseurl}}/assets/img/post/2018-12-17/run.png)
	</a>

6. 草稿

	创建草稿文件夹 `_drafts` ，把草稿里面的内容显示出来
	```bash
	bundle exec jekyll serve --drafts
	```

## 合并 Github Pages && Jekyll

1. 把第一部分的文件夹 `username.github.io` 的内容复制到第二部分的 `myblog` 里面。

2. 进入文件夹myblog
	```bash
	cd myblog
	```

3. 把文件推送到仓库
	```bash
	git add --all
	git commit -m "加入 Jekyll"
	git push 
	```

4. 打开网址 https://username.github.io 就可以看到之前提交的内容了


---

觉得文章不错就扫码支持一下呗～

![打赏二维码](https://june111.github.io/assets/img/post/pay-qr.jpg)

## 参考链接

* [Github Pages](https://pages.github.com/)
* [Jekyll Quickstart](https://jekyllrb.com/docs/)
* [MAC_Ruby 安装](https://www.jianshu.com/p/c073e6fc01f5)
