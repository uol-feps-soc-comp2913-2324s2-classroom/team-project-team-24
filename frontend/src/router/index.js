import { createRouter, createWebHistory } from "vue-router";

import WelcomePage from "../views/Welcome.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import apiTests from "../views/apiTests.vue";
import ActivityCenter from "../views/ActivityCenter.vue";
import Community from "../views/Community.vue";
import Membership from "../views/Membership.vue";
import MyAccount from "../views/MyAccount.vue";
import MyTrail from "../views/MyTrail.vue";
import StylingGuide from "../views/StylingGuide.vue";
import MyGroup from "@/views/Group.vue";
import UploadTrail from "@/views/UploadTrail.vue";
import axiosAuth from "@/api/axios-auth";

// Defines a variable using environment variables to disable
// logins for development purposes.
// Checks if environment variable VUE_APP_DISABLE_LOGIN exists
// If it exists takes its boolean value to disable or enable login
// Defaults to true if the variable doesn't exist (requiring login)
const authRequired =
  process.env.VUE_APP_DISABLE_LOGIN !== undefined
    ? !JSON.parse(process.env.VUE_APP_DISABLE_LOGIN)
    : true;
console.log(process.env.VUE_APP_DISABLE_LOGIN);

const routes = [
    {
        path: "/welcome",
        name: "Welcome",
        component: WelcomePage,
        meta: {
            title: 'Welcome to Walkley'
        }
    },
    {
        path: "/login",
        name: "Login",
        component: Login,
        meta: {
            title: 'Login'
        }
    },
    {
        path: "/register",
        name: "Register",
        component: Register,
        meta: {
            title: 'Register'
        }
    },
    {
        path: "/apitest",
        name: "API Tests",
        component: apiTests,
        meta: {
            title: 'API tests'
        }
    },
    {
        path: "/activitycenter",
        name: "Activity",
        component: ActivityCenter,
        meta: { requiresAuth: true, requiresMembership: true, title: 'Activity Center' },
        
    },
    {
        path: "/community",
        name: "Community",
        component: Community,
        meta: { requiresAuth: true, requiresMembership: true, title: 'Community' },
    },
    {
        path: "/membership",
        name: "Membership",
        component: Membership,
        meta: { requiresAuth: authRequired, title: 'Buy a membership' },
    },
    {
        path: "/group",
        name: "Group",
        component: MyGroup,
        meta: { requiresAuth: true, requiresMembership: true , title: 'Groups'},
    },
    {
        path: "/myaccount",
        name: "Account",
        component: MyAccount,
        meta: { requiresAuth: authRequired, title: 'Account Details' },
    },
    {
        path: "/mytrail",
        name: "MyTrail",
        component: MyTrail,
        meta: { requiresAuth: true, requiresMembership: true, title: 'Trail Info' },
    },
    {
        path: "/uploadtrail",
        name: "UploadTrail",
        component: UploadTrail,
        meta: { requiresAuth: true, requiresMembership: true, title: 'Upload a trail' },
    },
    {
        path: "/stylingguide",
        name: "StylingGuide",
        component: StylingGuide,
        meta: { requiresAuth: authRequired, title: 'Styling Guide' },
    },
]

const router = createRouter({
    history: createWebHistory("127.0.0.1:3000/"),
    routes,
})

router.beforeEach((to, from, next) => {
    // Check if the route has a meta field and a title in it
    if (to.meta.title) {
        document.title = to.meta.title; // Set the page title based on the route's meta title
    } else {
        document.title = 'Walkley'; // Set a default title if the route doesn't have a meta title
    }
    let token = localStorage.getItem('token');
    let requireAuth = to.matched.some(record => record.meta.requiresAuth);
    let requireMembership = to.matched.some(record => record.meta.requiresMembership);
    if (to.path === '/'){
        next('/welcome');
    }
    if (to.path === '/login') {
        if (token) {
            axiosAuth.post('/auth/verify-token').then(() => {
                next('/activitycenter');
            }).catch(() => {});
        }
    }
    
    if (!requireAuth && !requireMembership) {
        next();
    }

    else if (requireAuth && !token) {
        next('/login');
    }

    else if (requireAuth && token && !requireMembership) {
        axiosAuth.post('/auth/verify-token').then(() => {
            next();
        }).catch(() => {
            next('/login');
        })
    }
    else if (requireAuth && token && requireMembership) {
        axiosAuth.post('/auth/verify-token').then(() => {
            axiosAuth.get('/membership/get-current').then(
                response => {
                    if (response.data.membership !== null) {
                        next();
                    } else {
                        next('/membership');
                    }
                }
            ).catch(
                error => {
                    if (error.response.status !== 200) {
                        next('/membership');
                    }
                }
            )
        }).catch(() => {
            next('/login');
        })
    }

});

export default router
