<script>
import "@/assets/css/form.css"
export default {
    name: "RegisterForm1Component",
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
            
            let formData = {
                username: this.username,
                password: this.password,
                email: this.email,
            }

            this.$store.dispatch('auth/register', formData)
            .then(() => {
                console.log(formData);
                this.$parent.form1Submit();
            }).catch(console.log("errorcode"));
            
        },
    },
};
</script>

<template>
    <div class="registerbox-in">
        <form @submit.prevent="handleRegister">
            <div class="form-field">
                <label for="username">Username:</label>
                <input class="text-input" id="username" v-model="username" type="text"
                    placeholder="Enter your username" required />
            </div>
            <div class="form-field">
                <label for="email">Email:</label>
                <input class="text-input" id="email" v-model="email" type="email" placeholder="Enter your email"
                    required />
            </div>
            <div class="form-field">
                <label for="password">Password:</label>
                <input class="text-input" id="password" v-model="password" type="password"
                    placeholder="Create your password" required />
            </div>
            <div class="form-field">
                <label for="confirmPassword">Confirm Password:</label>
                <input class="text-input" id="confirmPassword" v-model="confirmPassword" type="password"
                    placeholder="Confirm your password" required />
            </div>
            <button type="submit" class="submit-button">Continue</button>
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
