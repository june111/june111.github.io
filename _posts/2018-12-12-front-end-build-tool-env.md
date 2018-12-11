---
layout: post
title: '用 Flutter 开发APP（开发环境篇）'
subtitle: '移动端跨平台APP之项目实战 —— 用 Flutter 开发APP'
date: 2018-12-12
author: June
cover: /assets/img/post/2018-12-12/front-end-build-tool-env.png
tags: 前端
---

# 用 Flutter 开发APP（开发环境篇）

文章结构如图

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/structure.svg">
![文章结构]({{site.baseurl}}/assets/img/post/2018-12-12/structure.svg)
</a>

Flutter 终于出 1.0.0 稳定版了，让我们来尝尝鲜，做个交互功能少，注重展示的app吧。

这篇是环境篇，开发篇：

[]()

## 安装 Flutter

去Flutter官网下载其最新可用的安装包，[跳去下载页](https://flutter.io/sdk-archive/#macos)。

下载完成后解压压缩包。
```bash
# 切到根目录
cd 
# 新建.bash_profile，如果已存在则直接打开该文件
touch .bash_profile 
# 打开.bash_profile
open .bash_profile
```

添加临时镜像
```html
export PUB_HOSTED_URL=https://pub.flutter-io.cn
export FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn
```
将flutter命令写进环境变量
```html
export FLUTTER_HOME=/你的flutter安装目录/flutter
export PATH=$PATH:$FLUTTER_HOME/bin:
```
把以上4行代码加入 .bash_profile 文件，保存。

```bash
# 编译
source .bash_profile
```

运行flutter doctor来安装其他依赖
```bash
flutter doctor
```

## 初始化项目

创建项目
```bash
flutter create myapp
```
进入项目
```bash
cd myap
```

## 平台设置

### iOS 设置

#### 安装 Xcode

要为iOS开发 Flutter 应用程序，需要 Xcode 9.0 或更高版本。如果要适配 iOS 12+，则要求Xcode 10.0 或更高版本。

配置 Xcode 命令行工具以使用新安装的Xcode版本 
```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
```
确保 Xcode 许可协议是通过打开一次Xcode或通过命令`sudo xcodebuild -licens`同意过了.

使用 Xcode，可以在iOS设备或模拟器上运行Flutter应用程序。

#### 设置iOS模拟器

要准备在iOS模拟器上运行并测试 Flutter 应用，请按以下步骤操作：

在Mac上，通过Spotlight或使用以下命令找到(打开)模拟器:
```bash
open -a Simulator
```
通过检查模拟器 硬件 > 设备 菜单中的设置，确保模拟器正在使用64位设备（iPhone 5s或更高版本）.

根据开发机器的屏幕大小，模拟的高清屏iOS设备可能会使屏幕溢出。在模拟器的 Window> Scale 菜单下设置设备比例

运行项目
```bash
flutter run
```
项目会在模拟器中自动安装，然后运行

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/sim-run.png">
![模拟器中运行项目]({{site.baseurl}}/assets/img/post/2018-12-12/sim-run.png)
</a>


#### 安装到iOS设备

要将 Flutter 应用安装到iOS真机设备，需要一些额外的工具和一个 Apple 帐户，还需要在Xcode中进行设置。

1. 安装 homebrew （如果已经安装了brew,跳过此步骤）.
2. 打开终端并运行这些命令来安装用于将Flutter应用安装到iOS设备的工具

```bash
 brew update
 # The following two steps are a temporary workaround to https://github.com/flutter/flutter/issues/22595
 brew install --HEAD usbmuxd
 brew link usbmuxd
 brew install --HEAD libimobiledevice
 brew install ideviceinstaller ios-deploy cocoapods
 pod setup
```

##### 遵循Xcode签名流程来配置项目

1. 在项目目录中打开默认的Xcode workspace.

	```bash
	open ios/Runner.xcworkspace 
	```

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/open-xcode.png">
	![自动打开Xcode]({{site.baseurl}}/assets/img/post/2018-12-12/open-xcode.png)
	</a>

2. 在Xcode中，选择导航面板左侧中的`Runner`项目

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/select-run.png">
	![选择Runner]({{site.baseurl}}/assets/img/post/2018-12-12/select-run.png)
	</a>

3. 要开始第一个iOS开发项目，可能需要使用Apple ID登录Xcode.

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/login-xcode.png">
	![登录Xcode]({{site.baseurl}}/assets/img/post/2018-12-12/login-xcode.png)
	</a>

4. 将iOS设备连接到Mac

	第一次attach真机设备进行iOS开发时，需要同时信任你的Mac和该设备上的开发证书。首次将iOS设备连接到 Mac 时,请在对话框中选择 Trust。

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/trust-computer.png">
	![信任设备]({{site.baseurl}}/assets/img/post/2018-12-12/trust-computer.png)
	</a>

5. 确认Xcode中的设备

	选择左上角的Runner，把设备切换为接入的iOS设备。

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/switch-device.png">
	![信任设备]({{site.baseurl}}/assets/img/post/2018-12-12/switch-device.png)
	</a>

6. 如果Xcode中的自动签名失败，请验证项目的 General > Identity > Bundle Identifier 值是否唯一。检测通过后，Xcode会自动签名成功。

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/check-id.png">
	![检查 Bundle Identifier]({{site.baseurl}}/assets/img/post/2018-12-12/check-id.png)
	</a>

7. 适配高版本iOS

	如果出现以下报错，可能是 iOS 版本太高，Xcode 不兼容。我的 Xcode 是 9.2 的，只支持到 11.2。更新 Xcode 到 10.1，才能支持到12.1。Xcode 到10.1要求 macOS 系统 10.13.6+，所以也要升级系统。我把系统升级到了 macOS Mojave(10.14.2)

	```bash
	Unable to locate DeviceSupport directory with suffix 'DeveloperDiskImage.dmg'.
	```

8. 信任 App

	进入手机 设置 > 设备管理 > 开发者应用。点击信任XXX。

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/trust.png">
	![信任应用]({{site.baseurl}}/assets/img/post/2018-12-12/trust.png)
	</a>

9. 运行项目

	```bash
	flutter run
	```
	第一次构建会要求输入密码。输入密码后选择始终允许，否则弹窗会一直存在。

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/password.png">
	![输入密码]({{site.baseurl}}/assets/img/post/2018-12-12/password.png)
	</a>

### Android设置

#### 安装Android Studio

下载并安装 [Android Studio](https://developer.android.com/studio).

启动Android Studio，然后执行“Android Studio安装向导”。这将安装最新的Android SDK，Android SDK平台工具和Android SDK构建工具，这是Flutter为Android开发时所必需的

下面展示一下我的Android Studio安装向导，其实不用设置，打开的时候注意不要点代理就可以。

这步点取消，不要点设置代理。
<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/open-1.png">
![打开Android Studio]({{site.baseurl}}/assets/img/post/2018-12-12/open-1.png)
</a>

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/intro-1.png">
![向导1]({{site.baseurl}}/assets/img/post/2018-12-12/intro-1.png)
</a>

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/intro-2.png">
![向导2]({{site.baseurl}}/assets/img/post/2018-12-12/intro-2.png)
</a>

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/intro-3.png">
![向导3]({{site.baseurl}}/assets/img/post/2018-12-12/intro-3.png)
</a>

安装期间会让输入密码。下图为安装完成。

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/intro-4.png">
![向导4]({{site.baseurl}}/assets/img/post/2018-12-12/intro-4.png)
</a>

导入项目

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/import-a.png">
![导入项目]({{site.baseurl}}/assets/img/post/2018-12-12/import-a.png)
</a>

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/import-b.png">
![导入项目完成]({{site.baseurl}}/assets/img/post/2018-12-12/import-b.png)
</a>

需要 Flutter 下载插件，下载完成后按编辑器提示进行重启

<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/download-f.png">
![下载插件]({{site.baseurl}}/assets/img/post/2018-12-12/download-f.png)
</a>

#### 设置Android模拟器

要准备在Android模拟器上运行并测试Flutter应用，请按照以下步骤操作：

1. 启动 Android Studio>Tools>Android>AVD Manager 并选择 Create Virtual Device.

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/create-d.png">
	![新建设备]({{site.baseurl}}/assets/img/post/2018-12-12/create-d.png)
	</a>

2. 选择一个设备并选择 Next。

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/select-device.png">
	![选择设备]({{site.baseurl}}/assets/img/post/2018-12-12/select-device.png)
	</a>

3. 为要模拟的Android版本选择一个或多个系统映像，然后选择 Next. 建议使用 x86 或 x86_64 image .

	选择系统映像

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/download-image.png">
	![选择系统映像]({{site.baseurl}}/assets/img/post/2018-12-12/download-image.png)
	</a>

	下载系统映像

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/download-image-2.png">
	![下载系统映像]({{site.baseurl}}/assets/img/post/2018-12-12/download-image-2.png)
	</a>

	下载系统映像完成

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/download-image-3.png">
	![下载系统映像完成]({{site.baseurl}}/assets/img/post/2018-12-12/download-image-3.png)
	</a>

4. 验证AVD配置是否正确，然后选择 Finish。

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/download-image-4.png">
	![设置设备名称]({{site.baseurl}}/assets/img/post/2018-12-12/download-image-4.png)
	</a>

	有关上述步骤的详细信息，请参阅 [Managing AVDs](https://developer.android.com/studio/run/managing-avds).

5. 在 Android Virtual Device Manager中, 点击工具栏的 Run。模拟器启动并显示所选操作系统版本或设备的启动画面.

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/start-app.png">
	![启动app]({{site.baseurl}}/assets/img/post/2018-12-12/start-app.png)
	</a>

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/start-app-2.png">
	![启动app]({{site.baseurl}}/assets/img/post/2018-12-12/start-app-2.png)
	</a>

6. 检查环境，看有没有缺少的东西。
	```bash
	flutter doctor
	```

	我的缺了一条
	```bash
	[!] Android toolchain - develop for Android devices (Android SDK 28.0.3)
    ! Some Android licenses not accepted.  To resolve this, run: flutter doctor
      --android-licenses
	```

	意思是缺少许可认证，运行以下命令，然后一直输入y和回车，就可以了。
	```bash
	flutter doctor  --android-licenses
	```

7. 启动 App

	运行 `flutter run` 启动设备. 连接的设备名是` Android SDK built for <platform>`,其中 platform 是芯片系列, 如 x86. 

	也可以点击 Android Studio 菜单栏的启动按钮，启动 App。

	<a data-fancybox="gallery" href="{{site.baseurl}}/assets/img/post/2018-12-12/start-menu.png">
	![菜单栏启动app]({{site.baseurl}}/assets/img/post/2018-12-12/start-menu.png)
	</a>

#### 设置Android设备

要准备在Android设备上运行并测试 Flutter 应用，需要安装 Android 4.1（API level 16）或更高版本的Android设备.

1. 在设备上启用***开发人员选项***和***USB调试***。详细说明可在[Android](https://developer.android.com/studio/debug/dev-options.html)文档中找到。

2. 使用USB将手机插入电脑。如果设备出现提示，请授权计算机访问设备。

3. 在终端中，运行 `flutter devices` 命令以验证Flutter识别所连接的Android设备。

	要确保只有一个设备连接到电脑。如果开了模拟器，则要关闭模拟器。

4. 运行启动应用程序 `flutter run`。

	需要在手机上点击允许安装app。

默认情况下，Flutter 使用的 Android SDK 版本是基于你的 `adb` 工具版本。 如果想让 Flutter 使用不同版本的 Android SDK，则必须将该 `ANDROID_HOME` 环境变量设置为SDK安装目录。

---

觉得文章不错就扫码支持一下呗～

![打赏二维码]({{site.baseurl}}/assets/img/post/pay-qr.jpg)

## 参考链接

* [flutter 官方文档](https://flutter.io/docs/get-started/install/macos)
* [flutter 中文文档](https://flutterchina.club/setup-macos/)
