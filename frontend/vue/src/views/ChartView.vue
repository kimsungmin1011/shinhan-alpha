<template>
    <div>
      <line-chart :chart-data="chartData" :options="options"></line-chart>
    </div>
  </template>
  
  <script>
  import LineChart from '../components/LineChart.vue'
  
  export default {
    components: {
      LineChart
    },
    data () {
      return {
        chartData: {
          labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
          datasets: [
            {
              label: 'Data 1',
              borderColor: '#f87979',
              data: [40, 39, 10, 40, 39, 80, 40]
            },
            {
              label: 'Data 2',
              borderColor: '#46BFBD',
              data: [60, 55, 90, 60, 55, 20, 60]
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false
        }
      }
    }
  }
  </script>
  