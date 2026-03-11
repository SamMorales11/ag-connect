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
        
        <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 gap-4 border-b border-white/10 pb-4">
          
          <div class="flex gap-2">
            <button @click="activeTab = 'AG'" :class="activeTab === 'AG' ? 'bg-ag-purple text-white shadow-lg shadow-ag-purple/20' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="px-6 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent" :style="activeTab === 'AG' ? 'border-color: rgba(124,40,137,0.5)' : ''">
              Ibadah AG ({{ agLogs.length }})
            </button>
            <button @click="activeTab = 'AG Lite'" :class="activeTab === 'AG Lite' ? 'bg-ag-yellow text-gray-900 shadow-lg shadow-ag-yellow/20' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="px-6 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent" :style="activeTab === 'AG Lite' ? 'border-color: rgba(253,224,33,0.5)' : ''">
              Ibadah AG Lite ({{ agLiteLogs.length }})
            </button>
          </div>

          <div class="relative">
            <button @click="isDropdownOpen = !isDropdownOpen" class="flex items-center gap-3 bg-black/40 px-5 py-2.5 rounded-xl border border-white/10 backdrop-blur-md hover:bg-white/5 transition-all outline-none shadow-lg">
              <svg class="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
              <span class="text-sm font-bold text-white">{{ currentFilterName }}</span>
              <svg class="w-4 h-4 text-gray-500 transition-transform duration-300" :class="{'rotate-180': isDropdownOpen}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
            </button>

            <div v-if="isDropdownOpen" @click="isDropdownOpen = false" class="fixed inset-0 z-40"></div>

            <transition name="dropdown-fade">
              <div v-if="isDropdownOpen" class="absolute right-0 mt-2 w-48 bg-[#111] border border-white/10 rounded-2xl shadow-[0_0_50px_rgba(0,0,0,0.8)] z-50 overflow-hidden py-1.5 backdrop-blur-xl">
                <button v-for="option in filterOptions" :key="option.id" @click="selectFilter(option.id)" 
                        class="w-full text-left px-4 py-3 text-sm font-semibold transition-colors flex items-center gap-3" 
                        :class="timeFilter === option.id ? 'bg-ag-purple/10 text-ag-purple' : 'text-gray-300 hover:bg-white/5 hover:text-white'">
                  <svg v-if="timeFilter === option.id" class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
                  <div v-else class="w-4 h-4 shrink-0"></div> {{ option.name }}
                </button>
              </div>
            </transition>
          </div>
          </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div class="bg-white/5 border border-white/10 rounded-2xl p-6 backdrop-blur-md relative overflow-hidden group">
            <div class="absolute -right-4 -top-4 w-24 h-24 rounded-full blur-2xl opacity-20 transition-all duration-500" :class="activeTab === 'AG' ? 'bg-ag-purple group-hover:bg-fuchsia-500' : 'bg-ag-yellow group-hover:bg-yellow-300'"></div>
            <h3 class="text-gray-400 text-sm font-bold uppercase tracking-widest mb-2 flex items-center gap-2">
              Total Hadir
              <span class="text-[10px] bg-white/10 px-2 py-0.5 rounded text-gray-300">{{ filterLabel }}</span>
            </h3>
            <p class="text-5xl font-black" :class="activeTab === 'AG' ? 'text-ag-purple' : 'text-ag-yellow'">
              {{ activeTab === 'AG' ? agLogs.length : agLiteLogs.length }}
            </p>
          </div>
        </div>

        <div class="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl shadow-lg overflow-hidden">
          <div class="p-6 border-b border-white/10 bg-black/40 flex justify-between items-center">
            <h3 class="text-lg font-bold text-white flex items-center gap-2">
              Log Kehadiran: <span :class="activeTab === 'AG' ? 'text-ag-purple' : 'text-ag-yellow'">{{ activeTab }}</span>
            </h3>
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
                  <td colspan="3" class="py-12 text-center text-gray-500 text-sm">
                    Tidak ada data absensi untuk <strong>{{ activeTab }}</strong> pada rentang waktu <strong>{{ currentFilterName }}</strong>.
                  </td>
                </tr>
                <tr v-else v-for="log in (activeTab === 'AG' ? agLogs : agLiteLogs)" :key="log.id" class="hover:bg-white/[0.02] transition-colors">
                  <td class="py-4 px-6">
                    <span class="px-3 py-1 bg-white/5 border border-white/10 rounded-lg text-xs font-mono text-gray-300">
                      {{ formatTime(log.scan_time) }}
                    </span>
                  </td>
                  <td class="py-4 px-6">
                    <div class="font-bold text-gray-200">{{ log.user?.fullname || 'User Dihapus' }}</div>
                  </td>
                  <td class="py-4 px-6">
                    <span v-if="log.user" class="text-xs font-bold px-2 py-0.5 rounded border uppercase tracking-wider"
                          :class="log.user.status === 'Pelayan Tuhan' ? 'bg-ag-yellow/10 text-ag-yellow border-ag-yellow/20' : 'bg-ag-purple/10 text-ag-purple border-ag-purple/20'">
                      {{ log.user.status }}
                    </span>
                    <span v-else class="text-xs font-bold px-2 py-0.5 rounded border bg-gray-500/10 text-gray-400 border-gray-500/20">UNKNOWN</span>
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

// State Interaktif
const activeTab = ref('AG')

// ==========================================
// [BARU] STATE UNTUK CUSTOM DROPDOWN
// ==========================================
const timeFilter = ref('today') 
const isDropdownOpen = ref(false)

const filterOptions = [
  { id: 'today', name: 'Hari Ini' },
  { id: 'week', name: '7 Hari Terakhir' },
  { id: 'month', name: 'Bulan Ini' },
  { id: 'all', name: 'Semua Waktu' }
]

// Mendapatkan nama filter aktif untuk ditampilkan di tombol
const currentFilterName = computed(() => {
  const found = filterOptions.find(opt => opt.id === timeFilter.value)
  return found ? found.name : 'Hari Ini'
})

// Fungsi memilih opsi dan otomatis menutup dropdown
const selectFilter = (id) => {
  timeFilter.value = id
  isDropdownOpen.value = false
}
// ==========================================

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
    const response = await axios.get('https://semskii1-ag-connect-api.hf.space/attendance/logs', {
      headers: { Authorization: `Bearer ${token}` }
    })
    
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

// Logika Filter Waktu
const filteredLogsByTime = computed(() => {
  const now = new Date()
  
  return allLogs.value.filter(log => {
    if (!log.scan_time) return false
    const logDate = new Date(log.scan_time)

    if (timeFilter.value === 'today') {
      return logDate.toDateString() === now.toDateString()
    } 
    else if (timeFilter.value === 'week') {
      const oneWeekAgo = new Date(now.getTime() - 7 * 24 * 60 * 60 * 1000)
      return logDate >= oneWeekAgo
    } 
    else if (timeFilter.value === 'month') {
      return logDate.getMonth() === now.getMonth() && logDate.getFullYear() === now.getFullYear()
    }
    return true 
  })
})

const agLogs = computed(() => {
  return filteredLogsByTime.value.filter(log => log.service_type === 'AG').sort((a,b) => new Date(b.scan_time) - new Date(a.scan_time))
})

const agLiteLogs = computed(() => {
  return filteredLogsByTime.value.filter(log => log.service_type === 'AG Lite').sort((a,b) => new Date(b.scan_time) - new Date(a.scan_time))
})

// Label UPPERCASE untuk kotak statistik
const filterLabel = computed(() => {
  switch(timeFilter.value) {
    case 'today': return 'HARI INI'
    case 'week': return '7 HARI TERAKHIR'
    case 'month': return 'BULAN INI'
    case 'all': return 'SEMUA WAKTU'
    default: return ''
  }
})

const formatTime = (dateStr) => {
  if (!dateStr) return '-'
  const d = new Date(dateStr)
  const timePart = d.toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit' })
  
  if (timeFilter.value === 'today') {
    return timePart
  } else {
    const datePart = d.toLocaleDateString('id-ID', { day: 'numeric', month: 'short', year: 'numeric' })
    return `${datePart} • ${timePart}`
  }
}
</script>

<style scoped>
.animate-fade-in-up { animation: fadeInUp 0.5s ease-out forwards; }
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(20px) scale(0.95); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}

/* Animasi khusus untuk Custom Dropdown */
.dropdown-fade-enter-active, .dropdown-fade-leave-active {
  transition: opacity 0.2s ease, transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}
.dropdown-fade-enter-from, .dropdown-fade-leave-to {
  opacity: 0;
  transform: translateY(-10px) scale(0.95);
}
</style>