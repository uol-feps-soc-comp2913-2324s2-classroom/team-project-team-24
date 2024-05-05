<template>
        <div v-html="mapHtml"></div>
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
                console.log("Width: " + this.width + " Height: " + this.height)

                if (this.width == null || this.height == null) {
                    console.log("requesting map without width and height")
                    response = await axiosAuth.post("/trail/get-selected-map", {
                        trailIDs: this.selectedTrails,
                    });
                } else {
                    console.log("requesting map with width" + this.width + " and height" + this.height)
                    response = await axiosAuth.post("/trail/get-selected-map", {
                        trailIDs: this.selectedTrails,
                        width: this.width,
                        height: this.height
                    });
                }
                this.mapHtml = response.data.mapHtml;
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
</style>
