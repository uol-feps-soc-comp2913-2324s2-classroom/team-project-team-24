<template>
    <div class="d-flex flex-row">
        <div class="stats-group d-flex flex-column align-items-start me-5">
            <h3 class="my-0 monoText">{{ totalDuration.hours }}h {{ totalDuration.minutes }}m</h3>
            <p class="smallerText my-0">Total duration</p>
        </div>
        <div class="verticalLine"></div>
        <div class="stats-group d-flex flex-column align-items-start ms-5 me-4">
            <h3 class="my-0 monoText">{{ longestTime.hours }}h {{ longestTime.minutes }}m</h3>
            <p class="smallerText my-0">Longest time</p>
        </div>
    </div>
</template>

<script>
import axiosAuth from "@/api/axios-auth.js"
export default {
    name: "OverallTrailStatsComponent",
    data() {
        return {
            totalDuration: {
                hours: 0,
                minutes: 0
            },
            longestTime: {
                hours: 0,
                minutes: 0
            },
        };
    },
    methods: {
        getPageData() {
            axiosAuth.get('/trail/get-overall-stats').then(
                response => {
                    this.totalDuration = response.data.totalDuration;
                    this.longestTime = response.data.longestTime;
                }
            )
        }
    },
    created() {
        this.getPageData();
    }
};
</script>

<style scoped>
.verticalLine {
    background-color: #000000;
    width: 0.5px;
}

.smallerText {
    font-size: 0.8rem;
}

.stats-group {}

.monoText {
    font-family: 'Roboto Mono', monospace;
}
</style>