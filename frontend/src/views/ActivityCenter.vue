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
    <div class="activityCenterPageContainer">
        <h1>Activity Center Page</h1>
        <GoalComponent />
        <MapViewerComponent />
        <OverallTrailStatsComponent />
        <TrailListComponent v-bind:trails="trails"/>
    </div>
</template>

<style scoped>
</style>
