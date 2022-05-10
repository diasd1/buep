<template>
    <div id="appWrapper">
        <div class="header">
            <RouterLink class="rLink" to="/">Home</RouterLink>
            <RouterLink class="rLink" to="/control">Control</RouterLink>
            <RouterLink class="rLink" to="/graph">Graph</RouterLink>
            <RouterLink class="rLink" to="/table">Table</RouterLink>
            <a class="rLink" href="https://github.com/diasd1/buep">Github</a>
        </div>
        <div class="view">
            <RouterView />
        </div>
        <div class="lowerHome">
            <div class="bottomWrapper">
                <p>A project realised for our BÜP</p>
                <p>© 2022 | David Dias Horta, Paul Meier</p>
            </div>
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

        --max-container-height: calc(100vh - 20px - 25px - 41px);
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
            flex: 1;
        }
    }
</style>

<style scoped lang="scss">
    .lowerHome {
        flex-grow: 0;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        align-items: center;
        width: 100%;

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
</style>