import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import './assets/styles.css'  // 🔥 Importação do CSS global

const app = createApp(App)
app.use(router)
app.mount('#app')
