<template>
    <div class="my-trail-container">
      <div class="map-container">
        <MapViewerComponent :trailID="trailID" :selectedTrails="[trailID]" />
      </div>
      <div class="trail-stats">
        <TrailInfoComponent :trailID="trailID" />
      </div>
    </div>
  </template>
  
  <script>
  import MapViewerComponent from "@/components/MapViewer.vue";
  import TrailInfoComponent from "@/components/TrailInfo.vue";
  import axiosAuth from "@/api/axios-auth.js";
  
  export default {
    name: "MyTrail",
    data() {
      return {
        trailID: null,
      };
    },
    created() {
      this.trailID = this.$route.query.trailID;
      this.fetchTrailData();
    },
    methods: {
      async fetchTrailData() {
        try {
          const response = await axiosAuth.post("/trail/get-data", { trailID: this.trailID });
          // Update TrailInfoComponent with the fetched trail data
          this.$refs.trailInfo.updateTrailData(response.data);
        } catch (error) {
          console.error("Error fetching trail data:", error);
        }
      },
    },
    components: {
      MapViewerComponent,
      TrailInfoComponent,
    },
  };
  </script>
  
  <style scoped>
  .my-trail-container {
    display: flex;
    height: 100vh;
  }
  
  .map-container {
    flex: 2;
  }
  
  .trail-stats {
    flex: 1;
    padding: 1rem;
  }
  </style>