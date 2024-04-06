<script>
import MapViewerComponent from "@/components/MapViewer.vue";
import GoalComponent from "@/components/Goal.vue";
import OverallTrailStatsComponent from "@/components/OverallTrailStats.vue";
import TrailListComponent from "@/components/lists/TrailList.vue";

export default {
    name: "ActivityCenter",
    data() {
        return {
            trails: ["trail1", "trail2", "trail3", "trail4"],
        };
    },
    methods: {

    },
    components: {
        MapViewerComponent,
        GoalComponent,
        OverallTrailStatsComponent,
        TrailListComponent,
    },
};
</script>

<template>
    <div class="activityCenterPageContainer p-2">
        <div class="main-container">
            <div class="map-view-column p-3">
                <GoalComponent />
                <MapViewerComponent />
            </div>
            <div class="track-stats-column p-3">
                <OverallTrailStatsComponent />
            </div>
        </div>
        <div class="trails-container p-2">
          <TrailListComponent :trails="trails" />
        </div>
    </div>
</template>

<style scoped>
.activityCenterPageContainer {
  display: flex;
  flex-direction: column;
}

.main-container {
  display: flex;
  height: 80vh;
}

.map-view-column {
  flex: 2; /* Occupy 2/3 of the container */
  margin-right: 10px; /* Add some space between columns */
  background-color: var(--l1-color);
  border-radius: var(--border-radius);
  width: 100%;
  height: 100%;
}

.track-stats-column {
  flex: 1; /* Occupy 1/3 of the container */
  margin-right: 10px; /* Add some space between columns */
  background-color: var(--l1-color);
  border-radius: var(--border-radius);
  
}

.trails-container {
  margin-top: 20px;
  margin-right: 10px; /* Add some space between columns */
  background-color: var(--l1-color);
  border-radius: var(--border-radius);
  width: 100%;
  height: 100%;
}
</style>