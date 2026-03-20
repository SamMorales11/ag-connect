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
          <p class="text-gray-400 text-sm font-medium">Pantau statistik kehadiran dan kelola poin apresiasi jemaat.</p>
        </div>
        
        <button @click="$router.push('/profile')" class="group shrink-0 flex items-center gap-2 px-5 py-2.5 bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl transition-all duration-300 backdrop-blur-sm">
          <svg class="w-4 h-4 text-gray-400 group-hover:text-white transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
          <span class="text-sm font-semibold text-gray-300 group-hover:text-white">Kembali ke Portal</span>
        </button>
      </div>

      <div v-if="isInitialLoading" class="flex flex-col items-center justify-center py-20">
        <svg class="animate-spin h-10 w-10 text-ag-yellow mb-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
        <p class="text-gray-400">Menyiapkan Analytics Workspace...</p>
      </div>

      <div v-else>
        
        <div class="flex flex-col gap-5 border-b border-white/10 pb-6 mb-8">
          <div class="w-full overflow-x-auto pb-2 -mb-2 hide-scrollbar relative">
            <div class="flex items-center gap-2 w-max pr-4">
              <button @click="activeTab = 'Ringkasan'" :class="activeTab === 'Ringkasan' ? 'bg-indigo-600 text-white shadow-lg' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent whitespace-nowrap">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
                Ringkasan Analitik
              </button>

              <button @click="activeTab = 'Leaderboard'" :class="activeTab === 'Leaderboard' ? 'bg-blue-600 text-white shadow-lg' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent whitespace-nowrap">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path></svg>
                Klasemen Poin
              </button>
              
              <button @click="activeTab = 'AG'" :class="activeTab === 'AG' ? 'bg-ag-purple text-white shadow-lg' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent whitespace-nowrap">
                AG
              </button>
              <button @click="activeTab = 'AG Lite'" :class="activeTab === 'AG Lite' ? 'bg-ag-yellow text-gray-900 shadow-lg' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent whitespace-nowrap">
                AG Lite
              </button>
              <button @click="activeTab = 'Doa Fajar'" :class="activeTab === 'Doa Fajar' ? 'bg-blue-500 text-white shadow-lg' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent whitespace-nowrap">
                Doa Fajar
              </button>
              <button @click="activeTab = 'Doa Pengerja'" :class="activeTab === 'Doa Pengerja' ? 'bg-orange-500 text-white shadow-lg' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent whitespace-nowrap">
                Doa Pengerja
              </button>
              <button @click="activeTab = 'AGC/Fellowship'" :class="activeTab === 'AGC/Fellowship' ? 'bg-pink-500 text-white shadow-lg' : 'bg-white/5 text-gray-400 hover:text-white hover:bg-white/10'" class="flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm transition-all border border-transparent whitespace-nowrap">
                AGC / Fellowship
              </button>
            </div>
          </div>

          <div v-if="activeTab !== 'Ringkasan'" class="flex flex-col sm:flex-row items-center justify-end gap-3 w-full shrink-0">
            <div v-if="activeTab !== 'Leaderboard'" class="relative w-full sm:w-40">
              <input v-model="selectedDate" type="date" class="w-full bg-black/50 border border-gray-700 text-white text-sm rounded-xl px-4 py-2.5 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-all cursor-pointer custom-date-input">
              <button v-if="selectedDate" @click="selectedDate = ''" class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 hover:text-red-400">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
              </button>
            </div>

            <div class="relative w-full sm:w-56">
              <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <svg class="w-4 h-4 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
              </div>
              <input v-model="searchQuery" type="text" @keyup.enter="triggerSearch" placeholder="Cari (Tekan Enter)..." class="w-full bg-black/50 border border-gray-700 text-white text-sm rounded-xl pl-10 pr-4 py-2.5 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-all placeholder-gray-500">
            </div>

            <button v-if="activeTab === 'Leaderboard'" @click="showResetModal = true" class="w-full sm:w-auto px-5 py-2.5 rounded-xl font-bold text-sm transition-all border border-red-500/30 bg-red-500/10 text-red-500 hover:bg-red-500 hover:text-white flex items-center justify-center gap-2">
              <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
              <span class="whitespace-nowrap">Reset Data</span>
            </button>
          </div>
        </div>

        <div v-if="activeTab === 'Ringkasan'" class="animate-fade-in-up space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="bg-white/5 border border-white/10 rounded-2xl p-6 backdrop-blur-md">
              <p class="text-gray-400 text-sm font-semibold uppercase tracking-widest mb-1">Total Jemaat Terdaftar</p>
              <h3 class="text-4xl font-black text-white">{{ allUsers.length }}</h3>
            </div>
            <div class="bg-blue-500/10 border border-blue-500/20 rounded-2xl p-6 backdrop-blur-md">
              <p class="text-blue-400 text-sm font-semibold uppercase tracking-widest mb-1">Total Poin Beredar</p>
              <h3 class="text-4xl font-black text-blue-300">{{ totalPointsInSystem }} <span class="text-lg font-medium text-blue-500/50">pts</span></h3>
            </div>
          </div>

          <div class="bg-[#111] border border-white/10 rounded-2xl p-6 shadow-2xl relative">
            <h3 class="text-lg font-bold text-white mb-6 flex items-center gap-2">
              <svg class="w-5 h-5 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z"></path></svg>
              Grafik Kehadiran Jemaat (30 Hari Terakhir)
            </h3>
            
            <div class="h-[300px] w-full">
              <apexchart type="area" height="100%" :options="chartOptions" :series="chartSeries"></apexchart>
            </div>
          </div>
        </div>

        <div v-if="activeTab === 'Leaderboard'" class="animate-fade-in-up">
          <div class="space-y-3">
            
            <div v-if="paginatedUsers.length === 0" class="py-16 text-center text-gray-500 text-sm font-medium bg-white/5 rounded-2xl border border-white/5 backdrop-blur-md">
              Data jemaat tidak ditemukan.
            </div>

            <div v-else v-for="(user, index) in paginatedUsers" :key="user.id"
                 class="relative group flex flex-col p-5 rounded-2xl transition-all duration-300 overflow-hidden backdrop-blur-md border hover:border-white/20"
                 :class="{
                   'bg-blue-900/10 border-blue-500/20': (currentPage - 1) * itemsPerPage + index === 0 && user.points > 0,
                   'bg-white/[0.02] border-white/5 hover:bg-white/[0.04]': !((currentPage - 1) * itemsPerPage + index === 0 && user.points > 0)
                 }">

              <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between w-full relative z-10 gap-4">
                
                <div class="flex items-center gap-4 w-full sm:w-auto">
                  <div class="flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm transition-colors"
                       :class="{
                         'bg-blue-600 text-white shadow-lg shadow-blue-500/20': (currentPage - 1) * itemsPerPage + index === 0 && user.points > 0,
                         'bg-white/10 text-white': (currentPage - 1) * itemsPerPage + index === 1 && user.points > 0,
                         'bg-white/5 text-gray-300': (currentPage - 1) * itemsPerPage + index === 2 && user.points > 0,
                         'bg-transparent border border-white/10 text-gray-500': (currentPage - 1) * itemsPerPage + index > 2 || user.points === 0
                       }">
                    {{ (currentPage - 1) * itemsPerPage + index + 1 }}
                  </div>

                  <div class="hidden md:flex w-10 h-10 rounded-full bg-black/50 border border-white/10 items-center justify-center font-bold text-sm text-gray-300">
                    {{ user.fullname.charAt(0).toUpperCase() }}
                  </div>

                  <div>
                    <h3 class="text-base font-bold text-gray-100 group-hover:text-white transition-colors flex items-center gap-2">
                      {{ user.fullname }}
                      <span v-if="(currentPage - 1) * itemsPerPage + index === 0 && user.points > 0" class="text-[9px] font-bold px-2 py-0.5 bg-blue-500/20 text-blue-400 rounded border border-blue-500/30 uppercase tracking-widest">
                        Teratas
                      </span>
                    </h3>
                    <p class="text-xs text-gray-500 mt-0.5 font-mono">@{{ user.username }}</p>
                  </div>
                </div>

                <div class="flex items-center justify-between w-full sm:w-auto gap-4 md:gap-4">
                  <div class="flex flex-col items-start sm:items-end">
                    <span class="text-[10px] font-semibold text-gray-500 uppercase tracking-wider mb-1">Total Poin</span>
                    <div class="flex items-center gap-2 px-3 py-1 rounded-lg bg-black/40 border border-white/5">
                      <span class="font-bold text-base text-gray-200">{{ user.points }}</span>
                    </div>
                  </div>

                  <div class="flex gap-2">
                    <button @click="openConfirmModal(user)" class="shrink-0 flex items-center justify-center gap-2 px-3 py-2 bg-white/5 hover:bg-blue-500/20 border border-white/10 hover:border-blue-500/50 text-gray-300 hover:text-blue-400 text-xs font-semibold rounded-lg transition-all outline-none" title="Tambah Poin">
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path></svg>
                    </button>
                    
                    <button @click="openRedeemModal(user)" class="shrink-0 flex items-center justify-center gap-2 px-3 py-2 bg-white/5 hover:bg-orange-500/20 border border-white/10 hover:border-orange-500/50 text-gray-300 hover:text-orange-400 text-xs font-semibold rounded-lg transition-all outline-none" title="Tukar Poin (Redeem)">
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    </button>
                  </div>
                </div>
              </div>

              <div class="w-full mt-4 bg-white/5 rounded-full h-1 overflow-hidden">
                <div class="h-full rounded-full transition-all duration-1000 ease-out"
                     :class="user.points > 0 ? 'bg-blue-500' : 'bg-transparent'"
                     :style="{ width: `${(user.points / maxLeaderboardPoints) * 100}%` }">
                </div>
              </div>

            </div>
          </div>
        </div>
        
        <div v-if="!['Leaderboard', 'Ringkasan'].includes(activeTab)" class="animate-fade-in-up">
          <div class="bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl shadow-lg overflow-hidden relative">
            
            <div v-if="isLoadingLogs" class="absolute inset-0 bg-[#0A0A0A]/50 backdrop-blur-sm z-20 flex items-center justify-center">
               <svg class="animate-spin h-8 w-8 text-blue-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
            </div>

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
                  <tr v-if="currentLogs.length === 0 && !isLoadingLogs">
                    <td colspan="3" class="py-12 text-center text-gray-500 text-sm">
                      Data absensi belum tersedia.
                    </td>
                  </tr>
                  <tr v-else v-for="log in currentLogs" :key="log.id" class="hover:bg-white/[0.02] transition-colors">
                    <td class="py-4 px-6"><span class="text-xs font-mono text-gray-400">{{ new Date(log.scan_time).toLocaleString('id-ID') }}</span></td>
                    <td class="py-4 px-6 font-bold text-gray-200">{{ log.user?.fullname || 'User Dihapus' }}</td>
                    <td class="py-4 px-6 text-xs text-gray-400">{{ log.user?.status || '-' }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <div v-if="currentTotalPages > 1 && activeTab !== 'Ringkasan'" class="flex flex-col sm:flex-row justify-between items-center mt-6 px-2 gap-4 animate-fade-in-up">
          <span class="text-sm font-medium text-gray-500">
            Halaman <span class="text-white">{{ currentPage }}</span> dari <span class="text-white">{{ currentTotalPages }}</span>
          </span>
          <div class="flex gap-2">
            <button @click="prevPage" :disabled="currentPage === 1 || isLoadingLogs" class="px-4 py-2 bg-white/5 hover:bg-white/10 border border-white/10 rounded-lg text-sm font-bold transition-all disabled:opacity-30 disabled:cursor-not-allowed">
              Sebelumnya
            </button>
            <button @click="nextPage" :disabled="currentPage === currentTotalPages || isLoadingLogs" class="px-4 py-2 bg-white/5 hover:bg-white/10 border border-white/10 rounded-lg text-sm font-bold transition-all disabled:opacity-30 disabled:cursor-not-allowed">
              Selanjutnya
            </button>
          </div>
        </div>

      </div>
    </div>

    <transition name="fade">
      <div v-if="showConfirmModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm px-4">
        <div class="bg-[#111] border border-white/10 p-6 md:p-8 rounded-2xl max-w-sm w-full text-center shadow-2xl transform transition-all">
          <h3 class="text-xl font-bold text-white mb-2">Tambah Data Poin</h3>
          <p class="text-gray-400 text-sm mb-8 leading-relaxed">Sistem akan menambahkan +10 poin untuk <br><span class="font-bold text-blue-400 text-base">{{ selectedUser?.fullname }}</span></p>
          <div class="flex gap-3">
            <button @click="showConfirmModal = false" :disabled="isProcessingApi" class="flex-1 py-2.5 rounded-lg font-bold text-gray-400 bg-white/5 hover:bg-white/10 hover:text-white border border-white/5 transition-colors disabled:opacity-50">Batal</button>
            <button @click="confirmGivePoints" :disabled="isProcessingApi" class="flex-1 py-2.5 rounded-lg font-bold text-white bg-blue-600 hover:bg-blue-500 transition-all flex justify-center items-center disabled:opacity-50">
              <span v-if="isProcessingApi" class="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></span>
              <span v-else>Konfirmasi</span>
            </button>
          </div>
        </div>
      </div>
    </transition>

    <transition name="fade">
      <div v-if="showRedeemModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm px-4">
        <div class="bg-[#111] border border-white/10 p-6 md:p-8 rounded-2xl max-w-sm w-full text-center shadow-2xl transform transition-all">
          <div class="w-16 h-16 rounded-full bg-orange-500/10 border border-orange-500/30 flex items-center justify-center mx-auto mb-4 text-orange-500">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          </div>
          <h3 class="text-xl font-bold text-white mb-2">Tukar Poin Jemaat</h3>
          <p class="text-gray-400 text-sm mb-4 leading-relaxed">
            Saldo <span class="font-bold text-white">{{ selectedUser?.fullname }}</span> saat ini: 
            <span class="font-bold text-orange-400">{{ selectedUser?.points }} Pts</span>
          </p>
          
          <div class="text-left mb-6">
            <label class="block text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Jumlah Poin yang Dipotong</label>
            <input v-model="redeemAmount" type="number" min="1" :max="selectedUser?.points" class="w-full bg-black/50 border border-gray-700 text-white rounded-lg px-4 py-3 focus:border-orange-500 focus:ring-1 focus:ring-orange-500 outline-none transition-all text-center font-bold text-xl" placeholder="Misal: 50">
          </div>

          <div class="flex gap-3">
            <button @click="showRedeemModal = false" :disabled="isProcessingApi" class="flex-1 py-2.5 rounded-lg font-bold text-gray-400 bg-white/5 hover:bg-white/10 hover:text-white border border-white/5 transition-colors disabled:opacity-50">Batal</button>
            <button @click="confirmRedeemPoints" :disabled="isProcessingApi || redeemAmount < 1 || redeemAmount > selectedUser?.points" class="flex-1 py-2.5 rounded-lg font-bold text-white bg-orange-600 hover:bg-orange-500 transition-all flex justify-center items-center disabled:opacity-50">
              <span v-if="isProcessingApi" class="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></span>
              <span v-else>Potong Poin</span>
            </button>
          </div>
        </div>
      </div>
    </transition>

    <transition name="bounce">
      <div v-if="showToast" class="fixed bottom-10 left-1/2 transform -translate-x-1/2 z-50 px-6 py-3 rounded-xl border backdrop-blur-xl flex items-center gap-3 shadow-2xl"
           :class="toastType === 'success' ? 'bg-emerald-500/10 border-emerald-500/30 text-emerald-400' : 'bg-red-500/10 border-red-500/30 text-red-400'">
        <svg v-if="toastType === 'success'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
        <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        <span class="font-bold text-sm tracking-wide">{{ toastMessage }}</span>
      </div>
    </transition>

  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import VueApexCharts from 'vue3-apexcharts' 

// Registrasi komponen ApexCharts agar bisa dipakai di template
const apexchart = VueApexCharts

const router = useRouter()
const isInitialLoading = ref(true)
const isLoadingLogs = ref(false)

const allUsers = ref([])
const currentLogs = ref([]) 
const totalLogs = ref(0)    

// Tab Default diubah menjadi Ringkasan
const activeTab = ref('Ringkasan') 
const searchQuery = ref('')
const selectedDate = ref('') 
const currentPage = ref(1)
const itemsPerPage = 20

// State untuk Modals
const showConfirmModal = ref(false)
const showRedeemModal = ref(false)
const showResetModal = ref(false)
const selectedUser = ref(null)
const redeemAmount = ref(0)
const isProcessingApi = ref(false)

const showToast = ref(false)
const toastMessage = ref('')
const toastType = ref('success')
let toastTimer = null

// --- KONFIGURASI GRAFIK APEXCHARTS ---
const chartOptions = ref({
  chart: {
    type: 'area',
    background: 'transparent',
    toolbar: { show: false },
    fontFamily: 'inherit'
  },
  theme: { mode: 'dark' },
  colors: ['#8b5cf6', '#eab308'],
  dataLabels: { enabled: false },
  stroke: { curve: 'smooth', width: 3 },
  xaxis: {
    categories: ['Minggu 1', 'Minggu 2', 'Minggu 3', 'Minggu 4', 'Minggu 5'], // Label Dummy untuk presentasi
    axisBorder: { show: false },
    axisTicks: { show: false }
  },
  yaxis: { show: false },
  grid: { borderColor: 'rgba(255,255,255,0.05)', strokeDashArray: 4 },
  fill: {
    type: 'gradient',
    gradient: { shadeIntensity: 1, opacityFrom: 0.4, opacityTo: 0.05, stops: [0, 100] }
  },
  legend: { position: 'top', horizontalAlign: 'right' }
})

// Data Dummy Grafik (Bisa diganti dinamis dari backend nantinya)
const chartSeries = ref([
  { name: 'Ibadah AG', data: [45, 52, 68, 84, 110] },
  { name: 'AG Lite', data: [20, 35, 41, 60, 85] }
])

onMounted(async () => {
  const token = localStorage.getItem('access_token')
  if (!token) {
    router.push('/login')
    return
  }
  
  try {
    const usersRes = await axios.get('https://semskii1-ag-connect-api.hf.space/users', { headers: { Authorization: `Bearer ${token}` } })
    allUsers.value = usersRes.data
  } catch (error) {
    console.error("Gagal memuat data", error)
  } finally {
    isInitialLoading.value = false
  }
})

watch([activeTab, selectedDate], () => {
  currentPage.value = 1
  if (!['Leaderboard', 'Ringkasan'].includes(activeTab.value)) {
    fetchLogsFromServer()
  }
})

watch(currentPage, () => {
  if (!['Leaderboard', 'Ringkasan'].includes(activeTab.value)) {
    fetchLogsFromServer()
  }
})

const triggerSearch = () => {
  currentPage.value = 1
  if (!['Leaderboard', 'Ringkasan'].includes(activeTab.value)) {
    fetchLogsFromServer()
  }
}

const fetchLogsFromServer = async () => {
  isLoadingLogs.value = true
  try {
    const token = localStorage.getItem('access_token')
    const params = new URLSearchParams({ page: currentPage.value, limit: itemsPerPage, service_type: activeTab.value })
    if (searchQuery.value) params.append('search', searchQuery.value)
    if (selectedDate.value) params.append('date_filter', selectedDate.value)

    const res = await axios.get(`https://semskii1-ag-connect-api.hf.space/attendance/logs?${params.toString()}`, {
      headers: { Authorization: `Bearer ${token}` }
    })
    
    currentLogs.value = res.data.data
    totalLogs.value = res.data.total
  } catch (error) {
    console.error("Gagal memuat log:", error)
  } finally {
    isLoadingLogs.value = false
  }
}

// Menampilkan Toast Notifikasi
const displayToast = (msg, type = 'success') => {
  clearTimeout(toastTimer)
  toastMessage.value = msg
  toastType.value = type
  showToast.value = true
  toastTimer = setTimeout(() => { showToast.value = false }, 3000)
}

// --- LOGIKA MODAL ---
const openConfirmModal = (user) => { selectedUser.value = user; showConfirmModal.value = true }
const openRedeemModal = (user) => { selectedUser.value = user; redeemAmount.value = 0; showRedeemModal.value = true }

// Fungsi Tambah Poin Asli
const confirmGivePoints = async () => {
  if (!selectedUser.value) return
  isProcessingApi.value = true

  try {
    const token = localStorage.getItem('access_token')
    const response = await axios.post(`https://semskii1-ag-connect-api.hf.space/users/${selectedUser.value.id}/add-quiz-points`, {}, {
      headers: { Authorization: `Bearer ${token}` }
    })
    selectedUser.value.points += 10
    displayToast(response.data.message)
  } catch (error) {
    displayToast(error.response?.data?.detail || "Gagal memperbarui data.", 'error')
  } finally {
    isProcessingApi.value = false; showConfirmModal.value = false; selectedUser.value = null
  }
}

// Fungsi TUKAR POIN (Baru)
const confirmRedeemPoints = async () => {
  if (!selectedUser.value || redeemAmount.value < 1) return
  isProcessingApi.value = true

  try {
    const token = localStorage.getItem('access_token')
    const response = await axios.post(`https://semskii1-ag-connect-api.hf.space/users/${selectedUser.value.id}/redeem-points`, 
      { points_to_deduct: redeemAmount.value }, 
      { headers: { Authorization: `Bearer ${token}` } }
    )
    
    // Kurangi poin secara visual di Frontend
    selectedUser.value.points -= redeemAmount.value
    displayToast(response.data.message)
    
  } catch (error) {
    displayToast(error.response?.data?.detail || "Gagal memotong poin.", 'error')
  } finally {
    isProcessingApi.value = false; showRedeemModal.value = false; selectedUser.value = null
  }
}

// Computed Properties
const totalPointsInSystem = computed(() => {
  return allUsers.value.reduce((total, user) => total + (user.points > 0 ? user.points : 0), 0)
})

const filteredUsers = computed(() => {
  let users = [...allUsers.value].sort((a, b) => b.points - a.points).filter(u => u.points >= 0)
  if (searchQuery.value && activeTab.value === 'Leaderboard') {
    const q = searchQuery.value.toLowerCase()
    users = users.filter(u => u.fullname.toLowerCase().includes(q) || u.username.toLowerCase().includes(q))
  }
  return users
})

const maxLeaderboardPoints = computed(() => {
  if (filteredUsers.value.length === 0) return 1;
  return Math.max(filteredUsers.value[0].points, 1);
})

const paginatedUsers = computed(() => filteredUsers.value.slice((currentPage.value - 1) * itemsPerPage, currentPage.value * itemsPerPage))

const currentTotalPages = computed(() => {
  if (activeTab.value === 'Leaderboard') return Math.ceil(filteredUsers.value.length / itemsPerPage) || 1
  return Math.ceil(totalLogs.value / itemsPerPage) || 1
})

const nextPage = () => { if (currentPage.value < currentTotalPages.value) currentPage.value++ }
const prevPage = () => { if (currentPage.value > 1) currentPage.value-- }
</script>

<style scoped>
.animate-fade-in-up { animation: fadeInUp 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(20px); }
  100% { opacity: 1; transform: translateY(0); }
}

.fade-enter-active, .fade-leave-active { transition: opacity 0.2s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
.fade-enter-active .bg-\[\#111\] { animation: scaleIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; }

@keyframes scaleIn {
  0% { transform: scale(0.95); opacity: 0; }
  100% { transform: scale(1); opacity: 1; }
}
.custom-date-input::-webkit-calendar-picker-indicator { filter: invert(1); cursor: pointer; }
.hide-scrollbar::-webkit-scrollbar { display: none; }
.hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
</style>