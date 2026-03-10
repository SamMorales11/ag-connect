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
          <button @click="tab = 'jemaat'" :class="tab === 'jemaat' ? 'bg-gradient-to-r from-ag-purple to-[#5b1d66] text-white shadow-lg' : 'text-gray-400 hover:text-white'" class="flex-1 py-2.5 rounded-lg text-sm font-bold transition-all duration-300">👤 Jemaat Umum</button>
          <button @click="tab = 'pelayan'" :class="tab === 'pelayan' ? 'bg-gradient-to-r from-ag-yellow to-[#e5c910] text-gray-900 shadow-lg' : 'text-gray-400 hover:text-white'" class="flex-1 py-2.5 rounded-lg text-sm font-bold transition-all duration-300">🎸 Pelayan Tuhan</button>
        </div>

        <div v-if="errorMessage" class="mb-6 p-4 bg-red-500/10 border border-red-500/50 text-red-400 rounded-xl text-sm text-center backdrop-blur-sm">
          ❌ {{ errorMessage }}
        </div>

        <form @submit.prevent="handleRegister" class="space-y-5">
          <div>
            <label class="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">Nama Lengkap</label>
            <input v-model="form.fullname" type="text" required class="w-full px-4 py-3 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-ag-purple/50 text-white placeholder-gray-600 outline-none transition-all" placeholder="Misal: Samuel Christian">
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
              <label class="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">Username Sosmed / WA</label>
              <input v-model="form.whatsapp" type="text" class="w-full px-4 py-3 bg-black/50 border border-gray-700 rounded-xl focus:ring-2 focus:ring-ag-purple/50 text-white placeholder-gray-600 outline-none transition-all" placeholder="@instagram atau 0812...">
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
              <div>
                <label class="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">Buat Username Login</label>
                <input v-model="form.username" type="text" required class="w-full px-4 py-3 bg-black/60 border border-gray-600 rounded-xl focus:ring-2 focus:ring-ag-yellow/50 text-white placeholder-gray-500 outline-none transition-all" placeholder="Misal: usher_samuel">
              </div>
              <div class="grid grid-cols-2 gap-4">
                <div>
                  <label class="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">Password</label>
                  <input v-model="form.password" type="password" required class="w-full px-4 py-3 bg-black/60 border border-gray-600 rounded-xl focus:ring-2 focus:ring-ag-yellow/50 text-white outline-none transition-all" placeholder="••••••••">
                </div>
                <div>
                  <label class="block text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1.5">Konfirmasi</label>
                  <input v-model="form.confirmPassword" type="password" required class="w-full px-4 py-3 bg-black/60 border border-gray-600 rounded-xl focus:ring-2 focus:ring-ag-yellow/50 text-white outline-none transition-all" placeholder="••••••••">
                </div>
              </div>
            </div>
          </template>

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
        <p class="text-gray-400 text-sm mb-8 px-4">
          Ini adalah Kartu Jemaat Anda. Silakan unduh dan simpan di galeri HP Anda.
        </p>

        <div class="flex flex-col items-center justify-center mb-8 relative">
          <div class="absolute inset-0 bg-gradient-to-r from-ag-purple/30 to-ag-yellow/30 blur-2xl rounded-full"></div>
          
          <div ref="qrContainer" class="relative p-5 bg-white rounded-2xl shadow-[0_0_50px_rgba(253,224,33,0.3)] border-4 border-white">
            <qrcode-vue :value="registeredData.qr_code_data" :size="220" level="H" />
          </div>
          
          <div class="mt-5 bg-black/40 border border-white/10 px-4 py-2 rounded-xl backdrop-blur-md">
            <p class="text-xs text-gray-400 font-mono tracking-wider break-all text-center max-w-[250px]">
              <span class="text-ag-yellow font-bold text-sm">{{ registeredData.fullname }}</span>
            </p>
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

// Referensi DOM untuk membungkus QR Code agar bisa di-download
const qrContainer = ref(null)

const form = ref({
  fullname: '',
  whatsapp: '',
  date_of_birth: '',
  pekerjaan: 'Siswa',
  pelayanan: 'Praise and Worship',
  username: '', 
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

  const safeName = form.value.fullname.toLowerCase().replace(/[^a-z0-9]/g, '')
  const randomNum = Math.floor(100 + Math.random() * 900)
  
  const finalUsername = isUsher ? form.value.username : `${safeName}${randomNum}`
  const finalPassword = isUsher ? form.value.password : 'default_ag_password_123!'

  const payload = {
    fullname: form.value.fullname,
    username: finalUsername,
    password: finalPassword,
    whatsapp: form.value.whatsapp,
    date_of_birth: form.value.date_of_birth,
    status: tab.value === 'jemaat' ? form.value.pekerjaan : 'Pelayan Tuhan',
    talents: tab.value === 'pelayan' ? form.value.pelayanan : 'Jemaat Umum'
  }

  try {
    const response = await axios.post('http://127.0.0.1:8000/register', payload)
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

// FUNGSI BARU: MENGUNDUH QR CODE SEBAGAI GAMBAR
const downloadQRCode = () => {
  if (!qrContainer.value) return

  // Cari elemen <canvas> yang dihasilkan oleh komponen <qrcode-vue>
  const canvas = qrContainer.value.querySelector('canvas')
  
  if (canvas) {
    // Ubah kanvas menjadi data URL gambar berformat PNG
    const imageUrl = canvas.toDataURL('image/png')
    
    // Buat tag <a> sementara di balik layar
    const downloadLink = document.createElement('a')
    downloadLink.href = imageUrl
    
    // Bersihkan spasi dari nama user untuk dijadikan nama file (misal: Kartu_Samuel_Christian.png)
    const safeFilename = registeredData.value.fullname.replace(/\s+/g, '_')
    downloadLink.download = `Kartu_AG_${safeFilename}.png`
    
    // Simulasikan klik untuk memicu unduhan, lalu hapus tag <a> tersebut
    document.body.appendChild(downloadLink)
    downloadLink.click()
    document.body.removeChild(downloadLink)
  } else {
    alert("Gagal memuat gambar QR. Silakan screenshot layar ini.")
  }
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