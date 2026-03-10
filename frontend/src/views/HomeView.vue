<template>
  <div class="min-h-screen bg-[#0A0A0A] font-sans overflow-x-hidden selection:bg-ag-purple selection:text-white flex flex-col relative">
    
    <header class="fixed top-0 w-full z-40 bg-black/40 backdrop-blur-md border-b border-white/5 transition-all duration-300">
      <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between relative">
        
        <div class="flex items-center gap-3 cursor-pointer" @click="router.push('/')">
          <img src="/src/assets/LOGO AG .png" alt="AG Logo" class="h-15 object-contain drop-shadow-[0_0_15px_rgba(124,40,137,0.5)]" />
        </div>
        
        <nav class="hidden md:flex absolute left-1/2 transform -translate-x-1/2 items-center gap-10 text-sm font-bold text-gray-300 tracking-wide">
          <button @click="router.push('/')" class="text-white hover:text-ag-yellow transition-colors">Home</button>
          <button @click="scrollToFooter" class="hover:text-ag-purple transition-colors">Kontak</button>
        </nav>

        <div class="flex items-center gap-3 md:gap-5">
          <button @click="showUsherModal = true" class="flex items-center gap-2 text-xs md:text-sm font-bold text-ag-yellow hover:text-white transition-colors bg-ag-yellow/10 px-3 md:px-4 py-2 rounded-lg border border-ag-yellow/20 hover:bg-ag-yellow/20">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
            <span class="hidden md:block">Buka Scanner</span>
          </button>
          <button @click="router.push('/login')" class="hidden md:block text-sm font-bold text-gray-300 hover:text-white transition-colors">
            Admin Login
          </button>
          <button @click="router.push('/register')" class="text-xs md:text-sm font-extrabold bg-gradient-to-r from-ag-purple to-[#5b1d66] text-white px-4 md:px-6 py-2.5 rounded-full hover:shadow-[0_0_20px_rgba(124,40,137,0.5)] transform hover:scale-105 transition-all">
            Gabung
          </button>
        </div>
      </div>
    </header>

    <main class="relative flex-grow flex items-center justify-center pt-24 md:pt-32 pb-24">
      <div class="absolute inset-0 opacity-20 pointer-events-none" style="background-image: linear-gradient(rgba(255,255,255,0.1) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.1) 1px, transparent 1px); background-size: 60px 60px;"></div>
      <div class="absolute bottom-0 w-full h-64 bg-gradient-to-t from-[#0A0A0A] to-transparent z-10 pointer-events-none"></div>

      <div class="relative z-20 w-full max-w-7xl mx-auto px-4 md:px-6 flex flex-col items-center justify-center text-center">
        <div class="absolute top-1/4 right-[10%] md:right-[20%] transform rotate-12 animate-float hidden md:block z-30">
          <div class="bg-ag-yellow text-gray-900 font-black text-xl px-4 py-1 tracking-widest uppercase shadow-[0_0_30px_rgba(253,224,33,0.4)]">Connect & Grow</div>
        </div>

        <div class="relative inline-block mt-4 md:mt-6">
          <h1 class="text-[15vw] md:text-[11vw] font-black uppercase leading-[0.8] tracking-tighter text-white drop-shadow-2xl">
            <span class="block text-transparent bg-clip-text bg-gradient-to-b from-white to-gray-400 transform hover:scale-105 transition duration-500">Welcome</span>
            <span class="block relative flex justify-center items-center">
              <span class="text-[4vw] md:text-[2.5vw] text-ag-purple transform -rotate-90 origin-center mr-2 md:mr-6 tracking-normal">TO</span>
              <span class="text-transparent bg-clip-text bg-gradient-to-r from-ag-yellow to-[#e5c910] drop-shadow-[0_0_20px_rgba(253,224,33,0.2)]">Arrow</span>
            </span>
            <span class="block text-transparent bg-clip-text bg-gradient-to-b from-gray-200 to-gray-700">Generation</span>
          </h1>
          <div class="absolute bottom-[10%] right-0 md:right-[-5%] bg-ag-purple text-white px-3 py-1.5 md:px-5 md:py-2 text-xs md:text-sm font-bold tracking-widest uppercase z-30 shadow-xl border border-white/20 backdrop-blur-sm">Sistem Manajemen Jemaat</div>
        </div>
        
        <p class="mt-12 text-gray-400 md:text-lg max-w-2xl font-medium tracking-wide z-20 leading-relaxed">
          Pusat layanan digital terintegrasi untuk mengelola data jemaat, mencatat kehadiran ibadah secara <span class="italic text-gray-300">real-time</span>, dan mendukung setiap langkah pelayanan Arrow Generation.
        </p>
      </div>
    </main>

    <footer id="footer-section" class="relative w-full border-t border-white/5 bg-[#0A0A0A]/90 backdrop-blur-xl z-20 pt-16 pb-8 mt-auto">
      <div class="absolute top-0 left-1/2 transform -translate-x-1/2 w-3/4 h-[1px] bg-gradient-to-r from-transparent via-ag-purple/50 to-transparent"></div>
      <div class="max-w-7xl mx-auto px-6">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-12 md:gap-8 mb-12">
          <div class="col-span-1 md:col-span-2">
            <div class="flex items-center gap-3 mb-5">
              <img src="/src/assets/LOGO AG .png" alt="AG Logo" class="h-8 object-contain" />
              <span class="text-xl font-black text-white tracking-widest uppercase">AG <span class="text-ag-purple">Connect</span></span>
            </div>
            <p class="text-gray-400 text-sm leading-relaxed max-w-md font-medium">Sebuah inovasi sistem manajemen jemaat modern untuk mengoptimalkan pendaftaran, pencatatan absensi, dan pengelolaan data pelayanan secara aman, cepat, dan presisi.</p>
          </div>
          <div>
            <h4 class="text-white font-extrabold mb-5 uppercase tracking-widest text-xs">Navigasi Utama</h4>
            <ul class="space-y-3 text-sm font-medium text-gray-400">
              <li><button @click="router.push('/')" class="hover:text-ag-yellow transition-colors flex items-center gap-2"><span class="text-ag-purple">▸</span> Beranda</button></li>
              <li><button @click="router.push('/register')" class="hover:text-ag-yellow transition-colors flex items-center gap-2"><span class="text-ag-purple">▸</span> Pendaftaran Jemaat</button></li>
              <li><button @click="router.push('/login')" class="hover:text-ag-yellow transition-colors flex items-center gap-2"><span class="text-ag-purple">▸</span> Login Admin / Staff</button></li>
            </ul>
          </div>
          <div>
            <h4 class="text-white font-extrabold mb-5 uppercase tracking-widest text-xs">Hubungi Kami</h4>
            <ul class="space-y-3 text-sm font-medium text-gray-400">
              <li class="flex items-start gap-3"><svg class="w-5 h-5 text-ag-yellow shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg><span>Balikpapan, Kalimantan Timur, Indonesia</span></li>
              <li class="flex items-center gap-3"><svg class="w-5 h-5 text-ag-yellow shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"></line></svg><span>@arrowgeneration</span></li>
            </ul>
          </div>
        </div>
        <div class="pt-8 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-4">
          <p class="text-gray-500 text-xs text-center md:text-left font-medium tracking-wide">&copy; 2026 Arrow Generation Connect. All rights reserved.</p>
        </div>
      </div>
    </footer>

    <div v-if="showUsherModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md transition-opacity">
      <div class="bg-[#111] border border-white/10 p-8 rounded-3xl w-full max-w-sm shadow-[0_0_50px_rgba(0,0,0,0.8)] relative animate-fade-in-up">
        
        <button @click="closeUsherModal" class="absolute top-4 right-4 text-gray-500 hover:text-white transition-colors">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>

        <div class="text-center mb-6">
          <div class="w-16 h-16 bg-ag-yellow/10 rounded-full flex items-center justify-center mx-auto mb-3 border border-ag-yellow/20 text-ag-yellow shadow-[0_0_15px_rgba(253,224,33,0.2)]">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
          </div>
          <h3 class="text-xl font-extrabold text-white">Akses Scanner</h3>
          <p class="text-xs text-gray-400 mt-1">Masukkan data login Usher Anda</p>
        </div>

        <div v-if="usherError" class="mb-4 p-3 bg-red-500/10 border border-red-500/50 text-red-400 rounded-xl text-xs text-center">
          {{ usherError }}
        </div>

        <form @submit.prevent="handleUsherLogin" class="space-y-4">
          <div>
            <label class="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">Username</label>
            <input v-model="usherUsername" type="text" required class="w-full px-4 py-3 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-ag-yellow/50 text-white outline-none" placeholder="Masukkan username">
          </div>
          <div>
            <label class="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">Password</label>
            <input v-model="usherPassword" type="password" required class="w-full px-4 py-3 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-ag-yellow/50 text-white outline-none" placeholder="••••••••">
          </div>
          
          <button type="submit" :disabled="isUsherLoading" class="w-full mt-4 bg-gradient-to-r from-ag-yellow to-[#e5c910] hover:shadow-[0_0_20px_rgba(253,224,33,0.4)] text-gray-900 font-extrabold py-3.5 px-4 rounded-xl transition-all duration-300 transform hover:scale-[1.02] flex justify-center items-center disabled:opacity-50">
            <span v-if="isUsherLoading">Memverifikasi...</span>
            <span v-else>Buka Kamera Scanner</span>
          </button>
        </form>

      </div>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

// Fungsi Navigasi Footer
const scrollToFooter = () => {
  const footer = document.getElementById('footer-section')
  if (footer) footer.scrollIntoView({ behavior: 'smooth' })
}

// State untuk Modal Usher
const showUsherModal = ref(false)
const usherUsername = ref('')
const usherPassword = ref('')
const usherError = ref('')
const isUsherLoading = ref(false)

const closeUsherModal = () => {
  showUsherModal.value = false
  usherUsername.value = ''
  usherPassword.value = ''
  usherError.value = ''
}

// Logika Super Aman untuk memastikan hanya Usher/Admin yang masuk
const handleUsherLogin = async () => {
  isUsherLoading.value = true
  usherError.value = ''

  try {
    // 1. Dapatkan Token Login
    const params = new URLSearchParams()
    params.append('username', usherUsername.value)
    params.append('password', usherPassword.value)
    
    const loginRes = await axios.post('http://127.0.0.1:8000/login', params)
    const token = loginRes.data.access_token

    // 2. Verifikasi Data (Apakah dia benar-benar Usher atau Admin?)
    const profileRes = await axios.get('http://127.0.0.1:8000/users/me', {
      headers: { Authorization: `Bearer ${token}` }
    })
    
    const user = profileRes.data

    if (user.talents === 'Usher / Greeter' || user.is_admin) {
      // 3. Jika ya, simpan token dan izinkan masuk ke Scanner
      localStorage.setItem('access_token', token)
      router.push('/scan')
    } else {
      // 4. Jika bukan Usher (misal: jemaat biasa yg menebak password), tendang!
      usherError.value = 'Akses ditolak. Akun Anda bukan terdaftar sebagai Usher.'
    }
  } catch (error) {
    usherError.value = 'Username atau Password salah.'
  } finally {
    isUsherLoading.value = false
  }
}
</script>

<style scoped>
.animate-float { animation: float 6s ease-in-out infinite; }
@keyframes float {
  0% { transform: translateY(0px) rotate(12deg); }
  50% { transform: translateY(-20px) rotate(15deg); }
  100% { transform: translateY(0px) rotate(12deg); }
}

.animate-fade-in-up { animation: fadeInUp 0.4s ease-out forwards; }
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(20px) scale(0.95); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}
</style>