import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/Home.vue";
import Login from "../components/Login.vue";
import Help from "../components/Help.vue";
import Contact from "../components/Contact.vue";
import About from "../components/About.vue";
import Legal from "../components/Legal.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/help",
    name: "Help",
    component: Help,
  },
  {
    path: "/contact",
    name: "Contact",
    component: Contact,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/legal",
    name: "Legal",
    component: Legal,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
