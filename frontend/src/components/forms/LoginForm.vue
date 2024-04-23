<template>
    <form>
        <div class="inner-container">
            <div class="form-field">
                <label for="email">Username</label>
                <textInputQuiet
                    width="100%"
                    class="text-input"
                    id="username"
                    v-model="username"
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

            <div class="form-actions">
                <a href="#" @click.prevent="forgotPassword">Forgot password</a>

                <primaryButton class="login-button" :on-click="onSubmit">
                    Login
                </primaryButton>
            </div>

            <div class="separator">
                <hr class="separator-line" />
                <div class="separator-text">Or</div>
                <hr class="separator-line" />
            </div>
        </div>
        <div class="form-footer">
            <span>Don't have an account yet?</span>
            <a href="#" @click="createAccount"> Create an account</a>
        </div>
    </form>
</template>

<script>
import '@/assets/css/form.css'
import textInputQuiet from '@/components/ui-components/textInputQuiet.vue'
import primaryButton from '@/components/ui-components/primaryButton.vue'

export default {
    name: 'LoginFormComponent',
    components: {
        textInputQuiet,
        primaryButton,
    },
    data() {
        return {
            username: '',
            password: '',
            invalidCredentials: false,
        }
    },
    methods: {
        onSubmit() {
            console.log("Submitting...")
            let formData = {
                username: this.username,
                password: this.password,
            }
            console.log(this.username, this.password)
            this.$store.dispatch('auth/login', formData).then(() => {
                this.$router.push('/activitycenter')
            })
        },
        forgotPassword() {
            this.$router.push('/resetpassword')
        },
        createAccount() {
            this.$router.push('/register')
        },
    },
}
</script>

<style scoped>
.inner-container {
    display: flex;
    flex-direction: column;
    justify-content: space-between; /* This will push the .form-actions to the bottom */
    height: 100%;
    box-shadow: none;
    border-radius: 8px;
}

.form-field {
    margin-bottom: 20px;
}

.form-footer {
    text-align: center;
    margin-top: 10px;
    margin-bottom: 20px;
}

.separator {
    display: flex;
    text-align: center;
    margin-top: 20px;
}

.form-actions {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    margin-top: 20px;
    gap: 30px;
}

.form-actions a {
    text-decoration: none;
}

.form-footer a {
    text-decoration: none;
}

.separator-line {
    flex-grow: 1;
    border: none;
    height: 1px;
    background-color: #666666;
    margin: 0 10px;
}
.separator-text {
    padding: 0 10px;
}

.remember-me {
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 10px;
    margin-top: 10px;
}
</style>
