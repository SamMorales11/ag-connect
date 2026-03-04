/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'ag-purple': '#7C2889', // Warna ungu logo AG
        'ag-yellow': '#FDE021', // Warna kuning keemasan logo AG
      }
    },
  },
  plugins: [],
}