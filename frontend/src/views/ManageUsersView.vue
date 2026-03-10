<template>
  <div class="min-h-screen bg-[#0A0A0A] text-white p-4 md:p-8 font-sans relative overflow-x-hidden">
    
    <div class="fixed top-[-20%] left-[-10%] w-[600px] h-[600px] bg-blue-600 rounded-full mix-blend-screen filter blur-[200px] opacity-10 pointer-events-none"></div>
    <div class="fixed bottom-[-20%] right-[-10%] w-[500px] h-[500px] bg-ag-purple rounded-full mix-blend-screen filter blur-[200px] opacity-10 pointer-events-none"></div>

    <transition name="toast-fade">
      <div v-if="toast.show" class="fixed top-6 right-6 z-[60] flex items-center gap-3 px-5 py-3.5 rounded-2xl shadow-[0_0_30px_rgba(0,0,0,0.5)] backdrop-blur-xl border"
           :class="toast.type === 'success' ? 'bg-emerald-500/10 border-emerald-500/30 text-emerald-400' : 'bg-red-500/10 border-red-500/30 text-red-400'">
        <svg v-if="toast.type === 'success'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
        <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        <span class="text-sm font-bold tracking-wide">{{ toast.message }}</span>
      </div>
    </transition>

    <div class="max-w-7xl mx-auto relative z-10 animate-fade-in-up">
      
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-10 gap-4">
        <div>
          <h1 class="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-white to-gray-400 tracking-tight mb-1">
            Manajemen <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-blue-600">Jemaat</span>
          </h1>
          <p class="text-gray-400 text-sm font-medium">Kelola database pendaftaran, cetak ulang QR, dan atur hak akses.</p>
        </div>
        
        <button @click="router.push('/profile')" class="group flex items-center gap-2 px-5 py-2.5 bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl transition-all duration-300 backdrop-blur-sm">
          <svg class="w-4 h-4 text-gray-400 group-hover:text-white transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
          <span class="text-sm font-semibold text-gray-300 group-hover:text-white">Kembali ke Portal</span>
        </button>
      </div>

      <div class="flex flex-col md:flex-row justify-between items-center gap-4 mb-6 bg-white/5 p-4 border border-white/10 rounded-2xl backdrop-blur-md">
        <div class="relative w-full md:w-96">
          <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
            <svg class="w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
          </div>
          <input v-model="searchQuery" type="text" class="w-full pl-11 pr-4 py-3 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-blue-500/50 text-white placeholder-gray-500 outline-none transition-all text-sm" placeholder="Cari nama, status, atau pelayanan...">
        </div>
        <div class="flex items-center gap-3">
          <span v-if="isSuperAdmin" class="px-3 py-1 bg-ag-yellow/20 text-ag-yellow border border-ag-yellow/30 rounded-lg text-xs font-black uppercase tracking-widest flex items-center gap-1 shadow-[0_0_10px_rgba(253,224,33,0.3)]">
            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 7 6-7 6 7 3-7v12H3V6z"></path></svg>
            Mode Superadmin
          </span>
          <span class="text-xs font-bold text-gray-400 uppercase tracking-widest ml-4">Total:</span>
          <span class="px-3 py-1 bg-blue-500/20 text-blue-400 border border-blue-500/30 rounded-lg font-black">{{ filteredUsers.length }}</span>
        </div>
      </div>

      <div v-if="isLoading" class="flex flex-col items-center justify-center py-20">
        <svg class="animate-spin h-10 w-10 text-blue-500 mb-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
        <p class="text-gray-400 font-medium animate-pulse">Memuat database jemaat...</p>
      </div>

      <div v-else class="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl shadow-lg overflow-hidden flex flex-col">
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse whitespace-nowrap">
            <thead>
              <tr class="bg-black/40 text-gray-400 text-xs uppercase tracking-widest border-b border-white/10">
                <th class="py-5 px-6 font-bold">Data Profil</th>
                <th class="py-5 px-6 font-bold">Kategori / Peran</th>
                <th class="py-5 px-6 font-bold">Kontak / Tgl Lahir</th>
                <th class="py-5 px-6 font-bold text-center">Aksi (Admin)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-white/5">
              <tr v-if="filteredUsers.length === 0">
                <td colspan="4" class="py-16 text-center text-gray-500 text-sm font-medium">
                  Tidak ada data yang cocok dengan pencarian Anda.
                </td>
              </tr>
              <tr v-else v-for="user in filteredUsers" :key="user.id" class="hover:bg-white/[0.03] transition-colors group relative">
                
                <td class="py-4 px-6">
                  <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-full bg-gradient-to-br from-gray-700 to-gray-900 border border-gray-600 flex items-center justify-center text-sm font-bold shadow-inner relative">
                      {{ user.fullname.charAt(0).toUpperCase() }}
                      <div v-if="user.is_admin" class="absolute -bottom-1 -right-1 bg-ag-purple text-white p-0.5 rounded-full border border-black">
                        <svg class="w-2.5 h-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
                      </div>
                    </div>
                    <div>
                      <div class="font-bold text-gray-200 text-sm group-hover:text-blue-400 transition-colors">
                        {{ user.fullname }}
                      </div>
                      <div class="text-[10px] text-gray-500 font-mono mt-0.5">@{{ user.username }}</div>
                    </div>
                  </div>
                </td>
                
                <td class="py-4 px-6">
                  <div class="flex flex-col items-start gap-1.5">
                    <div class="flex items-center gap-2">
                      <span :class="user.status === 'Pelayan Tuhan' ? 'bg-ag-yellow/10 text-ag-yellow border-ag-yellow/20' : 'bg-ag-purple/10 text-ag-purple border-ag-purple/20'" class="px-2 py-0.5 border text-[10px] font-bold rounded uppercase tracking-wider">
                        {{ user.status }}
                      </span>
                      <span v-if="user.is_admin" class="px-2 py-0.5 bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 text-[10px] font-bold rounded uppercase tracking-wider">
                        Admin
                      </span>
                    </div>
                    <span class="text-xs text-gray-400 font-medium">{{ user.talents }}</span>
                  </div>
                </td>

                <td class="py-4 px-6">
                  <div class="text-sm text-gray-300 font-medium flex items-center gap-2 mb-1">
                    <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
                    {{ user.whatsapp || '-' }}
                  </div>
                  <div class="text-xs text-gray-500 flex items-center gap-2">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                    {{ formatDate(user.date_of_birth) }}
                  </div>
                </td>

                <td class="py-4 px-6 text-center">
                  <div class="flex items-center justify-center gap-2 opacity-100 md:opacity-0 group-hover:opacity-100 transition-opacity">
                    
                    <button @click="openQRModal(user)" class="p-2 bg-blue-500/10 text-blue-400 hover:bg-blue-500 hover:text-white rounded-lg transition-colors border border-blue-500/20 hover:shadow-[0_0_15px_rgba(59,130,246,0.5)]" title="Lihat Kartu QR">
                      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v1m6 11h2m-6 0h-2v4m0-11v3m0 0h.01M12 12h4.01M16 20h4M4 12h4m12 0h.01M5 8h2a1 1 0 001-1V5a1 1 0 00-1-1H5a1 1 0 00-1 1v2a1 1 0 001 1zm14 0h2a1 1 0 001-1V5a1 1 0 00-1-1h-2a1 1 0 00-1 1v2a1 1 0 001 1zM5 20h2a1 1 0 001-1v-2a1 1 0 00-1-1H5a1 1 0 00-1 1v2a1 1 0 001 1z"></path></svg>
                    </button>

                    <button v-if="isSuperAdmin && !user.is_admin" @click="openConfirmModal('promote', user)" class="p-2 bg-ag-yellow/10 text-ag-yellow hover:bg-ag-yellow hover:text-gray-900 rounded-lg transition-colors border border-ag-yellow/20 hover:shadow-[0_0_15px_rgba(253,224,33,0.5)]" title="Angkat Menjadi Admin">
                      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 7 6-7 6 7 3-7v12H3V6z"></path></svg>
                    </button>

                    <button v-if="isSuperAdmin && user.username !== 'admin_ag'" @click="openConfirmModal('delete', user)" class="p-2 bg-red-500/10 text-red-400 hover:bg-red-500 hover:text-white rounded-lg transition-colors border border-red-500/20" title="Hapus Data">
                      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                    </button>

                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>

    <div v-if="confirmModal.show" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md transition-opacity animate-fade-in-up">
      <div class="bg-[#111] border border-white/10 p-8 rounded-[2rem] shadow-[0_0_50px_rgba(0,0,0,0.8)] w-full max-w-sm relative text-center">
        
        <div class="w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-5 border shadow-lg"
             :class="confirmModal.type === 'delete' ? 'bg-red-500/10 border-red-500/30 text-red-500 shadow-red-500/20' : 'bg-ag-yellow/10 border-ag-yellow/30 text-ag-yellow shadow-ag-yellow/20'">
          <svg v-if="confirmModal.type === 'delete'" class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
          <svg v-else class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 7 6-7 6 7 3-7v12H3V6z"></path></svg>
        </div>

        <h3 class="text-2xl font-black text-white mb-2">
          {{ confirmModal.type === 'delete' ? 'Konfirmasi Hapus' : 'Promosi Akses' }}
        </h3>
        <p class="text-sm text-gray-400 mb-6 leading-relaxed">
          {{ confirmModal.type === 'delete' ? 'Anda yakin ingin menghapus data' : 'Anda yakin ingin mengangkat' }}
          <strong class="text-white">"{{ confirmModal.userName }}"</strong>
          {{ confirmModal.type === 'delete' ? 'secara permanen? Aksi ini tidak dapat dibatalkan.' : 'menjadi Admin Sistem?' }}
        </p>
        
        <div class="flex gap-3">
          <button @click="closeConfirmModal" :disabled="confirmModal.isLoading" class="flex-1 px-4 py-3 bg-white/5 hover:bg-white/10 text-white font-bold rounded-xl transition-all border border-white/10 disabled:opacity-50">
            Batal
          </button>
          <button @click="executeAction" :disabled="confirmModal.isLoading" class="flex-1 px-4 py-3 font-bold rounded-xl transition-all shadow-lg flex items-center justify-center disabled:opacity-50"
                  :class="confirmModal.type === 'delete' ? 'bg-red-500 hover:bg-red-600 text-white' : 'bg-ag-yellow hover:bg-[#e5c910] text-gray-900'">
            <svg v-if="confirmModal.isLoading" class="animate-spin h-5 w-5 mr-2" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
            <span v-else>{{ confirmModal.type === 'delete' ? 'Ya, Hapus' : 'Ya, Promosikan' }}</span>
          </button>
        </div>
      </div>
    </div>

    <div v-if="selectedUserQR" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md transition-opacity animate-fade-in-up">
      <div class="bg-white p-8 rounded-[2rem] shadow-[0_0_50px_rgba(59,130,246,0.3)] w-full max-w-sm relative text-center">
        <button @click="selectedUserQR = null" class="absolute top-4 right-4 text-gray-400 hover:text-gray-800 transition-colors">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>

        <h3 class="text-xl font-black text-gray-900 mb-1">Kartu Jemaat</h3>
        <p class="text-xs text-gray-500 font-bold uppercase tracking-widest mb-6 border-b pb-4">{{ selectedUserQR.fullname }}</p>
        
        <div class="flex justify-center mb-6">
          <qrcode-vue :value="selectedUserQR.qr_code_data" :size="220" level="M" />
        </div>

        <button @click="selectedUserQR = null" class="w-full bg-gray-900 hover:bg-black text-white font-bold py-3 rounded-xl transition-all">
          Selesai (Tutup)
        </button>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import QrcodeVue from 'qrcode.vue'

const router = useRouter()
const users = ref([])
const isLoading = ref(true)
const searchQuery = ref('')
const selectedUserQR = ref(null)

// State untuk Toast Notification
const toast = ref({ show: false, message: '', type: 'success' })

// State untuk Modal Konfirmasi Custom
const confirmModal = ref({
  show: false,
  type: '', // 'delete' atau 'promote'
  userId: null,
  userName: '',
  isLoading: false
})

const currentUser = ref(null)
const isSuperAdmin = computed(() => {
  return currentUser.value && currentUser.value.username === 'admin_ag'
})

onMounted(async () => {
  const token = localStorage.getItem('access_token')
  if (!token) {
    router.push('/login')
    return
  }
  
  try {
    const meRes = await axios.get('http://127.0.0.1:8000/users/me', {
      headers: { Authorization: `Bearer ${token}` }
    })
    currentUser.value = meRes.data
    await fetchUsers()
  } catch (error) {
    localStorage.removeItem('access_token')
    router.push('/login')
  }
})

const fetchUsers = async () => {
  isLoading.value = true
  try {
    const response = await axios.get('http://127.0.0.1:8000/users')
    users.value = response.data
  } catch (error) {
    showToast('Gagal memuat data dari server.', 'error')
  } finally {
    isLoading.value = false
  }
}

const filteredUsers = computed(() => {
  if (!searchQuery.value) return users.value
  const query = searchQuery.value.toLowerCase()
  return users.value.filter(u => 
    (u.fullname && u.fullname.toLowerCase().includes(query)) ||
    (u.status && u.status.toLowerCase().includes(query)) ||
    (u.talents && u.talents.toLowerCase().includes(query)) ||
    (u.whatsapp && u.whatsapp.toLowerCase().includes(query))
  )
})

const formatDate = (dateString) => {
  if (!dateString) return '-'
  return new Date(dateString).toLocaleDateString('id-ID', { day: 'numeric', month: 'long', year: 'numeric' })
}

const openQRModal = (user) => { selectedUserQR.value = user }

// Fungsi untuk memunculkan Toast Notification
const showToast = (message, type = 'success') => {
  toast.value = { show: true, message, type }
  setTimeout(() => { toast.value.show = false }, 3000)
}

// Buka Custom Modal
const openConfirmModal = (type, user) => {
  confirmModal.value = {
    show: true,
    type: type,
    userId: user.id,
    userName: user.fullname,
    isLoading: false
  }
}

// Tutup Custom Modal
const closeConfirmModal = () => {
  confirmModal.value.show = false
}

// Eksekusi API berdasarkan tipe Modal (Delete/Promote)
const executeAction = async () => {
  confirmModal.value.isLoading = true
  const { type, userId, userName } = confirmModal.value

  try {
    if (type === 'delete') {
      await axios.delete(`http://127.0.0.1:8000/users/${userId}`)
      showToast(`Data ${userName} berhasil dihapus.`, 'success')
    } 
    else if (type === 'promote') {
      await axios.put(`http://127.0.0.1:8000/users/${userId}/promote`)
      showToast(`${userName} berhasil diangkat menjadi Admin!`, 'success')
    }
    await fetchUsers() 
  } catch (error) {
    showToast(`Gagal memproses permintaan Anda.`, 'error')
  } finally {
    closeConfirmModal()
  }
}
</script>

<style scoped>
.animate-fade-in-up { animation: fadeInUp 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(20px) scale(0.95); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}

/* Animasi untuk Toast Notifikasi */
.toast-fade-enter-active, .toast-fade-leave-active { transition: all 0.5s ease; }
.toast-fade-enter-from { opacity: 0; transform: translateX(50px); }
.toast-fade-leave-to { opacity: 0; transform: translateY(-20px); }
</style>