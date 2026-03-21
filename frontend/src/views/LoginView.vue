<template>
  <div class="min-h-screen bg-[#0A0A0A] flex items-center justify-center p-4 relative overflow-hidden font-sans">
    
    <div class="fixed top-[-10%] left-[-10%] w-[500px] h-[500px] bg-ag-purple rounded-full mix-blend-screen filter blur-[150px] opacity-20 animate-pulse pointer-events-none"></div>
    <div class="fixed bottom-[-10%] right-[-10%] w-[400px] h-[400px] bg-ag-yellow rounded-full mix-blend-screen filter blur-[150px] opacity-10 pointer-events-none"></div>

    <div class="w-full max-w-md relative z-10 animate-fade-in-up">
      
      <div class="text-center mb-8">
        <img src="/src/assets/LOGO%20AG%20.png" alt="AG Logo" class="h-16 mx-auto mb-6 drop-shadow-[0_0_15px_rgba(124,40,137,0.5)]" />
        <h1 class="text-3xl font-black text-white tracking-tight mb-2">Selamat Datang</h1>
        <p class="text-gray-400 text-sm font-medium">Silakan pilih jalur akses Anda ke portal AG Connect.</p>
      </div>

      <div class="bg-white/5 backdrop-blur-xl border border-white/10 p-6 sm:p-8 rounded-3xl shadow-2xl relative overflow-hidden">
        
        <div class="flex p-1 mb-8 bg-black/40 rounded-xl border border-white/10 relative z-20">
          <button @click="loginRole = 'jemaat'" :class="loginRole === 'jemaat' ? 'bg-gradient-to-r from-emerald-400 to-cyan-500 text-white shadow-lg' : 'text-gray-400 hover:text-white'" class="flex-1 py-3 rounded-lg text-sm font-bold transition-all duration-300 flex items-center justify-center gap-2">
            <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
            Jemaat Biasa
          </button>
          
          <button @click="loginRole = 'admin'" :class="loginRole === 'admin' ? 'bg-gradient-to-r from-ag-purple to-[#5b1d66] text-white shadow-lg' : 'text-gray-400 hover:text-white'" class="flex-1 py-3 rounded-lg text-sm font-bold transition-all duration-300 flex items-center justify-center gap-2">
            <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 11c0 3.517-1.009 6.799-2.753 9.571m-3.44-2.04l.054-.09A13.916 13.916 0 008 11a4 4 0 118 0c0 1.017-.07 2.019-.203 3m-2.118 6.844A21.88 21.88 0 0015.171 17m3.839 1.132c.645-2.266.99-4.659.99-7.132A8 8 0 008 4.07M3 15.364c.64-1.319 1-2.8 1-4.364 0-1.457.39-2.823 1.07-4"></path></svg>
            Admin / Usher
          </button>
        </div>

        <div v-if="errorMessage" class="mb-6 p-4 bg-red-500/10 border border-red-500/50 text-red-400 rounded-xl text-sm text-center flex items-center justify-center gap-2 animate-fade-in-up">
          <svg class="w-5 h-5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          <span>{{ errorMessage }}</span>
        </div>

        <form @submit.prevent="handleLogin" class="space-y-5">
          
          <div class="transition-all duration-300">
            <label class="block text-xs font-bold text-gray-400 uppercase tracking-wider mb-2">
              {{ loginRole === 'jemaat' ? 'Username / Kode Referal' : 'Username Admin' }}
            </label>
            <div class="relative">
              <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                <span class="text-gray-500 font-bold">@</span>
              </div>
              <input v-model="form.username" type="text" required class="w-full pl-10 pr-4 py-3.5 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-ag-purple/50 text-white outline-none transition-all placeholder-gray-600" :placeholder="loginRole === 'jemaat' ? 'Masukkan username Anda...' : 'Ketik username...'">
            </div>
            <p v-if="loginRole === 'jemaat'" class="text-[10px] text-gray-500 mt-2 ml-1">
              *Tanpa perlu password. Pastikan Anda sudah mendaftar.
            </p>
          </div>

          <transition name="slide-fade">
            <div v-if="loginRole === 'admin'">
              <label class="block text-xs font-bold text-gray-400 uppercase tracking-wider mb-2">Password Akses</label>
              <div class="relative">
                <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                  <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
                </div>
                <input v-model="form.password" type="password" required class="w-full pl-10 pr-4 py-3.5 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-ag-purple/50 text-white outline-none transition-all placeholder-gray-600" placeholder="••••••••">
              </div>
            </div>
          </transition>

          <button type="submit" :disabled="isLoading" class="w-full mt-6 font-extrabold py-4 px-4 rounded-xl transition-all duration-300 transform hover:scale-[1.02] flex justify-center items-center disabled:opacity-50 text-white shadow-lg" :class="loginRole === 'jemaat' ? 'bg-gradient-to-r from-emerald-500 to-cyan-600 hover:shadow-[0_0_20px_rgba(16,185,129,0.4)]' : 'bg-gradient-to-r from-ag-purple to-[#5b1d66] hover:shadow-[0_0_20px_rgba(124,40,137,0.4)]'">
            <span v-if="isLoading" class="flex items-center gap-2">
              <svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
              Memproses...
            </span>
            <span v-else class="tracking-wide">
              {{ loginRole === 'jemaat' ? 'Masuk ke Portal Jemaat' : 'Login sebagai Admin' }}
            </span>
          </button>

        </form>
      </div>
      
      <p class="mt-8 text-center text-sm text-gray-400">
        Belum punya akun? <button @click="$router.push('/register')" class="text-ag-yellow font-bold hover:underline">Daftar Jemaat Baru</button>
      </p>
      
      <p class="mt-2 text-center text-sm text-gray-500">
        Kembali ke <button @click="$router.push('/')" class="text-white hover:text-ag-yellow transition-colors hover:underline">Beranda Utama</button>
      </p>

    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const loginRole = ref('jemaat') 
const isLoading = ref(false)
const errorMessage = ref('')

const form = ref({
  username: '',
  password: ''
})

// Fungsi pintar: Reset kolom password & error jika user ganti tab
watch(loginRole, () => {
  form.value.password = ''
  errorMessage.value = ''
})

const handleLogin = async () => {
  isLoading.value = true
  errorMessage.value = ''

  try {
    const params = new URLSearchParams()
    
    // Mencegah error jika jemaat mengetik spasi atau huruf besar
    const cleanUsername = form.value.username.trim().toLowerCase().replace('@', '')
    params.append('username', cleanUsername)
    
    // Otomatis selipkan password untuk jemaat
    if (loginRole.value === 'jemaat') {
      params.append('password', 'default_ag_password_123!')
    } else {
      params.append('password', form.value.password)
    }

    // Tembak ke Backend (main.py)
    const response = await axios.post('https://semskii1-ag-connect-api.hf.space/login', params)
    
    // Simpan kunci akses
    localStorage.setItem('access_token', response.data.access_token)
    
    // Bawa ke Profil / Portal
    router.push('/profile')
    
  } catch (error) {
    if (loginRole.value === 'jemaat') {
      errorMessage.value = 'Username tidak ditemukan. Pastikan Anda mengetik dengan benar atau daftar terlebih dahulu.'
    } else {
      errorMessage.value = 'Username atau Password Admin salah. Akses ditolak.'
    }
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
.animate-fade-in-up { animation: fadeInUp 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(20px) scale(0.95); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}

.slide-fade-enter-active { transition: all 0.3s ease-out; }
.slide-fade-leave-active { transition: all 0.2s cubic-bezier(1, 0.5, 0.8, 1); }
.slide-fade-enter-from, .slide-fade-leave-to {
  transform: translateY(-15px);
  opacity: 0;
}
</style>