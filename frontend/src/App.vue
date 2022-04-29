<template>
  <div id="sub-app">
    <LeftMenu />
    <NavBar :posts="posts" />
    <section class="container">
      <router-view ></router-view>
    </section>
  </div>
</template>

<script>
import NavBar from './components/NavBar';
// import Button from 'primevue/button';
import LeftMenu from './components/LeftMenu';
import axios from 'axios'


export default {
  name: 'app',
  components: {
      NavBar,
      LeftMenu
  },
  data() {
    return {
      activeFilter: false,
      posts: [],
    }
  },
  created() {
    this.getPosts()
  },
  methods: {
    async getPosts() {
        try{
            const res = await axios.get('http://localhost:8000/api/v1/posts/');
            this.posts = res.data;
            this.filteredPosts = res.data;
        } catch(error) {
            console.log(error);
        }
    },
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
