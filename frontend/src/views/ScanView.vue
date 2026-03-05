<template>
  <div class="min-h-screen bg-[#0A0A0A] flex flex-col items-center py-12 px-4 relative overflow-hidden">
    
    <div class="absolute top-[-10%] left-[-10%] w-[500px] h-[500px] bg-ag-purple rounded-full mix-blend-screen filter blur-[150px] opacity-20 animate-pulse"></div>
    <div class="absolute bottom-[-10%] right-[-10%] w-[400px] h-[400px] bg-ag-yellow rounded-full mix-blend-screen filter blur-[150px] opacity-10"></div>

    <div class="w-full max-w-md relative z-10 flex flex-col items-center">
      
      <div class="text-center mb-8">
        <h1 class="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-ag-yellow to-ag-purple tracking-tight mb-2">
          Scanner Absensi
        </h1>
        <p class="text-gray-400 text-sm font-medium flex items-center justify-center gap-2">
          <span class="w-2 h-2 rounded-full bg-ag-yellow animate-pulse"></span>
          Menunggu pindaian QR Jemaat
        </p>
      </div>
      
      <div class="w-full bg-white/5 backdrop-blur-2xl border border-white/10 p-6 rounded-[2rem] shadow-[0_0_50px_rgba(0,0,0,0.5)] flex flex-col items-center">
        
        <div id="reader" class="w-full overflow-hidden rounded-2xl relative bg-black/40 border-2 border-dashed border-white/20 transition-all duration-300 hover:border-ag-purple/50"></div>
        
        <transition name="fade" mode="out-in">
          <div v-if="successMessage" class="w-full mt-6 p-4 bg-emerald-500/10 border border-emerald-500/30 rounded-xl text-center backdrop-blur-md shadow-[0_0_20px_rgba(16,185,129,0.15)] flex flex-col items-center transform transition-all">
            <div class="w-10 h-10 bg-emerald-500/20 rounded-full flex items-center justify-center mb-2 text-emerald-400">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
            </div>
            <p class="font-bold text-white text-lg mb-0.5">Berhasil!</p>
            <p class="text-emerald-400 text-sm font-medium">{{ successMessage }}</p>
          </div>
        </transition>
        
        <transition name="fade" mode="out-in">
          <div v-if="errorMessage" class="w-full mt-6 p-4 bg-red-500/10 border border-red-500/30 rounded-xl text-center backdrop-blur-md shadow-[0_0_20px_rgba(239,68,68,0.15)] flex flex-col items-center transform transition-all">
            <div class="w-10 h-10 bg-red-500/20 rounded-full flex items-center justify-center mb-2 text-red-400">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </div>
            <p class="font-bold text-white text-lg mb-0.5">Akses Ditolak</p>
            <p class="text-red-400 text-sm font-medium">{{ errorMessage }}</p>
          </div>
        </transition>

      </div>
      
      <button @click="goBack" class="group mt-10 px-6 py-3 bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl transition-all duration-300 backdrop-blur-sm flex items-center gap-2">
        <svg class="w-4 h-4 text-gray-400 group-hover:text-white transition-colors group-hover:-translate-x-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
        <span class="text-sm font-bold text-gray-300 group-hover:text-white transition-colors">Kembali ke Profil</span>
      </button>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { Html5QrcodeScanner } from 'html5-qrcode'
import axios from 'axios'

const router = useRouter()
const successMessage = ref('')
const errorMessage = ref('')
let html5QrcodeScanner = null

onMounted(() => {
  html5QrcodeScanner = new Html5QrcodeScanner(
    "reader",
    { fps: 10, qrbox: { width: 250, height: 250 } },
    /* verbose= */ false
  )
  
  html5QrcodeScanner.render(onScanSuccess, onScanFailure)
})

onUnmounted(() => {
  if (html5QrcodeScanner) {
    html5QrcodeScanner.clear().catch(error => {
      console.error("Gagal mematikan kamera", error)
    })
  }
})

const onScanSuccess = async (decodedText) => {
  html5QrcodeScanner.pause(true)
  successMessage.value = ''
  errorMessage.value = ''

  try {
    const response = await axios.post('http://127.0.0.1:8000/scan', {
      qr_code_data: decodedText
    })
    
    const jamAbsen = new Date(response.data.scan_time).toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit', second: '2-digit' })
    successMessage.value = `Tercatat pada jam ${jamAbsen}`
    
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
      html5QrcodeScanner.resume()
    }, 3000)
  }
}

const onScanFailure = (error) => {
  // Diabaikan
}

const goBack = () => {
  router.push('/profile')
}
</script>

<style>
/* =======================================================
   CSS AJAIB: MENGUBAH TAMPILAN BAWAAN LIBRARY HTML5-QRCODE
   AGAR COCOK DENGAN TEMA DARK MODE & GLASSMORPHISM
   ======================================================= */

/* Menghilangkan border bawaan dan merapikan kontainer video */
#reader {
  border: none !important;
  padding: 1rem !important;
}

#reader video {
  border-radius: 1rem !important;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5) !important;
}

/* Merapikan teks keterangan dari library */
#reader__dashboard_section_csr span {
  color: #9CA3AF !important; /* text-gray-400 */
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 0.875rem !important;
}

/* Mewarnai link 'Request Camera Permissions' */
#reader__dashboard_section_csr a {
  color: #FDE021 !important;
  text-decoration: none !important;
  font-weight: bold !important;
}

/* Mengubah Tombol Start / Stop / Permission bawaan library */
#html5-qrcode-button-camera-permission,
#html5-qrcode-button-camera-start,
#html5-qrcode-button-camera-stop {
  background: linear-gradient(to right, #FDE021, #e5c910) !important;
  color: #111827 !important; /* text-gray-900 */
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-weight: 800 !important;
  font-size: 0.875rem !important;
  padding: 0.75rem 1.5rem !important;
  border-radius: 0.75rem !important; /* rounded-xl */
  border: none !important;
  cursor: pointer !important;
  margin: 15px 5px !important;
  transition: all 0.3s ease !important;
  box-shadow: 0 0 20px rgba(253, 224, 33, 0.3) !important;
}

#html5-qrcode-button-camera-permission:hover,
#html5-qrcode-button-camera-start:hover {
  transform: scale(1.05) !important;
}

/* Khusus tombol Stop berwarna merah bata */
#html5-qrcode-button-camera-stop {
  background: linear-gradient(to right, #EF4444, #DC2626) !important;
  color: white !important;
  box-shadow: 0 0 20px rgba(239, 68, 68, 0.3) !important;
}

#html5-qrcode-button-camera-stop:hover {
  transform: scale(1.05) !important;
}

/* Transisi Halus untuk Notifikasi */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease, transform 0.5s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>