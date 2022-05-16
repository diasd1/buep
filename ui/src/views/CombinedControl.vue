<template>
<div class="wrap">
    <div class="overlay">
        <control v-if="showOverlay" />
    </div>
    <div class="underlay">
        <graph v-if="showUnderlay" />
    </div>
</div>
</template>

<script>
import Control from './Control.vue'
import Graph from './Graph.vue'
export default {
    components: { Control, Graph },
    data() {
        return {
            showUnderlay: true,
            showOverlay: true
        }
    },
    mounted() {
        window.addEventListener('keydown', (ev) => {
            if (!ev.altKey)
            {
                return;
            }

            if (ev.key == "1")
            {
                this.showUnderlay = true;
                this.showOverlay = true;
            }
            if (ev.key == "2")
            {
                this.showUnderlay = false;
                this.showOverlay = true;
            }
            if (ev.key == "3")
            {
                this.showUnderlay = true;
                this.showOverlay = false;
            }
        });
    }
}
</script>

<style lang="scss" scoped>
.wrap {
    position: relative;
    width: 100%;
    height: 100%;

    .overlay, .underlay {
        width: 100%;
        height: 100%;
    }
}

.overlay {
    position: absolute;
    top: 47px;
    left: 0;
    z-index: 10;
}

.underlay {
    z-index: 1;
}
</style>