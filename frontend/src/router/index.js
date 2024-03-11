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
import axiosAuth from "@/api/axios-auth"

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
        meta: { requiresAuth: true}
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

router.beforeEach((to, from, next) => {
	let token = localStorage.getItem('token');
	let requireAuth = to.matched.some(record => record.meta.requiresAuth);

	if (!requireAuth) {
		next();
	}

	if (requireAuth && !token) {
		next('/login');
	}

	if (to.path === '/login') {
		if (token) {
			axiosAuth.post('/auth/verify-token').then(() => {
				next('/activitycenter');
			}).catch(() => {
				next();
			});
		}
		else {
			next();
		}
	}

	if (requireAuth && token) {
		axiosAuth.post('/auth/verify-token').then(() => {
			next();
		}).catch(() => {
			next('/login');
		})
	}
});

export default router
