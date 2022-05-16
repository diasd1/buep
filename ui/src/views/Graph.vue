<template>
  <div class="wrapper">
    <div class="input">
      <div class="wrap">
        <label>Max. Distance [mm]:</label>
        <input type="number" v-model="maxValue" />
        {{chartRotation >= 180 ? (chartRotation - 180) : chartRotation + 180}}°
        <img @click="chartRotation += chartRotation < 360 ? 90 : -270" class="clickable" src="/src/assets/rotate.svg" />
      </div>
    </div>
    <div class="output">
      <RadarChart id="chart" :chartData="testData" :options="options" />
    </div>
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
        this.options.scale.max = this.maxValue || 1;
        this.$emit("changeControlWidth", Math.max((- this.maxValue / 3 + 150), 50))
      },
      chartRotation() {
        const labels = [ ];
        for (let i = 0; i < 360; i ++) {
          labels.push(this.parseChartRotationLabel(this.chartRotation, i));
        }

        this.testData.labels = labels;
      }
    },
    methods: {
      parseChartRotationLabel(chartRotation, i) {
        if (i % 45 !== 0)
        {
          return "";
        }

        chartRotation += 180;
        chartRotation -= chartRotation >= 360 ? 360 : 0;

        chartRotation = 360 - chartRotation

        return `${(i + chartRotation) < 360 ? (i + chartRotation) : (chartRotation + i - 360)}°`;
      }
    },
    data() {
      const data = [];
      const labels = [];
      const chartRotation = 180;

      for (let i = 0; i < 360; i ++) {
        labels.push(this.parseChartRotationLabel(chartRotation, i));
        data.push(i);
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
        labels,
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

      const update = () => {
        if (!this.$router.currentRoute.value.path.includes("graph") && !this.$router.currentRoute.value.path.includes("control")) { return; }

        fetch("/data").then(x => x.json())
          .then(jdata => {
            for (let i = 1; i < (jdata.length - 1); i++)
            {
              if ((jdata[i] > jdata[i - 1] + 100) && (jdata[i] > jdata[i + 1] + 100))
              {
                jdata[i] = (jdata[i - 1] + jdata[i + 1]) / 2;
              }
            }

            const jdata2 = jdata.splice(0, this.chartRotation);
            jdata.push(...jdata2);
            
            this.testData.datasets[0].data = jdata.reverse();
          })

        setTimeout(update, 500);
      }
      update();

      return {
        testData, options, maxValue, chartRotation
      };
    },
  });
</script>

<style lang="scss" scoped>
  #chart {
    width: 100%;
    height: 100%;
  }

  img.clickable {
    &:hover {
      cursor: pointer;
    }
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

  .wrapper {
    display: flex;
    flex-direction: column;
    height: 100%;

    .output {
      position: relative;
      height: 100%;
      width: 100%;
      flex: 1;
    }

    .input {
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;

      .wrap {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        width: 25%;
      }
    }
  }
</style>