<template>
    <div>
        <iframe :src="mapUrl" frameborder="0" style="width: 100%; height: 500px;"></iframe>
    </div>
</template>

<script>
import axiosAuth from "@/api/axios-auth"

export default {
    name: 'MapViewerComponent',
    props: {
        trailID: {
            
        }
    },
    data() {
        return {
            mapUrl: null,
        };
    },
    async mounted() {
        try {
            console.log(this.trailID);
            const response = await axiosAuth.post(`/trail/get-map`, {
                trailID: this.trailID,
            }).catch(
                error => {
                    console.log(error);
                }
            );
            const mapHtml = response.data;
            const blob = new Blob([mapHtml], { type: 'text/html' });
            this.mapUrl = URL.createObjectURL(blob);
        } catch (error) {
            console.error('Error fetching map:', error);
        }
    },
};
</script>