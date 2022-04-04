<template>
  <RadarChart :chartData="testData" />
</template>

<script lang="ts">
  import {
    defineComponent
  } from 'vue';
  import {
    RadarChart
  } from 'vue-chart-3';
  import {
    Chart,
    registerables
  } from "chart.js";

  Chart.register(...registerables);

  export default defineComponent({
    name: 'Graph',
    components: {
      RadarChart
    },
    data() {
      const data = [];
      for (let i = 0; i < 360; i++) {
        data.push(i)
      }

      const testData = {
        labels: data,
        options: {
          plugins: {
            legend: {
              labels: {
                fontSize: 0
              },
            }
          }
        },
        datasets: [{
          label: 'My First Dataset',
          data,
          fill: true,
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgb(255, 99, 132)',
          pointBackgroundColor: 'rgb(255, 99, 132)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgb(255, 99, 132)'
        }],
      };

      setInterval(() => {
        fetch("/data").then(x => x.json())
          .then(jdata => this.testData.datasets[0].data = jdata)
      }, 1000);

      return {
        testData
      };
    },
  });
</script>