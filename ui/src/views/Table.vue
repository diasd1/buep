<template>
    <div class="wrapper">
        <transition-group name="list" appear>
            <div class="row" v-for="(element, index) in distances" :key="index" :style="{'transition-delay': `${index * 0.02}s`}">
                <span class="angle">{{index}} °</span>
                <span class="distance">{{element}} mm</span>
            </div>
        </transition-group>
    </div>
</template>

<style>
.list-enter-active,
.list-leave-active {
  transition: all .5s ease;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(1em);
}
</style>

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
                background: var(--hover);
            }
        }
    }
</style>