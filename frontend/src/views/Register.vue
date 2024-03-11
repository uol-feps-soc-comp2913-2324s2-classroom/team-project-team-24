<script>
/* eslint-disable */
import axios from "axios";

export default {
    name: "Register",
    data() {
        return {
            username: "",
            email: "",
            password: "",
            confirmPassword: "",
        };
    },
    methods: {
        async handleRegister() {
            if (this.password !== this.confirmPassword) {
                alert("Passwords do not match.");
                return;
            }
            try {
                const response = await axios.post("/api/register", {
                    username: this.username,
                    email: this.email,
                    password: this.password,
                });
            } catch (error) {
                console.error("Registration error:", error);
                // Handle errors here
            }
        },
    },
};
</script>

<template>
    <div class="register-container">
        <h1 class="title">Create an Account</h1>
        <div class="registerbox-in">
            <form @submit.prevent="handleRegister">
                <div class="form-field">
                    <label for="username">Username:</label>
                    <input class="form-input" id="username" v-model="username" type="text"
                        placeholder="Enter your username" required />
                </div>
                <div class="form-field">
                    <label for="email">Email:</label>
                    <input class="form-input" id="email" v-model="email" type="email" placeholder="Enter your email"
                        required />
                </div>
                <div class="form-field">
                    <label for="password">Password:</label>
                    <input class="form-input" id="password" v-model="password" type="password"
                        placeholder="Create your password" required />
                </div>
                <div class="form-field">
                    <label for="confirmPassword">Confirm Password:</label>
                    <input class="form-input" id="confirmPassword" v-model="confirmPassword" type="password"
                        placeholder="Confirm your password" required />
                </div>
                <button type="submit" class="register-button">Register</button>
            </form>
        </div>
    </div>
</template>

<style scoped>
.register-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    text-align: center;
}

.registerbox-in {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 5px;
}

.form-field {
    margin-bottom: 15px;
}

.form-input {
    width: 100%;
    max-width: 400px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.register-button {
    width: 100%;
    max-width: 400px;
    padding: 10px 20px;
    border: none;
    background-color: #007bff;
    color: white;
    border-radius: 4px;
    cursor: pointer;
}

.register-button:hover {
    background-color: #0056b3;
}
</style>
