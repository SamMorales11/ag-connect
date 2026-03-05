<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="p-8 bg-white rounded-xl shadow-lg w-full max-w-sm">
      
      <div class="text-center mb-6">
        <h1 class="text-3xl font-extrabold text-ag-purple mb-1">AG Connect</h1>
        <p class="text-gray-500">Sistem Manajemen Jemaat</p>
      </div>

      <div v-if="errorMessage" class="mb-4 p-3 bg-red-100 text-red-600 rounded-lg text-sm text-center">
        {{ errorMessage }}
      </div>

      <form @submit.prevent="handleLogin">
        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700 mb-1">Username</label>
          <input 
            v-model="username" 
            type="text" 
            required 
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-ag-yellow focus:border-ag-purple outline-none transition-colors" 
            placeholder="Masukkan username"
          >
        </div>

        <div class="mb-6">
          <label class="block text-sm font-medium text-gray-700 mb-1">Password</label>
          <input 
            v-model="password" 
            type="password" 
            required 
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-ag-yellow focus:border-ag-purple outline-none transition-colors" 
            placeholder="••••••••"
          >
        </div>

        <button 
          type="submit" 
          :disabled="isLoading" 
          class="w-full bg-ag-yellow hover:bg-yellow-400 text-ag-purple font-bold py-2 px-4 rounded-lg transition-colors flex justify-center items-center"
        >
          <span v-if="isLoading">Memeriksa...</span>
          <span v-else>Masuk</span>
        </button>
      </form>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const username = ref('')
const password = ref('')
const errorMessage = ref('')
const isLoading = ref(false)

const handleLogin = async () => {
  isLoading.value = true
  errorMessage.value = ''

  try {
    // FastAPI meminta format data berupa x-www-form-urlencoded
    const formData = new URLSearchParams()
    formData.append('username', username.value)
    formData.append('password', password.value)

    const response = await axios.post('http://127.0.0.1:8000/login', formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    })

    // Jika berhasil, simpan Token JWT ke penyimpanan browser (LocalStorage)
    localStorage.setItem('access_token', response.data.access_token)
    
    // Pindah ke halaman Profil
    router.push('/profile')
    
  } catch (error) {
    if (error.response && error.response.status === 401) {
      errorMessage.value = 'Username atau password salah!'
    } else {
      errorMessage.value = 'Terjadi kesalahan pada server. Pastikan backend menyala.'
    }
  } finally {
    isLoading.value = false
  }
}
</script>