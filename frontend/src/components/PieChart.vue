<template>
    <div>
        <canvas id="pieChart"></canvas>
    </div>
</template>

<script>
import {Chart} from 'chart.js/auto'
// import Colors from 'chart.js'
import config from '@/components/chart/pieChartConfig.js'
import axiosAuth from '@/api/axios-auth.js'

export default {
    data() {
        return {
            ctx: null,
        }
    },
    methods: {
        getPageData() {
            axiosAuth.get('/owner/get-owner-membership-data').then(
                response => {
                    var memberships = response.data.memberships;
                    config.data.labels = [];
                    config.data.datasets[0].data = [];
                    for (let i = 0; i < memberships.length; i++) {
                        config.data.labels.push(memberships[i].name);
                        config.data.datasets[0].data.push(memberships[i].numMembers);
                    }
                    new Chart(this.ctx, config);
                }
            )
        }
    },
    mounted() {
        this.ctx = document.getElementById('pieChart').getContext('2d');
        this.getPageData();
    },
}
</script>
