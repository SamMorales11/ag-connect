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
          <p class="text-gray-400 text-sm font-medium">Pantau kehadiran dan berikan poin apresiasi jemaat.</p>
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
        
        <div class="flex flex-col lg:flex-row justify-between items-start lg:items-center mb-8 gap-4 border-b border-white/10 pb-4">
          <div class="flex flex-wrap gap-2">
            <button @click="activeTab = 'Leaderboard'" :class="activeTab === 'Leaderboard' ? 'bg-emerald-500 text-white shadow-lg shadow-emerald-500/20' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="px-6 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent">
              🏆 Top Leaderboard
            </button>
            <button @click="activeTab = 'AG'" :class="activeTab === 'AG' ? 'bg-ag-purple text-white shadow-lg shadow-ag-purple/20' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="px-6 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent">
              Ibadah AG ({{ filteredAgLogs.length }})
            </button>
            <button @click="activeTab = 'AG Lite'" :class="activeTab === 'AG Lite' ? 'bg-ag-yellow text-gray-900 shadow-lg shadow-ag-yellow/20' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="px-6 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent">
              Ibadah AG Lite ({{ filteredAgLiteLogs.length }})
            </button>
          </div>

          <div class="flex flex-col sm:flex-row gap-3 w-full lg:w-auto">
            
            <div v-if="activeTab !== 'Leaderboard'" class="relative w-full sm:w-44">
              <input 
                v-model="selectedDate" 
                type="date" 
                class="w-full bg-black/50 border border-gray-700 text-white text-sm rounded-xl px-4 py-2.5 focus:border-ag-purple focus:ring-1 focus:ring-ag-purple outline-none transition-all cursor-pointer custom-date-input"
              >
              <button v-if="selectedDate" @click="selectedDate = ''" class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 hover:text-red-400">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
              </button>
            </div>

            <div class="relative w-full sm:w-64">
              <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
              </div>
              <input 
                v-model="searchQuery" 
                type="text" 
                placeholder="Cari nama jemaat..." 
                class="w-full bg-black/50 border border-gray-700 text-white text-sm rounded-xl pl-10 pr-4 py-2.5 focus:border-ag-yellow focus:ring-1 focus:ring-ag-yellow outline-none transition-all placeholder-gray-500"
              >
            </div>
          </div>
        </div>

        <div v-if="activeTab === 'Leaderboard'" class="animate-fade-in-up">
          <div class="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl shadow-lg overflow-hidden mt-6">
            <div class="overflow-x-auto">
              <table class="w-full text-left whitespace-nowrap">
                <thead>
                  <tr class="bg-black/40 text-gray-500 text-xs uppercase tracking-widest border-b border-white/5">
                    <th class="py-5 px-6 font-bold text-center w-24">Rank</th>
                    <th class="py-5 px-6 font-bold">Jemaat (Gamers)</th>
                    <th class="py-5 px-6 font-bold text-right">Total Poin</th>
                    <th class="py-5 px-6 font-bold text-center w-36">Aksi Admin</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-white/5">
                  <tr v-if="paginatedUsers.length === 0">
                    <td colspan="4" class="py-16 text-center text-gray-500 text-sm font-medium">Jemaat tidak ditemukan.</td>
                  </tr>
                  <tr v-else v-for="(user, index) in paginatedUsers" :key="user.id" class="hover:bg-white/[0.03] transition-colors">
                    <td class="py-4 px-6 text-center">
                      <div v-if="(currentPage - 1) * itemsPerPage + index === 0" class="w-8 h-8 mx-auto bg-yellow-500 text-gray-900 rounded-full flex items-center justify-center font-black shadow-lg">1</div>
                      <div v-else-if="(currentPage - 1) * itemsPerPage + index === 1" class="w-8 h-8 mx-auto bg-gray-400 text-gray-900 rounded-full flex items-center justify-center font-black shadow-lg">2</div>
                      <div v-else-if="(currentPage - 1) * itemsPerPage + index === 2" class="w-8 h-8 mx-auto bg-orange-600 text-white rounded-full flex items-center justify-center font-black shadow-lg">3</div>
                      <div v-else class="text-gray-400 font-bold">{{ (currentPage - 1) * itemsPerPage + index + 1 }}</div>
                    </td>
                    <td class="py-4 px-6">
                      <div class="font-bold text-gray-200">{{ user.fullname }}</div>
                      <div class="text-[10px] text-gray-500 font-mono mt-0.5">@{{ user.username }}</div>
                    </td>
                    <td class="py-4 px-6 text-right">
                      <div class="inline-flex items-center gap-1 bg-emerald-500/10 px-3 py-1 rounded-lg border border-emerald-500/20">
                        <span class="font-black text-emerald-400">{{ user.points }}</span>
                      </div>
                    </td>
                    <td class="py-4 px-6 text-center">
                      <button @click="openConfirmModal(user)" class="bg-gradient-to-r from-ag-purple to-purple-600 hover:from-purple-500 hover:to-purple-400 text-white text-xs font-bold py-2 px-3 rounded-lg shadow-lg transform hover:scale-105 transition-all flex items-center justify-center gap-1 mx-auto">
                        🎁 +10 Kuis
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <div v-else class="animate-fade-in-up">
          <div class="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl shadow-lg overflow-hidden mt-6">
            <div class="overflow-x-auto">
              <table class="w-full text-left whitespace-nowrap">
                <thead>
                  <tr class="bg-black/40 text-gray-500 text-xs uppercase tracking-widest border-b border-white/5">
                    <th class="py-4 px-6 font-bold">Waktu Hadir</th>
                    <th class="py-4 px-6 font-bold">Nama Jemaat</th>
                    <th class="py-4 px-6 font-bold">Kategori</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-white/5">
                  <tr v-if="(activeTab === 'AG' ? paginatedAgLogs : paginatedAgLiteLogs).length === 0">
                    <td colspan="3" class="py-12 text-center text-gray-500 text-sm">
                      <span v-if="selectedDate">Tidak ada data absensi untuk tanggal ini.</span>
                      <span v-else>Data tidak ditemukan.</span>
                    </td>
                  </tr>
                  <tr v-else v-for="log in (activeTab === 'AG' ? paginatedAgLogs : paginatedAgLiteLogs)" :key="log.id" class="hover:bg-white/[0.02] transition-colors">
                    <td class="py-4 px-6"><span class="text-xs font-mono text-gray-300">{{ new Date(log.scan_time).toLocaleString('id-ID') }}</span></td>
                    <td class="py-4 px-6 font-bold text-gray-200">{{ log.user?.fullname || 'User Dihapus' }}</td>
                    <td class="py-4 px-6 text-xs text-gray-400">{{ log.user?.status || '-' }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <div v-if="currentTotalPages > 1" class="flex flex-col sm:flex-row justify-between items-center mt-6 px-2 gap-4 animate-fade-in-up">
          <span class="text-sm font-medium text-gray-500">
            Halaman <span class="text-white">{{ currentPage }}</span> dari <span class="text-white">{{ currentTotalPages }}</span>
          </span>
          <div class="flex gap-2">
            <button @click="prevPage" :disabled="currentPage === 1" class="px-4 py-2 bg-white/5 hover:bg-white/10 border border-white/10 rounded-lg text-sm font-bold transition-all disabled:opacity-30 disabled:cursor-not-allowed">
              Sebelumnya
            </button>
            <button @click="nextPage" :disabled="currentPage === currentTotalPages" class="px-4 py-2 bg-white/5 hover:bg-white/10 border border-white/10 rounded-lg text-sm font-bold transition-all disabled:opacity-30 disabled:cursor-not-allowed">
              Selanjutnya
            </button>
          </div>
        </div>

      </div>
    </div>

    <transition name="fade">
      <div v-if="showConfirmModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm px-4">
        <div class="bg-[#111] border border-white/10 p-6 md:p-8 rounded-3xl max-w-sm w-full text-center shadow-[0_0_50px_rgba(168,85,247,0.15)] transform transition-all">
          <div class="text-6xl mb-4 animate-bounce">🎁</div>
          <h3 class="text-2xl font-black text-white mb-2">Berikan +10 Poin?</h3>
          <p class="text-gray-400 text-sm mb-8 leading-relaxed">
            Anda akan mengirimkan poin kuis kepada <br>
            <span class="font-bold text-ag-yellow text-lg">{{ selectedUser?.fullname }}</span>
          </p>
          
          <div class="flex gap-3">
            <button @click="showConfirmModal = false" :disabled="isGivingPoints" class="flex-1 py-3 rounded-xl font-bold text-gray-400 bg-white/5 hover:bg-white/10 hover:text-white transition-colors disabled:opacity-50">
              Batal
            </button>
            <button @click="confirmGivePoints" :disabled="isGivingPoints" class="flex-1 py-3 rounded-xl font-bold text-white bg-gradient-to-r from-ag-purple to-purple-600 hover:from-purple-500 hover:to-purple-400 transition-all shadow-[0_0_20px_rgba(168,85,247,0.4)] flex justify-center items-center disabled:opacity-50">
              <span v-if="isGivingPoints" class="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></span>
              <span v-else>Ya, Berikan!</span>
            </button>
          </div>
        </div>
      </div>
    </transition>

    <transition name="bounce">
      <div v-if="showToast" class="fixed bottom-10 left-1/2 transform -translate-x-1/2 z-50 px-6 py-3 rounded-2xl border backdrop-blur-xl flex items-center gap-3 shadow-2xl"
           :class="toastType === 'success' ? 'bg-emerald-500/20 border-emerald-500/50 text-emerald-400' : 'bg-red-500/20 border-red-500/50 text-red-400'">
        <span class="text-2xl">{{ toastType === 'success' ? '🎉' : '❌' }}</span>
        <span class="font-bold text-sm tracking-wide">{{ toastMessage }}</span>
      </div>
    </transition>

  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const isLoading = ref(true)
const allLogs = ref([])
const allUsers = ref([])
const activeTab = ref('Leaderboard') 

// State Pencarian, Filter Tanggal & Paginasi
const searchQuery = ref('')
const selectedDate = ref('') // Menyimpan tanggal berformat YYYY-MM-DD
const currentPage = ref(1)
const itemsPerPage = 20

// Reset kembali ke Halaman 1 jika filter berubah
watch([searchQuery, activeTab, selectedDate], () => {
  currentPage.value = 1
})

const showConfirmModal = ref(false)
const selectedUser = ref(null)
const isGivingPoints = ref(false)
const showToast = ref(false)
const toastMessage = ref('')
const toastType = ref('success')
let toastTimer = null

onMounted(async () => {
  const token = localStorage.getItem('access_token')
  if (!token) {
    router.push('/login')
    return
  }
  await fetchData(token)
})

const fetchData = async (token) => {
  try {
    const [logsRes, usersRes] = await Promise.all([
      axios.get('https://semskii1-ag-connect-api.hf.space/attendance/logs', { headers: { Authorization: `Bearer ${token}` } }),
      axios.get('https://semskii1-ag-connect-api.hf.space/users', { headers: { Authorization: `Bearer ${token}` } })
    ])
    allLogs.value = logsRes.data.map(log => ({ ...log, service_type: log.service_type || 'AG' }))
    allUsers.value = usersRes.data
  } catch (error) {
    console.error("Gagal memuat data", error)
  } finally {
    isLoading.value = false
  }
}

const openConfirmModal = (user) => {
  selectedUser.value = user
  showConfirmModal.value = true
}

const confirmGivePoints = async () => {
  if (!selectedUser.value) return
  isGivingPoints.value = true
  clearTimeout(toastTimer)
  showToast.value = false

  try {
    const token = localStorage.getItem('access_token')
    const response = await axios.post(`https://semskii1-ag-connect-api.hf.space/users/${selectedUser.value.id}/add-quiz-points`, {}, {
      headers: { Authorization: `Bearer ${token}` }
    })
    selectedUser.value.points += 10
    toastType.value = 'success'
    toastMessage.value = response.data.message
    showToast.value = true
  } catch (error) {
    toastType.value = 'error'
    toastMessage.value = error.response?.data?.detail || "Gagal memberikan poin."
    showToast.value = true
  } finally {
    isGivingPoints.value = false
    showConfirmModal.value = false
    selectedUser.value = null
    toastTimer = setTimeout(() => { showToast.value = false }, 3000)
  }
}

// LOGIKA FILTER LEADERBOARD
const filteredUsers = computed(() => {
  let users = [...allUsers.value].sort((a, b) => b.points - a.points).filter(u => u.points >= 0)
  if (searchQuery.value) {
    const q = searchQuery.value.toLowerCase()
    users = users.filter(u => u.fullname.toLowerCase().includes(q) || u.username.toLowerCase().includes(q))
  }
  return users
})

// LOGIKA FILTER LOG ABSENSI (TANGGAL + PENCARIAN)
const getFilteredLogs = (type) => {
  let logs = allLogs.value.filter(log => log.service_type === type).sort((a,b) => new Date(b.scan_time) - new Date(a.scan_time))
  
  // 1. Filter Berdasarkan Pencarian Nama
  if (searchQuery.value) {
    const q = searchQuery.value.toLowerCase()
    logs = logs.filter(log => (log.user?.fullname || '').toLowerCase().includes(q))
  }

  // 2. Filter Berdasarkan Tanggal
  if (selectedDate.value) {
    logs = logs.filter(log => {
      // Mengubah scan_time (UTC) menjadi string tanggal lokal (YYYY-MM-DD)
      const dateObj = new Date(log.scan_time)
      const year = dateObj.getFullYear()
      const month = String(dateObj.getMonth() + 1).padStart(2, '0')
      const day = String(dateObj.getDate()).padStart(2, '0')
      const formattedLogDate = `${year}-${month}-${day}`
      
      return formattedLogDate === selectedDate.value
    })
  }

  return logs
}

const filteredAgLogs = computed(() => getFilteredLogs('AG'))
const filteredAgLiteLogs = computed(() => getFilteredLogs('AG Lite'))

// LOGIKA PAGINASI (20 DATA PER HALAMAN)
const paginatedUsers = computed(() => filteredUsers.value.slice((currentPage.value - 1) * itemsPerPage, currentPage.value * itemsPerPage))
const paginatedAgLogs = computed(() => filteredAgLogs.value.slice((currentPage.value - 1) * itemsPerPage, currentPage.value * itemsPerPage))
const paginatedAgLiteLogs = computed(() => filteredAgLiteLogs.value.slice((currentPage.value - 1) * itemsPerPage, currentPage.value * itemsPerPage))

// HITUNG TOTAL HALAMAN
const currentTotalPages = computed(() => {
  if (activeTab.value === 'Leaderboard') return Math.ceil(filteredUsers.value.length / itemsPerPage)
  if (activeTab.value === 'AG') return Math.ceil(filteredAgLogs.value.length / itemsPerPage)
  return Math.ceil(filteredAgLiteLogs.value.length / itemsPerPage)
})

// KONTROL TOMBOL HALAMAN
const nextPage = () => { if (currentPage.value < currentTotalPages.value) currentPage.value++ }
const prevPage = () => { if (currentPage.value > 1) currentPage.value-- }

</script>

<style scoped>
.animate-fade-in-up { animation: fadeInUp 0.5s ease-out forwards; }
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(20px) scale(0.95); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}

.animate-bounce { animation: bounce 2s infinite; }
@keyframes bounce {
  0%, 100% { transform: translateY(-20%); animation-timing-function: cubic-bezier(0.8, 0, 1, 1); }
  50% { transform: translateY(0); animation-timing-function: cubic-bezier(0, 0, 0.2, 1); }
}

.fade-enter-active, .fade-leave-active { transition: opacity 0.3s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
.fade-enter-active .bg-\[\#111\] { animation: scaleIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; }

@keyframes scaleIn {
  0% { transform: scale(0.9); opacity: 0; }
  100% { transform: scale(1); opacity: 1; }
}

.bounce-enter-active { animation: bounceInUp 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.bounce-leave-active { animation: fadeOutDown 0.3s ease-in forwards; }

@keyframes bounceInUp {
  0% { transform: translate(-50%, 100%); opacity: 0; }
  100% { transform: translate(-50%, 0); opacity: 1; }
}
@keyframes fadeOutDown {
  0% { transform: translate(-50%, 0); opacity: 1; }
  100% { transform: translate(-50%, 100%); opacity: 0; }
}

/* Modifikasi Icon Kalender bawaan browser agar tetap terlihat rapi di Dark Mode */
.custom-date-input::-webkit-calendar-picker-indicator {
  filter: invert(1);
  opacity: 0.6;
  cursor: pointer;
}
.custom-date-input::-webkit-calendar-picker-indicator:hover {
  opacity: 1;
}
</style>