<template>
    <div class="map-container">
      <div v-for="(mapHtml, index) in mapHtmls" :key="index">
        <input type="checkbox" :id="'map-' + index" v-model="selectedMaps" :value="index" />
        <label :for="'map-' + index">Trail {{ index + 1 }}</label>
        <div v-if="selectedMaps.includes(index)" v-html="mapHtml"></div>
      </div>
    </div>
  </template>
  
  <script>
  import axiosAuth from "@/api/axios-auth";
  
  export default {
    name: 'MapViewerComponent',
    data() {
      return {
        mapHtmls: [],
        selectedMaps: [],
      };
    },
    async mounted() {
      try {
        // Fetch the user's trails from the server
        const response = await axiosAuth.get('/trail/get-all');
        const trailIDs = response.data.trails;
  
        // Iterate over each trail ID and fetch the map HTML
        for (const trailID of trailIDs) {
          const mapResponse = await axiosAuth.post('/trail/get-map', {
            trailID: trailID,
          });
  
          const mapHtml = mapResponse.data;
          this.mapHtmls.push(mapHtml);
        }
      } catch (error) {
        console.error('Error fetching trail maps:', error);
      }
    },
  };
  </script>
  
  <style scoped>
  .map-container {
    width: 100%;
    height: 600px;
  }
  </style>