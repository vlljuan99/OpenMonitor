import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  base: '/openmonitor/',
  server: {
    host: '0.0.0.0',
    port: 5174,  // Cambia aquí el puerto
    strictPort: true,  // Para asegurar que no use otro puerto si este está ocupado
  }
});
