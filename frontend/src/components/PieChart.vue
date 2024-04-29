<template>
    <div>
        <canvas id="pieChart"></canvas>
    </div>
</template>

<script>
import Chart from 'chart.js/auto'
import config from '@/components/chart/pieChartConfig.js'

export default {
    mounted() {
        const ctx = document.getElementById('pieChart').getContext('2d')
        new Chart(ctx, config)
    },
}
</script>
