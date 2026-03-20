import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { 
      path: '/', 
      name: 'home', 
      // Lazy Load untuk Landing Page
      component: () => import('../views/HomeView.vue') 
    },
    { 
      path: '/login', 
      name: 'login', 
      component: () => import('../views/LoginView.vue') 
    },
    { 
      path: '/register', 
      name: 'register', 
      component: () => import('../views/RegisterView.vue') 
    },
    { 
      path: '/profile', 
      name: 'profile', 
      component: () => import('../views/ProfileView.vue') 
    },
    { 
      path: '/scan', 
      name: 'scan', 
      component: () => import('../views/ScanView.vue') 
    },
    { 
      path: '/manage-users', 
      name: 'manage-users', 
      component: () => import('../views/ManageUsersView.vue') 
    },
    { 
      path: '/dashboard', 
      name: 'dashboard', 
      component: () => import('../views/DashboardView.vue') 
    },
    {
      path: '/leaderboard',
      name: 'leaderboard',
      // Lazy Load untuk Public Leaderboard
      component: () => import('../views/PublicLeaderboardView.vue')
    }
  ]
})

export default router