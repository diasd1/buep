<template>
  <div class="home">
    <h1>curious<span class="accent">LiDAR</span></h1>
    <h3>A project realised by David Dias Horta and Paul Meier</h3>
    <p></p>
    <div class="button"><div class="buttonBack"></div><RouterLink class="link" to="/graph">Get Started!</RouterLink></div>
  </div>
</template>
<style lang="scss" scoped>
  .home {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: calc(100vh - 25px - 10px);

    h1 {
      font-size: 3em;
    }
  }

  span.accent {
    color: var(--red);
  }

  .button {
    z-index: 0;
    position: relative;
    width: 200px;
    height: 25px;
    text-align: center;
    padding: 20px;
    
    .buttonBack {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 0;
      background: var(--red);
      transform: scaleX(0);
      transition: 1s;
    }

    &:hover {
      .buttonBack {
        transform: scaleX(1);
      }

      cursor: pointer;
    }

    a.link {
      position: fixed;
      z-index: 10 !important;
      color: var(--text-main);
      left: 0;
      right: 0;
    }
  }
</style>