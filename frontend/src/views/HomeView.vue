<template>
  <div class="min-h-screen bg-[#0A0A0A] font-sans overflow-x-hidden selection:bg-ag-purple selection:text-white flex flex-col relative">
    
    <header class="fixed top-0 w-full z-40 bg-black/60 backdrop-blur-xl border-b border-white/5 transition-all duration-300">
      <div class="max-w-7xl mx-auto px-4 md:px-6 h-16 md:h-20 flex items-center justify-between relative">
        
        <div class="flex items-center gap-3 cursor-pointer shrink-0" @click="$router.push('/')">
          <img src="/src/assets/LOGO%20AG%20.png" alt="AG Logo" class="h-7 md:h-15 object-contain drop-shadow-[0_0_15px_rgba(124,40,137,0.5)]" />
        </div>
        
        <nav class="hidden md:flex absolute left-1/2 transform -translate-x-1/2 items-center gap-10 text-sm font-bold text-gray-300 tracking-wide">
          <button @click="$router.push('/')" class="text-white hover:text-ag-yellow transition-colors">Home</button>
          
          <button @click="$router.push('/leaderboard')" class="text-emerald-400 hover:text-ag-yellow font-black transition-all flex items-center gap-2 drop-shadow-[0_0_10px_rgba(52,211,153,0.4)] hover:scale-105">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path></svg>
            Klasemen
          </button>
          
          <button @click="scrollToFooter" class="hover:text-ag-purple transition-colors">Kontak</button>
        </nav>

        <div class="flex items-center gap-2 md:gap-5">
          <button @click="showUsherModal = true" class="flex items-center justify-center w-9 h-9 md:w-auto md:h-auto md:px-4 md:py-2 text-ag-yellow hover:text-white transition-colors bg-ag-yellow/10 rounded-lg md:rounded-xl border border-ag-yellow/20 hover:bg-ag-yellow/20">
            <svg class="w-4 h-4 md:w-5 md:h-5 md:mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
            <span class="hidden md:block text-sm font-bold">Scanner</span>
          </button>

          <button @click="$router.push('/login')" class="hidden md:block text-sm font-bold text-gray-300 hover:text-white transition-colors">
            Masuk / Login
          </button>
          
          <button @click="$router.push('/register')" class="text-[10px] md:text-sm font-extrabold bg-gradient-to-r from-ag-purple to-[#5b1d66] text-white px-4 py-2 md:px-6 md:py-2.5 rounded-full hover:shadow-[0_0_20px_rgba(124,40,137,0.5)] transform hover:scale-105 transition-all whitespace-nowrap">
            Gabung
          </button>

          <button @click="toggleMobileMenu" class="md:hidden text-gray-300 hover:text-white ml-1 p-1 focus:outline-none">
            <svg v-if="!isMobileMenuOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
            <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
          </button>
        </div>
      </div>

      <transition name="slide-down">
        <div v-if="isMobileMenuOpen" class="md:hidden absolute top-full left-0 w-full bg-[#0A0A0A]/95 backdrop-blur-2xl border-b border-white/10 flex flex-col items-center py-6 gap-6 shadow-[0_20px_40px_rgba(0,0,0,0.8)] z-50">
          <button @click="navigateMobile('/')" class="text-white hover:text-ag-yellow font-bold text-lg transition-colors tracking-wide">Home</button>
          
          <button @click="navigateMobile('/leaderboard')" class="text-emerald-400 hover:text-ag-yellow font-black text-lg transition-all flex items-center gap-2 drop-shadow-[0_0_10px_rgba(52,211,153,0.4)]">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path></svg>
            Klasemen
          </button>
          
          <button @click="handleMobileContact" class="text-gray-300 hover:text-ag-purple font-bold text-lg transition-colors tracking-wide">Kontak</button>
          <div class="w-1/3 h-px bg-white/10 my-1"></div>
          
          <button @click="navigateMobile('/login')" class="text-gray-400 hover:text-white font-bold text-sm transition-colors flex items-center gap-2">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 11c0 3.517-1.009 6.799-2.753 9.571m-3.44-2.04l.054-.09A13.916 13.916 0 008 11a4 4 0 118 0c0 1.017-.07 2.019-.203 3m-2.118 6.844A21.88 21.88 0 0015.171 17m3.839 1.132c.645-2.266.99-4.659.99-7.132A8 8 0 008 4.07M3 15.364c.64-1.319 1-2.8 1-4.364 0-1.457.39-2.823 1.07-4"></path></svg>
            Masuk / Login
          </button>
        </div>
      </transition>
    </header>

    <main class="relative grow flex items-center justify-center pt-20 md:pt-32 pb-24 overflow-hidden">
      <div class="absolute inset-0 opacity-20 pointer-events-none" style="background-image: linear-gradient(rgba(255,255,255,0.1) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.1) 1px, transparent 1px); background-size: 50px 50px;"></div>
      <div class="absolute bottom-0 w-full h-64 bg-gradient-to-t from-[#0A0A0A] to-transparent z-10 pointer-events-none"></div>

      <div class="relative z-20 w-full max-w-7xl mx-auto px-4 md:px-6 flex flex-col items-center justify-center text-center mt-8 md:mt-0">
        
        <div class="bg-ag-yellow text-gray-900 font-black text-xs md:text-xl px-3 py-1 md:px-4 md:py-1 tracking-widest uppercase shadow-[0_0_30px_rgba(253,224,33,0.4)] mb-6 md:absolute md:top-1/4 md:right-[15%] md:transform md:rotate-12 md:animate-float z-30">
          Connect & Grow
        </div>

        <div class="relative flex flex-col items-center justify-center w-full">
          <h1 class="text-5xl sm:text-7xl md:text-[10vw] font-black uppercase leading-[0.85] md:leading-[0.8] tracking-tighter text-white drop-shadow-2xl flex flex-col items-center w-full">
            <span class="block text-transparent bg-clip-text bg-gradient-to-b from-white to-gray-400 transform hover:scale-105 transition duration-500">Welcome</span>
            
            <span class="flex items-center justify-center w-full my-2 md:my-0">
              <span class="text-sm sm:text-2xl md:text-[2.5vw] text-ag-purple transform -rotate-90 origin-center mr-2 md:mr-6 tracking-normal">TO</span>
              <span class="text-transparent bg-clip-text bg-gradient-to-r from-ag-yellow to-[#e5c910] drop-shadow-[0_0_20px_rgba(253,224,33,0.2)]">Arrow</span>
            </span>
            
            <span class="block text-transparent bg-clip-text bg-gradient-to-b from-gray-200 to-gray-700">Generation</span>
          </h1>
          
          <div class="mt-6 md:mt-0 md:absolute md:bottom-[5%] md:right-[-2%] bg-ag-purple text-white px-4 py-2 text-[10px] md:text-sm font-bold tracking-widest uppercase z-30 shadow-xl border border-white/20 backdrop-blur-sm rounded-lg md:rounded-none">
            Sistem Manajemen Jemaat
          </div>
        </div>
        
        <p class="mt-10 md:mt-16 text-gray-400 text-sm sm:text-base md:text-lg max-w-2xl font-medium tracking-wide z-20 leading-relaxed px-2">
          Pusat layanan digital terintegrasi untuk mengelola data jemaat, mencatat kehadiran ibadah secara <span class="italic text-gray-300">real-time</span>, dan mendukung setiap langkah pelayanan Arrow Generation.
        </p>
      </div>
    </main>

    <footer id="footer-section" class="relative w-full border-t border-white/5 bg-[#0A0A0A]/90 backdrop-blur-xl z-20 pt-12 md:pt-16 pb-8 mt-auto">
      <div class="absolute top-0 left-1/2 transform -translate-x-1/2 w-3/4 h-[1px] bg-gradient-to-r from-transparent via-ag-purple/50 to-transparent"></div>
      <div class="max-w-7xl mx-auto px-6">
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-10 md:gap-8 mb-12">
          <div class="col-span-1 sm:col-span-2">
            <div class="flex items-center gap-3 mb-5">
              <img src="/src/assets/LOGO%20AG%20.png" alt="AG Logo" class="h-8 object-contain" />
              <span class="text-xl font-black text-white tracking-widest uppercase">AG <span class="text-ag-purple">Connect</span></span>
            </div>
            <p class="text-gray-400 text-xs md:text-sm leading-relaxed max-w-md font-medium">Sebuah inovasi sistem manajemen jemaat modern untuk mengoptimalkan pendaftaran, pencatatan absensi, dan pengelolaan data pelayanan secara aman, cepat, dan presisi.</p>
          </div>
          <div>
            <h4 class="text-white font-extrabold mb-4 uppercase tracking-widest text-xs">Navigasi Utama</h4>
            <ul class="space-y-3 text-xs md:text-sm font-medium text-gray-400">
              <li><button @click="$router.push('/')" class="hover:text-ag-yellow transition-colors flex items-center gap-2"><span class="text-ag-purple">▸</span> Beranda</button></li>
              <li><button @click="$router.push('/register')" class="hover:text-ag-yellow transition-colors flex items-center gap-2"><span class="text-ag-purple">▸</span> Pendaftaran Jemaat</button></li>
              <li><button @click="$router.push('/login')" class="hover:text-ag-yellow transition-colors flex items-center gap-2"><span class="text-ag-purple">▸</span> Login Jemaat & Admin</button></li>
            </ul>
          </div>
          <div>
            <h4 class="text-white font-extrabold mb-4 uppercase tracking-widest text-xs">Hubungi Kami</h4>
            <ul class="space-y-3 text-xs md:text-sm font-medium text-gray-400">
              <li class="flex items-start gap-3"><svg class="w-4 h-4 md:w-5 md:h-5 text-ag-yellow shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg><span>Balikpapan, Kalimantan Timur</span></li>
              <li class="flex items-center gap-3"><svg class="w-4 h-4 md:w-5 md:h-5 text-ag-purple shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg><span>arrowgenerationbfog</span></li>
            </ul>
          </div>
        </div>
        <div class="pt-6 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-4">
          <p class="text-gray-600 text-[10px] md:text-xs text-center md:text-left font-medium tracking-wide">&copy; 2026 Arrow Generation Connect. All rights reserved.</p>
        </div>
      </div>
    </footer>

    <div v-if="showUsherModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md transition-opacity">
      <div class="bg-[#111] border border-white/10 p-6 md:p-8 rounded-3xl w-full max-w-sm shadow-[0_0_50px_rgba(0,0,0,0.8)] relative animate-fade-in-up">
        
        <button @click="closeUsherModal" class="absolute top-4 right-4 text-gray-500 hover:text-white transition-colors p-2">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>

        <div class="text-center mb-6 mt-2">
          <div class="w-14 h-14 md:w-16 md:h-16 bg-ag-yellow/10 rounded-full flex items-center justify-center mx-auto mb-3 border border-ag-yellow/20 text-ag-yellow shadow-[0_0_15px_rgba(253,224,33,0.2)]">
            <svg class="w-7 h-7 md:w-8 md:h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
          </div>
          <h3 class="text-lg md:text-xl font-extrabold text-white">Akses Scanner</h3>
          <p class="text-[11px] md:text-xs text-gray-400 mt-1">Masukkan data login Usher Anda</p>
        </div>

        <div v-if="usherError" class="mb-4 p-3 bg-red-500/10 border border-red-500/50 text-red-400 rounded-xl text-xs text-center">
          {{ usherError }}
        </div>

        <form @submit.prevent="handleUsherLogin" class="space-y-4">
          <div>
            <label class="block text-[10px] md:text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">Username</label>
            <input v-model="usherUsername" type="text" required class="w-full px-4 py-3 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-ag-yellow/50 text-white outline-none text-sm" placeholder="Masukkan username">
          </div>
          <div>
            <label class="block text-[10px] md:text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">Password</label>
            <input v-model="usherPassword" type="password" required class="w-full px-4 py-3 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-ag-yellow/50 text-white outline-none text-sm" placeholder="••••••••">
          </div>
          
          <button type="submit" :disabled="isUsherLoading" class="w-full mt-4 bg-gradient-to-r from-ag-yellow to-[#e5c910] hover:shadow-[0_0_20px_rgba(253,224,33,0.4)] text-gray-900 font-extrabold py-3.5 px-4 rounded-xl transition-all duration-300 transform hover:scale-[1.02] flex justify-center items-center disabled:opacity-50 text-sm">
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

const isMobileMenuOpen = ref(false)

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}

const navigateMobile = (path) => {
  isMobileMenuOpen.value = false
  router.push(path)
}

const handleMobileContact = () => {
  isMobileMenuOpen.value = false
  scrollToFooter()
}

const scrollToFooter = () => {
  const footer = document.getElementById('footer-section')
  if (footer) footer.scrollIntoView({ behavior: 'smooth' })
}

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

const handleUsherLogin = async () => {
  isUsherLoading.value = true
  usherError.value = ''

  try {
    const params = new URLSearchParams()
    params.append('username', usherUsername.value)
    params.append('password', usherPassword.value)
    
    const loginRes = await axios.post('https://semskii1-ag-connect-api.hf.space/login', params)
    const token = loginRes.data.access_token

    const profileRes = await axios.get('https://semskii1-ag-connect-api.hf.space/users/me', {
      headers: { Authorization: `Bearer ${token}` }
    })
    
    const user = profileRes.data

    if (user.talents === 'Usher / Greeter' || user.is_admin) {
      localStorage.setItem('access_token', token)
      router.push('/scan')
    } else {
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
  50% { transform: translateY(-15px) rotate(15deg); }
  100% { transform: translateY(0px) rotate(12deg); }
}

.animate-fade-in-up { animation: fadeInUp 0.4s ease-out forwards; }
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(20px) scale(0.95); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}

.slide-down-enter-active, .slide-down-leave-active {
  transition: all 0.3s ease-out;
}
.slide-down-enter-from, .slide-down-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>