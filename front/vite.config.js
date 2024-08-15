import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'


export default defineConfig({
  plugins: [
    react(),
  ],

  server: {
    proxy: {
      '/api': {
        target: 'http://back:8000/api/',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      },
    }
  },
  
  build: {
    sourcemap: true,
  },
});