//项目全局变量设置
import Vue from 'vue'
import App from './App.vue'
import router from './router'

//引入ElementUI
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI, {size: "mini"});

//引入axios
import request from "./utils/request";

//设置全局变量
Vue.prototype.request = request

//引入vuex
import axios from "axios";

Vue.config.productionTip = false

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')
