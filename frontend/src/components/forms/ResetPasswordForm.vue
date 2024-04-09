<script>
import '@/assets/css/form.css'
import textInputQuiet from '@/components/ui-components/textInputQuiet.vue'
import primaryButton from '@/components/ui-components/primaryButton.vue'

export default {
    name: 'ResetPasswordFormComponent',
    components: {
        textInputQuiet,
        primaryButton,
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
                We will send you an email with a password reset link iff the
                email is registered.
            </p>
            <div class="form-field">
                <label for="email">Email:</label>
                <textInputQuiet
                    width="100%"
                    class="text-input"
                    id="email"
                    v-model="email"
                    type="email"
                    placeholder="Enter your email"
                    required
                ></textInputQuiet>
            </div>
            <div class="form-actions">
                <a href="#" @click.prevent="loginAccount">Return to login</a>

                <primaryButton @click="onSubmit"> Send </primaryButton>
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
}

img {
    height: 30px;
    width: 30px;
}
</style>
