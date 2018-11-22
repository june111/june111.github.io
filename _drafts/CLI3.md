
# 初探CLI3(3.0.1)

CLI 3全局安装

	sudo npm install -g @vue/cli

创建一个项目

	sudo vue create june-web


	Vue CLI v3.0.1
	? Please pick a preset: Manually select features
	? Check the features needed for your project: Babel, Router, CSS Pre-processor
	s, Linter
	? Use history mode for router? (Requires proper server setup for index fallbac
	k in production) Yes
	? Pick a CSS pre-processor (PostCSS, Autoprefixer and CSS Modules are supporte
	d by default): SCSS/SASS
	? Pick a linter / formatter config: Standard
	? Pick additional lint features: Lint on save
	? Where do you prefer placing config for Babel, PostCSS, ESLint, etc.? In dedi
	cated config files
	? Save this as a preset for future projects? Yes
	? Save preset as: cli3-june
	? Pick the package manager to use when installing dependencies: YARN

如果说检查npm速度慢，是否换成淘宝镜象，一定要选否，否则可能报错
``` bash
command failed: npm install --loglevel error --registry=https://registry.npm.taobao.org --disturl=https://npm.taobao.org/dist
```

就到用户的 home 目录下一个名为 .vuerc 的 JSON 文件，把"useTaobaoRegistry": true, 改为 false.


之前选择包管理用YARN，改为npm

``` bash
cd /Users/<用户名>/.vuerc
```
"packageManager": "yarn" 改为 "packageManager": "npm"


 Use history mode，后端要做相应的配置，否则会显示404。具体参考：
[HTML5 History 模式](https://cli.vuejs.org/zh/)

进入目录
 $ cd june-web

 运行项目
 $ yarn serve

加vuetify
vue add vuetify

配置信息

	? Use a pre-made template? (will replace App.vue and HelloWorld.vue) No
	? Use custom theme? Yes
	? Use a-la-carte components? No
	? Use babel/polyfill? Yes










##参考
[开发手册](https://cli.vuejs.org/zh/)
[webpack中的重要设置](https://blog.csdn.net/weixin_41892205/article/details/80960441)
[vue-cli3.0使用及配置（部分）](https://blog.csdn.net/qq_36407748/article/details/80739787)
[vue新vue-cli3环境配置和模拟json数据](https://blog.csdn.net/lfcss/article/details/81055847)
[vue.config.js](https://github.com/vuejs/vue-docs-zh-cn/blob/master/vue-cli/config.md)
[CLI 服务](https://github.com/vuejs/vue-docs-zh-cn/blob/master/vue-cli/cli-service.md#)
