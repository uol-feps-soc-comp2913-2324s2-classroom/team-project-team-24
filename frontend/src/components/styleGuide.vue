<script>

export default {
    name: 'styleGuideComponent',
    props: {
        msg: String
    },
    data() {
        return {
            count: 0
        }
    }
}

</script>

<template>
    <div class="stylingGuideContainer">
        <h1> Style Guide (owner's page)</h1>
        <h2> Button styling</h2>
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-8">
                    <div class="button-container text-center">
                        <div class="row justify-content-center">
                            <div class="col-md-12">
                                <button class="btn btn-primary">Primary Button</button>
                            </div>
                        </div>
                        <div class="row mt-3 justify-content-center">
                            <div class="col-md-12">
                                <button class="btn btn-secondary">Secondary Button</button>
                            </div>
                        </div>
                        <div class="row mt-3 justify-content-center">
                            <div class="col-md-12">
                                <button class="btn btn-tertiary">Tertiary Button</button>
                            </div>
                        </div>
                        <div class="row mt-3 justify-content-center">
                            <div class="col-md-12">
                                <button class="btn btn-success">Success Button</button>
                            </div>
                        </div>
                        <div class="row mt-3 justify-content-center">
                            <div class="col-md-12">
                                <button class="btn btn-danger">Danger Button</button>
                            </div>
                        </div>
                        <div class="row mt-3 justify-content-center">
                            <div class="col-md-12">
                                <button class="btn btn-info">Info Button</button>
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
                    <input type="text" class="text-input" placeholder="Enter your name">
                </div>
                <div class="form-field">
                    <input type="email" class="text-input" placeholder="Enter your email">
                </div>
                <button type="submit" class="submit-button">Submit</button>
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