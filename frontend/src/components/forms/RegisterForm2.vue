<script>
import "@/assets/css/form.css";
import axiosAuth from "@/api/axios-auth.js";
export default {
    name: "RegisterForm2Component",
    data() {
        return {
            gender: "",
            age: 0,
        };
    },
    methods: {
        async handleRegister() {
            console.log("Registering...");

            await axiosAuth.post('/account/set-details', {
                gender: this.gender,
                age: this.age,
            });
            this.$router.push('/activitycenter');
        },
    },
};
</script>

<template>
    <div class="registerbox-in">
        <form @submit.prevent="handleRegister">
            <div class="form-field">
                <label for="gender">Gender:</label>
                <input class="text-input" id="gender" v-model="gender" type="text"
                    required />
            </div>
            <div class="form-field">
                <label for="age">Age:</label>
                <input class="text-input" id="age" v-model="age" type="text"
                    placeholder="Enter your age" required />
            </div>
            <button type="submit" class="submit-button">Register</button>
        </form>
    </div>
</template>

<style scoped>
.registerbox-in {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 5px;
}

</style>
