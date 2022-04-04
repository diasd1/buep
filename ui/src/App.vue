<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <div id="appWrapper">
    <div class="header">
        <RouterLink class="rLink" to="/">Graph</RouterLink>
        <RouterLink class="rLink" to="/table">Table</RouterLink>
    </div>
    <div class="view">
        <RouterView />
    </div>
  </div>
</template>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');

:root {
    --light-background: #21262a;
    --text-main: #fff;
    --default-container-background: #16191c;
    --disabled: #8e92a3;
    --blue: #607cd8;
    --red: #dc0000;
    --green: #64aa67;
    --border: #2a3036;

    --font-family: 'Poppins', sans-serif;
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
  position: relative;
  display: flex;
  flex-direction: column;

    .header {
        width: 100%;
        height: 100%;
        position: relative;
        flex: 1;
        flex-grow: 0;
        display: flex;
        flex-direction: row;
        justify-content: center;

        .rLink {
            color: var(--text-main);
            text-decoration: none;

            &.router-link-active {
                color: var(--red);
            }

            &:not(:last-child) {
                border-right: 1px solid var(--border);
                padding: 0px 10px;
            }

            &:first-child {
                padding-left: 0px;
            }

            &:last-child {
                padding-left: 10px;
            }
        }
    }

    .view {
        width: 100%;
        height: 100%;
        flex: 1;
    }
}
</style>
