<script>
/* eslint-disable vue/no-unused-components */
/* eslint-disable no-unused-vars */
import MapViewerComponent from "@/components/MapViewer.vue";
import TrailInfoComponent from "@/components/TrailInfo.vue";
import axiosAuth from "@/api/axios-auth.js";

export default {
    name: "MyTrail",
    data() {
        return {
            trailID: null,
            mapWidth: null,
            mapHeight: null,
            trailDataReady: false,
            loadingTrailStats: true,
        };
    },
    methods: {
        calculateMapSize() {
            const mapContainer = document.getElementById("mapContainer");
            const myTrailContainer = document.getElementById("myTrailContainer");
            const trailStats = document.getElementById("trailStats");
            
            if (myTrailContainer && trailStats){
                this.mapWidth = mapContainer.getBoundingClientRect().width;
                this.mapHeight = mapContainer.getBoundingClientRect().height;
            }  else {
                console.error("Error calculating map size");
            }
        },
        initializeMap() {
            this.loadingTrailStats = false;
            this.$nextTick(() => {
                this.calculateMapSize();
            });
        }
    },
    created() {
        this.trailID = this.$route.query.trailID;
    },
    mounted() {

    },
    components: {
        MapViewerComponent,
        TrailInfoComponent,
    },
};
</script>

<template>
    <div class="my-trail-container d-flex flex-column" id="myTrailContainer">
        <div class="map-container" id="mapContainer" v-if="!loadingTrailStats">
            <MapViewerComponent v-if="mapHeight && mapWidth" :selectedTrails="[trailID]" :height="mapHeight" :width="mapWidth"/>
        </div>
        <TrailInfoComponent v-show="!loadingTrailStats" @trailDataChanged="initializeMap" :trailID="trailID" class="trail-stats px-3 py-2" id="trailStats"/>
        <div v-if="loadingTrailStats" class="loading-container">
            <h2>Loading trail data...</h2>
        </div>
    </div>
</template>

<style scoped>
.loading-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
}

.my-trail-container {
    height: 100%;
}

.map-container {
    background-color: var(--l1-color);
    border-radius: var(--border-radius);
    overflow: hidden;
    height: 100%;
}

.trail-stats {
    margin-top: 10px;
    background-color: var(--l1-color);
    border-radius: var(--border-radius);
    /* overflow: hidden; */
}
</style>