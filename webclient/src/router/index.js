import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../components/Home.vue';
import Events from '../components/Events.vue';
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
// views
import Mission from '../views/Mission.vue';

Vue.use(VueRouter);

const routes = [
  // components
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/events',
    name: 'Event',
    component: Events,
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
  // views
  {
    path: '/mission',
    name: 'Mission',
    component: Mission,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
