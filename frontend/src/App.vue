<script>
import sideNavComponent from './components/sideNav.vue';
import './api/axios-auth';
import axiosAuth from "@/api/axios-auth"  

export default {
    name: "App",
    created() {
        this.$watch('$route', () => {
            this.checkAuth();
        });
    },
    data() {
        return {
            showNav: false,
        };
    },
    methods: {
        checkAuth() {
            // Bypass login check if the environment variable is set
            if(process.env.VUE_APP_DISABLE_LOGIN !== undefined ? !JSON.parse(process.env.VUE_APP_DISABLE_LOGIN) : true) {
                // If the environment variable is not set, check the user's login status
                axiosAuth.post('/auth/verify-token')
                    .then(() => {
                        axiosAuth.get('/owner/current-is-owner').then(
                            response => {
                                if (response.status === 200) {
                                    this.showNav = false;
                                } else {
                                    this.showNav = true;
                                }
                            }
                        ).catch(() => {this.showNav = true;});
                    })
                    .catch(() => {
                        this.showNav = false;
                    });
                
            } else {
                this.showNav = true;
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
        <sideNavComponent v-if="showNav"/>
        <div class="navSpacer" v-if="showNav"></div>
        <div class="content">
            <router-view />
        </div>
    </div>
</template>

<style scoped></style>