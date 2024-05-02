<script>
import axiosAuth from "@/api/axios-auth";

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
    methods: {
        nextPage() {
            this.$router.push("/activitycentre");
        }
    }
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

            <!-- Select with "Walking" as default and made selection mandatory -->
            <select v-model="exerciseType" class="form-select mt-2" required>
                <option disabled value="">Please select one</option>
                <option value="Walking" selected>Walking</option>
                <option>Running</option>
                <option>Biking</option>
                <option>Hiking</option>
            </select>
            <p class="form-error-text">{{ errorMessage }}</p>
            <div class="d-grid gap-2 d-md-flex justify-content-md-center mt-2">
                <!-- Button disabled logic checks if routeName has content and file is uploaded -->
                <button class="btn-primary" @click="uploadData"
                    :disabled="!selectedFile || isDuplicateName">Upload</button>

            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const routeName = ref('');
const exerciseType = ref('Walking'); // set Walking as default
const selectedFile = ref(null);
var errorMessage = ref("");

const router = useRouter();

// ensures user uploads valid data
const handleFileUpload = event => {
    selectedFile.value = event.target.files[0] || null;
};

const uploadData = () => {
    console.log('Uploading data...');
    // Here you would typically handle the file upload to your backend
    var formData = new FormData();
    formData.append("file", selectedFile.value);
    formData.append("routeName", routeName.value);
    formData.append("exerciseType", exerciseType.value);
    console.log(formData);

    axiosAuth.post(`/trail/upload`, formData,
        {
            headers: { 'Content-Type': 'multipart/form-data' }
        })
        .then(
            function (response) {
                console.log("response:", response);
                router.push({
                    path: "/mytrail",
                    query: {trailID: response.data.trailID}
                });
            }
        ).catch(error => {
            errorMessage.value = error.response.data;
        });

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