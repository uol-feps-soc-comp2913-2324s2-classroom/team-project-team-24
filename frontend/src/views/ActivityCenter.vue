<template>
    <div class="activityCenterPageContainer p-2">
        <div class="main-container">
            <div class="map-view-column p-3">
                <GoalComponent />
                <MapViewerComponent
                    :selected-trails="selectedTrails"
                    ref="mapViewer"
                />
            </div>
            <div class="track-stats-column p-3">
                <OverallTrailStatsComponent />
            </div>
        </div>
        <div class="trails-container p-2">
            <ListComponent v-bind:dataArray="trails" v-slot="slotProps">
                <TrailListItemComponent
                    :trail="slotProps.data"
                    @trail-deleted="handleTrailDeleted"
                    @trail-selected="handleTrailSelected"
                    @zoom-to-trail="handleZoomToTrail"
                />
            </ListComponent>
        </div>
    </div>
</template>

<script>
import MapViewerComponent from '@/components/MapViewer.vue'
import GoalComponent from '@/components/Goal.vue'
import OverallTrailStatsComponent from '@/components/OverallTrailStats.vue'
import TrailListItemComponent from '@/components/lists/TrailListItem.vue'
import ListComponent from '@/components/lists/List.vue'
import axiosAuth from '@/api/axios-auth.js'

export default {
    name: 'ActivityCenter',
    data() {
        return {
            trails: [],
            longestTrailID: null,
            selectedTrails: [],
        }
    },
    methods: {
        async getPageData() {
            try {
                const response1 = await axiosAuth.get('/trail/get-all')
                this.trails = response1.data.trails

                const response2 = await axiosAuth.get('/trail/get-longest')
                this.longestTrailID = response2.data.trailID
            } catch (error) {
                console.error('Error fetching page data:', error)
            }
        },
        handleTrailDeleted(trailId) {
            // Remove the deleted trail from the trails array
            this.trails = this.trails.filter((trail) => trail.id !== trailId)

            // Remove the deleted trail from the selectedTrails array
            this.selectedTrails = this.selectedTrails.filter(
                (id) => id !== trailId
            )

            // Trigger the fetchSelectedTrails method to update the map
            this.$refs.mapViewer.fetchSelectedTrails()
        },
        handleZoomToTrail(trailId) {
            axiosAuth
                .post('/trail/zoom-to-trail', {
                    trailID: trailId,
                    selectedTrailIDs: this.selectedTrails,
                })
                .then((response) => {
                    this.$refs.mapViewer.mapHtml = response.data.mapHtml
                })
                .catch((error) => {
                    console.error('Error zooming to trail:', error)
                })
        },
        handleTrailSelected({ trailId, checked }) {
            console.log(
                'ActivityCenter: handleTrailSelected called with trailId:',
                trailId,
                'checked:',
                checked
            )
            console.log(
                'ActivityCenter: selectedTrails before update:',
                this.selectedTrails
            )

            if (checked) {
                // Trail not already in the array, add it
                this.selectedTrails = [...this.selectedTrails, trailId]
            } else {
                // Trail already in the array, remove it
                this.selectedTrails = this.selectedTrails.filter(
                    (id) => id !== trailId
                )
            }

            console.log(
                'ActivityCenter: selectedTrails after update:',
                this.selectedTrails
            )
        },
    },
    components: {
        MapViewerComponent,
        GoalComponent,
        OverallTrailStatsComponent,
        TrailListItemComponent,
        ListComponent,
    },
    created() {
        this.getPageData()
    },
}
</script>

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
    flex: 2; /* Occupy 2/3 of the container */
    margin-right: 10px; /* Add some space between columns */
    background-color: var(--l1-color);
    border-radius: var(--border-radius);
    width: 100%;
    height: 100%;
}

.map-view-column iframe {
    flex: 1; /* Allow the iframe to grow to fill available space */
    width: 100%; /* Ensure the iframe takes full width of its container */
    border: none; /* Remove iframe border */
}

.track-stats-column {
    flex: 1; /* Occupy 1/3 of the container */
    margin-right: 10px; /* Add some space between columns */
    background-color: var(--l1-color);
    border-radius: var(--border-radius);
}

.trails-container {
    margin-top: 20px;
    margin-right: 10px; /* Add some space between columns */
    background-color: var(--l1-color);
    border-radius: var(--border-radius);
    width: 100%;
    height: 100%;
}
</style>
