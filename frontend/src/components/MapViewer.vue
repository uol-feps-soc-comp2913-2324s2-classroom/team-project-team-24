<template>
    <div>
      <iframe :src="mapUrl" frameborder="0" style="width: 100%; height: 500px;"></iframe>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'MapViewer',
    data() {
      return {
        mapUrl: null,
      };
    },
    async mounted() {
      try {
        const response = await axios.get(`http://localhost:${process.env.VUE_APP_BACKEND_PORT}/core/map`);
        const mapHtml = response.data;
        const blob = new Blob([mapHtml], { type: 'text/html' });
        this.mapUrl = URL.createObjectURL(blob);
      } catch (error) {
        console.error('Error fetching map:', error);
      }
    },
  };
  </script>