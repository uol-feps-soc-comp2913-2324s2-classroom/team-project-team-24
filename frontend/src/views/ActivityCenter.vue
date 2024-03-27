<script>
import MapViewerComponent from "@/components/MapViewer.vue";
import GoalComponent from "@/components/Goal.vue";
import OverallTrailStatsComponent from "@/components/OverallTrailStats.vue";
import TrailListItemComponent from "@/components/lists/TrailListItem.vue";
import ListComponent from "@/components/lists/List.vue";
import axiosAuth from "@/api/axios-auth.js";

export default {
    name: "ActivityCenter",
    data() {
        return {
            trails: [],
            longestTrailID: null,
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
                    this.longestTrailID = response.data.trailID;

                    console.log(this.longestTrail);
                }
            )
        }
    },
    components: {
        MapViewerComponent,
        GoalComponent,
        OverallTrailStatsComponent,
        TrailListItemComponent,
        ListComponent,
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
        <MapViewerComponent v-bind:trailID="longestTrailID" :key="longestTrailID" />
        <OverallTrailStatsComponent />
        <ListComponent v-bind:dataArray="trails" v-slot="slotProps">
            <TrailListItemComponent v-bind:trailID="slotProps.data"/>
        </ListComponent>
    </div>
</template>

<style scoped>
</style>
