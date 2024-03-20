<script>
import axiosAuth from "@/api/axios-auth";
import primaryButton from './ui-components/primaryButton.vue';

export default {
    name: 'UploadGPXComponent',
    props: {
        msg: String
    },
    data() {
        return {
            count: 0
        }
    },
}

</script>

<template>
    <div class="upload-gpx-container p-5">
        <h1>Upload your new trail</h1>
        <!-- Wrapper div for fields, with Bootstrap classes for width and centering -->
        <div class="mx-auto" style="max-width: 50%;">
            <!-- File upload input is now required, only gpx files can be accepted -->
            <input type="file" @change="handleFileUpload" class="form-control" accept=".gpx" />
            <input type="text" placeholder="Enter the name of your route" v-model="routeName"
                class="form-control mt-2" />
            <!-- Warning for duplicate name -->
            <div v-if="isDuplicateName" class="text-danger mt-2">Duplicate name detected. Please choose a different
                name.</div>
            <!-- Select with "Walking" as default and made selection mandatory -->
            <select v-model="exerciseType" class="form-select mt-2" required>
                <option disabled value="">Please select one</option>
                <option value="Walking" selected>Walking</option>
                <option>Running</option>
                <option>Biking</option>
                <option>Hiking</option>
            </select>
            
            <div class="d-grid gap-2 d-md-flex justify-content-md-center mt-2">
                <!-- Button disabled logic checks if routeName has content and file is uploaded -->
                <primaryButton @click="uploadData"
                    :disabled="!selectedFile || isDuplicateName">Upload</primaryButton>

            </div>
        </div>
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
    </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const routeName = ref('');
const exerciseType = ref('Walking'); // set Walking as default
const selectedFile = ref(null);

// ensures user uploads valid data
const handleFileUpload = event => {
    selectedFile.value = event.target.files[0] || null;
};

// Example list of existing route names
const existingRouteNames = ['Trailblazer', 'Morning Run', 'Mountain Hike'];

// Ref to store whether the current route name is a duplicate
const isDuplicateName = ref(false);

// Watch for changes to routeName and validate for duplicates
watch(routeName, (newValue) => {
    isDuplicateName.value = existingRouteNames.includes(newValue);
});


const uploadData = () => {
    console.log('Uploading data...');
    // Here you would typically handle the file upload to your backend
    var formData = new FormData();
    formData.append("file", selectedFile.value);
    formData.append("routeName", routeName.value);
    formData.append("exerciseType", exerciseType.value);
    console.log(formData);

    axiosAuth.post(`upload`, formData,
        {
            headers: { 'Content-Type': 'multipart/form-data' }
        })
        .then(
            function (response) {
                console.log(response);
            }
        );

    // this.APIResponse = response.data
    // console.log(this.APIResponse)

    // This example just logs to the console
    console.log('File:', selectedFile.value);
    console.log('Route Name:', routeName.value);
    console.log('Exercise Type:', exerciseType.value);
};
</script>

<style scoped>
.upload-gpx-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    margin-top: 20px;
}
</style>