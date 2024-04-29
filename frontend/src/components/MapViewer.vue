<template>
    <div class="map-container">
        <div v-for="(trail, index) in trails" :key="index" class="trail-item">
            <input
                type="checkbox"
                :id="'trail-' + index"
                v-model="selectedTrails"
                :value="trail.id"
            />
            <label :for="'trail-' + index" class = trail-label>{{ trail.name }}</label>
            <button class="btn-tertiary zoom-button"
                v-if="selectedTrails.includes(trail.id)"
                @click="zoomToTrail(trail.id)"
            >
                Zoom
            </button>
        </div>
        <div v-if="mapHtml" v-html="mapHtml"></div>

    </div>
</template>

<script>
import axiosAuth from '@/api/axios-auth'

export default {
    name: 'MapViewerComponent',
    data() {
        return {
            trails: [],
            selectedTrails: [],
            mapHtml: '',
        }
    },
    async mounted() {
        try {
            const response = await axiosAuth.get('/trail/get-all')
            this.trails = response.data.trails
        } catch (error) {
            console.error('Error fetching trails:', error)
        }
    },
    watch: {
        selectedTrails: {
            handler: 'fetchSelectedTrailsMap',
            immediate: true,
        },
    },
    methods: {
        async fetchSelectedTrailsMap() {
            try {
                const response = await axiosAuth.post(
                    '/trail/get-selected-map',
                    {
                        trailIDs: this.selectedTrails,
                    }
                )
                this.mapHtml = response.data.mapHtml
            } catch (error) {
                console.error('Error fetching selected trails map:', error)
            }
        },
        async zoomToTrail(trailId) {
            try {
                const response = await axiosAuth.post('/trail/zoom-to-trail', {
                    trailID: trailId,
                    selectedTrailIDs: this.selectedTrails,
                })
                this.mapHtml = response.data.mapHtml
            } catch (error) {
                console.error('Error zooming to trail:', error)
            }
        },
    },
}
</script>

<style scoped>
.map-container {
    width: 70%;
    height: 20%;
}

.trail-item {
    margin-bottom: 8px;
}

.trail-label {
    margin-right: 6px; /* adjust spacing between zoom and route name */
}

.zoom-button {
    margin-left: 6px; /* also to adjust spacing between zoom and route name */
}
</style>
