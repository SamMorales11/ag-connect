<template>
  <div class="min-h-screen bg-gray-50 py-10 px-4 md:px-10">
    <div class="max-w-4xl mx-auto">
      
      <div class="flex justify-between items-center mb-8 bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <div>
          <h1 class="text-2xl font-extrabold text-ag-purple">Dashboard Kehadiran</h1>
          <p class="text-gray-500 text-sm">Pantau absensi jemaat Arrow Generation secara real-time</p>
        </div>
        <button @click="goBack" class="px-4 py-2 bg-gray-100 text-gray-600 rounded-lg hover:bg-gray-200 font-medium transition-colors">
          Kembali
        </button>
      </div>

      <div class="bg-white rounded-2xl shadow-md overflow-hidden border border-gray-200">
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse">
            <thead>
              <tr class="bg-ag-purple text-white text-sm uppercase tracking-wider">
                <th class="py-4 px-6 font-semibold">No</th>
                <th class="py-4 px-6 font-semibold">Nama Jemaat</th>
                <th class="py-4 px-6 font-semibold">Status</th>
                <th class="py-4 px-6 font-semibold">Waktu Hadir</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100">
              
              <tr v-if="isLoading">
                <td colspan="4" class="py-8 text-center text-gray-500">Memuat data absensi...</td>
              </tr>
              <tr v-else-if="attendances.length === 0">
                <td colspan="4" class="py-8 text-center text-gray-500">Belum ada data kehadiran hari ini.</td>
              </tr>

              <tr v-else v-for="(absen, index) in attendances" :key="absen.id" class="hover:bg-gray-50 transition-colors">
                <td class="py-4 px-6 text-gray-600">{{ index + 1 }}</td>
                <td class="py-4 px-6 font-bold text-gray-800">{{ absen.owner.fullname }}</td>
                <td class="py-4 px-6">
                  <span class="px-3 py-1 bg-ag-yellow text-ag-purple text-xs font-bold rounded-full">
                    {{ absen.owner.status }}
                  </span>
                </td>
                <td class="py-4 px-6 text-gray-600 font-medium">
                  {{ formatTime(absen.scan_time) }}
                </td>
              </tr>
              
            </tbody>
          </table>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const attendances = ref([])
const isLoading = ref(true)

// Ambil data dari Backend saat halaman dibuka
onMounted(async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/attendances')
    attendances.value = response.data
  } catch (error) {
    console.error("Gagal mengambil data", error)
  } finally {
    isLoading.value = false
  }
})

// Fungsi merapikan format jam/tanggal
const formatTime = (isoString) => {
  const date = new Date(isoString)
  return date.toLocaleString('id-ID', { 
    weekday: 'short', 
    day: 'numeric', 
    month: 'short', 
    hour: '2-digit', 
    minute: '2-digit',
    second: '2-digit'
  })
}

const goBack = () => {
  router.push('/profile')
}
</script>