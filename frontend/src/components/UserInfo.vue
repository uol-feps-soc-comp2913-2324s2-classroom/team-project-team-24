<template>
    <div>
        <div class="chart">
            <PieChart />
        </div>
        <div class="user-info">
            <h4>Total users:</h4>
            <p>{{ numberOfUsers }}</p>
        </div>
    </div>
</template>

<script>
import PieChart from '@/components/PieChart.vue'

export default {
    name: 'UserInfo',
    components: { PieChart },
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
    background-color: transparent;
    padding: 20px;
    margin: 20px 0;
    border-radius: 10px;
    text-align: center;
    border: none;
}
.user-info h2 {
    margin-bottom: 10px;
}
.user-info p {
    /* Your styles for the paragraph */
    font-size: 2em;
    margin: 0;
}

.chart {
    width: 400px;
    height: 400px;
    margin: 0 auto;
    margin-top: 50px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    background-color: #f9f9f9;
    display: flex;
    justify-content: center;
    align-items: center;
    border: none;
}
</style>
