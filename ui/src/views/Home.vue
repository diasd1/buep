<template>
  <div class="home">
    <div class="upperHome">
      <h1>
        <transition-group name="list" appear>
          <span v-for="(letter, index) in 'curious'" :key="index" :style="{'transition-delay': `${index * 0.05}s`}">{{letter}}</span>
        </transition-group>
        <span class="accent">
          <transition-group name="list" appear>
            <span v-for="(letter, index) in 'LiDAR'" :key="index" :style="{'transition-delay': `${index * 0.05}s`}">{{letter}}</span>
          </transition-group>
        </span>
      </h1>
      <div class="button"><RouterLink class="link" to="/control">Get Started!</RouterLink></div>
    </div>
  </div>
</template>

<style>
.list-move, /* apply transition to moving elements */
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(1em);
}

/* ensure leaving items are taken out of layout flow so that moving
   animations can be calculated correctly. */
.list-leave-active {
  position: absolute;
}
</style>

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

    h1 {
      display: flex;
      flex-direction: row;
    }
  }

  span.accent {
    background: var(--gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
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
      background: -webkit-linear-gradient(0deg, var(--red), #4b00ed);
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
        font-weight: bold;
        font-size: 2em;
        background: var(--gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
      }

      cursor: pointer;
    }
  }
</style>