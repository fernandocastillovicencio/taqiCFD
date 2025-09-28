import { createRouter, createWebHistory } from 'vue-router'
import CFDView from '@/views/CFDView.vue'
import AboutUs from '@/views/AboutUs.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: CFDView
  },
  {
    path: '/about',
    name: 'About',
    component: AboutUs
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
