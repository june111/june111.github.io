```js
   //判断网站语言
    var lang, para, scheduleContent, PayPalLang;

    var browser = {
        language: (navigator.browserLanguage || navigator.language).toLowerCase() //'zh-cn'or 'en'
    }

    if (browser.language.includes('zh')) {
        lang = 'cn';
        PayPalLang = 'zh_CN'
        scheduleContent = 'journeyCN'
    } else {
        lang = 'en';
        PayPalLang = 'en_US'
        scheduleContent = 'journey'
    }

     top.location.pathname.includes('cn') 
```

watch不能用箭头函数，this指向会出错
```js

  watch: {
      // 如果路由有变化，会再次执行该方法
      "$route": "getList"
    }

      watch: {
    '$route': function() {
      this.getCategory()
      this.getList()
    }
  }
```




vue的模版

    <template>
      <div>
      </div>
    </template>
    <script>
    import HelloWorld from '@/components/Tinymce'
    export default {
      name: 'HelloWorld',
      components: { HelloWorld },
      data() {
        return {}
      },
      created() {},
      mounted: function () {
        this.$nextTick(function () {
          // Code that will run only after the
          // entire view has been rendered
        })
      },
      methods: {
      },
      watch: {
        '$route': function () {
        }
      }
    }
    </script>



vuex中的state在组件中如何监听

如何检测state中的数据变化, state 的值改变，组件的值要随之改变
vuex的dispatch是异步执行的，所以如果有用到state的地方但是又没有绑定组件的话就会导致渲染完成了但是数据没有获取到的情况 
在computed中写一个计算属性getUserIcons,返回状态管理中的userIcons。然后在watch中监听这个计算属性的变化，对modifyhost.vue中的userIcons重新赋值。


1.vue

    computed: {
        getUserIcons() {
            return this.$store.state.topo.userIcons;
        }
    },
    watch: {
        getUserIcons(val) {
            this.userIcons = val;
        }
    }


2.vue

  computed: {
    ...mapState({
      //读取点击买单列表后，相应行的数据
      Order: state => state.Order,
    }),
    ...mapGetters([
      'selectedCoinInfo'
    ])
  },
  watch: {

    /**
     * @description 监听买单列表行数据的变化
     * @description 把数据展示到发起交易模块
     * @Author   June
     * @DateTime 2018-09-05T09:57:38+0800
     */
    Order: function () {
      this.buyForm.buyNum = toNum(this.Order.tokenamount)
      this.buyForm.buyPrice = toNum(this.Order.ethprice)
      this.buyForm.buyOfferIDs = [this.Order.id]
      this.sellForm.sellNum = toNum(this.Order.tokenamount)
      this.sellForm.sellPrice = toNum(this.Order.ethprice)
      this.sellForm.sellOfferIDs = [this.Order.id]
    },

    /**
     * @description 监听所选的币种信息，改变代币地址
     * @description 重新获取挂单列表，交易记录列表
     要注意selectedCoinInfo不能是对象，要是值，才能监听到变化
     * @Author   June
     * @DateTime 2018-09-05T09:58:45+0800
     */
    selectedCoinInfo: function () {
      this.getOrderByAccount()
      this.getOrderHistoryByAccount()
    },

  },

store.js

    getters: {
      selectedCoinInfo: state => {
        return state.selectedCoinInfo;
      },
    }










