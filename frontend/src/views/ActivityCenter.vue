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
            longestTrail: null,
        };
    },
    methods: {
        async getPageData() {
            await axiosAuth.get('/trail/get-all').then(
                response => {
                    this.trails = response.data.trails;
                }
            )
            // TODO: Get this to update the map element once completed
            await axiosAuth.get('/trail/get-longest').then(
                response => {
                    this.longestTrail = response.data.trailID;

                    console.log(this.longestTrail);
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
        <MapViewerComponent v-bind:trailID="longestTrail" />
        <OverallTrailStatsComponent />
        <TrailListComponent v-bind:trails="trails"/>
    </div>
</template>

<style scoped>
</style>
