<template>
    <div>
        <canvas id="lineChart"></canvas>
    </div>
</template>

<script>
import Chart from 'chart.js/auto'
import config from '@/components/chart/lineChartConfig.js'

export default {
    mounted() {
        const ctx = document.getElementById('lineChart').getContext('2d')
        new Chart(ctx, config)
    },
}
</script>
