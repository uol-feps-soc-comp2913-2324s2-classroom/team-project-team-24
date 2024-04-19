<script>
import '@/assets/css/form.css'
import textInputQuiet from '@/components/ui-components/textInputQuiet.vue'
import primaryButton from '@/components/ui-components/primaryButton.vue'

export default {
    name: 'RegisterForm1Component',
    components: {
        textInputQuiet,
        primaryButton,
    },
    data() {
        return {
            username: '',
            email: '',
            password: '',
            confirmPassword: '',
        }
    },
    methods: {
        async handleRegister() {
            if (this.password !== this.confirmPassword) {
                alert('Passwords do not match.')
                return
            }

            let formData = {
                username: this.username,
                password: this.password,
            }

            this.$store.dispatch('auth/register', formData).then(() => {
                this.$router.push('/activitycenter')
            })
            console.log(formData)
            this.$parent.form1Submit()
        },
        alreadyHaveAccount() {
            this.$router.push('/login')
        },
    },
}
</script>

<template>
    <div class="registerbox-in">
        <form @submit.prevent="handleRegister">
            <div class="form-field go-to-login">
                <span>Already have an account?</span>&nbsp;
                <a href="#" @click="alreadyHaveAccount">Login</a>
            </div>
            <div class="form-field">
                <label for="username">Username</label>
                <textInputQuiet
                    width="100%"
                    class="text-input"
                    id="username"
                    v-model="username"
                    type="text"
                ></textInputQuiet>
            </div>
            <div class="form-field">
                <label for="email">Email</label>
                <textInputQuiet
                    width="100%"
                    class="text-input"
                    id="email"
                    v-model="email"
                    type="email"
                ></textInputQuiet>
            </div>
            <div class="form-field">
                <label for="password">Password</label>
                <textInputQuiet
                    width="100%"
                    class="text-input"
                    id="password"
                    v-model="password"
                    type="password"
                ></textInputQuiet>
            </div>
            <div class="form-field">
                <label for="confirmPassword">Confirm Password</label>
                <textInputQuiet
                    width="100%"
                    class="text-input"
                    id="confirmPassword"
                    v-model="confirmPassword"
                    type="password"
                ></textInputQuiet>
            </div>

            <div class="submit-button-container">
                <primaryButton @click="$emit('formSubmitted')"
                    >Continue</primaryButton
                >
            </div>
        </form>
    </div>
</template>

<style scoped>
.registerbox-in {
    max-width: 500px; /* Adjust as needed for your design */
    margin: 0 auto; /* This centers the container */
    padding: 20px; /* Adjust as needed for your design */
    box-sizing: border-box;
}

.registerbox-in a {
    text-decoration: none;
}

.form-field {
    margin-bottom: 30px;
}

.go-to-login {
    display: flex;
    margin-bottom: 50px;
}

.submit-button-container {
    display: flex;
    justify-content: flex-end;
    width: 100%;
}
</style>
