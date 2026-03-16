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

      <div class="mb-6 w-full relative group z-20">
        <label class="block text-[10px] font-bold text-gray-500 uppercase tracking-widest mb-2 pl-2">Kategori Ibadah / Acara</label>
        <div class="relative bg-white/5 border border-white/10 rounded-2xl backdrop-blur-md overflow-hidden transition-all focus-within:border-ag-purple focus-within:shadow-[0_0_20px_rgba(168,85,247,0.3)] shadow-lg">
          <select v-model="selectedService" class="w-full bg-transparent text-white font-bold text-sm px-5 py-4 appearance-none outline-none cursor-pointer">
            <option value="AG" class="bg-[#111] text-white">⛪ Ibadah AG (Utama)</option>
            <option value="AG Lite" class="bg-[#111] text-white">🎸 Ibadah AG Lite</option>
            <option value="Doa Fajar" class="bg-[#111] text-white">🌅 Doa Fajar</option>
            <option value="Doa Pengerja" class="bg-[#111] text-white">🙏 Doa Pengerja</option>
            <option value="AGC/Fellowship" class="bg-[#111] text-white">🤝 AGC / Fellowship</option>
          </select>
          <div class="absolute right-5 top-1/2 transform -translate-y-1/2 pointer-events-none text-gray-400 group-hover:text-white transition-colors">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
          </div>
        </div>
      </div>
      
      <div class="w-full bg-white/5 backdrop-blur-2xl border border-white/10 p-6 rounded-[2rem] shadow-[0_0_50px_rgba(0,0,0,0.5)] flex flex-col items-center relative overflow-hidden">
        
        <div class="absolute top-8 right-8 z-30 px-3 py-1 bg-black/60 backdrop-blur-md rounded-lg border border-white/10 text-[10px] font-bold uppercase tracking-widest text-white">
          {{ selectedService }}
        </div>

        <div class="relative w-full overflow-hidden rounded-2xl bg-black/60 border-2 border-dashed border-white/20 transition-all duration-300"
             :class="{'border-emerald-500/50 shadow-[0_0_30px_rgba(16,185,129,0.2)]': successMessage, 'border-red-500/50': errorMessage}">
          
          <div id="reader" class="w-full h-[300px] flex items-center justify-center relative z-10"></div>
          <div v-if="successMessage" class="absolute inset-0 bg-emerald-500/20 z-20 transition-all duration-300 pointer-events-none"></div>
        </div>

        <button @click="toggleCamera" :disabled="isProcessing" class="mt-6 flex items-center gap-3 px-6 py-3 bg-gradient-to-r from-gray-800 to-gray-900 hover:from-gray-700 hover:to-gray-800 border border-gray-600 rounded-xl text-white font-bold text-sm transition-all shadow-lg transform active:scale-95 disabled:opacity-50">
          <svg class="w-5 h-5 text-ag-yellow" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
          Ganti Kamera {{ isFrontCamera ? 'Belakang' : 'Depan' }}
        </button>
        
        <transition name="fade" mode="out-in">
          <div v-if="successMessage" class="w-full mt-6 p-4 bg-emerald-500/10 border border-emerald-500/30 rounded-xl text-center backdrop-blur-md">
            <p class="font-bold text-white text-lg mb-0.5">Berhasil!</p>
            <p class="text-emerald-400 text-sm font-medium">{{ successMessage }}</p>
          </div>
          <div v-else-if="errorMessage" class="w-full mt-6 p-4 bg-red-500/10 border border-red-500/30 rounded-xl text-center backdrop-blur-md">
            <p class="font-bold text-white text-lg mb-0.5">Akses Ditolak</p>
            <p class="text-red-400 text-sm font-medium">{{ errorMessage }}</p>
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
const successMessage = ref('')
const errorMessage = ref('')
const isProcessing = ref(false)
const isFrontCamera = ref(false) 

// Variabel untuk menampung 5 pilihan Ibadah
const selectedService = ref('AG') 

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
    errorMessage.value = "Kamera tidak terdeteksi atau izin ditolak."
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
  successMessage.value = ''
  errorMessage.value = ''

  try {
    const response = await axios.post('https://semskii1-ag-connect-api.hf.space/scan', {
      qr_code_data: decodedText,
      service_type: selectedService.value // Akan mengirimkan nama acara yang dipilih di dropdown
    })
    
    // Mesin tetap menggunakan logika gamifikasi yang sama: 
    // Hanya absen pertama di hari itu yang mendapat +5 poin
    const msg = response.data.message;
    const jamAbsen = new Date().toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit', second: '2-digit' })
    
    successMessage.value = `${msg} di ${selectedService.value} (${jamAbsen})`
    
  } catch (error) {
    if (error.response && error.response.status === 404) {
      errorMessage.value = 'QR Code tidak terdaftar di sistem!'
    } else {
      errorMessage.value = 'Terjadi kesalahan jaringan atau server.'
    }
  } finally {
    setTimeout(() => {
      successMessage.value = ''
      errorMessage.value = ''
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