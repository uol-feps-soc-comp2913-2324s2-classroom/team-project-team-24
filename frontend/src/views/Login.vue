<template>
    <div class="login-container">
        <h1 class="title">Login to Your App</h1>
        <form>
            <div class="loginbox-in">
                <div class="username">
                    <input class="username" id="username" v-model="username" placeholder="Enter your username" />
                </div>
                <div class="password">
                    <input class="password" id="password" v-model="password" type="password"
                        placeholder="Enter your password" />
                </div>
                <button type="submit" @click.prevent="onSubmit">Login</button>
            </div>
        </form>
    </div>
    <br />
    <!-- <p>API Response: {{ APIResponse }}</p> -->
</template>

<script>
// import axios from "axios";

export default {
    name: "LoginComponent",
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

.loginbox-in {
    height: 250px;
    max-width: 500px;
    margin: auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 5px;
}

.username,
.password {
    margin-bottom: 15px;
}

.username input,
.password input {
    width: 400px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 80%;
    padding: 10px 20px;
    border: none;
    background-color: #007bff;
    color: white;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
</style>
