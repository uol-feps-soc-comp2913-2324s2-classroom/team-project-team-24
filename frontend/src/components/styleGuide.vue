<script>
import dangerButton from './ui-components/dangerButton.vue';
import primaryButton from './ui-components/primaryButton.vue';
import secondaryButton from './ui-components/secondaryButton.vue';
import tertiaryButton from './ui-components/tertiaryButton.vue';
import dangerButtonOutline from './ui-components/dangerButtonOutline.vue';
import quietButton from './ui-components/quietButton.vue';
import textButton from './ui-components/textButton.vue';
import textInputQuiet from './ui-components/textInputQuiet.vue';
import topNavRailed from './ui-components/topNavRailedCommunity.vue';
// import topNavElement from './ui-components/topNavElement.vue';

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
            // console.log('clicked', to);
            // console.log('event', event);
            console.log("We're going to tNR")
            this.$refs.topNavRailed.handleClicked({event, to});
            // this.currentSelection = to;
    
            // const clickedElement = event.target.getBoundingClientRect();
            // const parentElement = event.target.parentNode.getBoundingClientRect();
            // this.selectionTrainStyle.width = `${clickedElement.width}px`
            // this.selectionTrainStyle.transform = `translateX(${clickedElement.left - parentElement.left}px) translateY(-4px)`
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
        topNavRailed,
        // topNavElement,
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
        <div class="form-container d-flex flex-column">
            <form class="form-container">
                <div class="form-input">
                    <!-- Default width value for text input is auto -->
                    <textInputQuiet form-label="Name"></textInputQuiet>
                </div>
                
                <div class="form-input">
                    <textInputQuiet width="50%" form-label="Last name"></textInputQuiet>
                </div>
                <div class="form-input">
                    <textInputQuiet width="100%" form-label="Email" type="email"></textInputQuiet>
                </div>
            </form>
        </div>
        <div>
            <h2> Top Nav Railed </h2>
            <topNavRailed>
                <!-- <topNavElement to="#" @NavElementClicked="$emit('NavElementClicked')">Friends</topNavElement>
                <topNavElement to="#" @NavElementClicked="$emit('NavElementClicked')">Groups</topNavElement>
                <topNavElement to="#" @NavElementClicked="$emit('NavElementClicked')">Add Friends</topNavElement>
                <topNavElement to="#" @NavElementClicked="$emit('NavElementClicked')">Friend Requests</topNavElement> -->

                <!-- this is really interesting
                <template v-slot:left>
                    <textButton>Left</textButton>
                </template>
                <template v-slot:center>
                    <textButton>Center</textButton>
                </template>
                <template v-slot:right>
                    <textButton>Right</textButton>
                </template> -->
            </topNavRailed>
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