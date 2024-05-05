<template>
    <div class="login-container">
        <h2 class="title"><b>Login</b></h2>
        <LoginFormComponent />
    </div>
    <br />
</template>

<script>
import LoginFormComponent from '@/components/forms/LoginForm.vue'
import axiosAuth from '@/api/axios-auth.js'

export default {
    name: 'LoginView',
    data() {
        return {}
    },
    methods: {
        async autoLogin() {
            let token = localStorage.getItem('token');
            if (token) {
                axiosAuth.post('/auth/verify-token').then(() => {
                    axiosAuth.get('/owner/current-is-owner').then(
                        response => {
                            if (response.status == 200) {
                                this.$router.push('/owner');
                            } else {
                                this.$router.push('/activitycenter');
                            }
                        }
                    ).catch(() => {this.$router.push('/activitycenter')});
                }).catch(() => {});
            }
        }
    },
    components: {
        LoginFormComponent,
    },
    created() {
        this.autoLogin();
    }
}
</script>

<style scoped>
.title {
    color: #333;
    margin-bottom: 30px;
    text-align: left;
    margin-top: 40px;
    margin-left: 45px;
}

.login-container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
}
</style>
