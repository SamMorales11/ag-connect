<template>
  <div class="min-h-screen bg-[#0A0A0A] text-white p-4 md:p-8 font-sans relative overflow-x-hidden">
    
    <div class="fixed top-[-20%] left-[-10%] w-[600px] h-[600px] bg-ag-yellow rounded-full mix-blend-screen filter blur-[200px] opacity-10 pointer-events-none"></div>
    <div class="fixed bottom-[-20%] right-[-10%] w-[500px] h-[500px] bg-ag-purple rounded-full mix-blend-screen filter blur-[200px] opacity-10 pointer-events-none"></div>

    <div class="max-w-7xl mx-auto relative z-10 animate-fade-in-up">
      
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-10 gap-4">
        <div>
          <h1 class="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-ag-yellow to-ag-purple tracking-tight mb-1">
            Dashboard <span class="text-white">Analitik</span>
          </h1>
          <p class="text-gray-400 text-sm font-medium">Pantau kehadiran jemaat berdasarkan jenis ibadah secara real-time.</p>
        </div>
        
        <button @click="$router.push('/profile')" class="group flex items-center gap-2 px-5 py-2.5 bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl transition-all duration-300 backdrop-blur-sm">
          <svg class="w-4 h-4 text-gray-400 group-hover:text-white transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
          <span class="text-sm font-semibold text-gray-300 group-hover:text-white">Kembali ke Portal</span>
        </button>
      </div>

      <div v-if="isLoading" class="flex flex-col items-center justify-center py-20">
        <svg class="animate-spin h-10 w-10 text-ag-yellow mb-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
        <p class="text-gray-400">Menyinkronkan data...</p>
      </div>

      <div v-else>
        
        <div class="flex gap-2 mb-8 border-b border-white/10 pb-4">
          <button @click="activeTab = 'AG'" :class="activeTab === 'AG' ? 'bg-ag-purple text-white shadow-lg shadow-ag-purple/20' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="px-6 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent" :style="activeTab === 'AG' ? 'border-color: rgba(124,40,137,0.5)' : ''">
            Ibadah AG ({{ agLogs.length }})
          </button>
          <button @click="activeTab = 'AG Lite'" :class="activeTab === 'AG Lite' ? 'bg-ag-yellow text-gray-900 shadow-lg shadow-ag-yellow/20' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="px-6 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent" :style="activeTab === 'AG Lite' ? 'border-color: rgba(253,224,33,0.5)' : ''">
            Ibadah AG Lite ({{ agLiteLogs.length }})
          </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div class="bg-white/5 border border-white/10 rounded-2xl p-6 backdrop-blur-md">
            <h3 class="text-gray-400 text-sm font-bold uppercase tracking-widest mb-2">Total Hadir ({{ activeTab }})</h3>
            <p class="text-5xl font-black" :class="activeTab === 'AG' ? 'text-ag-purple' : 'text-ag-yellow'">
              {{ activeTab === 'AG' ? agLogs.length : agLiteLogs.length }}
            </p>
          </div>
        </div>

        <div class="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl shadow-lg overflow-hidden">
          <div class="p-6 border-b border-white/10 bg-black/40 flex justify-between items-center">
            <h3 class="text-lg font-bold text-white">Log Kehadiran: <span :class="activeTab === 'AG' ? 'text-ag-purple' : 'text-ag-yellow'">{{ activeTab }}</span></h3>
          </div>
          <div class="overflow-x-auto">
            <table class="w-full text-left whitespace-nowrap">
              <thead>
                <tr class="text-gray-500 text-xs uppercase tracking-widest border-b border-white/5">
                  <th class="py-4 px-6 font-bold">Waktu Hadir</th>
                  <th class="py-4 px-6 font-bold">Nama Jemaat</th>
                  <th class="py-4 px-6 font-bold">Kategori</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-white/5">
                <tr v-if="(activeTab === 'AG' ? agLogs : agLiteLogs).length === 0">
                  <td colspan="3" class="py-12 text-center text-gray-500 text-sm">Belum ada jemaat yang absen di sesi ini.</td>
                </tr>
                <tr v-else v-for="log in (activeTab === 'AG' ? agLogs : agLiteLogs)" :key="log.id" class="hover:bg-white/[0.02] transition-colors">
                  <td class="py-4 px-6">
                    <span class="px-3 py-1 bg-white/5 border border-white/10 rounded-lg text-xs font-mono text-gray-300">
                      {{ formatTime(log.scan_time) }}
                    </span>
                  </td>
                  <td class="py-4 px-6">
                    <div class="font-bold text-gray-200">{{ log.user.fullname }}</div>
                  </td>
                  <td class="py-4 px-6">
                    <span class="text-xs font-bold px-2 py-0.5 rounded border uppercase tracking-wider"
                          :class="log.user.status === 'Pelayan Tuhan' ? 'bg-ag-yellow/10 text-ag-yellow border-ag-yellow/20' : 'bg-ag-purple/10 text-ag-purple border-ag-purple/20'">
                      {{ log.user.status }}
                    </span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const isLoading = ref(true)
const allLogs = ref([])

// State Tab Aktif
const activeTab = ref('AG')

onMounted(async () => {
  const token = localStorage.getItem('access_token')
  if (!token) {
    router.push('/login')
    return
  }
  await fetchLogs(token)
})

const fetchLogs = async (token) => {
  try {
    // Kita panggil endpoint API (pastikan endpoint /attendance/logs ada di main.py Anda)
    // Jika belum ada, Anda harus menambahkan endpoint untuk mengambil semua attendance beserta relasi user
    const response = await axios.get('http://127.0.0.1:8000/attendance/logs', {
      headers: { Authorization: `Bearer ${token}` }
    })
    
    // Asumsi response API mengembalikan list objek { id, scan_time, service_type, user: { fullname, status } }
    // Jika service_type null di data lama, kita set default 'AG'
    allLogs.value = response.data.map(log => ({
      ...log,
      service_type: log.service_type || 'AG' 
    }))
  } catch (error) {
    console.error("Gagal memuat log", error)
  } finally {
    isLoading.value = false
  }
}

// [BARU] Memisahkan Log secara reaktif
const agLogs = computed(() => {
  return allLogs.value.filter(log => log.service_type === 'AG').sort((a,b) => new Date(b.scan_time) - new Date(a.scan_time))
})

const agLiteLogs = computed(() => {
  return allLogs.value.filter(log => log.service_type === 'AG Lite').sort((a,b) => new Date(b.scan_time) - new Date(a.scan_time))
})

const formatTime = (dateStr) => {
  if (!dateStr) return '-'
  return new Date(dateStr).toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit', second: '2-digit' })
}
</script>

<style scoped>
.animate-fade-in-up { animation: fadeInUp 0.5s ease-out forwards; }
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(20px) scale(0.95); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}
</style>