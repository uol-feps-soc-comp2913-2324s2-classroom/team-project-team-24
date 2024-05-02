<script>
// import axios from "axios";
import Login from "./Login.vue";
import Register from "./Register.vue";
import axiosAuth from "@/api/axios-auth"

export default {
    name: "API Test",
    data() {
        return {
            msg: "Welcome to Your Vue.js App",
            APIResponse: "",
        };
    },
    methods: {
        async testApi() {
            try {
                const response = await axiosAuth.get(
                    `/`
                );
                this.APIResponse = response.data;
            } catch (error) {
                this.APIResponse = "Error: " + error;
                console.error(error);
            }
        },
    },
    components: {
        Login,
        Register,
    },
};
</script>

<template>
    <div>
        <p>{{ msg }}</p>
    </div>
    <button @click="testApi">Test API</button>
    <p>API Response: {{ APIResponse }}</p>
    <Login></Login>
    <Register></Register>
</template>

<style scoped></style>