<template>
    <div class="map-container">
      <div v-html="mapHtml"></div>
    </div>
  </template>
  
  <script>
  import axiosAuth from "@/api/axios-auth";
  
  export default {
    name: "MapViewerComponent",
    props: {
      selectedTrails: {
        type: Array,
        required: true,
      },
    },
    created() {
        console.log("MapViewerComponent: selectedTrails prop:", this.selectedTrails);
    },
    data() {
      return {
        mapHtml: "",
      };
    },
    watch: {
      selectedTrails: {
        handler: "fetchSelectedTrails",
        immediate: true,
      },
    },
    methods: {
        async fetchSelectedTrails() {
    try {
      console.log('MapViewer: fetchSelectedTrails called with selectedTrails:', this.selectedTrails);
      const response = await axiosAuth.post("/trail/get-selected-map", {
        trailIDs: this.selectedTrails,
      });
      this.mapHtml = response.data.mapHtml;
    } catch (error) {
      console.error("Error fetching selected trails map:", error);
    }
  },
  },
}
  </script>

<style scoped>
.map-container {
    width: 70%;
    height: 20%;
}
</style>
