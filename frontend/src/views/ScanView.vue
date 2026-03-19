<template>
  <div class="min-h-screen bg-[#0A0A0A] flex flex-col items-center py-12 px-4 relative overflow-hidden font-sans">
    
    <div class="absolute top-[-10%] left-[-10%] w-[500px] h-[500px] bg-ag-purple rounded-full mix-blend-screen filter blur-[150px] opacity-20 animate-pulse"></div>
    <div class="absolute bottom-[-10%] right-[-10%] w-[400px] h-[400px] bg-ag-yellow rounded-full mix-blend-screen filter blur-[150px] opacity-10"></div>

    <transition name="pop-bounce">
      <div v-if="showWelcomePopup" class="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-black/80 backdrop-blur-md">
        <div class="bg-[#0A0A0A] border border-white/10 p-8 rounded-[2rem] shadow-[0_0_80px_rgba(16,185,129,0.2)] w-full max-w-sm text-center relative overflow-hidden">
          
          <div class="absolute top-[-50%] left-[-50%] w-[200%] h-[200%] bg-emerald-500/10 rounded-full blur-[80px] pointer-events-none"></div>

          <div class="relative z-10">
            <div class="w-20 h-20 mx-auto bg-gradient-to-br from-emerald-400 to-emerald-600 rounded-full flex items-center justify-center mb-5 border-4 border-[#0A0A0A] outline outline-2 outline-emerald-500/50 shadow-[0_0_30px_rgba(16,185,129,0.5)]">
              <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
            </div>
            
            <h2 class="text-sm font-bold text-gray-400 uppercase tracking-widest mb-1">Welcome</h2>
            <p class="text-3xl font-black text-transparent bg-clip-text bg-gradient-to-r from-white to-gray-300 mb-5 uppercase tracking-tight drop-shadow-lg leading-none">
              {{ scannedUserFullname.split(' ')[0] }}
            </p>
            
            <div class="inline-block bg-emerald-500/10 border border-emerald-500/20 px-5 py-2.5 rounded-xl backdrop-blur-sm">
              <p class="text-emerald-400 text-xs font-bold tracking-widest uppercase">Selamat Beribadah!</p>
            </div>
          </div>
        </div>
      </div>
    </transition>

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

      <div class="mb-6 w-full relative group z-30">
        <label class="block text-[10px] font-bold text-gray-500 uppercase tracking-widest mb-2 pl-2">Kategori Ibadah / Acara</label>
        
        <div class="relative w-full z-50">
          <div v-if="isDropdownOpen" @click="isDropdownOpen = false" class="fixed inset-0 z-40"></div>

          <div 
            @click="isDropdownOpen = !isDropdownOpen"
            class="relative z-50 bg-white/5 border rounded-2xl backdrop-blur-md overflow-hidden transition-all cursor-pointer flex items-center justify-between px-5 py-4 shadow-lg hover:border-ag-purple hover:shadow-[0_0_20px_rgba(168,85,247,0.3)]"
            :class="isDropdownOpen ? 'border-ag-purple shadow-[0_0_20px_rgba(168,85,247,0.3)]' : 'border-white/10'"
          >
            <div class="flex items-center gap-3 text-white font-bold text-sm">
              <div v-html="selectedOption.icon" class="w-5 h-5 text-ag-purple"></div>
              {{ selectedOption.label }}
            </div>
            <svg class="w-5 h-5 text-gray-400 transition-transform duration-300" :class="{'rotate-180': isDropdownOpen}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
          </div>

          <transition name="slide-down">
            <div v-if="isDropdownOpen" class="absolute top-full left-0 w-full mt-2 bg-[#111]/95 backdrop-blur-xl border border-white/10 rounded-2xl overflow-hidden shadow-[0_20px_40px_rgba(0,0,0,0.8)] z-50">
              <div 
                v-for="option in serviceOptions" 
                :key="option.value"
                @click="selectService(option)"
                class="flex items-center gap-3 px-5 py-3.5 hover:bg-white/10 cursor-pointer transition-colors"
                :class="{'bg-white/5': selectedService === option.value}"
              >
                <div v-html="option.icon" class="w-5 h-5" :class="selectedService === option.value ? 'text-ag-yellow' : 'text-gray-400'"></div>
                <span class="text-sm font-bold" :class="selectedService === option.value ? 'text-ag-yellow' : 'text-gray-300'">{{ option.label }}</span>
              </div>
            </div>
          </transition>
        </div>
      </div>
      
      <div class="w-full bg-white/5 backdrop-blur-2xl border border-white/10 p-6 rounded-[2rem] shadow-[0_0_50px_rgba(0,0,0,0.5)] flex flex-col items-center relative overflow-hidden z-10">
        
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
          <div v-if="errorMessage" class="w-full mt-6 p-4 bg-red-500/10 border border-red-500/30 rounded-xl text-center backdrop-blur-md">
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
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { Html5Qrcode } from 'html5-qrcode'
import axios from 'axios'

const router = useRouter()
const successMessage = ref('')
const errorMessage = ref('')
const isProcessing = ref(false)
const isFrontCamera = ref(false) 

// Variabel untuk menampung nama jemaat dan trigger pop-up
const showWelcomePopup = ref(false)
const scannedUserFullname = ref('')

const isDropdownOpen = ref(false)
const selectedService = ref('AG') 

const serviceOptions = [
  { value: 'AG', label: 'Ibadah AG (Utama)', icon: '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 14v3m4-3v3m4-3v3M3 21h18M3 10h18M3 7l9-4 9 4M4 10h16v11H4V10z"></path></svg>' },
  { value: 'AG Lite', label: 'Ibadah AG Lite', icon: '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>' },
  { value: 'Doa Fajar', label: 'Doa Fajar', icon: '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>' },
  { value: 'Doa Pengerja', label: 'Doa Pengerja', icon: '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>' },
  { value: 'AGC/Fellowship', label: 'AGC / Fellowship', icon: '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>' }
]

const selectedOption = computed(() => {
  return serviceOptions.find(opt => opt.value === selectedService.value) || serviceOptions[0]
})

const selectService = (option) => {
  selectedService.value = option.value
  isDropdownOpen.value = false
}

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
  showWelcomePopup.value = false

  try {
    const response = await axios.post('https://semskii1-ag-connect-api.hf.space/scan', {
      qr_code_data: decodedText,
      service_type: selectedService.value
    })
    
    // Membaca Fullname dari Backend yang sudah diupdate
    const namaJemaat = response.data.fullname || 'Jemaat'
    
    successMessage.value = 'Hadir' 
    
    // Menampilkan Popup Welcome
    scannedUserFullname.value = namaJemaat
    showWelcomePopup.value = true
    
  } catch (error) {
    if (error.response && error.response.status === 404) {
      errorMessage.value = 'QR Code tidak terdaftar di sistem!'
    } else {
      errorMessage.value = 'Terjadi kesalahan jaringan atau server.'
    }
  } finally {
    // Menutup Popup otomatis setelah 3 detik
    setTimeout(() => {
      successMessage.value = ''
      errorMessage.value = ''
      showWelcomePopup.value = false
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

.slide-down-enter-active, .slide-down-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.slide-down-enter-from, .slide-down-leave-to {
  opacity: 0;
  transform: translateY(-10px) scale(0.98);
}

/* Animasi khusus untuk Popup Welcome 3D */
.pop-bounce-enter-active {
  animation: popBounceIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.pop-bounce-leave-active {
  animation: popBounceOut 0.3s ease-in forwards;
}
@keyframes popBounceIn {
  0% { transform: scale(0.8) translateY(20px); opacity: 0; }
  100% { transform: scale(1) translateY(0); opacity: 1; }
}
@keyframes popBounceOut {
  0% { transform: scale(1); opacity: 1; }
  100% { transform: scale(0.9); opacity: 0; }
}
</style>