<template>
    <div class="stats-container">
        <h2>{{ name }}</h2>
        <p>{{ date }}</p>
        <div class="main-container">
            <div class="stat">
                <h4 class="monoText">{{ distance }} km</h4>
                <p class="smallerText">Total distance</p>
            </div>
            <div class="verticalLine mx-sm-5 mx-3"></div>
            <div v-if="hasTimeData" class="stat">
                <h4 class="monoText">{{ time.hours }}h {{ time.minutes }}m {{ time.seconds }}s</h4>
                <p class="smallerText">Time spent</p>
            </div>
            <div class="verticalLine mx-sm-5 mx-3"></div>
            <div v-if="hasTimeData" class="stat">
                <h4 class="monoText">{{ speed }} km/h</h4>
                <p class="smallerText">Average speed</p>
            </div>
        </div>
    </div>
</template>

<script>
import axiosAuth from "@/api/axios-auth.js";
export default {
    name: "TrailInfoComponent",
    data() {
        return {
            trailID: this.$route.query.trailID,
            name: "name",
            date: "",
            distance: 0.0,
            time: {
                hours: 0,
                minutes: 0,
                seconds: 0,
            },
            speed: 0.0,
            calories: 0,
            hasTimeData: true,
        };
    },
    methods: {
        getTrailData() {
            axiosAuth.post('/trail/get-data', {
                trailID: this.$route.query.trailID,
            }).then(
                response => {
                    this.name = response.data.name;
                    this.date = response.data.date;
                    this.distance = response.data.distance.toFixed(1);
                    this.time = response.data.time;
                    this.speed = response.data.speed.toFixed(2);
                    if (this.time == 0 || this.speed == 0) {
                        this.hasTimeData = false;
                    }
                    console.log("Trail data fetched")
                    this.$nextTick(() => {
                        this.$emit("trailDataChanged")
                    })
                }
            ).catch(() => { });
        }
    },
    created() {
        this.getTrailData();
    },
    mounted() {
    }
};
</script>


<style scoped>
h2{
    margin: 0;
}

h4{
    margin: 0;
}

p{
    margin: 0;
}

.verticalLine {
    background-color: #000000;
    width: 0.5px;
    height: auto;
}

.main-container {
    display: flex;
    flex-direction: row;
    justify-content: start;
    padding-top: 10px;
}

.stat {
    text-align: left;
    /* padding: 0 20px; */
    position: relative;
}

.loading-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
}

/* .stat:not(:last-child)::after {
    content: "";
    position: absolute;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
    height: 50%;
    width: 1px;
    background-color: #ccc;
} */
</style>