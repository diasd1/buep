<template>
    <div class="maintenance">
        <transition-group name="list" appear>
            <div class="settingsWrapper" :key="1">
                <h4>Application</h4>
                <div class="content">
                    <button class="accent" @click="restart">Restart</button>
                    <button @click="quit">Quit</button>
                </div>
            </div>
            <div class="settingsWrapper" style="transition-delay: 0.25s" :key="2">
                <h4>Propose Direction</h4>
                <div class="content">
                    <button @click="getRecommendedSpeeds">GET</button>
                    <div class="info">
                        <p>Speed L: {{speedL}}</p>
                        <p>Speed R: {{speedR}}</p>
                    </div>
                    <button @click="setSpeeds">Set for 1s</button>
                </div>
            </div>
            <div class="settingsWrapper" style="transition-delay: 0.5s" :key="3">
                <h4>Theme</h4>
                <div class="content">
                    <span class="clickable material-symbols-rounded" :class="{ selected: !lightMode }">dark_mode</span>
                    <Toggler class="toggler" :initialState="lightMode" @onChange="nm => lightMode = nm" />
                    <span class="clickable material-symbols-rounded" :class="{ selected: lightMode }">light_mode</span>
                </div>
            </div>
        </transition-group>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Toggler from '../components/Toggler.vue';
export default defineComponent({
    name: "Maintenance",
    watch: {
        lightMode() {
            window.setTheme(this.lightMode ? "default" : "dark");
        }
    },
    methods: {
        quit() {
            fetch("/system/exit");
        },
        restart() {
            fetch("/system/reboot");
        },
        getRecommendedSpeeds() {
            fetch("/auto").then(x => x.json()).then(jdata => {
                this.speedL = jdata.speedL;
                this.speedR = jdata.speedR;
            });
        },
        setSpeedLR(speedL, speedR) {
            fetch("/rover/speed", {
                method: "POST",
                body: JSON.stringify({
                    speedL: speedL,
                    speedR: speedR
                })
            });
        },
        setSpeeds() {
            this.setSpeedLR(Number(this.speedL), Number(this.speedR));
            setTimeout(() => this.setSpeedLR(127, 127), 1000);
        }
    },
    data() {
        this.$nextTick(() => {
            this.lightMode = window.getCurrentTheme() == "default";
        });
        return {
            speedL: 127,
            speedR: 127,
            lightMode: false
        };
    },
    components: { Toggler }
})
</script>

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

<style lang="scss" scoped>
    .maintenance {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
    }

    .toggler {
        margin: 0 10px;
    }

    span.clickable {
        &:hover {
            cursor: pointer;
        }

        color: var(--disabled);

        &.selected {
            color: var(--text-main);
        }
    }

    .settingsWrapper {
        background: var(--light-background);
        padding: 15px;
        margin: 10px;
        border-radius: 10px;

        h4 {
            margin: 0 0 10px 5px;
            font-weight: bold;
        }

        p {
            margin: 0 10px;
        }

        .content {
            background: var(--default-container-background);
            border-radius: 10px;
            padding: 5px;
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;

            button {
                border: none;
                margin: 5px;
                font-size: 1em;
                padding: 10px 20px;
                border-radius: 30px;
                letter-spacing: 1px;
                background: var(--text-main);
                color: var(--light-background);

                &.accent {
                    background: var(--red);
                    color: #fff;
                }

                &:hover {
                    cursor: pointer;

                    &.accent {
                        background: darken($color: #dc0000, $amount: 2%)
                    }
                }
            }
        }
    }
</style>