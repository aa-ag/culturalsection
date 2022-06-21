import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../components/Home.vue';
import Missions from '../components/Missions.vue';
import Login from '../components/Login.vue';
import Signup from '../components/Signup.vue';
import Calendar from '../components/Calendar.vue';
import Directory from '../components/Directory.vue';
import Help from '../components/Help.vue';
import About from '../components/About.vue';
import Legal from '../components/Legal.vue';
import Reset from '../components/Reset.vue';
import Admin from '../components/Admin.vue';
import Browse from '../components/Browse.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/missions',
    name: 'Missions',
    component: Missions,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/calendar',
    name: 'Calendar',
    component: Calendar,
  },
  {
    path: '/directory',
    name: 'Directory',
    component: Directory,
  },
  {
    path: '/browse',
    name: 'Browse',
    component: Browse,
  },
  {
    path: '/help',
    name: 'Help',
    component: Help,
  },
  {
    path: '/about',
    name: 'About',
    component: About,
  },
  {
    path: '/legal',
    name: 'Legal',
    component: Legal,
  },
  {
    path: '/reset',
    name: 'Reset',
    component: Reset,
  },
  {
    path: '/admin',
    name: 'Admin',
    component: Admin,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
