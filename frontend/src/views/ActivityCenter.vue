<script>
import MapViewerComponent from '@/components/MapViewer.vue'
// import GoalComponent from '@/components/Goal.vue'
import OverallTrailStatsComponent from '@/components/OverallTrailStats.vue'
import TrailListItemComponent from '@/components/lists/TrailListItem.vue'
import ListComponentNoDiv from '@/components/lists/ListNoDiv.vue'
import axiosAuth from '@/api/axios-auth.js'

export default {
    name: 'ActivityCenter',
    data() {
        return {
            trails: [],
            longestTrailID: null,
            selectedTrails: [],
            mapViewHeight: null,
            mapViewWidth: null,
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
                    height: this.mapViewHeight,
                    width: this.mapViewWidth,
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
            if (checked) {
                // Trail not already in the array, add it
                this.selectedTrails = [...this.selectedTrails, trailId]
            } else {
                // Trail already in the array, remove it
                this.selectedTrails = this.selectedTrails.filter(
                    (id) => id !== trailId
                )
            }
        },
        getMapDimensions() {
            const mapAndStatsContainer = document.getElementById('mapAndStatsContainer')
            const overAllTrailStatsComponent = document.getElementById('overAllTrailStatsComponent')
            if (mapAndStatsContainer && overAllTrailStatsComponent) {
                // this.mapViewHeight = mapAndStatsContainer.clientHeight - overAllTrailStatsComponent.clientHeight
                // this.mapViewWidth = mapAndStatsContainer.clientWidth
                this.mapViewHeight = mapAndStatsContainer.getBoundingClientRect().height - overAllTrailStatsComponent.getBoundingClientRect().height
                this.mapViewWidth = mapAndStatsContainer.getBoundingClientRect().width
            } else {
                console.error('Map div not found')
            }

            console.log('Map view height:', this.mapViewHeight)
            console.log('Map view width:', this.mapViewWidth)
            console.log('Map and stats container height:', mapAndStatsContainer.getBoundingClientRect().height)
            // console.log('Map and stats container width:', mapAndStatsContainer.getBoundingClientRect().width)

        },
    },
    components: {
        MapViewerComponent,
        // GoalComponent,
        ListComponentNoDiv,
        OverallTrailStatsComponent,
        TrailListItemComponent,
    },
    created() {
        this.getPageData()
    },
    mounted() {
        // Get the map view div width and height
        this.$nextTick(() => {
            this.getMapDimensions()
        })
    }
}
</script>

<template>
    <div class="activityCenterPageContainer">
        <div class="map-and-stats-container d-flex flex-column" id="mapAndStatsContainer">
            <div class="map-view" id="mapDiv">
                <!-- <GoalComponent /> -->
                <MapViewerComponent
                    v-if="mapViewHeight && mapViewWidth"
                    :selected-trails="selectedTrails"
                    ref="mapViewer"
                    :height="mapViewHeight"
                    :width="mapViewWidth"
                    class="mapViewerComponent"
                />
            </div>
            <div class="d-flex flex-row align-items-center justify-content-between px-4 py-2" id="overAllTrailStatsComponent">
                <h2>My trails</h2>
                <OverallTrailStatsComponent/>
            </div>
        </div>
        <div class="trails-container scrollableList">
            <table class="trailsListTable">
                <ListComponentNoDiv v-bind:dataArray="trails" v-slot="slotProps">
                    <TrailListItemComponent
                    :trail="slotProps.data"
                    @trail-deleted="handleTrailDeleted"
                    @trail-selected="handleTrailSelected"
                    @zoom-to-trail="handleZoomToTrail"
                    />
                </ListComponentNoDiv>
            </table>
        </div>
    </div>
</template>


<style scoped>

#mapDiv{
    width: 100%;
    height: 100%;
}

h2 {
    margin: 0;
}

.friendItem {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    transition: box-shadow 0.2s;
    transition: background-color 0.2s;
}



.slightlySmaller {
    width: 99.5%;
    margin-left: 1px;
}

.scrollableList {
    padding-top: 1px;
    overflow-y: auto;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.mapViewerComponent {
    width: 100%;
    height: 100%;
    filter: drop-shadow(0px 0px 5px rgba(0, 0, 0, 0.5));
}

.activityCenterPageContainer{
    display: grid;
    grid-template-rows: 2fr 1fr;
    row-gap: 10px;
}

.map-and-stats-container {
    border-radius: var(--border-radius);
    background-color: var(--l1-color);
    overflow: hidden;
}

.map-view {
    
    /* flex: 2; Occupy 2/3 of the container */
    /* margin-right: 10px; Add some space between columns */
    margin: 0;
    overflow: hidden;
    border-radius: var(--border-radius);
    height: 100%;
}

.track-stats-column {
    flex: 1; /* Occupy 1/3 of the container */
    margin-right: 10px; /* Add some space between columns */
    background-color: var(--l1-color);
    border-radius: var(--border-radius);
}

.trails-container {
    /* margin-top: 10px;
    margin-right: 10px; */
    background-color: var(--l1-color);
    border-radius: var(--border-radius);
    box-sizing: border-box;
    /* width: 100%;
    height: 100%; */
}

table{
    width: 100%;
}

.width100{
    width: 100%;
}
</style>
