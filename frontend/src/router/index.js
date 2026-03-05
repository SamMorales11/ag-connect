import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'login', component: LoginView },
    { path: '/profile', name: 'profile', component: () => import('../views/ProfileView.vue') },
    { path: '/scan', name: 'scan', component: () => import('../views/ScanView.vue') },
    // [BARU] Rute untuk halaman Dashboard
    { path: '/dashboard', name: 'dashboard', component: () => import('../views/DashboardView.vue') }
  ]
})

export default router