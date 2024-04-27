<script>
import '@/assets/css/form.css'

export default {
    name: 'ResetPasswordFormComponent',
    components: {
    },
    data() {
        return {}
    },
    methods: {
        resetPassword() {},

        loginAccount() {
            this.$router.push('/login')
        },
    },
}
</script>

<template>
    <div class="registerbox-in">
        <form @submit.prevent="resetPassword">
            <p>
                To reset your password, please enter the email address you have
                used to register for your Walkley account.
            </p>
            <p>
                We will send you an email with a password reset link if the
                email is registered.
            </p>
            <div class="form-field">
                <label for="email" class="input-label">Email</label>
                <input class="text-input" 
                    type="text" 
                    id="email" 
                    v-model="email" 
                    placeholder="Enter your email" 
                    required>
            </div>
            <div class="form-actions">
                <a href="#" @click.prevent="loginAccount">Return to login</a>

                <button class="btn-primary" @click="onSubmit">Send</button>
            </div>
        </form>
    </div>
</template>

<style scoped>
.registerbox-in {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 40px;
    border-radius: 5px;
}

.form-actions {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    margin-top: 40px;
    gap: 20px;
}

.form-actions a {
    display: flex;
    align-items: center;
    margin-right: 1px;
    margin-left: 210px;
    margin-bottom: 0;
    text-decoration: none;
}

img {
    height: 30px;
    width: 30px;
}

.text-input {
    width: 100%;
}
</style>
