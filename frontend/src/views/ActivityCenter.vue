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
    <div class="activityCenterPageContainer p-2">
        <div class="main-container">
            <div class="map-view-column p-3">
                <GoalComponent />
                <MapViewerComponent v-bind:trailID="longestTrailID" :key="longestTrailID" />
            </div>
            <div class="track-stats-column p-3">
                <OverallTrailStatsComponent />
            </div>
        </div>
        <div class="trails-container p-2">
            <ListComponent v-bind:dataArray="trails" v-slot="slotProps">
                <TrailListItemComponent :trailID="slotProps.data" />
            </ListComponent>
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
    flex: 2;
    /* Occupy 2/3 of the container */
    margin-right: 10px;
    /* Add some space between columns */
    background-color: var(--l1-color);
    border-radius: var(--border-radius);
    width: 100%;
    height: 100%;
}

.map-view-column iframe {
    flex: 1;
    /* Allow the iframe to grow to fill available space */
    width: 100%;
    /* Ensure the iframe takes full width of its container */
    border: none;
    /* Remove iframe border */
}

.track-stats-column {
    flex: 1;
    /* Occupy 1/3 of the container */
    margin-right: 10px;
    /* Add some space between columns */
    background-color: var(--l1-color);
    border-radius: var(--border-radius);
}

.trails-container {
    margin-top: 20px;
    margin-right: 10px;
    /* Add some space between columns */
    background-color: var(--l1-color);
    border-radius: var(--border-radius);
    width: 100%;
    height: 100%;
}
</style>