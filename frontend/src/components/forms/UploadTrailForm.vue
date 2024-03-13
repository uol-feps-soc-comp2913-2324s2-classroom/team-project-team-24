<template>
    <form @submit.prevent="handleRegister">
        <div class="form-field">
            <label for="route-data">Upload Data:</label>
            <input id="route-data" type="file" accept="gpx" @change="uploadImage"/>
        </div>
        <div class="form-field">
            <label for="Name">Name your route:</label>
            <input class="text-input" id="Name" v-model="text" type="text" />
        </div>
        <div class="form-field">
            <label for="exercise-type">Exercise type:</label>
            <input class="text-input" id="exercise-type" v-model="text" type="text"/>
        </div>
        <button type="submit" class="submit-button">Submit</button>
    </form>
</template>

<script>
import '@/assets/css/form.css'

export default {
    name: "UploadTrailFormComponent",
    data() {
        return {

        };
    },
    methods: {
        onSubmit() {

        }
    },
};
</script>

