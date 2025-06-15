import { createApp } from 'vue'; // Importa createApp desde vue
import App from './App.vue';
import vuetify from './plugins/vuetify'; // Importa vuetify


const app = createApp(App); // Crea la aplicación
app.use(vuetify); // Usa vuetify
app.mount('#app'); // Móntala en el DOM
