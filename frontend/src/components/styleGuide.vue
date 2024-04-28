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
        },
        handleClicked({event, to}) {
            console.log("We're going to tNR")
            this.$refs.topNavRailed.handleClicked({event, to});
        }
    },
    components: {
    }
}
</script>

<template>
    <div class="stylingGuideContainer p-5">
        <h1> Style Guide (owner's page)</h1>
        <p>there used to be things here until the fire nation attacked</p>
        
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