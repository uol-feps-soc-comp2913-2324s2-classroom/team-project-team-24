<script>
import MapViewerComponent from "@/components/MapViewer.vue";
import TrailInfoComponent from "@/components/TrailInfo.vue";

export default {
    name: "MyTrails",
    data() {
        return {
            trailName: this.$route.query.trailName,
        };
    },
    methods: {

    },
    components: {
        MapViewerComponent,
        TrailInfoComponent,
    },
};
</script>

<template>
    <div class="myTrailsPageContainer">
        <MapViewerComponent />
        <TrailInfoComponent />
    </div>
</template>

<style scoped></style>
