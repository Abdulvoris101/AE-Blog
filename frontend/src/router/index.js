import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home'
import PostView from '../views/PostView'

const routes = [
  {
      path: '/',
      name: 'index',
      component: Home 
  },
  {
      path: '/post/:slug',
      name: 'postView',
      component: PostView,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
