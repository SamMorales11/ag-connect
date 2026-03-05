<template>
  <div class="min-h-screen bg-[#0A0A0A] flex items-center justify-center p-4 relative overflow-hidden">
    
    <div class="absolute top-[-10%] left-[-10%] w-[500px] h-[500px] bg-ag-purple rounded-full mix-blend-screen filter blur-[150px] opacity-20 animate-pulse"></div>
    <div class="absolute bottom-[-10%] right-[-10%] w-[400px] h-[400px] bg-ag-yellow rounded-full mix-blend-screen filter blur-[150px] opacity-10"></div>

    <div class="relative w-full max-w-md bg-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl shadow-2xl overflow-hidden z-10 flex flex-col">
      
      <div class="p-6 text-center border-b border-white/5 bg-black/20">
        <h1 class="text-2xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-ag-yellow to-ag-purple tracking-tight mb-1">
          Kartu Jemaat
        </h1>
        <p class="text-gray-400 text-xs tracking-widest uppercase font-semibold">Arrow Generation</p>
      </div>

      <div v-if="isLoading" class="p-12 text-center text-gray-400 flex flex-col items-center">
        <svg class="animate-spin h-8 w-8 text-ag-yellow mb-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
        <p class="animate-pulse">Memuat data profil aman...</p>
      </div>

      <div v-else-if="errorMessage" class="p-10 text-center text-red-400">
        <div class="bg-red-500/10 border border-red-500/20 p-4 rounded-2xl backdrop-blur-sm">
          <p class="font-semibold">{{ errorMessage }}</p>
          <p class="text-xs mt-2 opacity-70">Mengalihkan ke halaman login...</p>
        </div>
      </div>

      <div v-else class="p-8">
        
        <div class="text-center mb-8">
          <h2 class="text-3xl font-bold text-white mb-1 tracking-tight">{{ user.fullname }}</h2>
          <p class="text-gray-400 font-medium">@{{ user.username }}</p>
          
          <div class="mt-4 flex justify-center items-center gap-2">
            <span class="px-3 py-1.5 bg-ag-yellow/10 text-ag-yellow border border-ag-yellow/20 text-xs font-bold rounded-full backdrop-blur-sm shadow-[0_0_10px_rgba(253,224,33,0.1)]">
              {{ user.status }}
            </span>
            <span v-if="user.is_admin" class="px-3 py-1.5 bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 text-xs font-bold rounded-full backdrop-blur-sm shadow-[0_0_10px_rgba(16,185,129,0.1)]">
              Admin
            </span>
          </div>
        </div>

        <div class="flex flex-col items-center justify-center mb-10 relative">
          <div class="absolute inset-0 bg-gradient-to-r from-ag-purple/20 to-ag-yellow/20 blur-2xl rounded-full"></div>
          
          <div class="relative p-5 bg-white rounded-2xl shadow-[0_0_40px_rgba(253,224,33,0.15)] transform transition-transform hover:scale-105 duration-500">
            <qrcode-vue :value="user.qr_code_data" :size="200" level="M" />
          </div>
          
          <div class="mt-5 bg-black/40 border border-white/10 px-4 py-2 rounded-xl backdrop-blur-md">
            <p class="text-[11px] text-gray-400 font-mono tracking-wider break-all text-center max-w-[250px]">
              ID: <span class="text-gray-300">{{ user.qr_code_data }}</span>
            </p>
          </div>
        </div>

        <div v-if="user.is_admin" class="grid grid-cols-2 gap-3 mb-4">
          <button @click="goToScan" class="group flex flex-col justify-center items-center gap-2 bg-white/5 hover:bg-ag-purple/20 border border-white/10 hover:border-ag-purple/50 text-gray-300 hover:text-white py-4 px-2 rounded-2xl transition-all duration-300">
            <svg class="w-6 h-6 text-ag-purple group-hover:scale-110 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
            <span class="text-sm font-semibold">Scanner</span>
          </button>
          
          <button @click="goToDashboard" class="group flex flex-col justify-center items-center gap-2 bg-white/5 hover:bg-ag-yellow/20 border border-white/10 hover:border-ag-yellow/50 text-gray-300 hover:text-white py-4 px-2 rounded-2xl transition-all duration-300">
            <svg class="w-6 h-6 text-ag-yellow group-hover:scale-110 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
            <span class="text-sm font-semibold">Data Hadir</span>
          </button>
        </div>

        <button @click="logout" class="w-full mt-2 flex justify-center items-center gap-2 bg-red-500/10 hover:bg-red-500/20 text-red-400 border border-red-500/20 font-bold py-3.5 px-4 rounded-2xl transition-all duration-300">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>
          Keluar
        </button>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import QrcodeVue from 'qrcode.vue'

const router = useRouter()
const user = ref(null)
const isLoading = ref(true)
const errorMessage = ref('')

onMounted(async () => {
  const token = localStorage.getItem('access_token')
  if (!token) {
    router.push('/')
    return
  }

  try {
    const response = await axios.get('http://127.0.0.1:8000/users/me', {
      headers: { Authorization: `Bearer ${token}` }
    })
    user.value = response.data
  } catch (error) {
    errorMessage.value = 'Sesi berakhir atau tidak valid.'
    localStorage.removeItem('access_token')
    setTimeout(() => router.push('/'), 2000)
  } finally {
    isLoading.value = false
  }
})

const goToScan = () => router.push('/scan')
const goToDashboard = () => router.push('/dashboard')
const logout = () => {
  localStorage.removeItem('access_token')
  router.push('/')
}
</script>