<template>
    <div class="login-container">
        <h1 class="title">Login to Your App</h1>
        <LoginFormComponent />
    </div>
    <br />
    <!-- <p>API Response: {{ APIResponse }}</p> -->
</template>

<script>
import LoginFormComponent from '@/components/LoginForm.vue';

export default {
    name: "LoginView",
    data() {
        return {

        };
    },
    methods: {

    },
    components: {
        LoginFormComponent,
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
