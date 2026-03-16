<template>
  <div class="min-h-screen bg-[#0A0A0A] text-white p-4 md:p-8 font-sans relative overflow-x-hidden">
    
    <div class="fixed top-[-20%] left-[-10%] w-[600px] h-[600px] bg-ag-yellow rounded-full mix-blend-screen filter blur-[200px] opacity-10 pointer-events-none"></div>
    <div class="fixed bottom-[-20%] right-[-10%] w-[500px] h-[500px] bg-ag-purple rounded-full mix-blend-screen filter blur-[200px] opacity-10 pointer-events-none"></div>

    <div class="max-w-7xl mx-auto relative z-10 animate-fade-in-up">
      
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 gap-4">
        <div>
          <h1 class="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-ag-yellow to-ag-purple tracking-tight mb-1">
            Dashboard <span class="text-white">Analitik</span>
          </h1>
          <p class="text-gray-400 text-sm font-medium">Pantau kehadiran dan berikan poin apresiasi jemaat.</p>
        </div>
        
        <button @click="$router.push('/profile')" class="group shrink-0 flex items-center gap-2 px-5 py-2.5 bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl transition-all duration-300 backdrop-blur-sm">
          <svg class="w-4 h-4 text-gray-400 group-hover:text-white transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
          <span class="text-sm font-semibold text-gray-300 group-hover:text-white">Kembali ke Portal</span>
        </button>
      </div>

      <div v-if="isLoading" class="flex flex-col items-center justify-center py-20">
        <svg class="animate-spin h-10 w-10 text-ag-yellow mb-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
        <p class="text-gray-400">Menyinkronkan data...</p>
      </div>

      <div v-else>
        
        <div class="flex flex-col gap-5 border-b border-white/10 pb-6 mb-8">
          
          <div class="w-full overflow-x-auto pb-2 -mb-2 hide-scrollbar relative">
            <div class="flex items-center gap-2 w-max pr-4">
              <button @click="activeTab = 'Leaderboard'" :class="activeTab === 'Leaderboard' ? 'bg-emerald-500 text-white shadow-lg shadow-emerald-500/20' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent whitespace-nowrap">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path></svg>
                Top Leaderboard
              </button>
              
              <button @click="activeTab = 'AG'" :class="activeTab === 'AG' ? 'bg-ag-purple text-white shadow-lg shadow-ag-purple/20' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent whitespace-nowrap">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 14v3m4-3v3m4-3v3M3 21h18M3 10h18M3 7l9-4 9 4M4 10h16v11H4V10z"></path></svg>
                AG ({{ filteredAgLogs.length }})
              </button>

              <button @click="activeTab = 'AG Lite'" :class="activeTab === 'AG Lite' ? 'bg-ag-yellow text-gray-900 shadow-lg shadow-ag-yellow/20' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent whitespace-nowrap">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                AG Lite ({{ filteredAgLiteLogs.length }})
              </button>

              <button @click="activeTab = 'Doa Fajar'" :class="activeTab === 'Doa Fajar' ? 'bg-blue-500 text-white shadow-lg shadow-blue-500/20' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent whitespace-nowrap">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                Doa Fajar ({{ filteredDoaFajarLogs.length }})
              </button>

              <button @click="activeTab = 'Doa Pengerja'" :class="activeTab === 'Doa Pengerja' ? 'bg-orange-500 text-white shadow-lg shadow-orange-500/20' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent whitespace-nowrap">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                Doa Pengerja ({{ filteredDoaPengerjaLogs.length }})
              </button>

              <button @click="activeTab = 'AGC/Fellowship'" :class="activeTab === 'AGC/Fellowship' ? 'bg-pink-500 text-white shadow-lg shadow-pink-500/20' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent whitespace-nowrap">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path></svg>
                AGC ({{ filteredAgcLogs.length }})
              </button>
            </div>
          </div>

          <div class="flex flex-col sm:flex-row items-center justify-end gap-3 w-full shrink-0">
            
            <div v-if="activeTab !== 'Leaderboard'" class="relative w-full sm:w-40">
              <input 
                v-model="selectedDate" 
                type="date" 
                class="w-full bg-black/50 border border-gray-700 text-white text-sm rounded-xl px-4 py-2.5 focus:border-ag-purple focus:ring-1 focus:ring-ag-purple outline-none transition-all cursor-pointer custom-date-input"
              >
              <button v-if="selectedDate" @click="selectedDate = ''" class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 hover:text-red-400">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
              </button>
            </div>

            <div class="relative w-full sm:w-56">
              <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
              </div>
              <input 
                v-model="searchQuery" 
                type="text" 
                placeholder="Cari jemaat..." 
                class="w-full bg-black/50 border border-gray-700 text-white text-sm rounded-xl pl-10 pr-4 py-2.5 focus:border-ag-yellow focus:ring-1 focus:ring-ag-yellow outline-none transition-all placeholder-gray-500"
              >
            </div>

            <button @click="showResetModal = true" class="w-full sm:w-auto px-5 py-2.5 rounded-xl font-bold text-sm transition-all border border-red-500/30 bg-red-500/10 text-red-500 hover:bg-red-500 hover:text-white shadow-[0_0_15px_rgba(239,68,68,0.2)] flex items-center justify-center gap-2">
              <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
              <span class="whitespace-nowrap">Reset Poin</span>
            </button>

          </div>
        </div>

        <div v-if="activeTab === 'Leaderboard'" class="animate-fade-in-up">
          <div class="space-y-4">
            
            <div v-if="paginatedUsers.length === 0" class="py-16 text-center text-gray-500 text-sm font-medium bg-white/5 rounded-3xl border border-white/10 backdrop-blur-md">
              Jemaat tidak ditemukan.
            </div>

            <div v-else v-for="(user, index) in paginatedUsers" :key="user.id"
                 class="relative group flex flex-col sm:flex-row items-center justify-between p-4 sm:p-5 rounded-2xl transition-all duration-300 overflow-hidden backdrop-blur-md"
                 :class="{
                   'bg-gradient-to-r from-yellow-500/10 via-black/40 to-black/40 border border-yellow-500/50 shadow-[0_0_30px_rgba(234,179,8,0.15)] transform hover:-translate-y-1 hover:shadow-[0_0_40px_rgba(234,179,8,0.3)]': (currentPage - 1) * itemsPerPage + index === 0 && user.points > 0,
                   'bg-gradient-to-r from-gray-400/10 via-black/40 to-black/40 border border-gray-400/50 shadow-[0_0_30px_rgba(156,163,175,0.1)] transform hover:-translate-y-1': (currentPage - 1) * itemsPerPage + index === 1 && user.points > 0,
                   'bg-gradient-to-r from-orange-600/10 via-black/40 to-black/40 border border-orange-600/50 shadow-[0_0_30px_rgba(234,88,12,0.1)] transform hover:-translate-y-1': (currentPage - 1) * itemsPerPage + index === 2 && user.points > 0,
                   'bg-white/5 border border-white/10 hover:bg-white/10 hover:border-white/30 transform hover:-translate-y-1': (currentPage - 1) * itemsPerPage + index > 2 || user.points === 0
                 }">

              <div class="flex items-center gap-4 w-full sm:w-auto mb-4 sm:mb-0">
                <div class="flex-shrink-0 w-12 h-12 rounded-full flex items-center justify-center font-black text-lg relative"
                     :class="{
                       'bg-gradient-to-br from-yellow-400 to-yellow-600 text-gray-900 shadow-[0_0_20px_rgba(250,204,21,0.5)]': (currentPage - 1) * itemsPerPage + index === 0 && user.points > 0,
                       'bg-gradient-to-br from-gray-300 to-gray-500 text-gray-900 shadow-[0_0_20px_rgba(156,163,175,0.4)]': (currentPage - 1) * itemsPerPage + index === 1 && user.points > 0,
                       'bg-gradient-to-br from-orange-400 to-orange-600 text-white shadow-[0_0_20px_rgba(249,115,22,0.4)]': (currentPage - 1) * itemsPerPage + index === 2 && user.points > 0,
                       'bg-black/50 text-gray-400 border border-gray-600': (currentPage - 1) * itemsPerPage + index > 2 || user.points === 0
                     }">
                  <span v-if="(currentPage - 1) * itemsPerPage + index === 0 && user.points > 0" class="absolute -top-3 text-2xl drop-shadow-md">👑</span>
                  {{ (currentPage - 1) * itemsPerPage + index + 1 }}
                </div>

                <div class="hidden md:flex w-12 h-12 rounded-full border border-white/10 bg-black/50 items-center justify-center font-black text-lg text-transparent bg-clip-text bg-gradient-to-br from-ag-yellow to-ag-purple">
                  {{ user.fullname.charAt(0).toUpperCase() }}
                </div>

                <div>
                  <h3 class="text-lg font-black text-white leading-tight group-hover:text-ag-yellow transition-colors flex items-center gap-2">
                    {{ user.fullname }}
                    <span v-if="(currentPage - 1) * itemsPerPage + index === 0 && user.points > 0" class="text-[10px] font-black px-2 py-0.5 bg-yellow-500/20 text-yellow-400 rounded-md border border-yellow-500/30 uppercase tracking-widest">MVP</span>
                  </h3>
                  <p class="text-xs font-mono text-gray-500 mt-0.5">@{{ user.username }}</p>
                </div>
              </div>

              <div class="flex items-center justify-between sm:justify-end w-full sm:w-auto gap-4 md:gap-8">
                
                <div class="flex flex-col items-start sm:items-end">
                  <span class="text-[10px] font-bold text-gray-500 uppercase tracking-widest mb-1">Total Poin</span>
                  <div class="flex items-center gap-1.5 px-4 py-1.5 rounded-xl border transition-all"
                       :class="{
                         'bg-yellow-500/10 border-yellow-500/30 text-yellow-400 shadow-[0_0_15px_rgba(234,179,8,0.2)]': (currentPage - 1) * itemsPerPage + index === 0 && user.points > 0,
                         'bg-emerald-500/10 border-emerald-500/30 text-emerald-400 shadow-[0_0_10px_rgba(16,185,129,0.2)]': ((currentPage - 1) * itemsPerPage + index > 0) || user.points === 0
                       }">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                    <span class="font-black text-xl">{{ user.points }}</span>
                  </div>
                </div>

                <button @click="openConfirmModal(user)" class="shrink-0 flex items-center justify-center gap-2 px-4 py-3 sm:py-2.5 bg-gradient-to-r from-ag-purple to-purple-600 hover:from-purple-500 hover:to-purple-400 text-white text-xs font-bold rounded-xl shadow-[0_0_15px_rgba(168,85,247,0.4)] transform hover:scale-105 transition-all focus:ring-2 focus:ring-purple-400 outline-none">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v13m0-13V6a2 2 0 112 2h-2zm0 0V5.5A2.5 2.5 0 109.5 8H12zm-7 4h14M5 12a2 2 0 110-4h14a2 2 0 110 4M5 12v7a2 2 0 002 2h10a2 2 0 002-2v-7"></path></svg>
                  <span class="hidden sm:inline">+10 Kuis</span>
                </button>

              </div>
            </div>

          </div>
        </div>
        
        <div v-else class="animate-fade-in-up">
          <div class="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl shadow-lg overflow-hidden">
            <div class="overflow-x-auto">
              <table class="w-full text-left whitespace-nowrap">
                <thead>
                  <tr class="bg-black/40 text-gray-500 text-xs uppercase tracking-widest border-b border-white/5">
                    <th class="py-4 px-6 font-bold">Waktu Hadir</th>
                    <th class="py-4 px-6 font-bold">Nama Jemaat</th>
                    <th class="py-4 px-6 font-bold">Kategori</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-white/5">
                  <tr v-if="currentPaginatedLogs.length === 0">
                    <td colspan="3" class="py-12 text-center text-gray-500 text-sm">
                      <span v-if="selectedDate">Tidak ada data absensi untuk tanggal ini.</span>
                      <span v-else>Data absensi belum tersedia.</span>
                    </td>
                  </tr>
                  <tr v-else v-for="log in currentPaginatedLogs" :key="log.id" class="hover:bg-white/[0.02] transition-colors">
                    <td class="py-4 px-6"><span class="text-xs font-mono text-gray-300">{{ new Date(log.scan_time).toLocaleString('id-ID') }}</span></td>
                    <td class="py-4 px-6 font-bold text-gray-200">{{ log.user?.fullname || 'User Dihapus' }}</td>
                    <td class="py-4 px-6 text-xs text-gray-400">{{ log.user?.status || '-' }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <div v-if="currentTotalPages > 1" class="flex flex-col sm:flex-row justify-between items-center mt-6 px-2 gap-4 animate-fade-in-up">
          <span class="text-sm font-medium text-gray-500">
            Halaman <span class="text-white">{{ currentPage }}</span> dari <span class="text-white">{{ currentTotalPages }}</span>
          </span>
          <div class="flex gap-2">
            <button @click="prevPage" :disabled="currentPage === 1" class="px-4 py-2 bg-white/5 hover:bg-white/10 border border-white/10 rounded-lg text-sm font-bold transition-all disabled:opacity-30 disabled:cursor-not-allowed">
              Sebelumnya
            </button>
            <button @click="nextPage" :disabled="currentPage === currentTotalPages" class="px-4 py-2 bg-white/5 hover:bg-white/10 border border-white/10 rounded-lg text-sm font-bold transition-all disabled:opacity-30 disabled:cursor-not-allowed">
              Selanjutnya
            </button>
          </div>
        </div>

      </div>
    </div>

    <transition name="fade">
      <div v-if="showConfirmModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm px-4">
        <div class="bg-[#111] border border-white/10 p-6 md:p-8 rounded-3xl max-w-sm w-full text-center shadow-[0_0_50px_rgba(168,85,247,0.15)] transform transition-all">
          <div class="w-16 h-16 rounded-full bg-ag-purple/10 border border-ag-purple/30 flex items-center justify-center mx-auto mb-4 text-ag-purple">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v13m0-13V6a2 2 0 112 2h-2zm0 0V5.5A2.5 2.5 0 109.5 8H12zm-7 4h14M5 12a2 2 0 110-4h14a2 2 0 110 4M5 12v7a2 2 0 002 2h10a2 2 0 002-2v-7"></path></svg>
          </div>
          <h3 class="text-2xl font-black text-white mb-2">Berikan +10 Poin?</h3>
          <p class="text-gray-400 text-sm mb-8 leading-relaxed">
            Anda akan mengirimkan poin kuis kepada <br>
            <span class="font-bold text-ag-yellow text-lg">{{ selectedUser?.fullname }}</span>
          </p>
          <div class="flex gap-3">
            <button @click="showConfirmModal = false" :disabled="isGivingPoints" class="flex-1 py-3 rounded-xl font-bold text-gray-400 bg-white/5 hover:bg-white/10 hover:text-white transition-colors disabled:opacity-50">Batal</button>
            <button @click="confirmGivePoints" :disabled="isGivingPoints" class="flex-1 py-3 rounded-xl font-bold text-white bg-gradient-to-r from-ag-purple to-purple-600 hover:from-purple-500 hover:to-purple-400 transition-all shadow-[0_0_20px_rgba(168,85,247,0.4)] flex justify-center items-center disabled:opacity-50">
              <span v-if="isGivingPoints" class="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></span>
              <span v-else>Ya, Berikan!</span>
            </button>
          </div>
        </div>
      </div>
    </transition>

    <transition name="fade">
      <div v-if="showResetModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm px-4">
        <div class="bg-[#111] border border-white/10 p-6 md:p-8 rounded-3xl max-w-sm w-full text-center shadow-[0_0_50px_rgba(239,68,68,0.2)] transform transition-all">
          <div class="w-16 h-16 rounded-full bg-red-500/10 border border-red-500/30 flex items-center justify-center mx-auto mb-4 text-red-500">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
          </div>
          <h3 class="text-2xl font-black text-white mb-2">Reset Semua Poin?</h3>
          <p class="text-gray-400 text-sm mb-6 leading-relaxed">
            Tindakan ini akan mengembalikan <strong class="text-red-400">POIN SELURUH JEMAAT menjadi 0</strong>. Gunakan hanya saat bersiap untuk pengujian publik atau memulai Musim (Season) baru. Tindakan ini tidak dapat dibatalkan.
          </p>
          <div class="flex gap-3">
            <button @click="showResetModal = false" :disabled="isResetting" class="flex-1 py-3 rounded-xl font-bold text-gray-400 bg-white/5 hover:bg-white/10 hover:text-white transition-colors disabled:opacity-50">Batal</button>
            <button @click="confirmResetPoints" :disabled="isResetting" class="flex-1 py-3 rounded-xl font-bold text-white bg-red-600 hover:bg-red-500 transition-all shadow-[0_0_20px_rgba(239,68,68,0.4)] flex justify-center items-center disabled:opacity-50">
              <span v-if="isResetting" class="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></span>
              <span v-else>Ya, Reset Poin!</span>
            </button>
          </div>
        </div>
      </div>
    </transition>

    <transition name="bounce">
      <div v-if="showToast" class="fixed bottom-10 left-1/2 transform -translate-x-1/2 z-50 px-6 py-3 rounded-2xl border backdrop-blur-xl flex items-center gap-3 shadow-2xl"
           :class="toastType === 'success' ? 'bg-emerald-500/20 border-emerald-500/50 text-emerald-400' : 'bg-red-500/20 border-red-500/50 text-red-400'">
        <span class="text-2xl">{{ toastType === 'success' ? '🎉' : '❌' }}</span>
        <span class="font-bold text-sm tracking-wide">{{ toastMessage }}</span>
      </div>
    </transition>

  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const isLoading = ref(true)
const allLogs = ref([])
const allUsers = ref([])
const activeTab = ref('Leaderboard') 

const searchQuery = ref('')
const selectedDate = ref('') 
const currentPage = ref(1)
const itemsPerPage = 20

watch([searchQuery, activeTab, selectedDate], () => {
  currentPage.value = 1
})

const showConfirmModal = ref(false)
const selectedUser = ref(null)
const isGivingPoints = ref(false)

const showResetModal = ref(false)
const isResetting = ref(false)

const showToast = ref(false)
const toastMessage = ref('')
const toastType = ref('success')
let toastTimer = null

onMounted(async () => {
  const token = localStorage.getItem('access_token')
  if (!token) {
    router.push('/login')
    return
  }
  await fetchData(token)
})

const fetchData = async (token) => {
  try {
    const [logsRes, usersRes] = await Promise.all([
      axios.get('https://semskii1-ag-connect-api.hf.space/attendance/logs', { headers: { Authorization: `Bearer ${token}` } }),
      axios.get('https://semskii1-ag-connect-api.hf.space/users', { headers: { Authorization: `Bearer ${token}` } })
    ])
    allLogs.value = logsRes.data.map(log => ({ ...log, service_type: log.service_type || 'AG' }))
    allUsers.value = usersRes.data
  } catch (error) {
    console.error("Gagal memuat data", error)
  } finally {
    isLoading.value = false
  }
}

const openConfirmModal = (user) => {
  selectedUser.value = user
  showConfirmModal.value = true
}

const confirmGivePoints = async () => {
  if (!selectedUser.value) return
  isGivingPoints.value = true
  clearTimeout(toastTimer)
  showToast.value = false

  try {
    const token = localStorage.getItem('access_token')
    const response = await axios.post(`https://semskii1-ag-connect-api.hf.space/users/${selectedUser.value.id}/add-quiz-points`, {}, {
      headers: { Authorization: `Bearer ${token}` }
    })
    selectedUser.value.points += 10
    toastType.value = 'success'
    toastMessage.value = response.data.message
    showToast.value = true
  } catch (error) {
    toastType.value = 'error'
    toastMessage.value = error.response?.data?.detail || "Gagal memberikan poin."
    showToast.value = true
  } finally {
    isGivingPoints.value = false
    showConfirmModal.value = false
    selectedUser.value = null
    toastTimer = setTimeout(() => { showToast.value = false }, 3000)
  }
}

const confirmResetPoints = async () => {
  isResetting.value = true
  clearTimeout(toastTimer)
  showToast.value = false

  try {
    const token = localStorage.getItem('access_token')
    const response = await axios.put('https://semskii1-ag-connect-api.hf.space/users/reset-points', {}, {
      headers: { Authorization: `Bearer ${token}` }
    })
    
    allUsers.value.forEach(u => u.points = 0)
    
    toastType.value = 'success'
    toastMessage.value = response.data.message
    showToast.value = true
  } catch (error) {
    toastType.value = 'error'
    toastMessage.value = error.response?.data?.detail || "Gagal mereset poin. Pastikan Anda memiliki akses Admin."
    showToast.value = true
  } finally {
    isResetting.value = false
    showResetModal.value = false
    toastTimer = setTimeout(() => { showToast.value = false }, 3000)
  }
}

const filteredUsers = computed(() => {
  let users = [...allUsers.value].sort((a, b) => b.points - a.points).filter(u => u.points >= 0)
  if (searchQuery.value) {
    const q = searchQuery.value.toLowerCase()
    users = users.filter(u => u.fullname.toLowerCase().includes(q) || u.username.toLowerCase().includes(q))
  }
  return users
})

const getFilteredLogs = (type) => {
  let logs = allLogs.value.filter(log => log.service_type === type).sort((a,b) => new Date(b.scan_time) - new Date(a.scan_time))
  
  if (searchQuery.value) {
    const q = searchQuery.value.toLowerCase()
    logs = logs.filter(log => (log.user?.fullname || '').toLowerCase().includes(q))
  }

  if (selectedDate.value) {
    logs = logs.filter(log => {
      const dateObj = new Date(log.scan_time)
      const year = dateObj.getFullYear()
      const month = String(dateObj.getMonth() + 1).padStart(2, '0')
      const day = String(dateObj.getDate()).padStart(2, '0')
      const formattedLogDate = `${year}-${month}-${day}`
      return formattedLogDate === selectedDate.value
    })
  }

  return logs
}

const filteredAgLogs = computed(() => getFilteredLogs('AG'))
const filteredAgLiteLogs = computed(() => getFilteredLogs('AG Lite'))
const filteredDoaFajarLogs = computed(() => getFilteredLogs('Doa Fajar'))
const filteredDoaPengerjaLogs = computed(() => getFilteredLogs('Doa Pengerja'))
const filteredAgcLogs = computed(() => getFilteredLogs('AGC/Fellowship'))

const paginatedUsers = computed(() => filteredUsers.value.slice((currentPage.value - 1) * itemsPerPage, currentPage.value * itemsPerPage))
const paginatedAgLogs = computed(() => filteredAgLogs.value.slice((currentPage.value - 1) * itemsPerPage, currentPage.value * itemsPerPage))
const paginatedAgLiteLogs = computed(() => filteredAgLiteLogs.value.slice((currentPage.value - 1) * itemsPerPage, currentPage.value * itemsPerPage))
const paginatedDoaFajarLogs = computed(() => filteredDoaFajarLogs.value.slice((currentPage.value - 1) * itemsPerPage, currentPage.value * itemsPerPage))
const paginatedDoaPengerjaLogs = computed(() => filteredDoaPengerjaLogs.value.slice((currentPage.value - 1) * itemsPerPage, currentPage.value * itemsPerPage))
const paginatedAgcLogs = computed(() => filteredAgcLogs.value.slice((currentPage.value - 1) * itemsPerPage, currentPage.value * itemsPerPage))

const currentPaginatedLogs = computed(() => {
  if (activeTab.value === 'AG') return paginatedAgLogs.value;
  if (activeTab.value === 'AG Lite') return paginatedAgLiteLogs.value;
  if (activeTab.value === 'Doa Fajar') return paginatedDoaFajarLogs.value;
  if (activeTab.value === 'Doa Pengerja') return paginatedDoaPengerjaLogs.value;
  if (activeTab.value === 'AGC/Fellowship') return paginatedAgcLogs.value;
  return [];
})

const currentTotalPages = computed(() => {
  if (activeTab.value === 'Leaderboard') return Math.ceil(filteredUsers.value.length / itemsPerPage)
  if (activeTab.value === 'AG') return Math.ceil(filteredAgLogs.value.length / itemsPerPage)
  if (activeTab.value === 'AG Lite') return Math.ceil(filteredAgLiteLogs.value.length / itemsPerPage)
  if (activeTab.value === 'Doa Fajar') return Math.ceil(filteredDoaFajarLogs.value.length / itemsPerPage)
  if (activeTab.value === 'Doa Pengerja') return Math.ceil(filteredDoaPengerjaLogs.value.length / itemsPerPage)
  if (activeTab.value === 'AGC/Fellowship') return Math.ceil(filteredAgcLogs.value.length / itemsPerPage)
  return 1;
})

const nextPage = () => { if (currentPage.value < currentTotalPages.value) currentPage.value++ }
const prevPage = () => { if (currentPage.value > 1) currentPage.value-- }

</script>

<style scoped>
.animate-fade-in-up { animation: fadeInUp 0.5s ease-out forwards; }
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(20px) scale(0.95); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}

.animate-bounce { animation: bounce 2s infinite; }
@keyframes bounce {
  0%, 100% { transform: translateY(-20%); animation-timing-function: cubic-bezier(0.8, 0, 1, 1); }
  50% { transform: translateY(0); animation-timing-function: cubic-bezier(0, 0, 0.2, 1); }
}

.fade-enter-active, .fade-leave-active { transition: opacity 0.3s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
.fade-enter-active .bg-\[\#111\] { animation: scaleIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; }

@keyframes scaleIn {
  0% { transform: scale(0.9); opacity: 0; }
  100% { transform: scale(1); opacity: 1; }
}

.bounce-enter-active { animation: bounceInUp 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.bounce-leave-active { animation: fadeOutDown 0.3s ease-in forwards; }

@keyframes bounceInUp {
  0% { transform: translate(-50%, 100%); opacity: 0; }
  100% { transform: translate(-50%, 0); opacity: 1; }
}
@keyframes fadeOutDown {
  0% { transform: translate(-50%, 0); opacity: 1; }
  100% { transform: translate(-50%, 100%); opacity: 0; }
}

.custom-date-input::-webkit-calendar-picker-indicator {
  filter: invert(1);
  opacity: 0.6;
  cursor: pointer;
}
.custom-date-input::-webkit-calendar-picker-indicator:hover {
  opacity: 1;
}

/* CSS KHUSUS UNTUK MENYEMBUNYIKAN SCROLLBAR DI MENU TABS */
.hide-scrollbar::-webkit-scrollbar {
  display: none;
}
.hide-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>