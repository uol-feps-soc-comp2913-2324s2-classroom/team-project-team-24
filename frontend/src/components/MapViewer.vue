<template>
        <div v-html="mapHtml"></div>
        <div v-if="loading" class="loading-container">
            <h2>Loading map...</h2>
        </div>
        <!-- <h2 v-if="loading">Loading...</h2> -->
</template>

<script>
import axiosAuth from "@/api/axios-auth";

export default {
    name: "MapViewerComponent",
    props: {
        selectedTrails: {
            type: Array,
            required: true,
        },
        width: {
            type: String
        },
        height: {
            type: String
        }
    },
    data() {
        return {
            mapHtml: "",
            loading: true,
        };
    },
    watch: {
        selectedTrails: {
            handler: "fetchSelectedTrails",
            immediate: true,
        },
    },
    methods: {
        async fetchSelectedTrails() {
            try {
                let response;
                if (this.width == null || this.height == null) {
                    response = await axiosAuth.post("/trail/get-selected-map", {
                        trailIDs: this.selectedTrails,
                    });
                } else {
                    response = await axiosAuth.post("/trail/get-selected-map", {
                        trailIDs: this.selectedTrails,
                        width: this.width,
                        height: this.height
                    });
                }
                this.mapHtml = response.data.mapHtml;
                this.loading = false;
            } catch (error) {
                console.error("Error fetching selected trails map:", error);
            }
        },
    },
}
</script>

<style scoped>
.map-container {
    width: 100%;
    height: 100%;
}

.loading-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
}
</style>
