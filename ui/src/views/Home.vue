<template>
  <div class="home">
    <div class="upperHome">
      <h1>curious<span class="accent">LiDAR</span></h1>
      <div class="button"><RouterLink class="link" to="/graph">Get Started!</RouterLink></div>
    </div>
  </div>
</template>
<style lang="scss" scoped>
  .justifyBottom {
    justify-self: flex-end;
  }

  .home {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;

    h1 {
      font-size: 5em;
    }
  }

  .upperHome {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
  }

  span.accent {
    color: var(--red);
  }

  .button {
    z-index: 1;
    position: relative;
    text-align: center;
    padding: 20px;
    
    .link::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 2px;
      z-index: 0;
      background: var(--red);
      transform: scaleX(0);
      opacity: 0;
      transition: 400ms;
    }

    a.link {
      position: relative;
      z-index: 10 !important;
      color: var(--text-main);
      left: 0;
      right: 0;
      font-size: 1.5em;
      text-decoration: none;
      transition: 400ms;
      text-transform: uppercase;
    }

    &:hover {
      .link::after {
        opacity: 1;
        transform: scaleX(1);
      }

      .link {
        color: var(--red);
        font-weight: bold;
        font-size: 2em;
      }

      cursor: pointer;
    }
  }
</style>