<template>
    <div class="map-container">
      <div v-for="(trail, index) in trails" :key="index">
        <input type="checkbox" :id="'trail-' + index" v-model="selectedTrails" :value="trail.id" />
        <label :for="'trail-' + index">{{ trail.name }}</label>
      </div>
      <button @click="fetchSelectedTrailsMap">Generate Map</button>
      <div v-if="mapHtml" v-html="mapHtml"></div>
    </div>
  </template>
  
  <script>
  import axiosAuth from "@/api/axios-auth";
  
  export default {
    name: 'MapViewerComponent',
    data() {
      return {
        trails: [],
        selectedTrails: [],
        mapHtml: '',
      };
    },
    async mounted() {
      try {
        // Fetch the user's trails from the server
        const response = await axiosAuth.get('/trail/get-all');
        this.trails = response.data.trails;
      } catch (error) {
        console.error('Error fetching trails:', error);
      }
    },
    methods: {
      async fetchSelectedTrailsMap() {
        try {
          const response = await axiosAuth.post('/trail/get-selected-map', {
            trailIDs: this.selectedTrails,
          });
          this.mapHtml = response.data.mapHtml;
        } catch (error) {
          console.error('Error fetching selected trails map:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .map-container {
    width: 100%;
    height: 600px;
  }
  </style>