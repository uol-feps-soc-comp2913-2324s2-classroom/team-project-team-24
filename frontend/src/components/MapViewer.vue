<template>
    <div
        style="height: 100%; width: 100%"
        v-html="mapHtml"
        class="map-container"
    ></div>
    <div v-if="loading" class="loading-container">
        <h2>Loading map...</h2>
    </div>
</template>

<script>
import axiosAuth from '@/api/axios-auth'

export default {
    name: 'MapViewerComponent',
    props: {
        selectedTrails: {
            type: Array,
            required: true,
        },
        width: {
            type: Number,
        },
        height: {
            type: Number,
        },
        groupID: {
            type: Number,
        }
    },
    data() {
        return {
            mapHtml: '',
            loading: true,
            mapStyle: {
                width: this.width,
                height: '',
            },
        }
    },
    watch: {
        selectedTrails: {
            handler: 'fetchSelectedTrails',
            immediate: true,
        },
    },
    methods: {
        cancerousHeightFix() {
            // Fixes a stupid damned bug where the map doesn't fill the container
            // because the iframe is a inside a fudging div with height 0.
            // WHY DOES IT HAVE THAT? THAT IS SO DUMB I'VE WASTED HOURS OF MY LIFE ON THIS
            // I have no idea how to fix this properly but this works for now.
            const iframes = document.getElementsByTagName('iframe')
            for (let i = 0; i < iframes.length; i++) {
                iframes[i].style.height = '100%'
                iframes[i].parentNode.style.height = '100%'

                iframes[i].parentNode.parentNode.style.height = '100%'
                iframes[i].parentNode.parentNode.parentNode.style.height =
                    '100%'
            }
        },
        async fetchSelectedTrails() {
            try {
                let response
                if (this.width == null || this.height == null) {
                    console.log(
                        'Getting map without width and height specified'
                    )
                    response = await axiosAuth.post('/trail/get-selected-map', {
                        trailIDs: this.selectedTrails,
                        groupID: this.groupID,
                    });
                } else {
                    console.log(
                        'Getting map with width: ' +
                            this.width +
                            ' and height: ' +
                            this.height
                    )
                    response = await axiosAuth.post('/trail/get-selected-map', {
                        trailIDs: this.selectedTrails,
                        width: this.width,
                        height: this.height,
                        groupID: this.groupID,
                    });
                }
                this.mapHtml = response.data.mapHtml;
                this.$nextTick(() => {
                    this.cancerousHeightFix()
                })
                this.loading = false
            } catch (error) {
                console.error('Error fetching selected trails map:', error)
            }
        },
    },
}
</script>

<style scoped>
.map-container {
    width: 100%;
    height: 100% !important;
}

.loading-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
}
</style>
