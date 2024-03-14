<script>
import UploadGPX from '@/components/UploadGPX.vue';
export default {
  name: "MyTrails",
  data() {
    return {

    };
  },
  methods: {

  },
  components: {
    UploadGPX
  },
};
</script>

<template>
  <div class="myTrailsPageContainer">
    <h1>Upload your new trail</h1>
    <UploadGPX />
  </div>
</template>
<style scoped></style>
