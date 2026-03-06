import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'login', component: LoginView },
    // [BARU] Rute untuk halaman Register
    { path: '/register', name: 'register', component: () => import('../views/RegisterView.vue') },
    
    { path: '/profile', name: 'profile', component: () => import('../views/ProfileView.vue') },
    { path: '/scan', name: 'scan', component: () => import('../views/ScanView.vue') },
    { path: '/dashboard', name: 'dashboard', component: () => import('../views/DashboardView.vue') }
  ]
})

export default router