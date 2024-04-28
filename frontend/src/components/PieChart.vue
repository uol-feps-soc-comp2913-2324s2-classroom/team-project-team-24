<!-- // MyChartComponent.vue
<template>
    <div>
        <bar
            type="pie"
            width="380"
            :options="chartOptions"
            :series="series"
        ></bar>
    </div>
</template>

<script>
import { defineComponent } from 'vue'
import { Bar } from 'vue3-chart-v2'

export default defineComponent({
    name: 'MonthlyChart',
    extends: Bar,
    mounted() {
        // Overwriting base render method with actual data.
        this.renderChart({
            labels: [
                'January',
                'February',
                'March',
                'April',
                'May',
                'June',
                'July',
                'August',
                'September',
                'October',
                'November',
                'December',
            ],
            datasets: [
                {
                    label: 'GitHub Commits',
                    backgroundColor: '#f87979',
                    data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11],
                },
            ],
        })
    },
})
</script> -->

<!-- <template>
    <div class="pie-chart-container">
        <canvas id="pie-chart"></canvas>
    </div>
</template>

<script>
import { Pie } from 'vue-chartjs'

export default {
    extends: Pie,
    props: {
        data: Object,
    },
    mounted() {
        this.renderChart(this.data, this.options)
    },
}
</script>

<style>
/* .pie-chart-container {
    // 你可以在这里添加样式
} */
</style> -->

<!-- <template>
    <div>
        <apexchart
            width="400"
            type="pie"
            :options="chartOptions"
            :series="series"
        ></apexchart>
    </div>
</template>

<script>
import VueApexCharts from 'vue3-apexcharts'

export default {
    extends: Pie,
    mounted() {
        this.renderChart(this.chartData, this.options);
    }
    components: {
        apexchart: VueApexCharts,
    },
    data() {
        return {
            chartOptions: {
                chart: {
                    type: 'pie',
                },
                labels: ['Apple', 'Banana', 'Orange', 'Mango', 'Grapes'],
            },
            series: [44, 55, 13, 43, 22],
        }
    },
}
</script> -->

<!-- <template>
    <div>
        <pie-chart></pie-chart>
    </div>
</template>

<script>
import { Pie } from 'vue-chartjs'

export default {
    components: {
        PieChart: Pie,
    },
    data() {
        return {
            chartData: {
                labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple'],
                datasets: [
                    {
                        label: '# of Votes',
                        data: [12, 19, 3, 5, 2],
                        backgroundColor: [
                            'Red',
                            'Blue',
                            'Yellow',
                            'Green',
                            'Purple',
                        ],
                    },
                ],
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
            },
        }
    },
    mounted() {
        this.renderChart(this.chartData, this.options)
    },
}
</script> -->

<!-- <template>
    <div>
        <pie :data="chartData" :options="options"></pie>
        <p>hahahahahha</p>
        <p>如果你能看到这行文字，PieChart 组件就被正确插入了。</p>
    </div>
</template>

<script>
import { Pie } from 'vue-chartjs'
import { defineComponent } from 'vue'

export default defineComponent({
    name: 'PieChart',
    components: {
        Pie, // This should match the name used when importing from vue-chartjs
    },
    props: {
        chartData: {
            type: Object,
            required: true,
        },
        options: {
            type: Object,
            required: true,
        },
    },
    mounted() {
        this.renderChart(this.chartData, this.options)
    },
    methods: {
        renderChart(data, options) {
            // You need to call this method to actually render the chart
            this.$refs.chart && this.$refs.chart.renderChart(data, options)
        },
    },
})
</script> -->
<!-- 
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
</script> -->
