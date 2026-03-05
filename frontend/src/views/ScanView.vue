<template>
  <div class="min-h-screen bg-gray-100 py-10 px-4 flex flex-col items-center">
    <div class="w-full max-w-md">
      <div class="bg-ag-purple p-4 rounded-t-2xl text-center text-white shadow-md">
        <h1 class="text-xl font-bold">Scanner Absensi</h1>
        <p class="text-ag-yellow text-xs">Arahkan kamera ke QR Jemaat</p>
      </div>
      
      <div class="bg-white p-6 rounded-b-2xl shadow-xl">
        <div id="reader" class="w-full overflow-hidden rounded-lg border-2 border-dashed border-gray-300"></div>
        
        <div v-if="successMessage" class="mt-6 p-4 bg-green-50 border border-green-200 text-green-700 rounded-xl text-center shadow-sm transition-all">
          <p class="font-bold text-lg mb-1">✅ Berhasil!</p>
          <p class="text-sm">{{ successMessage }}</p>
        </div>
        
        <div v-if="errorMessage" class="mt-6 p-4 bg-red-50 border border-red-200 text-red-700 rounded-xl text-center shadow-sm transition-all">
          <p class="font-bold text-lg mb-1">❌ Gagal</p>
          <p class="text-sm">{{ errorMessage }}</p>
        </div>
      </div>
      
      <button @click="goBack" class="mt-8 w-full text-center text-gray-500 hover:text-ag-purple font-medium underline transition-colors">
        Kembali ke Profil
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
  // 1. Konfigurasi Kamera (Kotak Scanner)
  html5QrcodeScanner = new Html5QrcodeScanner(
    "reader",
    { fps: 10, qrbox: { width: 250, height: 250 } },
    /* verbose= */ false
  )
  
  // 2. Nyalakan Scanner
  html5QrcodeScanner.render(onScanSuccess, onScanFailure)
})

// Matikan kamera jika user pindah ke halaman lain
onUnmounted(() => {
  if (html5QrcodeScanner) {
    html5QrcodeScanner.clear().catch(error => {
      console.error("Gagal mematikan kamera", error)
    })
  }
})

// Fungsi ini berjalan otomatis saat Kamera melihat sebuah QR Code
const onScanSuccess = async (decodedText) => {
  // Hentikan kamera sementara agar tidak mengirim data berkali-kali
  html5QrcodeScanner.pause(true)
  successMessage.value = ''
  errorMessage.value = ''

  try {
    // Tembak data QR ke API FastAPI backend Anda
    const response = await axios.post('http://127.0.0.1:8000/scan', {
      qr_code_data: decodedText
    })
    
    // Tampilkan pesan sukses dengan jam absen
    const jamAbsen = new Date(response.data.scan_time).toLocaleTimeString('id-ID')
    successMessage.value = `Kehadiran tercatat pada jam ${jamAbsen}`
    
  } catch (error) {
    // Jika API mengembalikan error (misal QR palsu)
    if (error.response && error.response.status === 404) {
      errorMessage.value = 'QR Code tidak terdaftar di sistem!'
    } else {
      errorMessage.value = 'Terjadi kesalahan pada server.'
    }
  } finally {
    // Apapun hasilnya, nyalakan kamera lagi setelah 3 detik
    setTimeout(() => {
      successMessage.value = ''
      errorMessage.value = ''
      html5QrcodeScanner.resume()
    }, 3000)
  }
}

const onScanFailure = (error) => {
  // Diabaikan: Kamera terus-terusan membaca frame meskipun tidak ada QR
}

const goBack = () => {
  router.push('/profile')
}
</script>

<style>
/* Memperbaiki tampilan tombol bawaan dari library html5-qrcode */
#html5-qrcode-button-camera-permission,
#html5-qrcode-button-camera-start,
#html5-qrcode-button-camera-stop {
  background-color: #FDE021;
  color: #7C2889;
  font-weight: bold;
  padding: 8px 16px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  margin: 10px 5px;
}
#reader__dashboard_section_csr span {
  color: red !important;
}
</style>