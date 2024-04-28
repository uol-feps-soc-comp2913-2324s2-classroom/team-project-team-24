<template>
    <div class="user-info">
        <h2>Total users:</h2>
        <p>{{ numberOfUsers }}</p>
    </div>
    <div class="chart"></div>
    <PieChart />
</template>

<script>
// import PieChart from '@/components/PieChart.vue'

export default {
    name: 'UserInfo',
    // components: { PieChart },
    props: {
        numberOfUsers: {
            type: Number,
            required: true,
        },
    },
}
</script>

<style>
.user-info {
    background-color: #f9f9f9;
    padding: 20px;
    margin: 20px 0;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    text-align: center;
}
.user-info h2 {
    margin-bottom: 10px;
}
.user-info p {
    /* Your styles for the paragraph */
    font-size: 2em;
    margin: 0;
}
</style>
