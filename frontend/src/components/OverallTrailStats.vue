<template>
  <div>
    <div class="stats-group">
      <p>Total duration this month:</p>
      <h4>{{ totalDuration.hours }}h{{ totalDuration.minutes }}m</h4>
    </div>
    <div class="stats-group">
      <p>Longest time:</p>
      <h4>{{ longestTime.hours }}h{{ longestTime.minutes }}m</h4>
    </div>
  </div>
</template>
  
<script>
import axiosAuth from "@/api/axios-auth.js"
export default {
  name: "OverallTrailStatsComponent",
  data() {
    return {
      totalDuration: {
        hours: 0,
        minutes: 0
      },
      longestTime: {
        hours: 0,
        minutes: 0
      },
    };
  },
  methods: {
    getPageData() {
      axiosAuth.get('/trail/get-overall-stats').then(
        response => {
          this.totalDuration = response.data.totalDuration;
          this.longestTime = response.data.longestTime;
        }
      )
    }
  },
  created() {
    this.getPageData();
  }
};
</script>
  
  <style scoped>
  .stats-group {
    margin-bottom: 20px; /* Add margin-bottom to create space between groups */
    border-bottom: 1px solid #ccc; /* Add border-bottom to distinguish groups */
  }
  </style>
  