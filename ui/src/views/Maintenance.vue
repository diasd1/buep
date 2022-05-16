<template>
    <div class="maintenance">
        <div class="settingsWrapper">
            <p>Application</p>
            <div class="content">
                <button @click="restart">Restart</button>
                <button @click="quit">Quit</button>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
    name: "Maintenance",
    methods: {
        quit() {
            fetch("/system/exit")
        },
        restart() {
            fetch("/system/reboot")
        }
    },
    data() {
        return {
        }
    }
})
</script>

<style lang="scss" scoped>
    .maintenance {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
    }

    .settingsWrapper {
        background: var(--light-background);
        padding: 15px;
        border-radius: 10px;

        p {
            margin: 0 0 10px 5px;
            font-weight: bold;
        }

        .content {
            background: var(--default-container-background);
            border-radius: 10px;
            padding: 5px;
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;

            button {
                background: var(--red);
                color: var(--text-main);
                border: none;
                margin: 5px;
                font-size: 1em;
                padding: 5px 15px;
                border-radius: 30px;
                letter-spacing: 1px;

                &:hover {
                    cursor: pointer;
                    background: darken($color: #dc0000, $amount: 10%)
                }
            }
        }
    }
</style>