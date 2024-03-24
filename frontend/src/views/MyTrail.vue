<script>
import MapViewerComponent from "@/components/MapViewer.vue";
import TrailInfoComponent from "@/components/TrailInfo.vue";

export default {
    name: "MyTrails",
    data() {
        return {
            trailID: this.$route.query.trailId,
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
        <MapViewerComponent v-bind:trailID="trailID"/>
        <TrailInfoComponent />
    </div>
</template>
<style scoped></style>
