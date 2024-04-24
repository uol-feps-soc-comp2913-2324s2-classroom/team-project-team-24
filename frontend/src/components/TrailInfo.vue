<template>
    <h2>{{ name }}</h2>
    <i>{{ date }}</i>
    <div style="display:flex;">
        <div>
            <h4>{{ distance }} Km</h4>
            <p>Total distance</p>
            
        </div>
        <div>
            <h4>{{ time.hours }}h {{ time.minutes }}m {{ time.seconds }}s</h4>
            <p>Time spent</p>
        </div>
        <div>
            <h4>{{ speed }} km/h</h4>
            <p>Average speed</p>
        </div>
        <div>
            <h4>{{ calories }} cal</h4>
            <p>Calories</p>
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
            calories: 0
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
                    this.distance = response.data.distance;
                    this.time = response.data.time;
                    this.speed = response.data.speed;
                    this.calories = response.data.calories;
                }
            ).catch(error => {
                console.log("error");
                console.log(error.response.data.error);
            })
        }
    },
    created() {
        this.getTrailData();
    }
};
</script>

