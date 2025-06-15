const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: '/openmonitor/',  // Cambiar para servir desde /openmonitor/
  devServer: {
    host: '0.0.0.0',
    port: 8080,
    allowedHosts: 'all',
  }
})
