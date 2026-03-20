<template>
  <div class="min-h-screen bg-[#0A0A0A] flex items-center justify-center p-4 relative overflow-x-hidden py-10 font-sans">
    <div class="fixed top-[-10%] left-[-10%] w-[500px] h-[500px] bg-ag-purple rounded-full mix-blend-screen filter blur-[150px] opacity-20 animate-pulse pointer-events-none"></div>
    <div class="fixed bottom-[-10%] right-[-10%] w-[400px] h-[400px] bg-ag-yellow rounded-full mix-blend-screen filter blur-[150px] opacity-10 pointer-events-none"></div>

    <div class="relative w-full max-w-lg p-8 sm:p-10 bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl shadow-2xl z-10 transition-all duration-500">
      
      <div v-if="!isRegistered">
        <div class="text-center mb-8">
          <h1 class="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-ag-yellow to-ag-purple mb-2 tracking-tight">Pendaftaran Baru</h1>
          <p class="text-gray-400 text-sm">Lengkapi data untuk mendapatkan Kartu Jemaat</p>
        </div>

        <div class="flex p-1 mb-8 bg-black/40 rounded-xl border border-white/10">
          <button @click="tab = 'jemaat'" :class="tab === 'jemaat' ? 'bg-gradient-to-r from-ag-purple to-[#5b1d66] text-white shadow-[0_0_15px_rgba(124,40,137,0.4)]' : 'text-gray-400 hover:text-white'" class="flex-1 py-2.5 rounded-lg text-sm font-bold transition-all duration-300 flex items-center justify-center gap-2">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
            Jemaat Umum
          </button>
          
          <button @click="tab = 'pelayan'" :class="tab === 'pelayan' ? 'bg-gradient-to-r from-ag-yellow to-[#e5c910] text-gray-900 shadow-[0_0_15px_rgba(253,224,33,0.4)]' : 'text-gray-400 hover:text-white'" class="flex-1 py-2.5 rounded-lg text-sm font-bold transition-all duration-300 flex items-center justify-center gap-2">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 18.657A8 8 0 016.343 7.343S7 9 9 10c0-2 .5-5 2.986-7C14 5 16.09 5.777 17.656 7.343A7.975 7.975 0 0120 13a7.975 7.975 0 01-2.343 5.657z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.879 16.121A3 3 0 1012.015 11L11 14H9c0 .768.293 1.536.879 2.121z"></path></svg>
            Pelayan Tuhan
          </button>
        </div>

        <div v-if="errorMessage" class="mb-6 p-4 bg-red-500/10 border border-red-500/50 text-red-400 rounded-xl text-sm text-center backdrop-blur-sm flex items-center justify-center gap-2">
          <svg class="w-5 h-5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          <span>{{ errorMessage }}</span>
        </div>

        <form @submit.prevent="handleRegister" class="space-y-5">
          <div>
            <label class="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">Nama Lengkap</label>
            <input v-model="form.fullname" type="text" required class="w-full px-4 py-3 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-ag-purple/50 text-white placeholder-gray-600 outline-none transition-all" placeholder="Misal: Samuel Christian">
          </div>

          <div>
            <label class="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">Buat Username (Untuk Kode Referal)</label>
            <input v-model="form.username" type="text" required class="w-full px-4 py-3 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-ag-purple/50 text-white placeholder-gray-600 outline-none transition-all" placeholder="Misal: samuel28 (Tanpa spasi)">
          </div>

          <div>
            <label class="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">Tanggal Lahir</label>
            <input v-model="form.date_of_birth" type="date" required class="w-full px-4 py-3 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-ag-purple/50 text-white outline-none transition-all appearance-none" style="color-scheme: dark;">
          </div>

          <template v-if="tab === 'jemaat'">
            <div>
              <label class="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">Status / Pekerjaan</label>
              <select v-model="form.pekerjaan" class="w-full px-4 py-3 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-ag-purple/50 text-white outline-none transition-all appearance-none">
                <option value="Siswa" class="bg-gray-900">Siswa</option>
                <option value="Mahasiswa" class="bg-gray-900">Mahasiswa</option>
                <option value="Pekerja" class="bg-gray-900">Pekerja / Karyawan</option>
                <option value="Lainnya" class="bg-gray-900">Lainnya</option>
              </select>
            </div>
            <div>
              <label class="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">Nomor WhatsApp</label>
              <input v-model="form.whatsapp" type="text" class="w-full px-4 py-3 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-ag-purple/50 text-white placeholder-gray-600 outline-none transition-all" placeholder="0812...">
            </div>
          </template>

          <template v-if="tab === 'pelayan'">
            <div>
              <label class="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">Bidang Pelayanan</label>
              <select v-model="form.pelayanan" class="w-full px-4 py-3 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-ag-yellow/50 text-white outline-none transition-all appearance-none">
                <option value="Praise and Worship" class="bg-gray-900">Praise and Worship</option>
                <option value="Musik Pujian" class="bg-gray-900">Musik Pujian</option>
                <option value="Usher / Greeter" class="bg-gray-900">Usher / Greeter</option>
                <option value="Multimedia & Dokumentasi" class="bg-gray-900">Multimedia & Dokumentasi</option>
              </select>
            </div>
            <div>
              <label class="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">Nomor WhatsApp</label>
              <input v-model="form.whatsapp" type="text" required class="w-full px-4 py-3 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-ag-yellow/50 text-white placeholder-gray-600 outline-none transition-all" placeholder="08123456789">
            </div>

            <div v-if="form.pelayanan === 'Usher / Greeter'" class="mt-4 p-5 bg-gradient-to-br from-ag-yellow/10 to-transparent border border-ag-yellow/30 rounded-2xl space-y-4 shadow-inner">
              <p class="text-[11px] font-black text-ag-yellow uppercase tracking-widest flex items-center gap-2 mb-2">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 11c0 3.517-1.009 6.799-2.753 9.571m-3.44-2.04l.054-.09A13.916 13.916 0 008 11a4 4 0 118 0c0 1.017-.07 2.019-.203 3m-2.118 6.844A21.88 21.88 0 0015.171 17m3.839 1.132c.645-2.266.99-4.659.99-7.132A8 8 0 008 4.07M3 15.364c.64-1.319 1-2.8 1-4.364 0-1.457.39-2.823 1.07-4"></path></svg>
                Akses Scanner Usher
              </p>
              <div class="grid grid-cols-2 gap-4">
                <div>
                  <label class="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">Password Login</label>
                  <input v-model="form.password" type="password" required class="w-full px-4 py-3 bg-black/60 border border-gray-600 rounded-xl focus:ring-2 focus:ring-ag-yellow/50 text-white outline-none transition-all" placeholder="••••••••">
                </div>
                <div>
                  <label class="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">Konfirmasi</label>
                  <input v-model="form.confirmPassword" type="password" required class="w-full px-4 py-3 bg-black/60 border border-gray-600 rounded-xl focus:ring-2 focus:ring-ag-yellow/50 text-white outline-none transition-all" placeholder="••••••••">
                </div>
              </div>
            </div>
          </template>

          <div class="mt-4 p-5 bg-black/40 border border-white/5 rounded-2xl relative overflow-hidden">
            <div class="absolute top-0 left-0 w-1 h-full" :class="referralStatus === 'valid' ? 'bg-emerald-500' : (referralStatus === 'invalid' ? 'bg-red-500' : 'bg-ag-purple')"></div>
            <label class="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5 pl-2">Kode Referal Teman (Opsional)</label>
            <div class="relative pl-2">
              <input 
                v-model="referralCode" 
                @input="debounceCheckReferral" 
                type="text" 
                class="w-full px-4 py-3 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-ag-purple/50 text-white placeholder-gray-600 outline-none transition-all" 
                placeholder="Ketik username teman yang mengajak..."
              >
              <div v-if="referralStatus === 'loading'" class="absolute right-4 top-3.5">
                <svg class="animate-spin h-5 w-5 text-ag-purple" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
              </div>
            </div>
            
            <div class="pl-2">
              <div v-if="referralStatus === 'valid'" class="mt-2 text-xs text-emerald-400 flex items-center gap-1.5 font-medium animate-fade-in-up">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                Kode Valid! Anda diajak oleh: <span class="font-bold text-white uppercase">{{ referrerName }}</span>
              </div>
              <div v-if="referralStatus === 'invalid'" class="mt-2 text-xs text-red-400 flex items-center gap-1.5 font-medium animate-fade-in-up">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                Username tidak ditemukan.
              </div>
              <p v-if="referralStatus === 'idle'" class="mt-2 text-[10px] text-gray-500 font-medium tracking-wide">
                Kosongkan jika Anda mendaftar sendiri.
              </p>
            </div>
          </div>

          <button type="submit" :disabled="isLoading" :class="tab === 'jemaat' ? 'from-ag-purple to-[#5b1d66] hover:shadow-[0_0_20px_rgba(124,40,137,0.4)] text-white' : 'from-ag-yellow to-[#e5c910] hover:shadow-[0_0_20px_rgba(253,224,33,0.4)] text-gray-900'" class="w-full mt-6 bg-gradient-to-r font-extrabold py-4 px-4 rounded-xl transition-all duration-300 transform hover:scale-[1.02] flex justify-center items-center disabled:opacity-50">
            <span v-if="isLoading">Memproses Data...</span>
            <span v-else>Daftar & Buat QR Code</span>
          </button>
        </form>

        <p class="mt-8 text-center text-sm text-gray-400">
          Kembali ke <button @click="$router.push('/')" class="text-ag-yellow font-bold hover:underline">Beranda</button>
        </p>
      </div>

      <div v-else class="text-center py-4 transform transition-all animate-fade-in-up">
        <div class="w-16 h-16 bg-emerald-500/20 rounded-full flex items-center justify-center mx-auto mb-4 text-emerald-400 shadow-[0_0_20px_rgba(16,185,129,0.2)]">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
        </div>
        <h2 class="text-3xl font-extrabold text-white mb-2">Pendaftaran Berhasil!</h2>
        <p class="text-gray-400 text-sm mb-6 px-4">
          Ini adalah Kartu Jemaat Anda. Silakan unduh dan simpan di galeri HP Anda.
        </p>

        <div class="flex flex-col items-center justify-center mb-6 relative">
          <div class="absolute inset-0 bg-gradient-to-r from-ag-purple/30 to-ag-yellow/30 blur-2xl rounded-full"></div>
          
          <div ref="qrContainer" class="relative p-5 bg-white rounded-2xl shadow-[0_0_50px_rgba(253,224,33,0.3)] border-4 border-white">
            <qrcode-vue :value="registeredData.qr_code_data" :size="220" level="H" />
          </div>
          
          <div class="mt-5 bg-black/60 border border-white/10 px-6 py-3 rounded-2xl backdrop-blur-md shadow-lg flex flex-col items-center">
            <p class="text-white font-bold text-lg mb-1">{{ registeredData.fullname }}</p>
            <div class="flex items-center gap-2 bg-white/10 px-3 py-1.5 rounded-lg border border-white/5">
              <span class="text-xs text-gray-400 font-medium uppercase tracking-wider">Kode Referal:</span>
              <span class="text-ag-yellow font-black tracking-widest">@{{ registeredData.username }}</span>
            </div>
            <p class="text-[10px] text-gray-500 mt-2 font-medium">Bagikan kode ini untuk mendapat poin!</p>
          </div>
        </div>

        <div class="flex flex-col gap-3">
          <button @click="downloadQRCode" class="w-full bg-gradient-to-r from-ag-yellow to-[#e5c910] text-gray-900 hover:shadow-[0_0_20px_rgba(253,224,33,0.4)] font-extrabold py-3.5 px-4 rounded-xl transition-all duration-300 flex items-center justify-center gap-2">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
            Unduh Kartu (Simpan ke Galeri)
          </button>

          <button @click="$router.push('/')" class="w-full bg-white/5 hover:bg-white/10 border border-white/20 text-gray-300 font-bold py-3.5 px-4 rounded-xl transition-all duration-300">
            Selesai & Tutup
          </button>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import QrcodeVue from 'qrcode.vue'

const router = useRouter()
const tab = ref('jemaat')
const isLoading = ref(false)
const errorMessage = ref('')
const isRegistered = ref(false)
const registeredData = ref(null)

const qrContainer = ref(null)

const referralCode = ref('')
const referralStatus = ref('idle') 
const referrerName = ref('')
let debounceTimer = null

const debounceCheckReferral = () => {
  clearTimeout(debounceTimer)
  
  if (!referralCode.value.trim()) {
    referralStatus.value = 'idle'
    referrerName.value = ''
    return
  }

  referralStatus.value = 'loading'
  
  debounceTimer = setTimeout(async () => {
    try {
      const cleanCode = referralCode.value.trim().toLowerCase().replace('@', '')
      const res = await axios.get(`https://semskii1-ag-connect-api.hf.space/users/check-referral/${cleanCode}`)
      referralStatus.value = 'valid'
      referrerName.value = res.data.fullname
    } catch (error) {
      referralStatus.value = 'invalid'
      referrerName.value = ''
    }
  }, 800)
}

const form = ref({
  fullname: '',
  username: '',
  whatsapp: '',
  date_of_birth: '',
  pekerjaan: 'Siswa',
  pelayanan: 'Praise and Worship',
  password: '', 
  confirmPassword: '' 
})

const handleRegister = async () => {
  isLoading.value = true
  errorMessage.value = ''

  const isUsher = tab.value === 'pelayan' && form.value.pelayanan === 'Usher / Greeter'

  if (isUsher) {
    if (form.value.password !== form.value.confirmPassword) {
      errorMessage.value = 'Password dan Konfirmasi Password tidak cocok!'
      isLoading.value = false
      return
    }
  }

  const finalUsername = form.value.username.toLowerCase().replace(/\s+/g, '')
  const finalPassword = isUsher ? form.value.password : 'default_ag_password_123!'
  const cleanReferral = referralStatus.value === 'valid' ? referralCode.value.trim().toLowerCase().replace('@', '') : null

  const payload = {
    fullname: form.value.fullname,
    username: finalUsername,
    password: finalPassword,
    whatsapp: form.value.whatsapp,
    date_of_birth: form.value.date_of_birth,
    status: tab.value === 'jemaat' ? form.value.pekerjaan : 'Pelayan Tuhan',
    talents: tab.value === 'pelayan' ? form.value.pelayanan : 'Jemaat Umum',
    referred_by: cleanReferral 
  }

  try {
    const response = await axios.post('https://semskii1-ag-connect-api.hf.space/register', payload)
    registeredData.value = response.data
    isRegistered.value = true
  } catch (error) {
    if (error.response && error.response.status === 400) {
      errorMessage.value = 'Username tersebut sudah dipakai, silakan gunakan yang lain.'
    } else {
      errorMessage.value = 'Terjadi kesalahan pada server saat mendaftar.'
    }
  } finally {
    isLoading.value = false
  }
}

// --- [DIPERBARUI] FUNGSI DOWNLOAD KARTU DIGITAL UTUH ---
const downloadQRCode = () => {
  if (!qrContainer.value) return

  const qrCanvas = qrContainer.value.querySelector('canvas')
  
  if (!qrCanvas) {
    alert("Gagal memuat gambar QR. Silakan screenshot layar ini.")
    return
  }

  // 1. Buat Kanvas Virtual untuk Menggambar Tiket Utuh
  const canvas = document.createElement('canvas')
  const ctx = canvas.getContext('2d')

  // Ukuran Kartu Jemaat
  canvas.width = 400
  canvas.height = 550

  // 2. Gambar Background Gelap Mewah
  ctx.fillStyle = '#0A0A0A'
  ctx.fillRect(0, 0, canvas.width, canvas.height)

  // 3. Gambar Garis Akses Atas (AG Colors)
  const gradient = ctx.createLinearGradient(0, 0, canvas.width, 0)
  gradient.addColorStop(0, '#7c2889') // AG Purple
  gradient.addColorStop(1, '#fde021') // AG Yellow
  ctx.fillStyle = gradient
  ctx.fillRect(0, 0, canvas.width, 10)

  // 4. GAMBAR ZONA PUTIH (QUIET ZONE) UNTUK QR CODE
  // Inilah rahasia yang membuat scan HP menjadi sangat cepat!
  const whiteBoxSize = 280 
  const boxX = (canvas.width - whiteBoxSize) / 2
  const boxY = 70
  
  ctx.fillStyle = '#FFFFFF'
  // Membuat kotak putih dengan sudut melengkung tipis
  ctx.beginPath()
  ctx.roundRect ? ctx.roundRect(boxX, boxY, whiteBoxSize, whiteBoxSize, 16) : ctx.fillRect(boxX, boxY, whiteBoxSize, whiteBoxSize)
  ctx.fill()

  // 5. Tempelkan QR Code Asli ke tengah kotak putih
  const qrImageSize = 240
  const qrOffset = (whiteBoxSize - qrImageSize) / 2
  ctx.drawImage(qrCanvas, boxX + qrOffset, boxY + qrOffset, qrImageSize, qrImageSize)

  // 6. Tulis Nama Jemaat
  ctx.textAlign = 'center'
  ctx.fillStyle = '#FFFFFF'
  ctx.font = 'bold 28px sans-serif'
  ctx.fillText(registeredData.value.fullname, canvas.width / 2, boxY + whiteBoxSize + 60)

  // 7. Label Kode Referal
  ctx.fillStyle = '#9CA3AF'
  ctx.font = 'bold 12px sans-serif'
  ctx.fillText('KODE REFERAL:', canvas.width / 2, boxY + whiteBoxSize + 95)

  // 8. Tulis Nilai Kode Referal
  ctx.fillStyle = '#fde021'
  ctx.font = 'bold 22px monospace'
  ctx.fillText('@' + registeredData.value.username, canvas.width / 2, boxY + whiteBoxSize + 125)

  // 9. Footer Watermark
  ctx.fillStyle = '#4B5563'
  ctx.font = '10px sans-serif'
  ctx.fillText('AG Connect - Arrow Generation', canvas.width / 2, canvas.height - 20)

  // 10. Proses Unduh Gambar
  const imageUrl = canvas.toDataURL('image/png')
  const downloadLink = document.createElement('a')
  downloadLink.href = imageUrl
  
  const safeFilename = registeredData.value.fullname.replace(/\s+/g, '_')
  downloadLink.download = `Kartu_AG_${safeFilename}.png`
  
  document.body.appendChild(downloadLink)
  downloadLink.click()
  document.body.removeChild(downloadLink)
}
</script>

<style scoped>
.animate-fade-in-up { animation: fadeInUp 0.6s ease-out forwards; }
@keyframes fadeInUp {
  0% { opacity: 0; transform: translateY(20px) scale(0.95); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}
input[type="date"]::-webkit-calendar-picker-indicator { filter: invert(1); cursor: pointer; }
</style>