import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: HomeView }, // Landing Page di depan
    { path: '/login', name: 'login', component: () => import('../views/LoginView.vue') }, // Login dipindah ke /login
    { path: '/register', name: 'register', component: () => import('../views/RegisterView.vue') },
    { path: '/profile', name: 'profile', component: () => import('../views/ProfileView.vue') },
    { path: '/scan', name: 'scan', component: () => import('../views/ScanView.vue') },
    { path: '/dashboard', name: 'dashboard', component: () => import('../views/DashboardView.vue') }
  ]
})

export default router