<script>
import RegisterForm1Component from '@/components/forms/RegisterForm1.vue'
import RegisterForm2Component from '@/components/forms/RegisterForm2.vue'

export default {
    name: 'RegisterView',
    data() {
        return {
            form1: true,
            form2: false,
        }
    },
    methods: {
        form1Submit() {
            this.form1 = false;
            this.form2 = true;
        },
    },
    components: {
        RegisterForm1Component,
        RegisterForm2Component,
    },
}
</script>

<template>
    <div class="register-container">
        <h2 class="title"><b>Create an account</b></h2>
        <RegisterForm1Component v-if="form1" @formSubmitted="form1Submit" />
        <RegisterForm2Component
            v-if="form2"
            @registrationSuccessful="handleRegistrationSuccessful"
        />
    </div>
</template>

<style scoped>
.title {
    color: #333;
    margin-bottom: 30px;
    text-align: left;
    margin-top: 40px;
    margin-left: 40px;
    margin-bottom: 1px;
}

.register-container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
}
</style>
