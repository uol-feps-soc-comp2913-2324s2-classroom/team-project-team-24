<script>
import '@/assets/css/form.css'
import textInputQuiet from '@/components/ui-components/textInputQuiet.vue'
import primaryButton from '@/components/ui-components/primaryButton.vue'
import axiosAuth from "@/api/axios-auth.js";
export default {
    name: 'RegisterForm2Component',
    components: {
        textInputQuiet,
        primaryButton,
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
                <span>Already have an account?</span> &nbsp;
                <a href="#" @click="alreadyHaveAccount">Login</a>
            </div>

            <div class="form-field">
                <label for="Gender">Gender</label>
                <textInputQuiet
                    width="100%"
                    class="text-input"
                    id="Gender"
                    v-model="text"
                    type="text"
                    required
                    @textInput="enterGender"
                ></textInputQuiet>
            </div>
            <div class="form-field">
                <label for="password">Age</label>
                <textInputQuiet
                    width="100%"
                    class="text-input"
                    id="password"
                    v-model="text"
                    type="text"
                    @textInput="enterAge"
                ></textInputQuiet>
            </div>
            <div class="submit-button-container">
                <primaryButton type="submit" class="submit-button"
                    :on-click="handleRegister">Register</primaryButton
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

.form-field input,
.submit-button-container button {
    box-sizing: border-box; /* Padding and border are included in the width */
    width: 40%;
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


</style>
