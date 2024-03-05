<script>
import HelloWorld from "./components/HelloWorld.vue";
import axios from "axios";
import Login from "./components/Login.vue";
import Register from "./components/Register.vue";
import UploadGPX from "./components/UploadGPX.vue";

export default {
  name: "App",
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
      APIResponse: "",
    };
  },
  methods: {
    async testApi() {
      try {
        const response = await axios.get(
          `http://localhost:${process.env.VUE_APP_BACKEND_PORT}/`
        );
        this.APIResponse = response.data;
        console.log(this.APIResponse);
        console.log(process.env.VUE_APP_BACKEND_PORT);
      } catch (error) {
        this.APIResponse = "Error: " + error;
        console.error(error);
      }
    },
  },
  components: {
    HelloWorld,
    Login,
    Register,
    UploadGPX,
  },
};
</script>

<template>
  <div>
    <p>{{ msg }}</p>
  </div>
  <HelloWorld msg="Vite + Vue" />

  <button @click="testApi">Test API</button>
  <p>API Response: {{ APIResponse }}</p>
  <UploadGPX></UploadGPX>
  <Login></Login>
  <Register></Register>
</template>

<style scoped></style>
