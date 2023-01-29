import { createPinia, setActivePinia } from 'pinia'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap' 
import 'bootstrap/dist/css/bootstrap.min.css'
import axios from 'axios'
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";



axios.defaults.baseURL='http://127.0.0.1:8000'

const pinia = createPinia()
setActivePinia(pinia)
const app = createApp(App)
const options = {
    position: "top-center",
    timeout: 5000,
    closeOnClick: true,
    pauseOnFocusLoss: true,
    pauseOnHover: true,
    draggable: true,
    draggablePercent: 0.6,
    showCloseButtonOnHover: false,
    hideProgressBar: true,
    closeButton: "button",
    icon: true,
    rtl: false
}
app.use(Toast,options)
app.use(router,pinia,axios,)

app.mount('#app')
