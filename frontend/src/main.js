import { createApp } from 'vue'
import './style.css'
import router from './router'
import App from './App.vue'
import store from './store/index'
import 'bootstrap/dist/css/bootstrap.css'
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:5001';

createApp(App).use(router).use(store).mount('#app')

