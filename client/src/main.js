import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap/dist/css/bootstrap.css";
import VueBootstrapTypeahead from "vue-bootstrap-typeahead";

createApp(App).use(store).use(router).mount("#app");

Vue.component("vue-bootstrap-typeahead", VueBootstrapTypeahead)
