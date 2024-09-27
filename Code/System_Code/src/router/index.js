//路由文件

import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/filetest',
        name: 'filetest',
        component: () => import("../components/filetest.vue"),
        meta: {title: '测试'},
    },
    {
        path: '/test',
        name: 'test',
        component: () => import("../components/Test.vue"),
        meta: {title: '测试'},
    },
    {
        path: '/index',
        name: 'index',
        component: () => import("../components/Index.vue"),
        meta: {title: '主页'},
    },
    {
        path: '/header',
        name: 'header',
        component: () => import("../components/Header.vue"),
        meta: {title: '主页'},
    },
    {
        path: '/fileUpload',
        name: 'fileUpload',
        component: () => import("../components/FileUpload.vue"),
        meta: {title: '主页'},
    },
    {
        path: '/',
        name: 'home',
        component: () => import("../views/Home.vue"),
        meta: {title: '主页'},
    },
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router