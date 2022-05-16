<template>
    <div class="maintenance">
        <div class="settingsWrapper">
            <p>Application</p>
            <div class="content">
                <button @click="restart">Restart</button>
                <button @click="quit">Quit</button>
            </div>
        </div>
        <div class="settingsWrapper">
            <p>Propose Direction</p>
            <div class="content">
                <button @click="getRecommendedSpeeds">GET</button>
                <div class="info">
                    <p>Speed L: {{speedL}}</p>
                    <p>Speed R: {{speedR}}</p>
                </div>
                <button @click="setSpeeds">Set for 1s</button>
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
        },
        getRecommendedSpeeds() {
            fetch("/auto").then(x => x.json()).then(jdata => {
                this.speedL = jdata.speedL
                this.speedR = jdata.speedR
            })
        },
        setSpeedLR(speedL, speedR)
        {
            fetch("/rover/speed", {
                method: "POST",
                body: JSON.stringify({
                    speedL: speedL,
                    speedR: speedR
                })
            })
        },
        setSpeeds() {

            this.setSpeedLR(Number(this.speedL), Number(this.speedR))
            

            setTimeout(() => this.setSpeedLR(127, 127), 1000)
        }
    },
    data() {
        return {
            speedL: 127,
            speedR: 127,
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
        margin: 10px;
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