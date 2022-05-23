<template>
    <div @click="active = !active" class="toggle" :class="{ active: active }">
        <div class="bubble"></div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
    props: {
        initialState: Boolean
    },
    data() {
        return {
            active: this.initialState
        }
    },
    watch: {
        active() {
            this.$emit("onChange", this.active);
        },
        initialState() {
            this.active = this.initialState
        }
    }
})
</script>

<style lang="scss" scoped>

    .toggle {
        border-radius: 25px;
        background: var(--light-background);
        border: 1px solid var(--border);
        width: 50px;
        display: flex;
        flex-direction: row;

        &:hover {
            cursor: pointer;
        }

        &.active .bubble {
            transform: translateX(25px);
        }
    }

    .bubble {
        border-radius: 50%;
        width: 25px;
        height: 25px;
        background: var(--text-main);

        transition: transform 0.25s cubic-bezier(0.5, 0, 0.5, 1);
        transform: translateX(0px);
    }

</style>