import { createStore } from 'vuex'
import axios from 'axios';

export default createStore({
  state () {
    return {
      posts: []
    }
  },
  getters: {
    getAllPosts(state) {
      return state.posts
    },
  },
  mutations: {
    SET_POSTS(state, payload) {
      state.posts = payload
    }
  },
  actions: {
    async get_posts({ commit }) {
      try {
        const posts = await axios.get(`http://localhost:8000/api/v1/posts/`);
        commit('SET_POSTS', posts.data)

      } catch (error) {
        console.log(error);
      }
    }
  },
})
