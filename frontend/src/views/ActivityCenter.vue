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
    <div class="activityCenterPageContainer p-5">
        <div class="top-container">
        <GoalComponent />
        </div>
        <div class="main-container">
            <div class="left-column">
                <MapViewerComponent />
            </div>
            <div class="right-column">
                <OverallTrailStatsComponent />
            </div>
        </div>
        <div class="bottom-container">
        <TrailListComponent :trails="trails" />
        </div>
    </div>
</template>

<style scoped>
.activityCenterPageContainer {
  display: flex;
  flex-direction: column;
}

.top-container {
  margin-bottom: 20px;
}

.main-container {
  display: flex;
}

.left-column {
  flex: 2; /* Occupy 2/3 of the container */
  margin-right: 10px; /* Add some space between columns */
}

.right-column {
  flex: 1; /* Occupy 1/3 of the container */
}

.bottom-container {
  margin-top: 20px;
}
</style>