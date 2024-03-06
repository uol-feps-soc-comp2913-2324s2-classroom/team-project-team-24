import { createApp } from 'vue'
import './style.css'
import router from './router'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css'

createApp(App).use(router).mount('#app')
//createApp(App).mount('#app')
