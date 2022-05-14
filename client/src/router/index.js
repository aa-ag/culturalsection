import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/Home.vue";
import Missions from "../components/Missions.vue";
import Login from "../components/Login.vue";
import Signup from "../components/Signup.vue";
import Calendar from "../components/Calendar.vue";
import Help from "../components/Help.vue";
import Contact from "../components/Contact.vue";
import About from "../components/About.vue";
import Legal from "../components/Legal.vue";
import Reset from "../components/Reset.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/missions",
    name: "Missions",
    component: Missions,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/calendar",
    name: "Calendar",
    component: Calendar,
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
  {
    path: "/reset",
    name: "Reset",
    component: Reset,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
