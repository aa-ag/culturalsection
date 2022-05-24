import BootstrapVue from 'bootstrap-vue';
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import 'bootstrap/dist/css/bootstrap.css';

createApp(App).use(store).use(router).use(BootstrapVue).mount("#app");
