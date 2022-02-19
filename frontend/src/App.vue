<template>
  <div id="sub-app">
    <NavBar />
  </div>
</template>

<script>
import NavBar from './components/NavBar'
// import Button from 'primevue/button';

export default {
  name: 'app',
  components: {
      NavBar
  }
}
</script>

<style>
body {
  margin: 0;
}
#sub-app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
