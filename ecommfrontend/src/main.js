import { createPinia, setActivePinia } from 'pinia'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap' 
import 'bootstrap/dist/css/bootstrap.min.css'
import axios from 'axios'


axios.defaults.baseURL='http://127.0.0.1:8000'

const pinia = createPinia()
setActivePinia(pinia)
const app = createApp(App)

app.use(router,pinia,axios)

app.mount('#app')
