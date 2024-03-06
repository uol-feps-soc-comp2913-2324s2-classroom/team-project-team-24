import { createRouter, createWebHistory } from "vue-router";

import App from "../App.vue";
import Login from "../components/Login.vue";
import Register from "../components/Register.vue";
import apiTests from "../components/apiTests.vue";

const routes = [
    {
        path: "/",
        name: "App",
        component: App,
    },
    {
        path: "/login",
        name: "Login",
        component: Login,
    },
    {
        path: "/register",
        name: "Register",
        component: Register,
    },
    {
        path: "/apitest",
        name: "API Tests",
        component: apiTests,
    },
]

const router = createRouter({
    history: createWebHistory("127.0.0.1:3000/"),
    routes,
})

export default router
