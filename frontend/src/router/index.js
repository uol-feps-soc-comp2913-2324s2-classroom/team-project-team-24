import { createRouter, createWebHistory } from 'vue-router'

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
import ResetPassword from "@/views/ResetPassword.vue";
import UploadTrail from "@/views/UploadTrail.vue";
import OwnerPage from "@/views/OwnerPage.vue";
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
        path: '/welcome',
        name: 'Welcome',
        component: WelcomePage,
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
    },
    {
        path: '/register',
        name: 'Register',
        component: Register,
    },
    {
        path: '/apitest',
        name: 'API Tests',
        component: apiTests,
    },
    {
        path: '/activitycenter',
        name: 'Activity',
        component: ActivityCenter,
        meta: { requiresAuth: true, requiresMembership: true },
    },
    {
        path: '/community',
        name: 'Community',
        component: Community,
        meta: { requiresAuth: true, requiresMembership: true },
    },
    {
        path: '/membership',
        name: 'Membership',
        component: Membership,
        meta: { requiresAuth: authRequired },
    },
    {
        path: '/group',
        name: 'Group',
        component: MyGroup,
        meta: { requiresAuth: true, requiresMembership: true },
    },
    {
        path: '/myaccount',
        name: 'Account',
        component: MyAccount,
        meta: { requiresAuth: authRequired },
    },
    {
        path: '/mytrail',
        name: 'MyTrail',
        component: MyTrail,
        meta: { requiresAuth: true, requiresMembership: true },
    },
    {
        path: '/uploadtrail',
        name: 'UploadTrail',
        component: UploadTrail,
        meta: { requiresAuth: true, requiresMembership: true },
    },
    {
        path: '/resetpassword',
        name: 'ResetPassword',
        component: ResetPassword,
    },
    {
        path: '/stylingguide',
        name: 'StylingGuide',
        component: StylingGuide,
        meta: { requiresAuth: authRequired },
    },
    {
        path: '/owner',
        name: 'Owner',
        component: OwnerPage,
        meta: { requiresAuth: true, requiresOwner: true }
    },
]

const router = createRouter({
    history: createWebHistory('127.0.0.1:3000/'),
    routes,
})

router.beforeEach(async (to, from, next) => {
    let token = localStorage.getItem('token');
    let requireAuth = to.matched.some(record => record.meta.requiresAuth);
    let requireMembership = to.matched.some(record => record.meta.requiresMembership);
    let requireOwner = to.matched.some(record => record.meta.requiresOwner);
    
    var nextPage = '';
    if (to.path === '/'){
        nextPage = '/welcome';
    }
    if (to.path === '/login') {
        if (token) {
            await axiosAuth.post('/auth/verify-token').then(() => {
                nextPage = '/activitycenter';
            }).catch(() => {});
        }
    }
    
    // Rewrite
    if (requireAuth) {
        if (token) {
            await axiosAuth.post('/auth/verify-token').then(() => {
                
            }).catch(() => {
                console.log("catch");
                nextPage = '/login';
            })
        } else {
            nextPage = '/login';
        }
    }
    if (requireMembership) {
        await axiosAuth.get('/membership/get-current').then(
            response => {
                if (response.data.membership === null) {
                    nextPage = '/membership';
                }
            }
        ).catch(
            error => {
                if (error.response.status !== 200) {
                    nextPage = '/membership';
                }
            }
        )
    }
    if (requireOwner) {
        console.log("is maybe owner");
        await axiosAuth.get('/owner/current-is-owner').then(
            response => {
                if (response.status !== 200) {
                    nextPage = '/activitycenter';
                }
            }
        ).catch(error => {
            console.log(error);
            nextPage = '/activitycenter';
        });
    }
    
    console.log("next page: ", nextPage);
    if (nextPage === '') {
        next();
    } else {
        console.log(nextPage);
        next(nextPage);
    }
    

});

export default router
