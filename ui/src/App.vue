<template>
    <div id="appWrapper">
        <div class="header">
            <div class="title">
                <img src="/src/assets/favicon.png">
                <RouterLink class="rLink noBorder" to="/">curious<span class="accent">LiDAR</span></RouterLink>
            </div>
            <div class="links">
                <RouterLink class="rLink" to="/">Home</RouterLink>
                <RouterLink class="rLink" to="/control">Control</RouterLink>
                <RouterLink class="rLink" to="/table">Table</RouterLink>
                <RouterLink class="rLink" to="/maintenance">Maintenance</RouterLink>
            </div>
        </div>
        <div class="view">
            <router-view v-slot="{ Component, route }">
                <transition name="slide-fade">
                    <component :is="Component" :key="route.path" />
                </transition>
            </router-view>
        </div>
        <div class="lowerHome">
            <div class="bottomWrapper">
                <p>A project realised for our BüP</p>
                <p>© 2022 | David Dias Horta, Paul Meier</p>
            </div>
        </div>
    </div>
</template>

<script>
import themes from "/src/assets/themes.json";

const LOCAL_STORAGE_KEY = "theme" // change it to whatever you like

window.getThemes = () => { // returns a string array of all available themes
    window.themes = Object.keys(themes[Object.keys(themes)[0]]);
    return window.themes;
}

window.getCurrentTheme = () => {
    return window.localStorage.getItem(LOCAL_STORAGE_KEY) || "default"
}

window.setTheme = (theme) => { // accepts a string (theme name)
    if (!window.getThemes().includes(theme))
    {
        return;
    }

    window.localStorage.setItem(LOCAL_STORAGE_KEY, theme)
    for (const key of Object.keys(themes))
    {
        document.documentElement.style.setProperty(`--${key}`, themes[key][theme] || themes[key]["default"]);
    }
}

window.setTheme(window.localStorage.getItem(LOCAL_STORAGE_KEY) || "default") // optional, loads the default theme

export default {
    
}
</script>

<style lang="scss">
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

    :root {
        --font-family: 'Poppins', sans-serif;

        --max-container-height: calc(100vh - 20px - 25px - 42px - 20px);
    }

    /* width */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
        padding: 0;
        margin: 0;
        z-index: 101;
    }

    /* Track */
    ::-webkit-scrollbar-track {
        border-radius: 8px;
    }

    /* Handle */
    ::-webkit-scrollbar-thumb {
        background: var(--text-main);
        border-radius: 8px;
    }

    /* Handle on hover */
    ::-webkit-scrollbar-thumb:hover {
        background: var(--disabled);
    }

    html,
    body {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
        position: relative;
        background: var(--default-container-background);
    }

    body {
        padding: 10px;
        width: calc(100% - 20px);
        height: calc(100% - 20px);

        * {
            font-family: var(--font-family);
            color: var(--text-main);
        }
    }

    #appWrapper,
    #app {
        width: 100%;
        height: 100%;
        position: relative;
        display: flex;
        flex-direction: column;

        .header {
            width: calc(100% - 400px);
            height: 100%;
            position: relative;
            flex: 1;
            flex-grow: 0;
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: stretch;
            padding: 0 200px;

            .links {
                display: flex;
                flex-direction: row;
                align-items: stretch;
            }

            .rLink {
                color: var(--text-main);
                margin: 0;
                text-decoration: none;
                height: 100%;
                position: relative;
                transition: color .25s;

                &.router-link-active:not(.noBorder) {
                    border-bottom: 1px solid var(--red);
                }

                padding: 0px 10px;

                &:hover {
                    color: var(--red);
                }
            }
        }

        .view {
            flex: 1;
            max-width: 100vw;
            overflow: hidden;
            max-height: calc(100vh - 30px - 20px - 42px - 5px);
        }
    }
</style>

<style>
  .slide-fade-enter-active {
    transition: all .5s ease-out;
  }
  .slide-fade-enter-from,
  .slide-fade-leave-to {
    transform: translateY(1em);
    opacity: 0;
  }
</style>

<style scoped lang="scss">
    .accent {
        background: var(--gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .lowerHome {
        border-top: 1px solid var(--border);
        flex-grow: 0;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        align-items: center;
        width: calc(100% - 400px);
        padding: 0 200px;

        .bottomWrapper {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            width: 100%;

            p {
                color: var(--disabled);
                margin-bottom: 0;
            }
        }
    }

    .title {
        display: flex;
        align-items: center;
        font-size: 1.2em;
        font-weight: 600;
        letter-spacing: 1px;

        img {
            width: 20px;
        }
    }

    .header {
        padding-bottom: 5px;
        margin-bottom: 10px;
        border-bottom: 1px solid var(--border);

        .title a {
            color: var(--text-main) !important;
        }
    }
</style>