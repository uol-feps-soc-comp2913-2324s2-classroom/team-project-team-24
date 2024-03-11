<script>
import axios from 'axios'

export default {
    name: 'UploadGPX',
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
    <div class="upload-gpx-container">
        <h1>Begin your new trail</h1>
        <input type="file" @change="handleFileUpload" />
        <input type="text" placeholder="Enter the name of your route" v-model="routeName" />
        <select v-model="exerciseType">
            <option disabled value="">Please select one</option>
            <option>Running</option>
            <option>Biking</option>
            <option>Hiking</option>
        </select>
        <button @click="uploadData">Upload</button>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const routeName = ref('');
const exerciseType = ref('');
const selectedFile = ref(null);

const handleFileUpload = event => {
    selectedFile.value = event.target.files[0];
};

const uploadData = () => {
    console.log('Uploading data...');
    // Here you would typically handle the file upload to your backend
    var formData = new FormData();
    formData.append("file", selectedFile.value);
    formData.append("routeName", routeName.value);
    formData.append("exerciseType", exerciseType.value);
    console.log(formData);

    axios.post(`http://localhost:${process.env.VUE_APP_BACKEND_PORT}/upload`, formData,
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