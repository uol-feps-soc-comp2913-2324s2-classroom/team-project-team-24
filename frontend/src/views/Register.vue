<script>
import RegisterForm1Component from "@/components/forms/RegisterForm1.vue";
import RegisterForm2Component from "@/components/forms/RegisterForm2.vue";

export default {
    name: "RegisterView",
    data() {
        return {
           form1: true,
           form2: false
        };
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
};
</script>

<template>
    <div class="register-container">
        <h1 class="title">Create an Account</h1>
        <RegisterForm1Component v-if="form1"/>
        <RegisterForm2Component v-if="form2"/>
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

</style>
