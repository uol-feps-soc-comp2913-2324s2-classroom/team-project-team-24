<script>
import dangerButton from './ui-components/dangerButton.vue';
import primaryButton from './ui-components/primaryButton.vue';
import secondaryButton from './ui-components/secondaryButton.vue';
import tertiaryButton from './ui-components/tertiaryButton.vue';
import dangerButtonOutline from './ui-components/dangerButtonOutline.vue';
import quietButton from './ui-components/quietButton.vue';
import textButton from './ui-components/textButton.vue';
import textInputQuiet from './ui-components/textInputQuiet.vue';

export default {
    name: 'styleGuideComponent',
    props: {
        msg: String
    },
    data() {
        return {
            count: 0
        }
    },
    methods: {
        increment() {
            this.count++;
        }
    },
    components: {
        primaryButton,
        secondaryButton,
        tertiaryButton,
        dangerButton,
        dangerButtonOutline,
        quietButton,
        textButton,
        textInputQuiet,
    }
}

</script>

<template>
    <div class="stylingGuideContainer p-5">
        <h1> Style Guide (owner's page)</h1>
        <h2> Button styling</h2>
        <p>Count {{count}}</p>
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-8">
                    <div class="button-container text-center">
                        <div class="row justify-content-center">
                            <div class="col-md-12">
                                <primaryButton :on-click="this.increment">Action name</primaryButton>
                            </div>
                        </div>
                        <div class="row mt-3 justify-content-center">
                            <div class="col-md-12">
                                <secondaryButton :on-click="this.increment">Action name</secondaryButton>
                            </div>
                        </div>
                        <div class="row mt-3 justify-content-center">
                            <div class="col-md-12">
                                <tertiaryButton :on-click="this.increment">Action name</tertiaryButton>
                            </div>
                        </div>
                        <div class="row mt-3 justify-content-center">
                            <div class="col-md-12">
                                <dangerButton :on-click="this.increment">Action name</dangerButton>
                            </div>
                        </div>
                        <div class="row mt-3 justify-content-center">
                            <div class="col-md-12">
                                <dangerButtonOutline :on-click="this.increment">Action name</dangerButtonOutline>
                            </div>
                        </div>
                        <div class="row mt-3 justify-content-center">
                            <div class="col-md-12">
                                <quietButton :on-click="this.increment">Action name</quietButton>
                            </div>
                        </div>
                        <div class="row mt-3 justify-content-center">
                            <div class="col-md-12">
                                <textButton :on-click="this.increment">Action name</textButton>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    </div>
        <h2> Form styling </h2>
        <div class="form-container">
            <form>
                <div class="form-field">
                    <textInputQuiet form-label="Name"></textInputQuiet>
                </div>
                <div class="form-field">
                    <textInputQuiet form-label="Email" type="email"></textInputQuiet>
                </div>
            </form>
        </div>

        
    </div>

</template>

<script setup>

</script>

<style scoped>
    .form-container {
        display: flex;
        justify-content: center; /* Horizontally center the content */
    }
    form {
        width: 100%; /* Make sure the form takes the full width of the container */
        max-width: 400px; /* Limit the maximum width of the form */
    }
</style>