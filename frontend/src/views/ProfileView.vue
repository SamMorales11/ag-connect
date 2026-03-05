<template>
  <div class="min-h-screen bg-gray-100 py-10 px-4">
    <div class="max-w-md mx-auto bg-white rounded-2xl shadow-xl overflow-hidden">
      
      <div class="bg-ag-purple p-6 text-center text-white">
        <h1 class="text-2xl font-extrabold mb-1">Kartu Jemaat</h1>
        <p class="text-ag-yellow text-sm font-medium">Arrow Generation Connect</p>
      </div>

      <div v-if="isLoading" class="p-8 text-center text-gray-500">
        <p>Memuat data profil...</p>
      </div>

      <div v-else-if="errorMessage" class="p-8 text-center text-red-500">
        <p>{{ errorMessage }}</p>
        <p class="text-sm mt-2 text-gray-400">Mengalihkan ke halaman login...</p>
      </div>

      <div v-else class="p-6">
        <div class="text-center mb-6">
          <h2 class="text-xl font-bold text-gray-800">{{ user.fullname }}</h2>
          <p class="text-gray-500 text-sm">@{{ user.username }}</p>
          
          <div class="mt-2 flex justify-center items-center gap-2">
            <span class="inline-block px-3 py-1 bg-ag-yellow text-ag-purple text-xs font-bold rounded-full">
              {{ user.status }}
            </span>
            <span v-if="user.is_admin" class="inline-block px-3 py-1 bg-green-100 text-green-700 text-xs font-bold rounded-full border border-green-200">
              Admin
            </span>
          </div>
        </div>

        <hr class="border-gray-200 mb-6">

        <div class="flex flex-col items-center justify-center mb-6">
          <p class="text-xs text-gray-500 mb-3 font-semibold uppercase tracking-wider">QR Absensi Anda</p>
          <div class="p-3 bg-white border-2 border-gray-100 rounded-xl shadow-sm">
            <qrcode-vue :value="user.qr_code_data" :size="200" level="M" />
          </div>
          <p class="text-[10px] text-gray-400 mt-2 text-center max-w-[250px] break-all">
            ID: {{ user.qr_code_data }}
          </p>
        </div>

        <div v-if="user.is_admin" class="flex gap-3 mb-4 mt-8">
          <button @click="goToScan" class="flex-1 bg-ag-purple text-white font-bold py-3 px-2 rounded-xl hover:bg-purple-800 transition-colors shadow-sm text-sm flex justify-center items-center">
            📷 Buka Scanner
          </button>
          <button @click="goToDashboard" class="flex-1 bg-ag-yellow text-ag-purple font-bold py-3 px-2 rounded-xl hover:bg-yellow-400 transition-colors shadow-sm text-sm flex justify-center items-center">
            📊 Data Hadir
          </button>
        </div>

        <button 
          @click="logout" 
          class="w-full bg-red-50 text-red-600 hover:bg-red-100 font-bold py-3 px-4 rounded-xl transition-colors mt-2 text-sm"
        >
          Keluar (Logout)
        </button>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import QrcodeVue from 'qrcode.vue'

const router = useRouter()
const user = ref(null)
const isLoading = ref(true)
const errorMessage = ref('')

onMounted(async () => {
  const token = localStorage.getItem('access_token')
  if (!token) {
    router.push('/')
    return
  }

  try {
    const response = await axios.get('http://127.0.0.1:8000/users/me', {
      headers: { Authorization: `Bearer ${token}` }
    })
    user.value = response.data
  } catch (error) {
    errorMessage.value = 'Sesi Anda telah berakhir atau terjadi kesalahan.'
    localStorage.removeItem('access_token')
    setTimeout(() => router.push('/'), 2000)
  } finally {
    isLoading.value = false
  }
})

// Fungsi-fungsi Tombol
const goToScan = () => router.push('/scan')
const goToDashboard = () => router.push('/dashboard')
const logout = () => {
  localStorage.removeItem('access_token')
  router.push('/')
}
</script>