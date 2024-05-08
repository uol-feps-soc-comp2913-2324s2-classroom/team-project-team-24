<script>
import sideNavComponent from './components/sideNav.vue'
import './api/axios-auth'
import axiosAuth from '@/api/axios-auth'

export default {
    name: 'App',
    created() {
        this.$watch('$route', () => {
            this.checkAuth()
        })
    },
    data() {
        return {
            showNav: false,
            contentStyle: {
                height: "100vh",
            },
        }
    },
    methods: {
        calculateContentHeight() {
            const navSpacerHeightMobile = document.getElementById(
                'mobileNavSpacerElement'
            ).clientHeight
            this.contentStyle.height =
                window.innerHeight - navSpacerHeightMobile + 'px'
        },
        checkAuth() {
            // Bypass login check if the environment variable is set
            if (
                process.env.VUE_APP_DISABLE_LOGIN !== undefined
                    ? !JSON.parse(process.env.VUE_APP_DISABLE_LOGIN)
                    : true
            ) {
                // If the environment variable is not set, check the user's login status
                axiosAuth
                    .post('/auth/verify-token')
                    .then(() => {
                        axiosAuth
                            .get('/owner/current-is-owner')
                            .then((response) => {
                                if (response.status === 200) {
                                    this.showNav = false
                                } else {
                                    this.showNav = true
                                    if (
                                        this.$route.name == 'Welcome' ||
                                        this.$route.name == 'login' ||
                                        this.$route.name == 'Register'
                                    ) {
                                        this.showNav = false
                                    }
                                }
                            })
                            .catch(() => {
                                this.showNav = true
                                if (
                                    this.$route.name == 'Welcome' ||
                                    this.$route.name == 'login' ||
                                    this.$route.name == 'Register'
                                ) {
                                    this.showNav = false
                                }
                            })
                    })
                    .catch(() => {
                        this.showNav = false
                    })
            } else {
                this.showNav = true
            }
        },
    },
    components: {
        sideNavComponent,
    },
    mounted() {
        document.documentElement.setAttribute('lang', 'en')
        this.checkAuth()
    },
    updated() {
        if (window.innerWidth < 600 && this.showNav) {
            this.$nextTick(() => {
                this.calculateContentHeight()
            })
        }
    },
}
</script>

<template>
    <div class="main" id="mainElement">
        <sideNavComponent v-if="showNav" />
        <div class="navSpacer" v-if="showNav"></div>
        <div class="content" id="contentContainer" :style="contentStyle">
            <router-view />
            <div class="mobileNavSpacer" v-if="showNav" id="mobileNavSpacerElement"></div>
        </div>
    </div>
</template>

<style scoped>
@media (max-width: 480px) {
    .content {
        overflow-y: hidden;
        overflow-x: hidden;
    }
}

</style>
