<template>
  <div class="min-h-screen bg-[#0A0A0A] flex items-center justify-center p-4 relative overflow-hidden">
    
    <div class="absolute top-[-15%] left-[-10%] w-[500px] h-[500px] bg-ag-purple rounded-full mix-blend-screen filter blur-[120px] opacity-20 animate-pulse"></div>
    
    <div class="absolute bottom-[-15%] right-[-10%] w-[400px] h-[400px] bg-ag-yellow rounded-full mix-blend-screen filter blur-[120px] opacity-10"></div>

    <div class="relative w-full max-w-md p-10 bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl shadow-2xl z-10">
      
      <div class="text-center mb-10">
        <h1 class="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-ag-yellow to-ag-purple mb-2 tracking-tight">
          AG Connect
        </h1>
        <p class="text-gray-400 text-sm tracking-widest uppercase font-semibold">Sistem Manajemen Jemaat</p>
      </div>

      <div v-if="errorMessage" class="mb-6 p-4 bg-red-500/10 border border-red-500/50 text-red-400 rounded-xl text-sm text-center backdrop-blur-sm transition-all">
        {{ errorMessage }}
      </div>

      <form @submit.prevent="handleLogin" class="space-y-6">
        <div>
          <label class="block text-sm font-medium text-gray-300 mb-2">Username</label>
          <input 
            v-model="username" 
            type="text" 
            required 
            class="w-full px-5 py-3 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-ag-yellow/50 focus:border-ag-yellow text-white placeholder-gray-600 outline-none transition-all duration-300" 
            placeholder="Masukkan username"
          >
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-300 mb-2">Password</label>
          <input 
            v-model="password" 
            type="password" 
            required 
            class="w-full px-5 py-3 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-ag-yellow/50 focus:border-ag-yellow text-white placeholder-gray-600 outline-none transition-all duration-300" 
            placeholder="••••••••"
          >
        </div>

        <button 
          type="submit" 
          :disabled="isLoading" 
          class="w-full bg-gradient-to-r from-ag-yellow to-[#e5c910] hover:from-[#e5c910] hover:to-ag-yellow text-gray-900 font-extrabold py-3.5 px-4 rounded-xl transition-all duration-300 transform hover:scale-[1.02] shadow-[0_0_20px_rgba(253,224,33,0.3)] flex justify-center items-center disabled:opacity-50 disabled:hover:scale-100"
        >
          <span v-if="isLoading" class="flex items-center gap-2">
            <svg class="animate-spin h-5 w-5 text-gray-900" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
            Memeriksa Kredensial...
          </span>
          <span v-else>Masuk ke Sistem</span>
        </button>
      </form>
      <p class="mt-8 text-center text-sm text-gray-400">
        Belum memiliki Kartu Jemaat? 
        <button @click="$router.push('/register')" class="text-ag-purple hover:text-ag-yellow font-bold transition-colors">Daftar di sini</button>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const username = ref('')
const password = ref('')
const errorMessage = ref('')
const isLoading = ref(false)

const handleLogin = async () => {
  isLoading.value = true
  errorMessage.value = ''

  try {
    const formData = new URLSearchParams()
    formData.append('username', username.value)
    formData.append('password', password.value)

    const response = await axios.post('https://semskii1-ag-connect-api.hf.space/login', formData, {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    })

    localStorage.setItem('access_token', response.data.access_token)
    router.push('/profile')
  } catch (error) {
    if (error.response && error.response.status === 401) {
      errorMessage.value = 'Kredensial tidak valid. Silakan coba lagi.'
    } else {
      errorMessage.value = 'Server tidak merespons. Pastikan backend menyala.'
    }
  } finally {
    isLoading.value = false
  }
}
</script>