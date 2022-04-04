<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <div id="appWrapper">
    <div class="header">
        <RouterLink class="rLink" to="/">Graph</RouterLink>
        <RouterLink class="rLink" to="/table">Table</RouterLink>
        <RouterLink class="rLink" to="/download">Export</RouterLink>
    </div>
    <div class="view">
        <RouterView />
    </div>
  </div>
</template>

<style lang="scss">
html,
body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    position: relative;
}

body {
    padding: 10px;
    width: calc(100% - 20px);
    height: calc(100% - 20px);
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
            color: black;
            text-decoration: none;

            &.router-link-active {
                color: green;
            }

            &:not(:last-child) {
                border-right: 1px solid grey;
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
