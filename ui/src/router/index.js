import { createRouter, createWebHashHistory } from 'vue-router';

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/Home.vue')
    },
    {
      path: '/control',
      name: 'control',
      component: () => import('../views/CombinedControl.vue')
    },
    {
      path: '/graph',
      name: 'graph',
      component: () => import('../views/Graph.vue')
    },
    {
      path: '/maintenance',
      name: 'maintenance',
      component: () => import('../views/Maintenance.vue')
    },
    {
      path: '/table',
      name: 'table',
      component: () => import('../views/Table.vue')
    }
  ]
})

export default router;
