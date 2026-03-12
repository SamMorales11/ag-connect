<template>
  <div class="min-h-screen bg-[#0A0A0A] flex flex-col items-center py-12 px-4 relative overflow-hidden font-sans">
    
    <div class="absolute top-[-10%] left-[-10%] w-[500px] h-[500px] bg-ag-purple rounded-full mix-blend-screen filter blur-[150px] opacity-20 animate-pulse"></div>
    <div class="absolute bottom-[-10%] right-[-10%] w-[400px] h-[400px] bg-ag-yellow rounded-full mix-blend-screen filter blur-[150px] opacity-10"></div>

    <div class="w-full max-w-md relative z-10 flex flex-col items-center">
      
      <div class="text-center mb-6">
        <h1 class="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-ag-yellow to-ag-purple tracking-tight mb-2">
          Scanner Absensi
        </h1>
        <p class="text-gray-400 text-sm font-medium flex items-center justify-center gap-2">
          <span class="w-2 h-2 rounded-full bg-ag-yellow animate-pulse" :class="{'bg-emerald-400': isProcessing}"></span>
          {{ isProcessing ? 'Memproses data...' : 'Menunggu pindaian QR Jemaat' }}
        </p>
      </div>

      <div class="mb-6 w-full p-1 bg-white/5 border border-white/10 rounded-2xl flex backdrop-blur-md relative shadow-lg">
        <div class="absolute top-1 bottom-1 w-[calc(50%-4px)] rounded-xl transition-all duration-300 shadow-[0_0_15px_rgba(0,0,0,0.5)]"
             :class="selectedService === 'AG' ? 'left-1 bg-gradient-to-r from-ag-purple to-[#5b1d66]' : 'left-[calc(50%+3px)] bg-gradient-to-r from-ag-yellow to-[#e5c910]'">
        </div>
        
        <button @click="selectedService = 'AG'" class="flex-1 py-3 text-sm font-bold z-10 transition-colors"
                :class="selectedService === 'AG' ? 'text-white' : 'text-gray-400 hover:text-white'">
          ⛪ Ibadah AG
        </button>
        <button @click="selectedService = 'AG Lite'" class="flex-1 py-3 text-sm font-bold z-10 transition-colors"
                :class="selectedService === 'AG Lite' ? 'text-gray-900' : 'text-gray-400 hover:text-white'">
          🎸 Ibadah AG Lite
        </button>
      </div>
      
      <div class="w-full bg-white/5 backdrop-blur-2xl border border-white/10 p-6 rounded-[2rem] shadow-[0_0_50px_rgba(0,0,0,0.5)] flex flex-col items-center relative overflow-hidden">
        
        <div class="absolute top-8 right-8 z-30 px-3 py-1 bg-black/60 backdrop-blur-md rounded-lg border border-white/10 text-xs font-bold uppercase tracking-widest text-white">
          Mode: {{ selectedService }}
        </div>

        <div class="relative w-full overflow-hidden rounded-2xl bg-black/60 border-2 border-dashed border-white/20 transition-all duration-300"
             :class="{
               'border-emerald-500/50 shadow-[0_0_30px_rgba(16,185,129,0.2)]': statusType === 'success', 
               'border-amber-500/50 shadow-[0_0_30px_rgba(245,158,11,0.2)]': statusType === 'warning',
               'border-red-500/50 shadow-[0_0_30px_rgba(239,68,68,0.2)]': statusType === 'error'
             }">
          
          <div id="reader" class="w-full h-[300px] flex items-center justify-center relative z-10"></div>
          
          <div v-if="statusType === 'success'" class="absolute inset-0 bg-emerald-500/20 z-20 transition-all duration-300 pointer-events-none"></div>
          <div v-else-if="statusType === 'warning'" class="absolute inset-0 bg-amber-500/20 z-20 transition-all duration-300 pointer-events-none"></div>
          <div v-else-if="statusType === 'error'" class="absolute inset-0 bg-red-500/20 z-20 transition-all duration-300 pointer-events-none"></div>
        </div>

        <button @click="toggleCamera" :disabled="isProcessing" class="mt-6 flex items-center gap-3 px-6 py-3 bg-gradient-to-r from-gray-800 to-gray-900 hover:from-gray-700 hover:to-gray-800 border border-gray-600 rounded-xl text-white font-bold text-sm transition-all shadow-lg transform active:scale-95 disabled:opacity-50">
          <svg class="w-5 h-5 text-ag-yellow" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
          Ganti Kamera {{ isFrontCamera ? 'Belakang' : 'Depan' }}
        </button>
        
        <transition name="fade" mode="out-in">
          <div v-if="statusType === 'success'" class="w-full mt-6 p-4 bg-emerald-500/10 border border-emerald-500/30 rounded-xl text-center backdrop-blur-md">
            <p class="font-bold text-white text-lg mb-0.5">{{ statusTitle }}</p>
            <p class="text-emerald-400 text-sm font-medium">{{ statusMessage }}</p>
          </div>
          <div v-else-if="statusType === 'warning'" class="w-full mt-6 p-4 bg-amber-500/10 border border-amber-500/30 rounded-xl text-center backdrop-blur-md">
            <p class="font-bold text-white text-lg mb-0.5">{{ statusTitle }}</p>
            <p class="text-amber-400 text-sm font-medium">{{ statusMessage }}</p>
          </div>
          <div v-else-if="statusType === 'error'" class="w-full mt-6 p-4 bg-red-500/10 border border-red-500/30 rounded-xl text-center backdrop-blur-md">
            <p class="font-bold text-white text-lg mb-0.5">{{ statusTitle }}</p>
            <p class="text-red-400 text-sm font-medium">{{ statusMessage }}</p>
          </div>
        </transition>

      </div>
      
      <button v-if="isUserLoaded" @click="goBack" class="group mt-8 px-6 py-3 bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl transition-all duration-300 backdrop-blur-sm flex items-center gap-2">
        <svg class="w-4 h-4 text-gray-400 group-hover:text-white transition-colors group-hover:-translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
        <span class="text-sm font-bold text-gray-300 group-hover:text-white transition-colors">
          {{ isAdmin ? 'Kembali ke Portal Admin' : 'Selesai & Keluar ke Beranda' }}
        </span>
      </button>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { Html5Qrcode } from 'html5-qrcode'
import axios from 'axios'

const router = useRouter()

// Manajemen Notifikasi
const statusType = ref('') // 'success', 'warning', 'error', atau ''
const statusTitle = ref('')
const statusMessage = ref('')

const isProcessing = ref(false)
const isFrontCamera = ref(false) 
const selectedService = ref('AG') 

// Logika Hak Akses
const isAdmin = ref(false)
const isUserLoaded = ref(false)

let html5QrCode = null

onMounted(async () => {
  const token = localStorage.getItem('access_token')
  if (!token) {
    router.push('/')
    return
  }
  try {
    const response = await axios.get('https://semskii1-ag-connect-api.hf.space/users/me', {
      headers: { Authorization: `Bearer ${token}` }
    })
    isAdmin.value = response.data.is_admin
    isUserLoaded.value = true
  } catch (error) {
    localStorage.removeItem('access_token')
    router.push('/')
    return
  }
  
  html5QrCode = new Html5Qrcode("reader")
  startCamera()
})

onUnmounted(async () => {
  if (html5QrCode && html5QrCode.isScanning) {
    try {
      await html5QrCode.stop()
      html5QrCode.clear()
    } catch (error) {}
  }
})

const startCamera = async () => {
  try {
    const facingMode = isFrontCamera.value ? "user" : "environment"
    await html5QrCode.start(
      { facingMode: facingMode },
      { fps: 10, qrbox: { width: 220, height: 220 }, aspectRatio: 1.0 },
      onScanSuccess,
      onScanFailure
    )
  } catch (err) {
    statusType.value = 'error'
    statusTitle.value = 'Kamera Gagal'
    statusMessage.value = 'Kamera tidak terdeteksi atau izin ditolak.'
  }
}

const toggleCamera = async () => {
  if (isProcessing.value) return 
  if (html5QrCode && html5QrCode.isScanning) {
    try {
      await html5QrCode.stop() 
      isFrontCamera.value = !isFrontCamera.value 
      await startCamera() 
    } catch (error) {}
  }
}

const onScanSuccess = async (decodedText) => {
  if (isProcessing.value) return 
  
  isProcessing.value = true
  statusType.value = ''
  statusTitle.value = ''
  statusMessage.value = ''

  try {
    const response = await axios.post('https://semskii1-ag-connect-api.hf.space/scan', {
      qr_code_data: decodedText,
      service_type: selectedService.value
    })
    
    const msg = response.data.message
    const jamAbsen = new Date().toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit', second: '2-digit' })
    
    // Logika Pemisahan Warna Berdasarkan Balasan Backend
    if (msg.includes('+5')) {
      statusType.value = 'success'
      statusTitle.value = 'Poin Bertambah! 🎉'
      statusMessage.value = `${msg} pada ${jamAbsen}`
    } else {
      statusType.value = 'warning'
      statusTitle.value = 'Hadir Tercatat ✅'
      statusMessage.value = `${msg} pada ${jamAbsen}`
    }
    
  } catch (error) {
    statusType.value = 'error'
    statusTitle.value = 'Akses Ditolak ❌'
    if (error.response && error.response.status === 404) {
      statusMessage.value = 'QR Code tidak terdaftar di sistem!'
    } else {
      statusMessage.value = 'Terjadi kesalahan jaringan atau server.'
    }
  } finally {
    // Hilangkan notifikasi dan buka kunci scanner setelah 3 detik
    setTimeout(() => {
      statusType.value = ''
      statusTitle.value = ''
      statusMessage.value = ''
      isProcessing.value = false
    }, 3000)
  }
}

const onScanFailure = (error) => {}

const goBack = () => {
  if (isAdmin.value) {
    router.push('/profile')
  } else {
    localStorage.removeItem('access_token')
    router.push('/')
  }
}
</script>

<style>
#reader video {
  border-radius: 1rem !important;
  object-fit: cover !important;
  width: 100% !important;
  height: 100% !important;
}
#reader img { display: none !important; }
.fade-enter-active, .fade-leave-active { transition: opacity 0.5s ease, transform 0.5s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; transform: translateY(-10px); }
</style>