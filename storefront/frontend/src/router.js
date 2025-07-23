import { createRouter, createWebHistory } from "vue-router";
import Home from "@/pages/HomePage.vue";
import Detail from "@/pages/DetailPage.vue";
// import { create } from "core-js/core/object";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/', name: 'home', component: Home},
        {path: '/product/:id', name: 'detail', component: Detail}
    ],
    linkActiveClass: 'active'
})

export default router;