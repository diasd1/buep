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

        const update = () => {
            if (!this.$router.currentRoute.value.path.includes("table")) { return; }

            fetch("/data").then(x => x.json())
                .then(jdata => this.distances = jdata)

            setTimeout(update, 500);
        }
        update();

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
        height: 100%;
        overflow-x: auto;
        max-height: var(--max-container-height);

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