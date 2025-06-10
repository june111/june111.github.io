/* 
可以让 deepseek 等大模型实现css，实现卡片样式自定义，以下是发送的提示词模板：

我需要在 md2card.com 实现自定义微信公众号样式
以下是 md2card.com 中卡片的HTML结构：
```html
<div class="card">
  <div class="card-header"></div>
  <div class="card-content">
    <div class="card-content-inner">
      <h1 data-text="标题">标题</h1>
      <h2 data-text="标题二">标题二</h2>
      <h3 data-text="标题三">标题三</h2>
      <h4 data-text="标题四">标题四</h2>
      <h5 data-text="标题五">标题五</h2>
      <p>内容</p>
      <ol>
        <li data-index="0">列表</li>
      </ol>
    </div>
  </div>
  <div class="card-footer"></div>
</div>
```
`card-content-inner` 为 markdown 编译后的内容区域，还包括标题、列表、引用、代码、加粗等常见 markdown 编译的内容

请为我设计一个微信公众号的内容排版样式，其风格为"简约现代"，可以进一步融入"留白"的设计理念，应用"分享"的场景
【设计风格要求】：简约、大气、层次分明、高亮明显，紫色
【输入要求】：只需要返回 css 代码
 */
/* 有序列表样式优化 */

.card {
  width: 100%;
  max-width: 600px;
  margin: 40px auto;
  border-radius: 16px;
  background: #ffffff;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
  color: #333333;
  box-sizing: border-box;
  padding: 20px;

}

/* 卡片头尾留白 */
.card-header,
.card-footer {
  height: 24px;
}

/* 主体内容 */
.card-content-inner {
  line-height: 1.8;
  font-size: 16px;
  color: #333;
}

/* 标题样式 */
.card-content-inner h1 {
  font-size: 32px;
  font-weight: 700;
  color: #333333;
  margin: 36px 0 24px;
  line-height: 1.4;
  padding: 16px 20px;
  position: relative;
  background: linear-gradient(to right, rgba(91, 60, 196, 0.08), rgba(140, 111, 230, 0.02));
  border-radius: 8px;
}

.card-content-inner h1::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 6px;
  background: linear-gradient(180deg, #5B3CC4, #8C6FE6);
  border-radius: 3px 0 0 3px;
}

.card-content-inner h2 {
  font-size: 24px;
  font-weight: 600;
  color: #5B3CC4;
  margin: 32px 0 20px;
  line-height: 1.5;
  padding: 0 31px;
  text-align: center;
  display: inline-block;
  position: relative;
  letter-spacing: 0.02em;
  box-sizing: border-box;
  width: fit-content;
  left: 50%;
  transform: translateX(-50%);
}

.card-content-inner h2::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 31px;
  right: 31px;
  height: 1px;
  background: linear-gradient(90deg, 
    rgba(140, 111, 230, 0) 0%,
    rgba(140, 111, 230, 0.6) 20%,
    rgba(91, 60, 196, 1) 50%,
    rgba(140, 111, 230, 0.6) 80%,
    rgba(140, 111, 230, 0) 100%
  );
}

/* Remove the previous left border style for h2 */
.card-content-inner h2::before {
  display: none;
}

/* Remove the wrapper since we don't need it anymore */
.card-content-inner h2-wrapper {
  display: none;
}

.card-content-inner h3 {
  font-size: 20px;
  font-weight: 600;
  color: #5B3CC4;
  margin: 24px 0 16px;
  line-height: 1.4;
  padding: 0 0 8px 0;
  position: relative;
  display: block;
  width: 100%;
  box-sizing: border-box;
}

.card-content-inner h3::before {
  display: none;
}

.card-content-inner h3::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 80px;
  height: 3px;
  background: linear-gradient(90deg, 
    #5B3CC4 0%,
    #8C6FE6 50%,
    rgba(140, 111, 230, 0) 100%
  );
  border-radius: 1.5px;
}

.card-content-inner h4 {
  font-size: 17px;
  font-weight: 600;
  color: #5B3CC4;
  margin: 2px 0;
  line-height: 1.3;
  padding: 0 0 0 9px;
  position: relative;
  border-left: 5px solid #5B3CC4;
  display: inline-block;
  width: auto;
  vertical-align: top;
  min-width: 10%;
  max-width: 100%;
  box-sizing: border-box;
  align-self: flex-start;
}

/* Remove previous h4 border style */
.card-content-inner h4::before {
  display: none;
}

.card-content-inner h5 {
  font-size: 17px;
  font-weight: 600;
  color: #666666;
  margin: 20px 0 12px;
  line-height: 1.4;
  padding: 0 0 0 12px;
  position: relative;
}

/* 段落 */
.card-content-inner p {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  line-height: 1.9;  /* 增加行高 */
  font-size: 16px;
  color: #444;
  margin-bottom: 0em;  /* 段落之间的间距 */
}

.card-content-inner p span {
  display: inline;
  line-height: inherit;
}

/* 加粗强调 */
.card-content-inner strong {
  font-weight: 600;
  color: #5B3CC4;
}

/* 有序列表样式 */
.card-content-inner ol {
  list-style: none;
  padding-left: 0;
  margin: 0.5em 0;
  counter-reset: custom-counter;
}

.card-content-inner ol > li {
  position: relative;
  margin: 0;
  color: #333;
  line-height: 1.9;
  counter-increment: custom-counter;
  padding-left: 28px;
}

/* 隐藏原生prefix */
.card-content-inner ol > li .prefix {
  display: none;
}

/* 内容区域样式 */
.card-content-inner ol > li section {
  position: relative;
}

/* 自定义数字样式 */
.card-content-inner ol > li::before {
  content: counter(custom-counter);
  position: absolute;
  left: 0;
  top: 0.4em;
  width: 22px;
  height: 22px;
  color: #ffffff;
  font-weight: 500;
  font-size: 13px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-feature-settings: "tnum";
  background: #5B3CC4;
  border-radius: 50%;
}

/* 嵌套有序列表样式 */
.card-content-inner ol ol {
  counter-reset: custom-counter;  /* 重置嵌套列表的计数器 */
  margin: 0;
  padding-left: 1em;
}

/* 无序列表样式 */
.card-content-inner ul {
  list-style: none;
  padding-left: 0;
  margin: 8px 0;
}

.card-content-inner li ul {
  margin-top: 4px;
  margin-bottom: 4px;
  padding-left: 0px;
}

/* 二级列表缩进 */
.card-content-inner ul ul {
  padding-left: 0px;
}

/* 三级列表缩进 */
.card-content-inner ul ul ul {
  padding-left: 2px;
}

.card-content-inner ul > li {
  position: relative;
  padding-left: 10px;
  margin: 3px 0;
  color: #444;
  line-height: 1.9;
  list-style-type: none !important;
}

/* 简洁的无序列表标记 */
.card-content-inner ul > li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0.8em;
  width: 5px;
  height: 5px;
  background-color: #8C6FE6;
  border-radius: 2px;
  transform: rotate(45deg);
}

/* 二级列表标记样式 */
.card-content-inner ul ul > li::before {
  background-color: #B4A1F0;
  width: 4px;
  height: 4px;
  left: 0;
  top: 0.8em;
}

/* 三级列表标记样式 */
.card-content-inner ul ul ul > li::before {
  background-color: #D4C7F6;
  width: 4px;
  height: 4px;
  left: 0;
  top: 0.8em;
}

/* 引用块 */
.card-content-inner blockquote {
  border-left: 4px solid #D4C7F6;
  background: #FAF9FE;
  padding: 12px 16px;
  margin: 16px 0;
  color: #555;
  font-style: italic;
  border-radius: 6px;
}

/* 代码块 */
.card-content-inner pre {
  background: #F3F2FA;
  padding: 12px 16px;
  border-radius: 8px;
  overflow-x: auto;
  font-family: 'Courier New', Courier, monospace;
  font-size: 14px;
  color: #5E5C6C;
  margin: 16px 0;
}

/* 行内代码 */
.card-content-inner code {
  background: #F0EBFA;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: 'Courier New', Courier, monospace;
  font-size: 14px;
  color: #6C4BC1;
}
