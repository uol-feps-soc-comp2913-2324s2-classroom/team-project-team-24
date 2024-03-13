<script>
import "@/assets/css/form.css"
export default {
    name: "ResetPasswordFormComponent",
    data() {
        return {
            
        };
    },
    methods: {
        resetPassword() {
            
        }
    },
};
</script>

<template>
    <div class="registerbox-in">
        <form @submit.prevent="resetPassword">
            <div class="form-field">
                <label for="email">Email:</label>
                <input class="text-input" id="email" v-model="email" type="email" placeholder="Enter your email"
                    required />
            </div>
            <button type="submit" class="submit-button">Reset Password</button>
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

img {
    height: 30px;
    width: 30px;
}

</style>
