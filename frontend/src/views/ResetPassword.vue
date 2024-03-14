<template>
    <div class="login-container">
        <h1 class="title">Reset Password</h1>
        <ResetPasswordFormComponent />
    </div>
    <br />
    <!-- <p>API Response: {{ APIResponse }}</p> -->
</template>

<script>
import ResetPasswordFormComponent from '@/components/forms/ResetPasswordForm.vue';

export default {
    name: "ResetPasswordView",
    data() {
        return {

        };
    },
    methods: {

    },
    components: {
        ResetPasswordFormComponent,
    },
};
</script>

<style scoped>
.title {
    margin-top: 5cm;
}

.login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    text-align: center;
}
</style>
