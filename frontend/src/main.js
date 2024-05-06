import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css'
import axios from 'axios'
import CanvasJSChart from '@canvasjs/vue-charts'

// CSS
import '@/assets/css/style.css'
import '@/assets/css/button.css'
import '@/assets/css/nav.css'
import '@/assets/css/pages.css'
import '@/assets/css/form.css'

// CSS
import '@/assets/css/style.css'
import '@/assets/css/button.css'
import '@/assets/css/nav.css'
import '@/assets/css/pages.css'
import '@/assets/css/form.css'

axios.defaults.baseURL = `${process.env.VUE_APP_BACKEND_URL}`;

createApp(App).use(router).mount('#app').use(CanvasJSChart)
