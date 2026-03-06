<template>
  <div class="min-h-screen bg-[#0A0A0A] font-sans overflow-hidden selection:bg-ag-purple selection:text-white">
    
    <header class="fixed top-0 w-full z-50 bg-black/40 backdrop-blur-md border-b border-white/5 transition-all duration-300">
      <div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <img src="/src/assets/LOGO AG .png" alt="AG Logo" class="h-15 object-contain drop-shadow-[0_0_15px_rgba(124,40,137,0.5)]" />
        </div>
        
        <nav class="hidden md:flex items-center gap-8 text-sm font-bold text-gray-300 tracking-wide">
          <button @click="$router.push('/')" class="text-white">Home</button>
          <button @click="$router.push('/register')" class="hover:text-ag-yellow transition-colors">Daftar Akun</button>
          <button @click="$router.push('/login')" class="hover:text-ag-purple transition-colors">Admin Login</button>
        </nav>

        <div class="flex items-center gap-4">
          <button @click="$router.push('/login')" class="hidden md:block text-sm font-bold text-white hover:text-ag-yellow transition">Masuk</button>
          <button @click="$router.push('/register')" class="text-sm font-extrabold bg-gradient-to-r from-ag-purple to-[#5b1d66] text-white px-6 py-2.5 rounded-full hover:shadow-[0_0_20px_rgba(124,40,137,0.5)] transform hover:scale-105 transition-all">
            Gabung Sekarang
          </button>
        </div>
      </div>
    </header>

    <main class="relative min-h-screen flex items-center justify-center pt-20">
      
      <div class="absolute inset-0 opacity-20" 
           style="background-image: linear-gradient(rgba(255,255,255,0.1) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.1) 1px, transparent 1px); background-size: 60px 60px;">
      </div>
      
      <div class="absolute bottom-0 w-full h-64 bg-gradient-to-t from-[#0A0A0A] to-transparent z-10"></div>

      <div class="relative z-20 w-full max-w-7xl mx-auto px-4 md:px-6 flex flex-col items-center justify-center text-center">
        
        <div class="absolute top-1/4 right-[10%] md:right-[20%] transform rotate-12 animate-float hidden md:block z-30">
          <div class="bg-ag-yellow text-gray-900 font-black text-xl px-4 py-1 tracking-widest uppercase shadow-[0_0_30px_rgba(253,224,33,0.4)]">
            Connect & Grow
          </div>
        </div>

        <div class="relative inline-block">
          <h1 class="text-[15vw] md:text-[11vw] font-black uppercase leading-[0.8] tracking-tighter text-white drop-shadow-2xl">
            <span class="block text-transparent bg-clip-text bg-gradient-to-b from-white to-gray-400 transform hover:scale-105 transition duration-500">Welcome</span>
            
            <span class="block relative flex justify-center items-center">
              <span class="text-[4vw] md:text-[2.5vw] text-ag-purple transform -rotate-90 origin-center mr-2 md:mr-6 tracking-normal">TO</span>
              <span class="text-transparent bg-clip-text bg-gradient-to-r from-ag-yellow to-[#e5c910] drop-shadow-[0_0_20px_rgba(253,224,33,0.2)]">Arrow</span>
            </span>
            
            <span class="block text-transparent bg-clip-text bg-gradient-to-b from-gray-200 to-gray-700">Generation</span>
          </h1>

          <div class="absolute bottom-[10%] right-0 md:right-[-5%] bg-ag-purple text-white px-3 py-1.5 md:px-5 md:py-2 text-xs md:text-sm font-bold tracking-widest uppercase z-30 shadow-xl border border-white/20 backdrop-blur-sm">
            Sistem Manajemen Jemaat
          </div>
        </div>
        
        <p class="mt-12 text-gray-400 md:text-lg max-w-2xl font-medium tracking-wide z-20">
          Platform digital terintegrasi untuk pendaftaran jemaat, absensi *real-time*, dan pemantauan aktivitas pelayanan Arrow Generation.
        </p>

        <div class="absolute bottom-10 left-1/2 transform -translate-x-1/2 flex flex-col items-center gap-2 animate-bounce z-20 opacity-50">
          <span class="text-xs font-bold tracking-widest uppercase text-gray-500">Scroll</span>
          <svg class="w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path></svg>
        </div>

      </div>
    </main>

  </div>
</template>

<style scoped>
.animate-float {
  animation: float 6s ease-in-out infinite;
}

@keyframes float {
  0% { transform: translateY(0px) rotate(12deg); }
  50% { transform: translateY(-20px) rotate(15deg); }
  100% { transform: translateY(0px) rotate(12deg); }
}
</style>