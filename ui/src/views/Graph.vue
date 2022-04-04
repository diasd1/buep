<template>
  <div class="wrapper">
    <input type="number" v-model="maxValue" />
    <RadarChart id="chart" :chartData="testData" :options="options" />
  </div>
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
    watch: {
      maxValue() {
        this.options.scale.max = this.maxValue;
      }
    },
    data() {
      const data = [];
      for (let i = 0; i < 360; i ++) {
        data.push(i % 45 == 0 ? `${i}°` : "")
      }

      const maxValue = 500;

      const options = {
        scale: {
          max: maxValue,
          min: 0,
        },
        plugins: {  // 'legend' now within object 'plugins {}'
          legend: {
            labels: {
              color: "#fff",
              font: {
                size: 16,
                family: "'Poppins', sans-serif"
              }
            }
          }
        },
        scales: {
           r: {
            ticks: {
              color: "#8e92a3",
              backdropColor: "rgba(0, 0, 0, 0.5)",
              font: {
                size: 12,
                family: "'Poppins', sans-serif"
              }
            },
            grid: {
              color: "#8e92a3"
            },
            pointLabels: {
              color: "#8e92a3",
              font: {
                size: 10,
                family: "'Poppins', sans-serif"
              }
            }
          }
        }
      }

      const testData = {
        labels: data,
        datasets: [{
          label: 'LiDAR',
          data,
          fill: true,
          backgroundColor: 'rgba(220, 0, 0, 0.2)',
          borderColor: 'rgb(220, 0, 0)',
          pointBackgroundColor: 'rgb(220, 0, 0)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgb(220, 0, 0)'
        }],
      };

      setInterval(() => {
        fetch("/data").then(x => x.json())
          .then(jdata => {
            for (let i = 1; i < (jdata.length - 1); i++)
            {
              if ((jdata[i] > jdata[i - 1] + 100) && (jdata[i] > jdata[i + 1] + 100))
              {
                jdata[i] = (jdata[i - 1] + jdata[i + 1]) / 2;
              }
            }
            this.testData.datasets[0].data = jdata;
          })
      }, 500);

      return {
        testData, options, maxValue
      };
    },
  });
</script>

<style lang="scss" scoped>
  #chart {
    width: 100%;
    height: 90vh;
  }

  input {
    background-color: var(--light-background);
    color: var(--text-main);
    border: 1px solid var(--border);
    font-family: var(--font-family);
    padding: 10px;
    font-size: 1em;
    border-radius: 10px;

    &:focus {
      outline: none;
    }
  }
</style>