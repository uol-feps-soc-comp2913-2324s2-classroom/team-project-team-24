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
export default {
  name: "OverallTrailStatsComponent",
  data() {
    return {
      totalDuration: {
        hours: 10,
        minutes: 10
      },
      longestTime: {
        hours: 5,
        minutes: 30
      },
    };
  },
  methods: {},
};
</script>
  
  <style scoped>
  .stats-group {
    margin-bottom: 20px; /* Add margin-bottom to create space between groups */
    border-bottom: 1px solid #ccc; /* Add border-bottom to distinguish groups */
  }
  </style>
  