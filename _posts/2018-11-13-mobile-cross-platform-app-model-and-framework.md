---
layout: post
title: '移动端跨平台APP'
date: 2018-11-13
author: June
cover: /assets/img/post/2018-11-13/mobile-cross-platform-app-model-and-framework.png
tags: 前端
reward: 1
copyright: 1
---

# 移动端跨平台APP之模式与框架

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-13/structure.svg">
![文章结构]({{site.baseurl}}/assets/img/post/2018-11-13/structure.svg)
</a>

## 为什么要开发跨平台APP

为了开发速度，节省成本。

## 如何开发跨平台APP

### 开发模式

* Native App

	即原生开发模式,开发出来的是原生程序，有iOS和Android两大系统，需要各自语言(Java、C++、Swift / Objective-C)开发各自App。

	优势
	* 相比于其它模式，提供最佳的用户体验，最优质的用户界面，最华丽的交互
	* 针对不同平台提供不同体验
	* 可节省带宽成本，打开速度更快
	* 功能最为强大,特别是在与系统交互中,几乎所有功能都能实现

	劣势
	* 门槛高，原生开发人才稀缺，至少比前端和后端少，开发环境昂贵
	* 无法跨平台，开发的成本比较大，各个系统独立开发
	* 发布成本高，需要通过store或market的审核，导致更新缓慢
	* 维持多个版本、多个系统的成本比较高，而且必须做兼容
	* 应用市场逐渐饱和，怎么样抢占用户时间需要投入大量时间和金钱，这也导致“僵尸”App的增多

	适合
	* 性能要求极高,体验要求极好,不追求开发效率
	* 一般属于吹毛求疵的那种级别了,因为正常来说如果要求不是特别高,会有Hybrid

	例子：iOS 的有道词典，Android 的爱奇艺

* Hybrid App

	混合开发，也就是半原生半Web的开发模式，由原生提供统一的API给JS调用，实际的主要逻辑有Html和JS来完成，最终是放在webview中显示的，所以只需要写一套代码即可达到跨平台效果，另外也可以直接在浏览器中调试，很方便。

	原理：用Html+Css实现界面，JS来写逻辑，调用API，最终的页面在Webview中显示。是在 WebView 的基础上，与原生客户端建立 JS Bridge 桥接，以达到 JS 调用 Native API 和 Native 执行 JS 方法的目的。

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-13/hybrid-principle.jpg">
	![Hybrid原理]({{site.baseurl}}/assets/img/post/2018-11-13/hybrid-principle.jpg)
	</a>

	优势
	* 开发和发布都比较方便，效率介于Native App、Web App之间。
	* 开发成本较低,可以跨平台,调试方便
	* 维护成本低,功能可复用
	* 更新较为自由
	* 功能更加完善,性能和体验要比起web app好太多

	劣势
	* 部分性能要求的页面可用原生实现
	* 相比原生,性能仍然有较大损耗
	* 不适用于交互性较强的app

	适合
	* 大部分情况下的App都推荐采用这种模式
	* 这种模式可以用原生来实现要求高的界面,对于一些比较通用型,展示型的页面完全可以用web来实现,达到跨平台效果,提升效率

	例子：LinkedIn的iPad App

* Web App

	使用网页技术实现的App，常被称为H5应用。就是运行于网络和标准浏览器上，基于网页技术开发实现特定功能的应用。一般泛指 SPA(Single Page Application)模式开发出的网站，与MPA（Multi-page Application）对应。

	原理：网页在不同的浏览器中运行。

	优势
	* 开发和发布成本最低。
	* 可以跨平台，调试方便
	* 无需安装，不会占用手机内存，而且更新速度最快
	* 不存在多版本问题，维护成本低
	* 临时入口，可以随意嵌入

	劣势
	* 依赖于网络，第一次访问页面速度慢，耗费流量
	* 受限于手机和浏览器性能，用户体验相较于其他模式最差
	* 功能受限，大量移动端功能无法实现
	* 性能和体验不能讲是最差的，但也受到浏览器处理能力的限制
	* 入口强依赖于第三方浏览器，且只能以URL地址的形式存在，导致用户留存率低（优点即缺点）

	适合
	* 不追求用户体验和性能,对离线访问没要求
	* 没有额外功能,只有一些信息展示

	例子：[Financial Times](http://app.ft.com)

* PWA

	[Progressive Web App](https://developers.google.com/web/progressive-web-apps/), 简称 PWA，是提升 Web App 的体验的一种新方法，能给用户带来原生应用的体验。PWA 能做到原生应用的体验不是靠某一项特定技术，而是经过应用一系列新技术进行改进，在安全、性能和体验三个方面都有很大提升，PWA 本质上还是 Web App。

	优势

	* 后台加载：引入Service Worker概念，即使网页关闭仍然可以在后台运行获取数据更新（只能更新小部分数据有限制）
	* 消息推送：用户允许，即使网页关闭后依然可以接受到系统通知栏推送
	* 原生应用界面：可以隐藏浏览器本身的所有视觉部分，光光从UI和UX上面看,用户会很容易认为这就是一个原生界面
	* 离线使用：离线浏览（ Service Worker 能让 Web 站点离线）
	* 桌面图标：只要配置一个图标，应用就能生成快捷方式在桌面上，结合上面的效果基本能和原生相对比。（但国内权限被默认禁止）
	* 无需安装
	* 优雅降级、渐进增强

	劣势

	* 根据国情来看哈，目前 Native App 的使用用户都已经习惯了，虽然会下载一下，但是现在 WiFi 到处都是了，毕竟 WiFi 的普及太快了。让用户使用 PWA 来替代 Native App 短时间会不适应。
	            
	* 消息推送问题，PWA的消息推送走的是 GCM（ FCM ）通道。而国内 Google 是无法访问的。

	例子：[饿了么官网](https://www.ele.me/home/)、[PWA 小应用集合](https://pwa.rocks/)

### 开发框架

* React Native

	[React Native](https://facebook.github.io/react-native/) 是 Facebook发现Hybrid App存在很多缺陷和不足，于是发起开源的一套新的App开发方案RN。使用JSX语言写原生界面，js通过JSBridge调用原生API渲染UI交互通信。

	架构
	https://zhuanlan.zhihu.com/p/41900859

	React Native技术抛开了WebView，利用JavaScriptCore来做桥接，将JS调用转为native调用，只牺牲了小部分性能获取的跨平台开发，这是一大步进步。但是由于依然存在一个从JS代码到原生代码的转化过程，在界面UI被频繁操作的情况下，可能会导致性能问题。

	React Native的效率由于是将View编译成了原生View，所以效率上要比基于Cordova的HTML5高很多，但是它也有效率问题。React Native的渲染机制是基于前端框架的考虑，复杂的UI渲染是需要依赖多个view叠加。比如我们渲染一个复杂的ListView，每一个小的控件，都是一个native的view，然后相互组合叠加。想想此时如果我们的list再需要滑动刷新，会有多少个对象需要渲染。所以它的列表方案不友好。

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-13/react-native-a.png">
	![React Native框架原理]({{site.baseurl}}/assets/img/post/2018-11-13/react-native-a.png)
	</a>

	优点

	* 效率体验接近Native App，发布和开发成本低于Native App
	* 虽然不能做到一次编码到处运行，但是基本上即使是两套代码，也是相同的jsx语法，使用js进行开发。用户体验高于html， 开发效率较高
	* Flexbox布局据说比native的自适应布局更加简单高效
	* 非常大的和活跃的社区支持

	缺点

	对开发人员要求较高，不是懂点web技术就行的，当官方封装的 控件、API无法满足需 求时就必然需要懂一些native的东西去 扩展，扩展性仍然远远不如web，也远远不如直 接写Native Code。


* Flutter

	[Flutter](https://flutter.io/) 是 Google 在 2017 年的 Google I/O 上推出的移动端 UI 开发框架，可以快速在 iOS 和 Android 上构建高质量的原生用户界面。同时也将是 Google 新系统 Fuchsia 下开发应用的主要工具。

	这里需要强调的是，Flutter 与 React Native/Weex 本质上是不同的，它并没有使用 WebView、JavaScript 解释器或者系统平台自带的原生控件，而是有自己专属的一套 Widget，界面开发使用 Dart 语言，而底层渲染使用自身的高性能 C/C++ 引擎自绘。

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-13/flutter-a.png">
	![Flutter框架原理]({{site.baseurl}}/assets/img/post/2018-11-13/flutter-a.png)
	</a>

	架构

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-13/flutter-b.png">
	![Flutter 架构]({{site.baseurl}}/assets/img/post/2018-11-13/flutter-b.png)
	</a>

	Flutter Framework: 这是一个纯 Dart实现的 SDK，类似于 React在 JavaScript中的作用。它实现了一套基础库， 用于处理动画、绘图和手势。并且基于绘图封装了一套 UI组件库，然后根据 Material 和Cupertino两种视觉风格区分开来。这个纯 Dart实现的 SDK被封装为了一个叫作 dart:ui的 Dart库。我们在使用 Flutter写 App的时候，直接导入这个库即可使用组件等功能。

	Flutter Engine: 这是一个纯 C++实现的 SDK，其中囊括了 Skia引擎、Dart运行时、文字排版引擎等。不过说白了，它就是 Dart的一个运行时，它可以以 JIT、JIT Snapshot 或者 AOT的模式运行 Dart代码。在代码调用 dart:ui库时，提供 dart:ui库中 Native Binding 实现。 不过别忘了，这个运行时还控制着 VSync信号的传递、GPU数据的填充等，并且还负责把客户端的事件传递到运行时中的代码。 

	优点

	* 响应式视图，不需要 JavaScript 的桥接器
	* 快速，流畅，可预测; 代码将 AOT 编译为本机（ARM）代码
	* 开发人员完全控制 UI 组件和布局
	* 配有美观，可定制的 UI 组件
	* 强大的开发者工具，惊人的热重新加载
	* 性能更好，兼容性更好，开发起来更有乐趣

	缺点

	* 采用Dart语言开发，属于小众语言，需要一切都要重新学习。
	* 现在还处在Beta阶段，第三方库很少。

	例子：闲鱼，腾讯NOW直播(iOS)，京东金融等

* Ionic 

	[Ionic](https://ionicframework.com/) = Cordova + AngularJS + 一套样式库。使用标准的HTML、 CSS和JavaScript，开发跨平台（目前支持：Android、iOS，计划支持：Windows Phone、Firefox OS） 的原生App应用。绑定了与AngularJS和Sass。基于PhoneGap的编译平台，可以实现编译成各个平台的应用程序。

	架构

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-13/Ionic.png">
	![Ionic的基本组成]({{site.baseurl}}/assets/img/post/2018-11-13/Ionic.png)
	</a>

	在上图中，ionic所包含的范围为上图中蓝色部分。这四个部分都是现有的工具或技术，各个部分分别负责如下模块：

	Angular & Angular UI： 用于构建APP页面的框架，以及组件UI。
	Sass：用于编写和编译页面和组件样式。
	iconfont：用于iconfont图标。
	Cordova：用于将HTML，JS，CSS打包编译为不同终端的安卓包，并且为js与对应平台上的native api提供交互能力。  

	优点

	* 漂亮的界面，追求性能，专注原生，免费开源
	* Angular JS MVVM 开发理念，数据双向绑定
	* 继承自 Cordova，可以使用 Cordova 的插件

	缺点

	* Angular JS 学习路线陡峭
	* Ionic 框架相比于原生的 Cordova 有所差异，Cordova 某些官方插件可能不适用于Ionic
	* 直接将页面打包发布会使得迭代不好解决，如果使用离线包机制可以解决这一问题，但是客户端的定制化仍然我们对预处理后的代码进行较大的二次修改
	* 依然停留在webview开发阶段，不能突破webview解析dom的性能问题
	* 目前没有自动化调试，需借助外部工具来做


* Weex

	[Weex](https://weex.incubator.apache.org/) 是阿里巴巴开发团队在RN的成功案例上，重新设计出的一套开发模式，站在了巨人肩膀上并有淘宝团队项目做养料，广受关注，2016年4月正式开源，并在v2.0版本官方支持Vue.js，与RN分庭抗礼。
	
	架构

	开发者在本地像编写 web 页面一样编写一个 app 的界面，然后通过命令行工具将之编译成一段 JavaScript 代码，生成一个 Weex 的 JS bundle；然后部署至云端；在移动应用客户端里，Weex SDK 会准备好一个 JavaScript 执行环境，并且在用户打开一个 Weex 页面时在这个执行环境中执行相应的 JS bundle，并将执行过程中产生的各种命令发送到 native 端进行界面渲染、数据存储、网络通信、调用设备功能及用户交互响应等功能。

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-13/weex-flow.png">
	![Weex 架构]({{site.baseurl}}/assets/img/post/2018-11-13/weex-flow.png)
	</a>

	优点：单页开发模式效率极高，热更新发包体积小，并且跨平台性更强。

	缺点：刚刚起步，文档欠缺；社区没有RN活跃，功能尚不健全，暂不适合完全使用Weex开发App。

	例子：阿里巴巴，饿了么，优酷

* NativeScript
	
	[NativeScript](https://www.nativescript.org) 是 Telerik（做过Kendo UI）推出的。是一套开源框架，负责利用Angular、TypeScript或者JavaScript构建起真正的原生iOS与Android应用。NativeScript不仅能够轻松处理iOS与Android API，亦可渲染原生iOS与Android用户界面。
	
	架构

	使用js或者TypeScript构建业务逻辑，使用xml和css设计app界面，NativeScript自动将你的代码编译成不同平台的app。

	目前NativeScript支持Android 4.2+ 和ios 7.1+

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-13/NativeScript.png">
	![NativeScript原理]({{site.baseurl}}/assets/img/post/2018-11-13/NativeScript.png)
	</a>

	1. 基于ns modules和ns runtime只需要一次编码就能实现跨平台
	2. 根据不同平台使用不同的资源比如icon，splash screen
	3. 编译你的app：当你启动编译的时候NS将非平台相关的代码编译成native 代码，NativeScript tools 使用native平台sdk和工具来生成一个代码包。
	4. 在模拟器或者真实设备中运行你的app

	优点

	* 真正的跨平台支持。用于开发所有支持平台的应用程序的单一代码库。
	* 100％Native API访问。您可以使用TypeScript / JavaScript代码访问诸如相机，触摸，日历，电话等硬件功能。
	* 使用AngularJS 2，以便您可以轻松地将以前的Web组件传输到应用程序中。

	缺点

	* 需要为组件单独下载许多插件。并非所有插件都可用或经过验证（即经过彻底测试）。
	* 应用程序的大小远大于ReactNative和Ionic 2.如果您的用户有较慢的互联网连接，那么这可能是一个问题。
	* 在NativeScript中不支持HTML和DOM，因此您需要学习不同的UI组件来构建应用程序的UI。

* Cordova／PhoneGap

	[Cordova](https://cordova.apache.org/) 是Apache旗下的一个开源的移动开发框架。它允许你使用WEB开发技术（HTML5、CSS3、JavaScript）进行跨平台开发。应用在每个平台的封装器中执行，并且依赖规范的API对设备进行高效的访问，比如传感器、数据、网络状态等等。

	Cordova通过对HTML、CSS、JS封装为原生APP。Cordova将不同设备的功能，按标准进行了统一封装，开发人员不需要了解设备的原生实现细节，并且提供了一组统一的JavaScript类库，以及为这些类库所使用的设备相关的原生后台代码。因此实现了“write once, run anywhere”(一次开发，随处运行)。

	Cordova前身是PhoneGap。2011年Adobe公司将其收购对其开源，并捐献给Apache，重新命名为Cordova。

	架构

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-13/Cordova.png">
	![Cordova框架原理]({{site.baseurl}}/assets/img/post/2018-11-13/Cordova.png)
	</a>

	以往最早的以Cordova为代表的Hybrid开发，主要依赖于WebView。但是WebView是一个很重的控件，很容易产生内存问题，而且复杂的UI在WebView上显示的性能不好。JS与Native代码之间的通信需要使用JSBridge进行上下文切换，因此会降低一些性能。

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-13/Cordova-b.png">
	![Cordova架构]({{site.baseurl}}/assets/img/post/2018-11-13/Cordova-b.png)
	</a>

	Cordova的基础是html和js运行在webView容器里面，通过Cordova提供的接口与硬件通讯；所以它的小路天生受到限制，而且也受到了各个厂商对webkit内核支持的好坏。

	优点

	* iOS和Android基本上可以共用代码，纯web思维，开发速度快，简单方便，一次编码，到处运行。如果熟悉web开发，文档很全， 系统级支持封装较好，所有UI组件都是有html模拟，可以统一使用。
	* 文档多，开发者多，遇到问题容易解决，技术成熟。
	* 多平台支持。Apache Cordova支持大多数开发者所使用的移动平台和操作系统，包括Android，iOS，Windows 8.1，iPhone 8.1和10，OS X，几乎可以覆盖所有移动用户。

	缺点

	* 性能：使用Apache Cordova创建的移动应用，会因性能问题而受到影响，因为它是一种混合的跨平台移动应用开发工具。
	* 开发工具：由于Apache Cordova使用HTML，CSS和JavaScript等Web技术，因此用于Apache Cordova的大多数开发工具都针对Web开发进行了优化，而非移动应用开发。
	* 测试：在Apache Cordova中调试代码会比较繁琐，虽然可以使用开发工具修复任何代码上的bug，但需要使用特定于平台的工具来修复特定平台中发生的问题。
	* 技术：即便开发者可能熟练掌握了HTML，CSS和JavaScript等网络技术，但仍需要具备Web和移动应用的经验才能创建Cordova移动应用。
	* 支持的平台：Cordova多年来已经弃用了许多支持的平台，包括BlackBerry，Firefox OS，Symbian，Ubuntu Touch，webOS，Windows Phone 8.1和Windows Phone 10.虽然Cordova可能很难弃用iOS和Android，但仍然无法保证它继续支持任何其他当前所有平台。
	* 更新延迟：Cordova的更新时间有时会比平台的更新更慢，无论是新功能的迭代还是其他，因此可能会导致应用出现一些问题。
	* 插件：虽然Cordova提供了比其他任何跨平台开发工具中都多的插件，但它仍然无法与本机移动应用开发工具相比。

* Xamarin

	Xamarin是一个跨平台的移动应用开发框架，由微软基于Mono（一个免费的开源.NET框架），使用C＃创建本地应用。

	Xamarin 的跨平台开发思路是：使用 C# 来完成所有平台共用的，和平台无关的 app 逻辑部分；由于各个平台的 UI 和交互不同，再使用由 Xamarin 封装好的 C# API 来访问和操控 native 的控件，分别进行不同平台的 UI 开发。

	架构

	Xamarin 提供两种商业产品：Xamarin.iOS 和 Xamarin.Android。

	* Xamarin.Android 实现原理

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-13/Xamarin-a.png">
	![Xamarin.Android架构图]({{site.baseurl}}/assets/img/post/2018-11-13/Xamarin-a.png)
	</a>

	Android Callable Wrappers（ACW）

	使用C#开发的Android应用程序在运行的时候，C#代码是在Mono虚拟机中执行的，而Mono虚拟机是寄宿在Dalvik虚拟机中运行的，所有的C#代码都通过ACW的方式被调用。

	由于需要打包Mono环境，使用C#开发的Android应用的APK文件会比原生开发的大，执行效率也会差一些。

	Managed Callable Wrapper（MCW）

	如果需要在C#中调用一些系统的功能或者Java实现的类库，该如何调用那？ 答案就是MCW，MCW就是一个JNI桥梁，可以使用托管代码调用Android的代码。MCW将整个Android.* 以及相关的命名空间通过 jar绑定的方式暴露出来，是的C#可以调用。

	* Xamarin.iOS 实现原理

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-11-13/Xamarin-ios.png">
	![Xamarin.iOS架构图]({{site.baseurl}}/assets/img/post/2018-11-13/Xamarin-ios.png)
	</a>

	对于开发者来说，Xamarin.IOS相对于Xamarin.Android就要简单很多了，我们用C#开发的iOS应用程序在被编译成IL代码之后，然后转交给Apple complier直接编译成iOS的本地机器码，也就是说C#写的iOS应用程序和Objective-C 写的是一样的。 

	透过 Ahead-of-Time (AOT) 编译程序，直接将Xamarin.iOS程序编译为ARM的执行档。编译封装完成的应用程序被直接编译为原生的二进制执行文件。

	优点

	* 完整的开发堆栈：许多开发者认为Xamarin是最完整的跨平台移动应用开发框架。拥有自己的专用堆栈，C＃作为编程语言；Visual Studio作为IDE，与Xamarin完全集成；.NET作为开发平台；Xamarin测试云进行测试；以及Xamarin.Insights用于分析。
	* 性能：Xamarin在性能方面也几乎与本地应用相同。 Xamarin比混合应用更快，因为混合应用必须在特定于平台的Web组件中运行代码。
	* 本地UI组件：使用Xamarin Native UI组件创建视图，这些组件通过Xamarin.Forms编译为特定于平台的UI组件，Xamarin.Forms包含面向.NET开发者的完整跨平台UI工具包，或可以通过Native UI开发。
	* 插件和API：Xamarin提供了一组允许访问硬件功能的插件和API。它还支持通过链接本地库进行自定义。 
	* 测试：通过在物理设备上安装Xamarin.Forms Live Player应用，开发者可以使用实时预览立即测试和调试应用，并可以实时同步应用与设备。
	* 可靠性：Xamarin于2016年被微软收购，截至目前，已在120多个国家/地区拥有超过140万名开发者。所以它绝对可靠且拥有良好的维护。

	缺点
	* 应用大小：通常已知Xamarin应用大小比本地应用更大，因此在内存管理方面不是很理想。
	* 更新延迟：Xamarin的更新时间有时会比平台的更新更慢，无论是新功能的迭代还是其他，因此可能会导致应用出现一些问题。
	* 本地代码：当使用Xamarin.iOS或Xamarin.Android开发具有原生外观的移动应用时，将需要一些本地语言的基本知识，如Objective-C、Swift和Java。
	* 图形：虽然Xamarin使用单个代码库为多个平台构建应用，但它主要在平台之间共享代码逻辑，而UI组件又是特定于平台的。这使得Xamarin并不适合严重依赖图形的应用，比如手机游戏。


### 总结

|框架|厂家|JS框架|GitHub Star|  
|:--|:--|:--|:--|
|React Native|Facebook|React|70833|
|Flutter|Google||40998|
|Ionic|		|Angular|35787|
|Weex|阿里|Vue|17211|
|NativeScript|Telerik|Angular|15368|
|Cordova／PhoneGap|Apache|||
|Xamarin|微软|||

---



## 参考链接

* [Hybrid APP基础篇(一)->什么是Hybrid App](https://dailc.github.io/2016/10/04/hybridBase01HybridInfo.html)
* [Hybrid APP基础篇(二)->Native、Hybrid、React Native、Weex等方案的分析比较](https://dailc.github.io/2016/10/04/hybridBase02HybridCompareOthers.html)
* [什么是 Native、Web App、Hybrid、React Native 和 Weex？](https://cloud.tencent.com/developer/article/1182782)
* [浅谈 2018 移动端跨平台开发方案](https://kangzubin.com/2018-mobile-end-cross-platform-dev/)
* [移动端跨平台开发框架对比分析](https://www.jianshu.com/p/900bf9cbd005)
* [PWA 是否能弥补Web 劣势，带来新一轮大前端技术洗牌？](https://zhuanlan.zhihu.com/p/31373357)
* [Flutter 原理简解](https://juejin.im/entry/5afa9769518825428630a61c)
* [ionic hybrid app：产品还是玩具？](https://cloud.tencent.com/developer/article/1009398)
* [IonicHybrid跨终端应用程序开发方案研究](http://imweb.io/topic/557fea79c35b19ff46ead229)
* [WEEX wiki](https://weex.apache.org/cn/wiki/)
* [必须收藏丨万字长文，带你了解跨平台移动应用开发工具](https://zhuanlan.zhihu.com/p/47748270)
* [nativescript 中文文档](https://doc.yonyoucloud.com/doc/nativescript-book/welcome.html)
* [Xamarin 技术全解析](https://cloud.tencent.com/developer/article/1017263)
