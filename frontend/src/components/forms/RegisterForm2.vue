<script>
import axiosAuth from "@/api/axios-auth.js";
export default {
    name: 'RegisterForm2Component',
    components: {
    },
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
        async alreadyHaveAccount() {
            this.$router.push('/login');
        },
        enterGender(event) {
            this.gender = event;
        },
        enterAge(event) {
            this.age = event;
        }
    },
}
</script>

<template>
    <div class="registerbox-in">
        <form @submit.prevent="handleRegister">
            <div class="form-field go-to-login">
                <span>Already have an account?</span>
                <a href="#" @click="alreadyHaveAccount"> Login</a>
            </div>

            <div class="form-field">
                <label for="Gender" class="input-label">Gender</label>
                <input class="text-input" id="gender" type="text" v-model="gender">
            </div>
            <div class="form-field">
                <label for="age" class="input-label">Age</label>
                <input class="text-input" id="age" type="text" v-model.number="age">
            </div>
            <div class="submit-button-container">
                <button class="btn-primary" type="submit">Register</button>
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

.form-field input,
.submit-button-container button {
    box-sizing: border-box; /* Padding and border are included in the width */
}

.submit-button-container {
    display: flex;
    justify-content: flex-end;
}

.form-field {
    margin-bottom: 40px;
}
.go-to-login {
    margin-bottom: 30px;
}

.text-input {
    width: 100%;
}

</style>
