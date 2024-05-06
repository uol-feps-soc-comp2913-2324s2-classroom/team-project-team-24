<template>
    <form @submit.prevent="onSubmit">
        <div class="inner-container">
            <div class="form-field">
                <label for="username" class="input-label">Username</label>
                <input class="text-input" id="username" v-model="username" type="username">
            </div>
            <div class="form-field">
                <label for="password" class="input-label">Password</label>
                <input class="text-input" id="password" v-model="password" type="password">
            </div>
            <div>
                <p v-if="invalidCredentials" class="error-ext">Your username/password is incorrect</p>
            </div>
            <div class="form-actions">
                <button type="submit" class="btn-primary">Login</button>
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
import axios from 'axios'
import axiosAuth from '@/api/axios-auth.js'

export default {
    name: 'LoginFormComponent',
    components: {
    },
    data() {
        return {
            username: '',
            password: '',
            invalidCredentials: false,
        }
    },
    methods: {
        async onSubmit() {
            let formData = {
                username: this.username,
                password: this.password,
            }
            axios.post("/auth/login", formData).then(response => {
                if (response.data.success === true) {
                    localStorage.setItem('token', response.data.token);
                    axiosAuth.get('/owner/current-is-owner').then(
                        response => {
                            if (response.status == 200) {
                                this.$router.push('/owner');
                            } else {
                                this.$router.push('/activitycenter');
                            }
                        }
                    ).catch(() => {this.$router.push('/activitycenter')});
                }
            }).catch(() => {
                this.invalidCredentials = true;
            });
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
    position: relative;
    top: -12px;
}

.remember-me {
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 10px;
    margin-top: 10px;
}

.error-ext {
    color: red;
}

.text-input {
    width: 100%;
}
</style>
