import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import PrimeVue from 'primevue/config';
// import 'primevue/resources/themes/saga-blue/theme.css';       //theme
import 'primevue/resources/primevue.min.css';                 //core css
import 'primeicons/primeicons.css'; 
import 'bootstrap/dist/css/bootstrap.css'
import 'primevue/resources/themes/mdc-dark-deeppurple/theme.css'

const app = createApp(App)

app.use(store).use(PrimeVue).use(router).mount('#app')