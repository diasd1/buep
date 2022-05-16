<template>
    <div class="top">
        <!--div>
            <button class="reset" @click="() => { lSpeed = 127; rSpeed = 127 }">STOP</button>
        </div-->
        <div class="control">
            <div class="range">
                <p>
                    {{displaySpeed(lSpeed)}}
                    ({{lSpeed}})
                </p>
                <input type="range" v-model="lSpeed" min="0" max="255" />
            </div>
            <img class="car" src="/src/assets/car.png" :style="{ width: `${width}px`, transform: 'rotate('+ rotation +'deg)'}" />
            <div class="range">
                <p>
                    {{displaySpeed(rSpeed)}}
                    ({{rSpeed}})
                </p>
                <input type="range" v-model="rSpeed" min="0" max="255" />
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        width: {
            type: Number,
            default: 300
        },
        rotation: {
            type: Number,
            default: 0
        }
    },
    data() {
        return {
            rSpeed: 127,
            lSpeed: 127
        }
    },
    methods: {
        displaySpeed(val) {
            const speed = val - 127;
            if (speed >= 0)
            {
                return `${Math.round(speed / 128 * 100)}%`
            }
            return `${Math.round(speed / 127 * 100)}%`
        },
        update() {
            fetch("/rover/speed", {
                method: "POST",
                body: JSON.stringify({
                    speedL: Number(this.lSpeed),
                    speedR: Number(this.rSpeed)
                })
            })
        }
    },
    watch: {
        lSpeed() {
            this.lSpeed = Math.max(Math.min(this.lSpeed, 255), 0)
            this.update();
        },
        rSpeed() {
            this.rSpeed = Math.max(Math.min(this.rSpeed, 255), 0)
            this.update();
        }
    },
    mounted() {
        window.addEventListener('keydown', (ev) => {
            if (ev.key == "ArrowUp")
            {
                if (this.rSpeed != this.lSpeed)
                {
                    this.rSpeed = this.lSpeed = Math.round(Math.abs((this.rSpeed + this.lSpeed) / 2));
                }

                this.rSpeed++;
                this.lSpeed++;
            }
            if (ev.key == "ArrowDown")
            {
                if (this.rSpeed != this.lSpeed)
                {
                    this.rSpeed = this.lSpeed = Math.round(Math.abs((this.rSpeed + this.lSpeed) / 2));
                }

                this.rSpeed--;
                this.lSpeed--;
            }
            if (ev.key == "ArrowRight")
            {
                this.rSpeed--;
                this.lSpeed++;
            }
            if (ev.key == "ArrowLeft")
            {
                this.rSpeed++;
                this.lSpeed--;
            }
            if (ev.key == " ")
            {
                this.lSpeed = this.rSpeed = 127;
            }
        });
    }
}
</script>

<style lang="scss" scoped>
    .top {
        display: flex;
        flex-direction: column;
        height: 100%;
        align-items: center;
        justify-content: center;
    }

    .reset {
        background: var(--red);
        color: var(--text-main);
        padding: 10px 20px;
        border-radius: 5px;
        margin-top: 20px;
        font-size: 1.2em;

        &:hover {
            cursor: pointer;
            background: darken($color: #dc0000, $amount: 10)
        }
    }

    .control {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        flex-grow: 1;
        flex-shrink: 1;
        width: 80%;

        .range {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        input[type="range"] {
            writing-mode: bt-lr; /* IE */
            -webkit-appearance: slider-vertical; /* Chromium */

            &:hover {
                cursor: pointer;
            }
        }
    }
</style>