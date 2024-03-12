<template>
    <div>
        <div>
            <h4>Total duration this month:</h4>
            <p>{{ totalDuration.hours }}h{{ totalDuration.minutes }}m</p>
        </div>
        <div>
            <h4>Longest time:</h4>
            <p>{{ longestTime.hours }}h{{ totalDuration.minutes }}m</p>
        </div>
        <div>
            <h4>Total Calorie Consumption:</h4>
            <p>{{ totalCalories }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: "OverallTrailStatsComponent",
    data() {
        return {
            totalDuration: {
                hours: 10,
                minutes: 10
            },
            longestTime: {
                hours: 5,
                minutes: 30
            },
            totalCalories: 2000,
        };
    },
    methods: {
        
    },
};
</script>

