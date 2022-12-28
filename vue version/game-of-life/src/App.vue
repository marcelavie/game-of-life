<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <h1>helor</h1>
    <GameLife>a</GameLife>
      <HelloWorld msg = "WELCOME" />
  </div>
</template>

<script>
import GameLife from './components/GameLife.vue'
export default {
  name: 'App',
  components: {
    GameLife
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
