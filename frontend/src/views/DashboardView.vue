<template>
  <div class="min-h-screen bg-[#0A0A0A] text-white p-4 md:p-8 font-sans relative overflow-x-hidden">
    
    <div class="fixed top-[-20%] left-[-10%] w-[600px] h-[600px] bg-ag-purple rounded-full mix-blend-screen filter blur-[200px] opacity-20 pointer-events-none"></div>
    <div class="fixed bottom-[-20%] right-[-10%] w-[500px] h-[500px] bg-ag-yellow rounded-full mix-blend-screen filter blur-[200px] opacity-10 pointer-events-none"></div>

    <div class="max-w-6xl mx-auto relative z-10">
      
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-10 gap-4">
        <div>
          <h1 class="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-white to-gray-400 tracking-tight mb-1">
            Dashboard <span class="text-transparent bg-clip-text bg-gradient-to-r from-ag-yellow to-ag-purple">Analitik</span>
          </h1>
          <p class="text-gray-400 text-sm font-medium">Pemantauan Absensi Real-Time AG Connect</p>
        </div>
        
        <button @click="goBack" class="group flex items-center gap-2 px-5 py-2.5 bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl transition-all duration-300 backdrop-blur-sm">
          <svg class="w-4 h-4 text-gray-400 group-hover:text-white transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
          <span class="text-sm font-semibold text-gray-300 group-hover:text-white">Kembali</span>
        </button>
      </div>

      <div v-if="isLoading" class="flex flex-col items-center justify-center py-20">
        <svg class="animate-spin h-10 w-10 text-ag-purple mb-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
        <p class="text-gray-400 font-medium animate-pulse">Menyinkronkan data dengan server...</p>
      </div>

      <div v-else>
        
        <div v-if="birthdays && birthdays.length > 0" class="mb-8 p-5 bg-gradient-to-r from-pink-500/10 via-purple-500/10 to-ag-yellow/10 border border-pink-500/30 rounded-3xl backdrop-blur-xl flex items-center gap-5 shadow-[0_0_40px_rgba(236,72,153,0.15)] relative overflow-hidden group">
          <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/stardust.png')] opacity-20"></div>
          
          <div class="w-12 h-12 bg-pink-500/20 rounded-full flex items-center justify-center text-2xl animate-bounce shadow-[0_0_20px_rgba(236,72,153,0.4)]">
            🎂
          </div>
          
          <div class="relative z-10">
            <h3 class="text-pink-400 font-extrabold text-lg flex items-center gap-2">
              Ulang Tahun Hari Ini! <span class="text-xs px-2 py-0.5 bg-pink-500/20 rounded-full text-pink-300 border border-pink-500/30">{{ birthdays.length }} Orang</span>
            </h3>
            <p class="text-gray-300 text-sm mt-0.5">
              Selamat ulang tahun untuk: 
              <span class="font-bold text-white tracking-wide">
                {{ birthdays.map(b => b.fullname).join(', ') }}
              </span>
            </p>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          
          <div class="bg-white/5 backdrop-blur-xl border border-white/10 p-6 rounded-3xl shadow-lg relative overflow-hidden group hover:border-ag-yellow/50 transition-colors duration-500">
            <div class="absolute top-0 right-0 w-32 h-32 bg-ag-yellow/10 rounded-full blur-3xl group-hover:bg-ag-yellow/20 transition-all"></div>
            <div class="flex justify-between items-start mb-4">
              <p class="text-gray-400 text-sm font-semibold uppercase tracking-wider">Hadir Hari Ini</p>
              <div class="p-2 bg-ag-yellow/10 rounded-lg text-ag-yellow border border-ag-yellow/20">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
              </div>
            </div>
            <h3 class="text-4xl font-extrabold text-white mb-1">{{ stats.today }} <span class="text-lg text-gray-500 font-medium">Jemaat</span></h3>
            <p class="text-xs text-emerald-400 flex items-center gap-1">
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg>
              Aktivitas sedang berlangsung
            </p>
          </div>

          <div class="bg-white/5 backdrop-blur-xl border border-white/10 p-6 rounded-3xl shadow-lg relative overflow-hidden group hover:border-ag-purple/50 transition-colors duration-500">
            <div class="absolute top-0 right-0 w-32 h-32 bg-ag-purple/10 rounded-full blur-3xl group-hover:bg-ag-purple/20 transition-all"></div>
            <div class="flex justify-between items-start mb-4">
              <p class="text-gray-400 text-sm font-semibold uppercase tracking-wider">Total Database</p>
              <div class="p-2 bg-ag-purple/10 rounded-lg text-ag-purple border border-ag-purple/20">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4"></path></svg>
              </div>
            </div>
            <h3 class="text-4xl font-extrabold text-white mb-1">{{ stats.total }} <span class="text-lg text-gray-500 font-medium">Rekaman</span></h3>
            <p class="text-xs text-gray-400">Total jejak scan absensi</p>
          </div>

          <div class="bg-white/5 backdrop-blur-xl border border-white/10 p-6 rounded-3xl shadow-lg relative overflow-hidden group hover:border-blue-500/50 transition-colors duration-500">
             <div class="absolute top-0 right-0 w-32 h-32 bg-blue-500/10 rounded-full blur-3xl group-hover:bg-blue-500/20 transition-all"></div>
            <div class="flex justify-between items-start mb-4">
              <p class="text-gray-400 text-sm font-semibold uppercase tracking-wider">Scan Terakhir</p>
              <div class="p-2 bg-blue-500/10 rounded-lg text-blue-400 border border-blue-500/20">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
              </div>
            </div>
            <h3 class="text-2xl font-bold text-white mb-2 truncate" :title="stats.lastScanTime">{{ stats.lastScanTime }}</h3>
            <p class="text-xs text-gray-400 truncate">Oleh: <span class="text-white">{{ stats.lastScanner }}</span></p>
          </div>

        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
          
          <div class="lg:col-span-1 bg-white/5 backdrop-blur-xl border border-white/10 p-6 rounded-3xl shadow-lg flex flex-col">
            <h2 class="text-lg font-bold text-white mb-6">Tren 7 Hari Terakhir</h2>
            
            <div class="flex-1 flex items-end justify-between gap-2 h-48 mt-auto pb-2 border-b border-white/10 relative">
              <div v-for="bar in chartData" :key="bar.day" class="flex flex-col items-center w-full group">
                <span class="text-[10px] text-gray-400 font-bold mb-2 opacity-0 group-hover:opacity-100 transition-opacity">{{ bar.count }}</span>
                <div class="w-full max-w-[40px] bg-gradient-to-t from-ag-purple/20 to-ag-yellow rounded-t-sm transition-all duration-1000 ease-out relative overflow-hidden" 
                     :style="`height: ${bar.heightPercentage}%`">
                     <div class="absolute inset-0 bg-white/20 transform translate-y-full group-hover:translate-y-0 transition-transform duration-300"></div>
                </div>
                <span class="text-[10px] text-gray-500 font-medium mt-3">{{ bar.day }}</span>
              </div>
              
              <div v-if="chartData.length === 0" class="absolute inset-0 flex items-center justify-center text-sm text-gray-500">
                Belum ada data grafik
              </div>
            </div>
          </div>

          <div class="lg:col-span-2 bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl shadow-lg overflow-hidden flex flex-col">
            <div class="p-6 border-b border-white/10 flex justify-between items-center bg-black/20">
              <h2 class="text-lg font-bold text-white">Log Absensi Terbaru</h2>
              <span class="px-3 py-1 bg-green-500/10 text-green-400 border border-green-500/20 text-[10px] font-bold rounded-full uppercase tracking-wider flex items-center gap-1.5">
                <span class="w-1.5 h-1.5 bg-green-400 rounded-full animate-pulse"></span>
                Live
              </span>
            </div>
            
            <div class="overflow-x-auto">
              <table class="w-full text-left border-collapse">
                <thead>
                  <tr class="bg-white/[0.02] text-gray-400 text-xs uppercase tracking-widest border-b border-white/5">
                    <th class="py-4 px-6 font-semibold">Jemaat</th>
                    <th class="py-4 px-6 font-semibold">Status</th>
                    <th class="py-4 px-6 font-semibold">Waktu Hadir</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-white/5">
                  
                  <tr v-if="attendances.length === 0">
                    <td colspan="3" class="py-12 text-center text-gray-500 text-sm">Belum ada data kehadiran.</td>
                  </tr>

                  <tr v-else v-for="absen in attendances.slice(0, 10)" :key="absen.id" class="hover:bg-white/[0.03] transition-colors group">
                    <td class="py-4 px-6">
                      <div class="font-bold text-gray-200 group-hover:text-ag-yellow transition-colors">{{ absen.owner.fullname }}</div>
                      <div class="text-[10px] text-gray-500 font-mono mt-0.5">ID: #{{ absen.id.toString().padStart(4, '0') }}</div>
                    </td>
                    <td class="py-4 px-6">
                      <span class="px-2.5 py-1 bg-ag-purple/10 text-ag-purple border border-ag-purple/20 text-[11px] font-bold rounded-md">
                        {{ absen.owner.status }}
                      </span>
                    </td>
                    <td class="py-4 px-6 text-gray-400 text-sm font-medium">
                      {{ formatTime(absen.scan_time) }}
                    </td>
                  </tr>
                  
                </tbody>
              </table>
            </div>
            
            <div v-if="attendances.length > 10" class="p-4 text-center border-t border-white/10 bg-black/10 text-xs text-gray-500">
              Menampilkan 10 data terakhir dari {{ attendances.length }} data.
            </div>
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
const attendances = ref([])
const birthdays = ref([])
const isLoading = ref(true)

const stats = ref({
  today: 0,
  total: 0,
  lastScanTime: '-',
  lastScanner: '-'
})

onMounted(async () => {
  try {
    const [absenRes, ultahRes] = await Promise.all([
      axios.get('http://127.0.0.1:8000/attendances'),
      axios.get('http://127.0.0.1:8000/birthdays')
    ])
    
    attendances.value = absenRes.data
    birthdays.value = ultahRes.data
    calculateStats()
  } catch (error) {
    console.error("Gagal mengambil data", error)
  } finally {
    isLoading.value = false
  }
})

const calculateStats = () => {
  const data = attendances.value
  if (!data || data.length === 0) return

  stats.value.total = data.length
  
  const todayDate = new Date().toLocaleDateString('id-ID')
  stats.value.today = data.filter(a => new Date(a.scan_time).toLocaleDateString('id-ID') === todayDate).length
  
  const lastRecord = data[0]
  if (lastRecord) {
    stats.value.lastScanner = lastRecord.owner.fullname
    stats.value.lastScanTime = new Date(lastRecord.scan_time).toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit', second: '2-digit' })
  }
}

const chartData = computed(() => {
  if (!attendances.value || attendances.value.length === 0) return []

  const groupedData = {}
  attendances.value.forEach(absen => {
    const dayName = new Date(absen.scan_time).toLocaleDateString('id-ID', { weekday: 'short' })
    groupedData[dayName] = (groupedData[dayName] || 0) + 1
  })

  const maxCount = Math.max(...Object.values(groupedData), 1)

  const finalChart = Object.keys(groupedData).map(day => {
    return {
      day: day,
      count: groupedData[day],
      heightPercentage: (groupedData[day] / maxCount) * 100
    }
  })

  return finalChart.slice(0, 7).reverse() 
})

const formatTime = (isoString) => {
  const date = new Date(isoString)
  return date.toLocaleString('id-ID', { 
    weekday: 'short', 
    day: 'numeric', 
    month: 'short', 
    hour: '2-digit', 
    minute: '2-digit'
  })
}

const goBack = () => {
  router.push('/profile')
}
</script>