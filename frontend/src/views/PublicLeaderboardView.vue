<template>
  <div class="min-h-screen bg-[#0A0A0A] text-white p-4 md:p-8 font-sans relative overflow-x-hidden pt-24">
    
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-gradient-to-b from-ag-purple/20 to-transparent rounded-full mix-blend-screen filter blur-[100px] opacity-50 pointer-events-none"></div>

    <div class="max-w-4xl mx-auto relative z-10">
      
      <div class="text-center mb-16 animate-fade-in-up">
        <div class="inline-flex items-center justify-center p-2 bg-white/5 rounded-2xl mb-4 border border-white/10 backdrop-blur-sm">
          <span class="px-4 py-1.5 bg-gradient-to-r from-ag-yellow to-ag-purple rounded-xl text-xs font-black uppercase tracking-widest text-white shadow-lg">AG Connect Season 1</span>
        </div>
        <h1 class="text-5xl md:text-6xl font-black text-transparent bg-clip-text bg-gradient-to-r from-white via-gray-200 to-gray-500 tracking-tight mb-4 drop-shadow-2xl">
          HALL OF <span class="text-transparent bg-clip-text bg-gradient-to-r from-ag-yellow to-yellow-500">FAME</span>
        </h1>
        <p class="text-gray-400 text-sm md:text-base font-medium max-w-xl mx-auto">
          Peringkat jemaat paling aktif beribadah dan membawa jiwa baru. Kumpulkan poin dan jadilah yang teratas!
        </p>
      </div>

      <div v-if="isLoading" class="flex flex-col items-center justify-center py-20">
        <div class="relative w-16 h-16">
          <div class="absolute inset-0 border-4 border-white/10 rounded-full"></div>
          <div class="absolute inset-0 border-4 border-ag-yellow rounded-full border-t-transparent animate-spin"></div>
        </div>
        <p class="text-gray-400 mt-4 font-semibold tracking-wider animate-pulse">MEMUAT KLASEMEN...</p>
      </div>

      <div v-else-if="topUsers.length > 0">
        
        <div class="flex justify-center items-end gap-2 md:gap-6 mb-16 mt-10 h-64 md:h-72">
          
          <div v-if="topUsers[1]" class="flex flex-col items-center w-28 md:w-36 animate-fade-in-up" style="animation-delay: 0.2s;">
            <div class="w-16 h-16 md:w-20 md:h-20 bg-gradient-to-br from-gray-300 to-gray-500 rounded-full flex items-center justify-center text-2xl font-black text-gray-900 border-4 border-gray-400 shadow-[0_0_30px_rgba(156,163,175,0.4)] relative z-10 -mb-6">
              {{ topUsers[1].fullname.charAt(0).toUpperCase() }}
            </div>
            <div class="w-full h-32 md:h-40 bg-gradient-to-t from-white/5 to-gray-400/20 border border-gray-400/30 rounded-t-2xl flex flex-col justify-end items-center pb-4 relative overflow-hidden backdrop-blur-md">
              <div class="absolute top-0 w-full h-1 bg-gradient-to-r from-transparent via-gray-300 to-transparent opacity-50"></div>
              <span class="text-3xl font-black text-gray-400 mb-1">2</span>
              <span class="text-xs font-bold text-white truncate w-11/12 text-center">{{ topUsers[1].fullname.split(' ')[0] }}</span>
              <span class="text-sm font-black text-gray-300 mt-1">{{ topUsers[1].points }} <span class="text-[10px] text-gray-500 font-normal">pts</span></span>
            </div>
          </div>

          <div v-if="topUsers[0]" class="flex flex-col items-center w-32 md:w-44 animate-fade-in-up z-20">
            <div class="absolute -top-10 text-4xl animate-bounce">👑</div>
            <div class="w-20 h-20 md:w-28 md:h-28 bg-gradient-to-br from-yellow-300 via-yellow-500 to-yellow-700 rounded-full flex items-center justify-center text-4xl font-black text-gray-900 border-4 border-yellow-400 shadow-[0_0_50px_rgba(234,179,8,0.5)] relative z-10 -mb-8">
              {{ topUsers[0].fullname.charAt(0).toUpperCase() }}
            </div>
            <div class="w-full h-40 md:h-48 bg-gradient-to-t from-ag-yellow/5 to-ag-yellow/20 border border-ag-yellow/40 rounded-t-2xl flex flex-col justify-end items-center pb-5 relative overflow-hidden backdrop-blur-md shadow-2xl shadow-ag-yellow/10">
              <div class="absolute top-0 w-full h-1 bg-gradient-to-r from-transparent via-yellow-400 to-transparent"></div>
              <span class="text-5xl font-black text-transparent bg-clip-text bg-gradient-to-b from-yellow-200 to-yellow-600 drop-shadow-md mb-1">1</span>
              <span class="text-sm font-black text-white truncate w-11/12 text-center uppercase tracking-wider">{{ topUsers[0].fullname.split(' ')[0] }}</span>
              <span class="text-lg font-black text-yellow-400 mt-1">{{ topUsers[0].points }} <span class="text-xs text-yellow-600 font-normal">pts</span></span>
            </div>
          </div>

          <div v-if="topUsers[2]" class="flex flex-col items-center w-28 md:w-36 animate-fade-in-up" style="animation-delay: 0.4s;">
            <div class="w-16 h-16 md:w-20 md:h-20 bg-gradient-to-br from-orange-400 to-orange-700 rounded-full flex items-center justify-center text-2xl font-black text-white border-4 border-orange-500 shadow-[0_0_30px_rgba(249,115,22,0.3)] relative z-10 -mb-6">
              {{ topUsers[2].fullname.charAt(0).toUpperCase() }}
            </div>
            <div class="w-full h-28 md:h-32 bg-gradient-to-t from-white/5 to-orange-500/20 border border-orange-500/30 rounded-t-2xl flex flex-col justify-end items-center pb-3 relative overflow-hidden backdrop-blur-md">
              <div class="absolute top-0 w-full h-1 bg-gradient-to-r from-transparent via-orange-400 to-transparent opacity-50"></div>
              <span class="text-3xl font-black text-orange-400/80 mb-1">3</span>
              <span class="text-xs font-bold text-white truncate w-11/12 text-center">{{ topUsers[2].fullname.split(' ')[0] }}</span>
              <span class="text-sm font-black text-orange-300 mt-1">{{ topUsers[2].points }} <span class="text-[10px] text-orange-500/80 font-normal">pts</span></span>
            </div>
          </div>

        </div>

        <div class="max-w-2xl mx-auto flex flex-col gap-3">
          <div v-for="(user, index) in otherUsers" :key="user.id" 
               class="flex items-center justify-between p-4 bg-white/5 hover:bg-white/10 border border-white/5 hover:border-white/10 rounded-2xl transition-all duration-300 backdrop-blur-sm group animate-fade-in-up"
               :style="{ animationDelay: `${(index + 3) * 0.1}s` }">
            
            <div class="flex items-center gap-4">
              <div class="w-10 text-center font-black text-gray-500 group-hover:text-white transition-colors text-lg">
                #{{ index + 4 }}
              </div>
              <div class="w-12 h-12 bg-gradient-to-br from-gray-800 to-black border border-gray-700 rounded-full flex items-center justify-center font-bold text-gray-300 shadow-inner">
                {{ user.fullname.charAt(0).toUpperCase() }}
              </div>
              <div>
                <h3 class="font-bold text-gray-200 text-base group-hover:text-white transition-colors">{{ user.fullname }}</h3>
                <p class="text-xs text-gray-500 font-mono mt-0.5">@{{ user.username }}</p>
              </div>
            </div>

            <div class="flex items-center gap-2 bg-black/40 px-4 py-2 rounded-xl border border-white/5">
              <svg class="w-4 h-4 text-ag-yellow" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
              <span class="font-black text-white">{{ user.points }}</span>
            </div>

          </div>
        </div>

      </div>
      
      <div v-else class="text-center py-20 bg-white/5 rounded-3xl border border-white/10 backdrop-blur-md">
        <div class="text-6xl mb-4">🌪️</div>
        <h3 class="text-xl font-bold text-white mb-2">Arena Masih Sepi</h3>
        <p class="text-gray-400 text-sm">Jadilah yang pertama mendapatkan poin dan puncaki klasemen!</p>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

const isLoading = ref(true)
const allUsers = ref([])

onMounted(async () => {
  try {
    // Karena ini halaman publik, kita coba fetch tanpa token (jika backend mengizinkan)
    // Atau jika backend Anda mengharuskan token, endpoint ini mungkin perlu disesuaikan di backend nanti
    const res = await axios.get('https://semskii1-ag-connect-api.hf.space/users')
    allUsers.value = res.data
  } catch (error) {
    console.error("Gagal memuat leaderboard:", error)
  } finally {
    isLoading.value = false
  }
})

// Menyaring dan mengurutkan user berdasarkan poin
const sortedUsers = computed(() => {
  return [...allUsers.value]
    .filter(u => u.points > 0) // Hanya tampilkan yang punya poin
    .sort((a, b) => b.points - a.points) // Urutkan dari tertinggi
})

// Memisahkan Top 3 untuk Podium
const topUsers = computed(() => sortedUsers.value.slice(0, 3))

// Memisahkan Peringkat 4-10 untuk Daftar Bawah
const otherUsers = computed(() => sortedUsers.value.slice(3, 10))

</script>

<style scoped>
.animate-fade-in-up { animation: fadeInUp 0.6s ease-out forwards; opacity: 0; }
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(30px) scale(0.95); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}
.animate-bounce { animation: bounce 2s infinite; }
@keyframes bounce {
  0%, 100% { transform: translateY(-25%); animation-timing-function: cubic-bezier(0.8, 0, 1, 1); }
  50% { transform: translateY(0); animation-timing-function: cubic-bezier(0, 0, 0.2, 1); }
}
</style>