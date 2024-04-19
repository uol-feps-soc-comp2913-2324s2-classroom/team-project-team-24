<script>
import '@/assets/css/form.css'
import textInputQuiet from '@/components/ui-components/textInputQuiet.vue'
import primaryButton from '@/components/ui-components/primaryButton.vue'

export default {
    name: 'RegisterForm2Component',
    components: {
        textInputQuiet,
        primaryButton,
    },
    data() {
        return {
            profilePreview: null,
            gender: '',
            age: '',
        }
    },
    methods: {
        async handleRegister() {
            console.log('Registering...')
            //this.$parent.clicked()
            this.$emit('registrationSuccessful')
        },
        uploadImage(e) {
            const image = e.target.files[0]
            const reader = new FileReader()
            reader.readAsDataURL(image)
            reader.onload = (e) => {
                this.profilePreview = e.target.result
            }
        },
    },
}
</script>

<template>
    <div class="registerbox-in">
        <form @submit.prevent="handleRegister">
            <div class="form-field go-to-login">
                <span>Already have an account?</span> &nbsp;
                <a href="#" @click="alreadyHaveAccount">Login</a>
            </div>

            <div class="form-field profile">
                <img
                    :src="profilePreview"
                    class="profile-preview"
                    alt="Profile Picture Preview"
                />
                <div class="profile-upload">
                    <label for="profile-photo"
                        >Profile picture <i class="bi bi-upload"></i>
                    </label>
                    <input
                        id="profile-photo"
                        type="file"
                        accept="image/jpeg"
                        @change="uploadImage"
                        class="file-input"
                    />
                </div>
            </div>

            <div class="form-field">
                <label for="email">Gender</label>
                <textInputQuiet
                    width="100%"
                    class="text-input"
                    id="Gender"
                    v-model="text"
                    type="text"
                    required
                ></textInputQuiet>
            </div>
            <div class="form-field">
                <label for="password">Age</label>
                <textInputQuiet
                    width="100%"
                    class="text-input"
                    id="password"
                    v-model="text"
                    type="text"
                ></textInputQuiet>
            </div>
            <div class="submit-button-container">
                <primaryButton type="submit" class="submit-button"
                    >Register</primaryButton
                >
            </div>
        </form>
    </div>
</template>

<style scoped>
.registerbox-in {
    max-width: 500px; /* Adjust as needed for your design */
    margin: 0 auto; /* This centers the container */
    padding: 20px; /* Adjust as needed for your design */
    box-sizing: border-box;
}

.registerbox-in a {
    text-decoration: none;
}

.form-field input,
.submit-button-container button {
    box-sizing: border-box; /* Padding and border are included in the width */
    width: 40%;
}

.submit-button-container {
    display: flex;
    justify-content: flex-end;
}

.form-field {
    margin-bottom: 40px;
}
.go-to-login {
    margin-bottom: 30px;
}
.profile-preview {
    border-radius: 50%;
    width: 80px;
    height: 80px; /* size for the preview */
    background-color: #ddd;
    display: block; /* Center the image preview in the form */
    margin-bottom: 1rem;
}

.profile {
    display: flex;
    align-items: center;
    gap: 50px;
}

.profile-upload {
    display: flex;
    align-items: center;
    cursor: pointer;
}

img {
    height: 30px;
    width: 30px;
}

.file-input {
    opacity: 0;
    position: absolute;
    z-index: -1;
    width: 1px;
    height: 1px;
    overflow: hidden;
}

.upload-label {
    display: inline-flex;
    align-items: center;
    cursor: pointer;
}

.bi-upload {
    font-size: 1.5rem;
    margin-right: 0.5rem;
}
</style>
