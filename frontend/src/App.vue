<script>
import sideNavComponent from './components/sideNav.vue';
import './api/axios-auth';
import axiosAuth from "@/api/axios-auth"  

export default {
    name: "App",
    created() {
        this.$store.dispatch('auth/autoLogin');
        this.$watch('$route', () => {
            this.checkAuth();
        });
    },
    data() {
        return {
            isLoggedIn: false,
        };
    },
    methods: {
        checkAuth() {
            // Bypass login check if the environment variable is set
            if(process.env.VUE_APP_DISABLE_LOGIN !== undefined ? !JSON.parse(process.env.VUE_APP_DISABLE_LOGIN) : true) {
                // If the environment variable is not set, check the user's login status
                axiosAuth.post('/auth/verify-token')
                    .then(() => {
                        this.isLoggedIn = true;
                    })
                    .catch(() => {
                        this.isLoggedIn = false;
                    });
            } else {
                this.isLoggedIn = true;
            }
        }
    },
    components: {
        sideNavComponent,
    },
    mounted() {
        this.checkAuth();
    },
};
</script>

<template>
    <div class="main" id="mainElement">
        <sideNavComponent v-if="isLoggedIn"/>
        <div class="navSpacer" v-if="isLoggedIn"></div>
        <div class="content">
            <router-view />
        </div>
    </div>
</template>

<style scoped></style>