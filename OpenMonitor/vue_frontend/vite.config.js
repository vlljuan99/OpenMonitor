import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vuetify from 'vite-plugin-vuetify'

export default defineConfig({
  plugins: [vue(), vuetify()],
  base: '/openmonitor/',
  server: {
    host: '0.0.0.0',
    port: 5174,
    strictPort: true
  }
})
