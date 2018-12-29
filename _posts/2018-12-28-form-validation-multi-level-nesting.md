---
layout: post
title: 'Vue ElementUI 表单校验（多层嵌套）'
date: 2018-12-28
author: June
cover: /assets/img/post/2018-12-28/form-validation-multi-level-nesting.png
tags: 前端
---

# Vue ElementUI 表单校验（多层嵌套）

如果表单对象里面又嵌套了一个对象，按照 ElementUI 文档里面的例子，会出现验证错误的提示，解决方法是在 rules 的 key 要和 prop 中的值相同。

```vue
<el-form :model="postForm" :rules="rules" ref="postForm">
  <el-form-item :label-width="formLabelWidth" label="活动">
    <el-radio-group v-model="postForm.isActivity">
      <el-radio :label="0">否</el-radio>
      <el-radio :label="1">是</el-radio>
    </el-radio-group>
  </el-form-item>
  <el-form-item :label-width="formLabelWidth" label="活动简介" prop="activity.content">
    <tinymce :height=150 v-model="postForm.activity.content"></tinymce>
  </el-form-item>
</el-form>
<script>
export default {
  data() {
    return {
      postForm: {
        isActivity: 0,
        activity: {
          content: ''
        }
      },
      rules: {
        isActivity: [{ required: true, message: 'required', trigger: 'blur' }],

        'activity.content': [{ required: true, message: 'required', trigger: 'blur' }],

      }
    }
  }
}
</script>
```

---

觉得文章不错就扫码支持一下呗～

![打赏二维码]({{site.baseurl}}/assets/img/post/pay-qr.jpg)

