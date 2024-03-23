<script>
import MapViewerComponent from "@/components/MapViewer.vue";
import GoalComponent from "@/components/Goal.vue";
import OverallTrailStatsComponent from "@/components/OverallTrailStats.vue";
import TrailListComponent from "@/components/lists/TrailList.vue";
import axiosAuth from "@/api/axios-auth.js";

export default {
    name: "ActivityCenter",
    data() {
        return {
            trails: [],
        };
    },
    methods: {
        getPageData() {
            axiosAuth.get('/get-trails').then(
                response => {
                    this.trails = response.data.trails;
                }
            )
        }
    },
    components: {
        MapViewerComponent,
        GoalComponent,
        OverallTrailStatsComponent,
        TrailListComponent,
    },
    created() {
        this.getPageData();
    }
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
