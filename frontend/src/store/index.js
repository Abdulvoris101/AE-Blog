import { createStore } from 'vuex'
import axios from 'axios';

export default createStore({
  state () {
    return {
      posts: [],
      loginStatus: false,
      registerStatus: false,
      user: [],
      isUser: false,
    }
  },
  getters: {
    getAllPosts(state) {
      return state.posts
    },
    getLoginStatus(state) {
      return state.loginStatus
    },
    getRegisterStatus(state) {
      return state.registerStatus
    },
    getUserInfo(state) {
      return state.user
    },
    getIsUser(state) {
      return state.isUser
    }
  },
  mutations: {
    SET_POSTS(state, payload) {
      state.posts = payload
    },
    SET_LOGINSTATUS(state, payload) {
      state.LoginStatus = payload
    },
    SET_USER(state, payload) {
      state.user = payload
    },
    SET_IS_USER(state, payload) {
      state.isUser = payload
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
    },
    async get_user_info({ commit }) {
      try {
        let userToken = localStorage.getItem('userToken');
        const user = await axios.get(`http://localhost:8000/user/info/`, {
          headers: {
            Authorization: `Token ${userToken}`
          },
        });
        commit('SET_USER', user.data)

      } catch (error) {
        console.log(error);
      }
    }
  },
})
