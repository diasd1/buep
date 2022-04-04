<template>
    <div class="wrapper">
        <div class="row" v-for="(element, index) in distances" :key="index">
            <span class="angle">{{index}} °</span>
            <span class="distance">{{element}} mm</span>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
    name: "Table",
    data() {
        const data = [ ]
        for (let i = 0; i < 360; i++) {
            data.push(360 - i)
        }

        setInterval(() => {
        fetch("/data").then(x => x.json())
          .then(jdata => this.distances = jdata)
      }, 500);

        return {
            distances: data
        }
    }
})
</script>

<style lang="scss" scoped>
    .wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;

        .row {
            width: 50%;
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            padding: 10px;
            border-radius: 5px;

            &:hover {
                background: var(--light-background);
            }
        }
    }
</style>