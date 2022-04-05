<template>
  <div id="sub-app">
    <LeftMenu />
    <NavBar />
    <section class="container">
      <router-view></router-view>
    </section>
  </div>
</template>

<script>
import NavBar from './components/NavBar';
// import Button from 'primevue/button';
import LeftMenu from './components/LeftMenu';

export default {
  name: 'app',
  components: {
      NavBar,
      LeftMenu
  }
}
</script>

<style>
body {
  margin: 0;
  background-color: var(--gray-800) !important;
}
#sub-app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}


</style>
