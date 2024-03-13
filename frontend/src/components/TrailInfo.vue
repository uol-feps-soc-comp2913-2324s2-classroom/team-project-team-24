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
export default {
    name: "TrailInfoComponent",
    data() {
        return {
            trailId: this.$route.query.trail,
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
            // Call to db and get all needed info
        }
    },
};
</script>

