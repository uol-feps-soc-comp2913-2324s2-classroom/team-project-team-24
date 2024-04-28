<template>
    <div>
        <pie-chart
            :data="chartData"
            :options="chartOptions"
            ref="chart"
        ></pie-chart>
    </div>
</template>

<script>
import { Pie } from 'vue-chartjs'

export default {
    extends: Pie,
    props: {
        chartData: {
            type: Object,
            required: true,
        },
        chartOptions: {
            type: Object,
            default: () => {},
        },
    },
    mounted() {
        this.renderChart(this.chartData, this.chartOptions)
    },
}
</script>
