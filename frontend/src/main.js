import { createApp } from 'vue'
import '@/assets/css/style.css'
import router from './router'
import App from './App.vue'
import store from './store/index'
import 'bootstrap/dist/css/bootstrap.css'
import axios from 'axios'
import CanvasJSChart from '@canvasjs/vue-charts'

axios.defaults.baseURL = `${process.env.VUE_APP_BACKEND_URL}`

createApp(App).use(router).use(store).mount('#app').use(CanvasJSChart)
