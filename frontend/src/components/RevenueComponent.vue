<template>
    <div>
        <canvas id="lineChart"></canvas>
    </div>
</template>

<script>
import Chart from 'chart.js/auto'
import config from '@/components/chart/lineChartConfig.js'
import axiosAuth from '@/api/axios-auth.js'

export default {
    data() {
        return {
            ctx: null,
        }
    },
    methods: {
        getPageData() {
            axiosAuth.get('/owner/get-future-revenue').then(
                response=> {
                    config.data.labels = [];
                    config.data.datasets[0].data = [];
                    config.data.datasets[0].label = "Total Income";
                    config.options = {
                        scales: {
                            x: {
                                title: {
                                    display: true,
                                    text: "Week",
                                }
                            },
                            y: {
                                beginAtZero: true,
                                title: {
                                    display: true,
                                    text: "Income (£)",
                                },
                            }
                        }
                    };
                    for (let i = 0; i < response.data.length; i++) {
                        config.data.labels.push(response.data[i].date);
                        config.data.datasets[0].data.push(response.data[i].amount); 
                    }
                    new Chart(this.ctx, config);
                }
            )
            
        }
    },
    mounted() {
        this.ctx = document.getElementById('lineChart').getContext('2d');
        this.getPageData();
    },
}
</script>
