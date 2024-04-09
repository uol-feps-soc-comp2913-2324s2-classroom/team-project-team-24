<template>
    <div class="login-container">
        <h2 class="title"><b>Reset Password</b></h2>
        <ResetPasswordFormComponent />
    </div>
    <br />
    <!-- <p>API Response: {{ APIResponse }}</p> -->
</template>

<script>
import ResetPasswordFormComponent from '@/components/forms/ResetPasswordForm.vue'

export default {
    name: 'ResetPasswordView',
    data() {
        return {}
    },
    methods: {},
    components: {
        ResetPasswordFormComponent,
    },
}
</script>

<style scoped>
.title {
    color: #333;
    margin-top: 10px;
    margin-left: 30px;
}

.login-container {
    max-width: 600px;
    margin: 70px auto;
    padding: 40px;
    background: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
}
</style>
