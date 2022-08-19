import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Home from '@/components/Home';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
  ],
  mode: 'history',
});
