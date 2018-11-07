---
layout: post
title: '入门DevOps'
date: 2018-06-20
author: June
cover: 'https://june111.github.io/blog/assets/img/post/computer.png'
tags: 技术
---

# 入门DevOps

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-10-25/structure.svg">
![文章结构]({{site.baseurl}}/assets/img/post/2018-10-25/structure.svg)
</a>

Devops一词来自于Development 和 Operations 的组合，从字面意思理解，就是让软件开发人员和运维人员更好的沟通合作，通过自动化流程让软件开发、测试、发布更快捷。实际上，Devops是对敏捷和精益开发的传承，是在整个IT价值流中实施精益的结果，Devops并不是只一个新的工程师，也不是一个部门，而是一种文化，没有什么工具可以把团队直接变成Devops组织，这是一种观念的转变。



DevOps（Development和Operations的组合词）是一种重视“软件开发人员（Dev）”和“IT运维技术人员（Ops）”之间沟通合作的文化、运动或惯例。透过自动化“软件交付”和“架构变更”的流程，来使得构建、测试、发布软件能够更加地快捷、频繁和可靠。



DevOps的三大原则：
1、基础设施即代码（Infrastructure as Code）
DeveOps的基础是将重复的事情使用自动化脚本或软件来实现，例如Docker（容器化）、Jenkins（持续集成）、Puppet（基础架构构建）、Vagrant（虚拟化平台）等
2、持续交付（Continuous Delivery）
持续交付是在生产环境发布可靠的软件并交付给用户使用。而持续部署则不一定交付给用户使用。涉及到2个时间，TTR（Time to Repair）修复时间，TTM（Time To Marketing）产品上线时间。要做到高效交付可靠的软件，需要尽可能的减少这2个时间。部署可以有多种方式，比如蓝绿部署、金丝雀部署等。
3、协同工作（Culture of Collaboration）
开发者和运维人员必须定期进行密切的合作。开发应该把运维角色理解成软件的另一个用户群体。协作有几个的建议：1、自动化（减少不必要的协作）；2、小范围（每次修改的内容不宜过多，减少发布的风险）；3、统一信息集散地（如wiki，让双方能够共享信息）；4、标准化协作工具（比如jenkins）

参考
(DevOps的三大原则)[https://blog.csdn.net/difffate/article/details/77542768]