<script>
import '@/assets/css/form.css'
import axios from 'axios'

export default {
    name: 'RegisterForm1Component',
    components: {
    },
    data() {
        return {
            username: '',
            email: '',
            password: '',
            confirmPassword: '',
            errorText: null,
        }
    },
    methods: {
        async handleRegister() {
            if (this.password !== this.confirmPassword) {
                this.errorText = "Passwords do not match";
                return
            }

            let formData = {
                username: this.username,
                password: this.password,
                email: this.email,
            }

            axios.post("/auth/register", formData).then(response => {
                if (response.data.success === true) {
                    localStorage.setItem('token', response.data.token);
                    this.$parent.form1Submit();
                } else {
                    this.errorText = response.data.error;
                }
            }).catch(error => {
                this.errorText = error.response.data.error;
            });
        },
        alreadyHaveAccount() {
            this.$router.push('/login')
        },
        enterUsername(event) {
            this.username = event;
        },
        enterPassword(event) {
            this.password = event;
        },
        enterPasswordConfirm(event) {
            this.confirmPassword = event;
        },
        enterEmail(event) {
            this.email = event;
        },
        removeErrorMessage() {
            this.errorText = "";
        }
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
                <label for="username" class="input-label">Username</label>
                <input class="text-input" id="username" type="username" v-model="username" @input="removeErrorMessage">
            </div>
            <div class="form-field">
                <label for="email" class="input-label">Email</label>
                <input class="text-input" id="email" type="email" v-model="email" @input="removeErrorMessage">
            </div>
            <div class="form-field">
                <label for="password" class="input-label">Password</label>
                <input class="text-input" id="password" type="password" v-model="password" @input="removeErrorMessage">
            </div>
            <div class="form-field">
                <label for="confirmPassword" class="input-label">Confirm Password</label>
                <input class="text-input" id="confirmPassword" type="password" v-model="confirmPassword" @input="removeErrorMessage">
            </div>
            <div>
                <p class="form-error-text" v-if="errorText !== null">{{ errorText }}</p>
            </div>

            <div class="submit-button-container">

                <button type="submit" class="btn-primary">Continue</button>
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

.text-input {
    width: 100%;
}
</style>
