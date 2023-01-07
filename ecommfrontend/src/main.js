import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap' 
import 'bootstrap/dist/css/bootstrap.min.css'
import axios from 'axios'
import { createPinia } from 'pinia'

axios.defaults.baseURL='http://127.0.0.1:8000'

const pinia = createPinia()

createApp(App).use(router,axios,pinia).mount('#app')
