<template>
    <form>
        <div class="inner-container">
            <div class="form-field">
                <input class="text-input" id="username" v-model="username" placeholder="Enter your username" />
            </div>
            <div class="form-field">
                <input class="text-input" id="password" v-model="password" type="password" placeholder="Enter your password" />
            </div>
            <button class="submit-button" type="submit" @click.prevent="onSubmit">Login</button>
        </div>
    </form>
</template>

<script>
import '@/assets/css/form.css'

export default {
    name: "LoginFormComponent",
    data() {
        return {
            username: '',
            password: '',
            invalidCredentials: false
        };
    },
    methods: {
        onSubmit() {
            let formData = {
                username: this.username,
                password: this.password,
            }

            this.$store.dispatch('auth/login', formData).then(() => {
                this.$router.push('/activitycenter');
            });
        }
    },
};
</script>

