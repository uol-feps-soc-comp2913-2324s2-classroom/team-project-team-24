// chartConfig.js

const data = {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple'],
    datasets: [
        {
            label: '# ',
            data: [12, 19, 3, 5, 2],
            backgroundColor: [
                '#ec516c',
                '#f2a254',
                '#f8ce6b',
                '#6cbdbf',
                'purple',
            ],
        },
    ],
}

const config = {
    type: 'pie',
    data: data,
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Subscription:',
            },
        },
    },
}

export default config
