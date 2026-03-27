# ⛪ AG Connect - Next-Generation Church Management System

![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

**AG Connect** adalah aplikasi web *Full-Stack* berstandar *Enterprise* yang dirancang untuk mendigitalisasi dan mengoptimalkan manajemen jemaat gereja. Aplikasi ini mengintegrasikan sistem pencatatan kehadiran berbasis QR Code, gamifikasi interaktif, dan *Dashboard Analytics real-time* untuk mendukung setiap langkah pelayanan Arrow Generation.

---

## ✨ Fitur Unggulan (Key Features)

### 1. 📱 Smart QR Attendance (Pemindaian Absensi Instan)
Sistem absensi super cepat menggunakan kamera perangkat (*Scanner*) yang langsung terhubung ke *database*. Kartu digital jemaat dilengkapi dengan *Quiet Zone* (bingkai putih) untuk pemindaian milidetik.

### 2. 📊 Enterprise Analytics Dashboard
Panel kendali komprehensif untuk Admin/Gembala yang menampilkan:
* **Real-time KPI:** Total jemaat, poin beredar, dan rata-rata poin.
* **Grafik Interaktif:** Tren kehadiran bulanan (*Area Chart*), demografi jemaat (*Donut Chart*), dan Top 5 MVP (*Bar Chart*) menggunakan ApexCharts.

### 3. 🎮 Interactive Gamification
Sistem poin cerdas untuk memotivasi jemaat:
* **Tiers & Level:** Pangkat jemaat dari Pemula (Bronze) hingga Pilar (Platinum).
* **Program Referal:** Sistem kode unik (*username*) untuk mengajak teman.
* **Reward Redemption:** Admin dapat memotong/menukar poin jemaat dengan hadiah fisik.

### 4. 🔐 Role-Based Access Control (RBAC) & Keamanan
Pemisahan ruang kerja yang ketat antara **Pusat Kendali Admin** dan **Portal Pribadi Jemaat**. Dilengkapi dengan enkripsi *password* Bcrypt, pengamanan token JWT, dan fitur "Ubah Password" mandiri.

### 5. 📇 Self-Service Member Portal
Jemaat dapat login secara mandiri untuk memantau poin, melihat 5 riwayat absensi terakhir, dan mengunduh (*download*) ulang Kartu ID Digital (QR Code) mereka kapan saja langsung ke galeri HP.

### 6. 📄 Auto-Format CSV Export
Sistem *generate* laporan kehadiran matriks otomatis yang langsung diformat secara sempurna (*delimiter* & *BOM UTF-8*) agar rapi saat dibuka di Microsoft Excel.

---

## 🛠️ Teknologi yang Digunakan (Tech Stack)

**Sisi Frontend (Client-Side):**
* **Framework:** Vue.js 3 (Composition API)
* **Routing:** Vue Router (dengan arsitektur *Lazy Loading*)
* **Styling:** Tailwind CSS (Glassmorphism & Dark Mode)
* **HTTP Client:** Axios
* **Library Ekstra:** Vue3-ApexCharts (Grafik), Qrcode.vue (Generator QR)

**Sisi Backend (Server-Side):**
* **Framework:** FastAPI (Python)
* **Database ORM:** SQLAlchemy
* **Security:** Bcrypt (Hashing), PyJWT (Autentikasi Token)

**Sisi Deployment:**
* **Frontend:** Vercel
* **Backend / API:** Hugging Face Spaces

---

## 📸 Cuplikan Layar (Screenshots)

*(Ganti URL gambar di bawah ini dengan screenshot aplikasi Anda yang sebenarnya)*

| Halaman Utama (Landing Page) | Dashboard Analitik (Admin) |
| :---: | :---: |
| <img src="https://via.placeholder.com/600x300/0A0A0A/FFFFFF?text=Landing+Page+Screenshot" alt="Landing Page"> | <img src="https://via.placeholder.com/600x300/111111/FFFFFF?text=Analytics+Dashboard" alt="Analytics Dashboard"> |

| Portal Pribadi (Jemaat) | Kartu ID Digital |
| :---: | :---: |
| <img src="https://via.placeholder.com/600x300/111111/FFFFFF?text=Self-Service+Portal" alt="Member Portal"> | <img src="https://via.placeholder.com/300x400/1E1030/FFFFFF?text=QR+Digital+Card" alt="ID Card"> |

---

## 🚀 Cara Menjalankan Proyek Secara Lokal (Local Setup)

### 1. Menjalankan Backend (FastAPI)
Pastikan Anda sudah menginstal Python 3.8+.
```bash
# Clone repository ini
git clone [https://github.com/username-anda/ag-connect.git](https://github.com/username-anda/ag-connect.git)

# Masuk ke folder backend
cd ag-connect/backend

# Buat virtual environment (opsional tapi disarankan)
python -m venv venv
source venv/bin/activate  # Untuk Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Jalankan server FastAPI
uvicorn main:app --reload

Menjalankan Frontend (Vue.js)
# Buka terminal baru, masuk ke folder frontend
cd ag-connect/frontend

# Install dependencies
npm install

# Jalankan server development Vue
npm run dev
