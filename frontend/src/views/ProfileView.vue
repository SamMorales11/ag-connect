<template>
  <div class="min-h-screen bg-[#0A0A0A] p-4 md:p-8 flex justify-center items-start pt-12 relative overflow-x-hidden font-sans">
    
    <div class="fixed top-[-10%] left-[-10%] w-[500px] h-[500px] bg-ag-purple rounded-full mix-blend-screen filter blur-[150px] opacity-20 pointer-events-none"></div>
    <div class="fixed bottom-[-10%] right-[-10%] w-[400px] h-[400px] bg-ag-yellow rounded-full mix-blend-screen filter blur-[150px] opacity-10 pointer-events-none"></div>

    <div v-if="isLoading" class="flex flex-col items-center justify-center mt-32 z-10">
      <svg class="animate-spin h-10 w-10 text-ag-purple mb-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
      <p class="text-gray-400 font-medium animate-pulse">Memuat Data Portal...</p>
    </div>

    <div v-else-if="user" class="w-full max-w-4xl z-10 animate-fade-in-up">
      
      <div class="mb-10 text-center md:text-left flex flex-col md:flex-row items-center justify-between gap-6">
        <div>
          <h1 class="text-3xl md:text-4xl font-black text-white tracking-tight mb-2">
            Portal <span class="text-transparent bg-clip-text bg-gradient-to-r" :class="user.is_admin ? 'from-ag-yellow to-ag-purple' : 'from-emerald-400 to-cyan-500'">
              {{ user.is_admin ? 'Admin' : 'Pribadi Jemaat' }}
            </span>
          </h1>
          <p class="text-gray-400 font-medium text-sm md:text-base">
            {{ user.is_admin ? 'Selamat bertugas! Kelola operasional dan pantau kehadiran jemaat hari ini.' : 'Selamat datang! Pantau kehadiran, tingkatkan poin, dan kelola ID Card Anda.' }}
          </p>
        </div>
        <div class="hidden md:block">
          <div class="px-4 py-2 bg-white/5 border border-white/10 rounded-xl backdrop-blur-md flex items-center gap-3">
             <div class="w-2 h-2 rounded-full animate-pulse" :class="user.is_admin ? 'bg-emerald-400' : 'bg-cyan-400'"></div>
             <span class="text-xs font-bold text-gray-300 tracking-wider uppercase">Status: Online</span>
          </div>
        </div>
      </div>

      <div class="bg-white/5 backdrop-blur-xl border border-white/10 p-6 md:p-8 rounded-[2rem] shadow-2xl flex flex-col md:flex-row items-center md:items-start justify-between gap-8 mb-8 relative overflow-hidden group">
        <div class="absolute top-0 left-0 w-2 h-full bg-gradient-to-b opacity-80" :class="user.is_admin ? 'from-ag-yellow to-ag-purple' : 'from-emerald-400 to-cyan-500'"></div>
        
        <div class="flex items-center gap-6 w-full">
          <div class="w-20 h-20 md:w-24 md:h-24 bg-gradient-to-br from-gray-800 to-black rounded-full border-2 border-white/10 flex items-center justify-center shadow-inner shrink-0 relative">
            <span class="text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-br" :class="user.is_admin ? 'from-ag-yellow to-ag-purple' : 'from-emerald-400 to-cyan-500'">
              {{ user.fullname.charAt(0).toUpperCase() }}
            </span>
            <div v-if="user.is_admin" class="absolute bottom-0 right-0 bg-ag-purple text-white p-1.5 rounded-full border-2 border-[#1a1a1a]">
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
            </div>
          </div>

          <div class="text-left w-full">
            <h2 class="text-2xl font-extrabold text-white tracking-tight mb-1">{{ user.fullname }}</h2>
            <p class="text-gray-400 text-sm font-medium mb-3">@{{ user.username }}</p>
            
            <div class="flex flex-wrap items-center gap-2 mb-3">
              <span class="px-3 py-1 bg-white/10 border border-white/20 text-gray-300 text-xs font-bold rounded-lg tracking-wide">
                {{ user.status }}
              </span>
              <span v-if="user.is_admin" class="px-3 py-1 bg-ag-purple/10 text-ag-purple border border-ag-purple/20 text-xs font-bold rounded-lg tracking-wide">
                Administrator
              </span>
            </div>

            <div class="inline-flex items-center gap-3 px-3 py-1.5 bg-black/50 border border-white/5 rounded-xl shadow-inner">
               <div class="p-1.5 bg-orange-500/20 rounded-lg"><svg class="w-4 h-4 text-orange-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
               <div>
                 <p class="text-[10px] text-gray-500 font-bold uppercase tracking-widest leading-none">Total Poin Saya</p>
                 <p class="text-lg font-black text-orange-400 leading-none mt-1">{{ user.points || 0 }} Pts</p>
               </div>
            </div>
          </div>
        </div>

        <div class="shrink-0 flex flex-col items-center bg-black/40 p-4 rounded-2xl border border-white/5 transition-transform duration-500 group-hover:scale-105">
          <div id="qr-canvas-container" class="p-2 bg-white rounded-xl shadow-[0_0_20px_rgba(255,255,255,0.1)]">
            <qrcode-vue :value="user.qr_code_data" :size="120" level="M" render-as="canvas" />
          </div>
          
          <p class="text-[10px] text-gray-500 font-mono mt-3 uppercase tracking-widest text-center w-full truncate max-w-[100px]" :title="user.qr_code_data">
            ID Akses
          </p>
          
          <button @click="generateCardAndDownload" class="mt-3 px-4 py-2 w-full font-bold text-xs rounded-lg shadow-lg transition-all flex justify-center items-center gap-1" :class="user.is_admin ? 'bg-gradient-to-r from-ag-purple to-purple-600 hover:from-purple-500 hover:to-purple-400 text-white shadow-[0_0_15px_rgba(168,85,247,0.4)]' : 'bg-gradient-to-r from-emerald-500 to-cyan-500 hover:from-emerald-400 hover:to-cyan-400 text-white shadow-[0_0_15px_rgba(16,185,129,0.4)]'">
            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
            Unduh Kartu
          </button>
        </div>
      </div>

      <div v-if="user.is_admin">
        <h3 class="text-lg font-bold text-white mb-5 flex items-center gap-2">
          <svg class="w-5 h-5 text-ag-yellow" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg>
          Pusat Kendali Admin
        </h3>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-5 mb-12">
          <button @click="goToScan" class="group relative bg-white/5 backdrop-blur-md border border-white/10 p-6 rounded-3xl text-left hover:bg-white/10 hover:border-ag-purple/50 transition-all duration-300 overflow-hidden shadow-lg">
            <div class="absolute -right-10 -top-10 w-32 h-32 bg-ag-purple/20 rounded-full blur-3xl group-hover:bg-ag-purple/40 transition-colors duration-500"></div>
            <div class="w-12 h-12 bg-gradient-to-br from-ag-purple to-[#5b1d66] rounded-2xl flex items-center justify-center mb-4 shadow-[0_0_15px_rgba(124,40,137,0.4)] transform group-hover:scale-110 transition-transform">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
            </div>
            <h4 class="text-xl font-bold text-white mb-2 group-hover:text-ag-purple transition-colors">Buka Scanner</h4>
            <p class="text-sm text-gray-400 font-medium">Aktifkan kamera untuk memindai kehadiran jemaat saat ibadah berlangsung.</p>
          </button>

          <button @click="goToDashboard" class="group relative bg-white/5 backdrop-blur-md border border-white/10 p-6 rounded-3xl text-left hover:bg-white/10 hover:border-ag-yellow/50 transition-all duration-300 overflow-hidden shadow-lg">
            <div class="absolute -right-10 -top-10 w-32 h-32 bg-ag-yellow/20 rounded-full blur-3xl group-hover:bg-ag-yellow/40 transition-colors duration-500"></div>
            <div class="w-12 h-12 bg-gradient-to-br from-ag-yellow to-[#e5c910] rounded-2xl flex items-center justify-center mb-4 shadow-[0_0_15px_rgba(253,224,33,0.4)] transform group-hover:scale-110 transition-transform">
              <svg class="w-6 h-6 text-gray-900" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
            </div>
            <h4 class="text-xl font-bold text-white mb-2 group-hover:text-ag-yellow transition-colors">Dashboard Analitik</h4>
            <p class="text-sm text-gray-400 font-medium">Pantau grafik statistik, total kehadiran, dan log absensi secara real-time.</p>
          </button>

          <button @click="router.push('/manage-users')" class="group relative bg-white/5 backdrop-blur-md border border-white/10 p-6 rounded-3xl text-left hover:bg-white/10 hover:border-blue-500/50 transition-all duration-300 overflow-hidden shadow-lg">
            <div class="absolute -right-10 -top-10 w-32 h-32 bg-blue-500/20 rounded-full blur-3xl group-hover:bg-blue-500/40 transition-colors duration-500"></div>
            <div class="w-12 h-12 bg-gradient-to-br from-blue-500 to-blue-700 rounded-2xl flex items-center justify-center mb-4 shadow-[0_0_15px_rgba(59,130,246,0.4)] transform group-hover:scale-110 transition-transform">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
            </div>
            <h4 class="text-xl font-bold text-white mb-2 group-hover:text-blue-400 transition-colors">Manajemen Jemaat</h4>
            <p class="text-sm text-gray-400 font-medium">Kelola database, edit profil, dan cetak ulang QR seluruh jemaat.</p>
          </button>

          <button @click="showExportModal = true" class="group relative bg-white/5 backdrop-blur-md border border-white/10 p-6 rounded-3xl text-left hover:bg-white/10 hover:border-emerald-500/50 transition-all duration-300 overflow-hidden shadow-lg">
            <div class="absolute -right-10 -top-10 w-32 h-32 bg-emerald-500/20 rounded-full blur-3xl group-hover:bg-emerald-500/40 transition-colors duration-500"></div>
            
            <div class="w-12 h-12 bg-gradient-to-br from-emerald-500 to-emerald-700 rounded-2xl flex items-center justify-center mb-4 shadow-[0_0_15px_rgba(16,185,129,0.4)] transform group-hover:scale-110 transition-transform">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
            </div>
            
            <h4 class="text-xl font-bold text-white mb-2 group-hover:text-emerald-400 transition-colors">
              Export Laporan
            </h4>
            <p class="text-sm text-gray-400 font-medium">Unduh laporan kehadiran seluruh jemaat dalam format Excel/CSV.</p>
          </button>
        </div>
      </div>

      <div v-else class="space-y-6 mb-12">
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="bg-[#111]/80 backdrop-blur-xl border border-white/10 rounded-3xl p-6 relative overflow-hidden shadow-lg group">
            <div class="absolute top-0 right-0 w-32 h-32 bg-cyan-500/10 rounded-full blur-3xl group-hover:bg-cyan-500/20 transition-all"></div>
            <h4 class="text-xs font-bold text-gray-500 uppercase tracking-widest mb-4 flex items-center gap-2">
              <svg class="w-4 h-4 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
              Status Pangkat Jemaat
            </h4>
            
            <div class="flex items-end gap-3 mb-2">
              <h3 class="text-2xl font-black text-white tracking-tight">{{ currentTier }}</h3>
            </div>
            <p class="text-sm text-gray-400 mb-6">Kumpulkan poin dengan hadir ibadah untuk naik ke level berikutnya!</p>
            
            <div class="w-full bg-white/5 rounded-full h-3 mb-2 border border-white/5 overflow-hidden">
              <div class="bg-gradient-to-r from-emerald-400 to-cyan-500 h-3 rounded-full transition-all duration-1000 ease-out shadow-[0_0_10px_rgba(16,185,129,0.5)]" :style="{ width: progressPercent + '%' }"></div>
            </div>
            <div class="flex justify-between text-xs font-bold text-gray-500">
              <span>{{ user.points }} Pts</span>
              <span>Target: {{ nextTierPoints }} Pts</span>
            </div>
          </div>

          <div class="bg-[#111]/80 backdrop-blur-xl border border-white/10 rounded-3xl p-6 relative overflow-hidden shadow-lg group">
            <div class="absolute top-0 left-0 w-32 h-32 bg-emerald-500/10 rounded-full blur-3xl group-hover:bg-emerald-500/20 transition-all"></div>
            <h4 class="text-xs font-bold text-gray-500 uppercase tracking-widest mb-4 flex items-center gap-2">
              <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
              Program Ajak Teman
            </h4>
            
            <p class="text-sm text-gray-300 leading-relaxed mb-4">
              Ajak teman Anda mendaftar AG Connect menggunakan <span class="text-white font-bold">Username</span> Anda di bawah ini sebagai Kode Referal. Anda berdua akan mendapatkan <strong class="text-emerald-400">+2 Poin Bonus!</strong>
            </p>
            
            <div class="bg-black/50 border border-white/10 rounded-xl p-3 flex justify-between items-center group-hover:border-emerald-500/30 transition-colors">
              <span class="font-mono text-emerald-400 font-bold tracking-widest text-lg ml-2">@{{ user.username }}</span>
              <button @click="copyReferral" class="px-4 py-2 bg-white/5 hover:bg-white/10 rounded-lg text-xs font-bold text-gray-300 transition-colors">
                {{ copySuccess ? 'Tersalin!' : 'Salin Kode' }}
              </button>
            </div>
          </div>
        </div>

        <div class="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl overflow-hidden shadow-lg">
          <div class="p-6 border-b border-white/5 flex justify-between items-center">
            <h3 class="text-lg font-bold text-white flex items-center gap-2">
              <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
              Riwayat Kehadiran Saya
            </h3>
            <span class="text-xs font-bold bg-white/10 text-gray-300 px-3 py-1 rounded-full">5 Terakhir</span>
          </div>
          
          <div class="overflow-x-auto relative">
            <div v-if="isLoadingMyLogs" class="py-12 flex justify-center items-center">
              <svg class="animate-spin h-6 w-6 text-cyan-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
            </div>

            <div v-else-if="myLogs.length === 0" class="py-12 text-center text-gray-500 text-sm font-medium">
              Belum ada catatan kehadiran ibadah.
            </div>

            <table v-else class="w-full text-left whitespace-nowrap">
              <tbody class="divide-y divide-white/5">
                <tr v-for="log in myLogs" :key="log.id" class="hover:bg-white/[0.02] transition-colors">
                  <td class="py-4 px-6">
                    <p class="font-bold text-gray-200">{{ log.service_type }}</p>
                    <p class="text-[11px] font-mono text-gray-500 mt-0.5">{{ new Date(log.scan_time).toLocaleString('id-ID') }}</p>
                  </td>
                  <td class="py-4 px-6 text-right">
                    <span class="inline-flex items-center gap-1 text-xs font-bold text-emerald-400 bg-emerald-400/10 px-2 py-1 rounded-md border border-emerald-400/20">
                      <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
                      Hadir
                    </span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

      </div>

      <div class="flex justify-center mb-10">
        <button @click="logout" class="flex items-center gap-3 px-8 py-3.5 bg-red-500/10 hover:bg-red-500/20 text-red-400 hover:text-red-300 border border-red-500/20 hover:border-red-500/50 rounded-2xl font-bold transition-all duration-300">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>
          Akhiri Sesi & Keluar
        </button>
      </div>

    </div>

    <div v-if="showExportModal && user?.is_admin" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md transition-opacity animate-fade-in-up">
      <div class="bg-[#111] border border-white/10 p-8 rounded-[2rem] shadow-[0_0_50px_rgba(0,0,0,0.8)] w-full max-w-sm relative text-center">
        <h3 class="text-2xl font-black text-white mb-2">Pilih Laporan</h3>
        <p class="text-sm text-gray-400 mb-6">Tentukan spesifikasi data kehadiran yang ingin Anda unduh ke Excel.</p>
        
        <div class="space-y-2 mb-6 text-left">
          <button @click="exportFilter = 'today'" class="w-full flex justify-between items-center px-4 py-2.5 rounded-xl border transition-all duration-300" :class="exportFilter === 'today' ? 'bg-emerald-500/10 border-emerald-500/50 text-emerald-400' : 'bg-white/5 border-white/10 text-gray-400 hover:text-white'">
            <span class="font-bold text-sm">Hari Ini</span>
            <svg v-if="exportFilter === 'today'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
          </button>
          
          <button @click="exportFilter = 'month'" class="w-full flex justify-between items-center px-4 py-2.5 rounded-xl border transition-all duration-300" :class="exportFilter === 'month' ? 'bg-emerald-500/10 border-emerald-500/50 text-emerald-400' : 'bg-white/5 border-white/10 text-gray-400 hover:text-white'">
            <span class="font-bold text-sm">Bulan Ini</span>
            <svg v-if="exportFilter === 'month'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
          </button>

          <button @click="exportFilter = 'all'" class="w-full flex justify-between items-center px-4 py-2.5 rounded-xl border transition-all duration-300" :class="exportFilter === 'all' ? 'bg-emerald-500/10 border-emerald-500/50 text-emerald-400' : 'bg-white/5 border-white/10 text-gray-400 hover:text-white'">
            <span class="font-bold text-sm">Semua Waktu</span>
            <svg v-if="exportFilter === 'all'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
          </button>
        </div>

        <div class="flex gap-3">
          <button @click="showExportModal = false" :disabled="isExporting" class="flex-1 px-4 py-3 bg-white/5 hover:bg-white/10 text-white font-bold rounded-xl transition-all border border-white/10 disabled:opacity-50">Batal</button>
          <button @click="downloadReport" :disabled="isExporting" class="flex-1 px-4 py-3 bg-emerald-500 hover:bg-emerald-600 text-white font-bold rounded-xl transition-all shadow-[0_0_15px_rgba(16,185,129,0.4)] flex items-center justify-center disabled:opacity-50">
            <span v-if="isExporting">Memproses...</span>
            <span v-else>Unduh CSV</span>
          </button>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import QrcodeVue from 'qrcode.vue'

const router = useRouter()
const user = ref(null)
const isLoading = ref(true)

// State khusus Jemaat
const myLogs = ref([])
const isLoadingMyLogs = ref(false)
const copySuccess = ref(false)

// State Admin
const showExportModal = ref(false)
const exportFilter = ref('today')
const exportServiceType = ref('Semua') 
const isExporting = ref(false)

onMounted(async () => {
  const token = localStorage.getItem('access_token')
  if (!token) {
    router.push('/login')
    return
  }

  try {
    // 1. Ambil Profil User
    const response = await axios.get('https://semskii1-ag-connect-api.hf.space/users/me', {
      headers: { Authorization: `Bearer ${token}` }
    })
    user.value = response.data

    // 2. Jika bukan Admin, tarik riwayat kehadiran pribadinya! (Trik menggunakan fitur search)
    if (!user.value.is_admin) {
      isLoadingMyLogs.value = true
      try {
        const logsRes = await axios.get(`https://semskii1-ag-connect-api.hf.space/attendance/logs?search=${encodeURIComponent(user.value.fullname)}&limit=5`, {
          headers: { Authorization: `Bearer ${token}` }
        })
        myLogs.value = logsRes.data.data
      } catch (err) {
        console.error("Gagal menarik riwayat", err)
      } finally {
        isLoadingMyLogs.value = false
      }
    }

  } catch (error) {
    console.error("Gagal mengambil data user", error)
    localStorage.removeItem('access_token')
    router.push('/login')
  } finally {
    isLoading.value = false
  }
})

// === LOGIKA GAMIFIKASI (JEMAAT) ===
const currentTier = computed(() => {
  const pts = user.value?.points || 0
  if (pts < 50) return 'Pemula (Bronze)'
  if (pts < 150) return 'Setia (Silver)'
  if (pts < 300) return 'Katalis (Gold)'
  return 'Pilar (Platinum)'
})

const nextTierPoints = computed(() => {
  const pts = user.value?.points || 0
  if (pts < 50) return 50
  if (pts < 150) return 150
  if (pts < 300) return 300
  return 'MAX'
})

const progressPercent = computed(() => {
  if (nextTierPoints.value === 'MAX') return 100
  return Math.min(100, ((user.value?.points || 0) / nextTierPoints.value) * 100)
})

const copyReferral = () => {
  navigator.clipboard.writeText(user.value.username)
  copySuccess.value = true
  setTimeout(() => { copySuccess.value = false }, 2000)
}

// === FUNGSI ADMIN & UMUM ===
const goToScan = () => router.push('/scan')
const goToDashboard = () => router.push('/dashboard')

const generateCardAndDownload = () => {
  const qrContainer = document.getElementById('qr-canvas-container');
  const originalQrCanvas = qrContainer ? qrContainer.querySelector('canvas') : null;

  if (!originalQrCanvas) {
    alert("Sistem masih memuat QR Code. Tunggu sebentar lalu klik lagi.");
    return;
  }

  const cardCanvas = document.createElement('canvas');
  cardCanvas.width = 800;
  cardCanvas.height = 1200;
  const ctx = cardCanvas.getContext('2d');

  const gradient = ctx.createLinearGradient(0, 0, 800, 1200);
  gradient.addColorStop(0, '#1E1030'); 
  gradient.addColorStop(1, '#0A0A0A'); 
  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, 800, 1200);

  ctx.fillStyle = '#FDE047'; 
  ctx.font = '900 60px sans-serif';
  ctx.textAlign = 'center';
  ctx.fillText('AG CONNECT', 400, 160);

  ctx.fillStyle = '#D1D5DB'; 
  ctx.font = 'bold 30px sans-serif';
  ctx.fillText('KARTU JEMAAT DIGITAL', 400, 220);

  ctx.fillStyle = '#FFFFFF';
  ctx.fillRect(200, 280, 400, 400); 
  ctx.drawImage(originalQrCanvas, 220, 300, 360, 360); 

  ctx.fillStyle = '#FFFFFF';
  ctx.font = '900 50px sans-serif';
  ctx.fillText(user.value.fullname.toUpperCase(), 400, 800);

  ctx.fillStyle = '#A855F7'; 
  ctx.font = 'bold 35px sans-serif';
  ctx.fillText(user.value.status || 'Jemaat AG', 400, 860);

  ctx.fillStyle = '#111111';
  ctx.fillRect(150, 950, 500, 150); 
  ctx.strokeStyle = '#374151'; 
  ctx.lineWidth = 4;
  ctx.strokeRect(150, 950, 500, 150); 

  ctx.fillStyle = '#9CA3AF'; 
  ctx.font = 'bold 22px sans-serif';
  ctx.fillText('KODE REFERAL SAYA:', 400, 1010);

  ctx.fillStyle = '#10B981'; 
  ctx.font = '900 45px sans-serif';
  ctx.fillText('@' + user.value.username, 400, 1060);

  const link = document.createElement('a');
  link.download = `ID_Card_AG_${user.value.username}.png`; 
  link.href = cardCanvas.toDataURL('image/png', 1.0);
  link.click();
}

const downloadReport = async () => {
  isExporting.value = true
  try {
    const token = localStorage.getItem('access_token')
    const response = await axios.get(`https://semskii1-ag-connect-api.hf.space/export/attendances?filter=${exportFilter.value}&service_type=${encodeURIComponent(exportServiceType.value)}`, {
      headers: { Authorization: `Bearer ${token}` },
      responseType: 'blob' 
    })
    const url = window.URL.createObjectURL(new Blob([response.data]))
    const link = document.createElement('a')
    link.href = url
    link.setAttribute('download', `Laporan_Kehadiran.csv`) 
    document.body.appendChild(link)
    link.click() 
    document.body.removeChild(link)
    window.URL.revokeObjectURL(url)
    showExportModal.value = false
  } catch (error) {
    alert("Terjadi kesalahan jaringan.")
  } finally {
    isExporting.value = false
  }
}

const logout = () => {
  localStorage.removeItem('access_token')
  router.push('/')
}
</script>

<style scoped>
.animate-fade-in-up { animation: fadeInUp 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(20px) scale(0.95); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}
</style>