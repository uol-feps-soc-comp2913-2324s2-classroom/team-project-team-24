import { createRouter, createWebHistory } from "vue-router";

//import App from "../App.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import apiTests from "../views/apiTests.vue";
import ActivityCenter from "../views/ActivityCenter.vue";
import Community from "../views/Community.vue";
import Membership from "../views/Membership.vue";
import MyAccount from "../views/MyAccount.vue";
import MyTrail from "../views/MyTrail.vue";

const routes = [
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
    {
        path: "/activitycenter",
        name: "Activity",
        component: ActivityCenter,
    },
    {
        path: "/community",
        name: "Community",
        component: Community,
    },
    {
        path: "/membership",
        name: "Membership",
        component: Membership,
    },
    {
        path: "/myaccount",
        name: "Account",
        component: MyAccount,
    },
    {
        path: "/mytrail",
        name: "MyTrail",
        component: MyTrail,
    },
]

const router = createRouter({
    history: createWebHistory("127.0.0.1:3000/"),
    routes,
})

export default router
