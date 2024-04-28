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
    },
    methods: {
        increment() {
            this.count++;
        }
    },
    components: {

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
                                <button class="btn-primary" @click.prevent="increment">Action name</button>
                            </div>
                        </div>
                        <div class="row mt-3 justify-content-center">
                            <div class="col-md-12">
                                <button class="btn-secondary" @click.prevent="increment">Action name</button>
                            </div>
                        </div>
                        <div class="row mt-3 justify-content-center">
                            <div class="col-md-12">
                                <button class="btn-tertiary" @click.prevent="increment">Action name</button>
                            </div>
                        </div>
                        <div class="row mt-3 justify-content-center">
                            <div class="col-md-12">
                                <button class="btn-danger" @click.prevent="increment">Action name</button>
                            </div>
                        </div>
                        <div class="row mt-3 justify-content-center">
                            <div class="col-md-12">
                                <button class="btn-danger-outline" @click.prevent="increment">Action name</button>
                            </div>
                        </div>
                        <div class="row mt-3 justify-content-center">
                            <div class="col-md-12">
                                <button class="btn-quiet" @click.prevent="increment">Action name</button>
                            </div>
                        </div>
                        <div class="row mt-3 justify-content-center">
                            <div class="col-md-12">
                                <button class="btn-text" @click.prevent="increment">Action name</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    </div>
        <h2> Form styling </h2>
        <div class="form-container d-flex flex-column">
            <form class="form-container">
                <div class="form-input">
                    <!-- Default width value for text input is auto -->
                    <label class="input-label" for="default-width">Name</label>
                    <input class="text-input" id="default-width">
                </div>
                <div class="form-input">
                    <label class="input-label" for="50%-width">Last name</label>
                    <input class="text-input" id="50%-width" style="width:50%">
                </div>
                <div class="form-input">
                    <label class="input-label" for="100%-width">Email</label>
                    <input class="text-input" id="100%-width" style="width:100%" type="email">
                </div>
            </form>
        </div>

        
    </div>

</template>

<style scoped>
.form-container {
    border: none;
}

.form-input{
    margin-bottom: 20px;
    margin-top: 20px;
}
</style>