<script>
import "@/assets/css/form.css";
import axiosAuth from "@/api/axios-auth.js";
export default {
    name: "RegisterForm2Component",
    data() {
        return {
            profilePreview: null,
            profilePhoto: null,
            gender: "",
            age: 0,
        };
    },
    methods: {
        async handleRegister() {
            console.log("Registering...");
            console.log(this.profilePhoto);
            let formData = new FormData();

            formData.append('profilePhoto', this.profilePhoto);
            formData.append('gender', this.gender);
            formData.append('age', this.age);

            await axiosAuth.post('/account/set-details', formData, {
                headers: {
                    // 'Content-Type': 'multipart/form-data',
                    'Content-type':'multipart/form-data', 
                }
            });
            this.$router.push('/activitycenter');
        },
        uploadImage(e) {
            const image = e.target.files[0];
            this.profilePhoto = image;
            const reader = new FileReader();
            reader.readAsDataURL(image);
            reader.onload = e =>{
                this.profilePreview = e.target.result;
            };
        }
    },
};
</script>

<template>
    <div class="registerbox-in">
        <form @submit.prevent="handleRegister">
            <div class="form-field">
                <img :src="profilePreview"/>
                <label for="profile-photo">Profile:</label>
                <input id="profile-photo" type="file" accept="image/jpeg" @change="uploadImage"/>
            </div>
            <div class="form-field">
                <label for="email">Gender:</label>
                <input class="text-input" id="Gender" v-model="gender" type="text"
                    required />
            </div>
            <div class="form-field">
                <label for="password">Age:</label>
                <input class="text-input" id="password" v-model="age" type="text"
                    placeholder="Enter your age" required />
            </div>
            <button type="submit" class="submit-button">Register</button>
        </form>
    </div>
</template>

<style scoped>
.registerbox-in {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 5px;
}

img {
    height: 30px;
    width: 30px;
}

</style>
