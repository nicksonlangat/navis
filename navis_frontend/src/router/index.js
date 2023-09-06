import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  {
    path: '/',
    name: 'dashboard',
    component: () => import( '../views/Dashboard.vue')
  },
  {
    path: '/shipments',
    name: 'shipments',
    component: () => import( '../views/Shipments.vue')
  },
  {
    path: '/shipment/:id',
    name: 'shipment',
    component: () => import( '../views/Shipment.vue')
  },
  {
    path: '/parcels',
    name: 'parcels',
    component: () => import( '../views/Parcels.vue')
  },
  {
    path: '/clients',
    name: 'clients',
    component: () => import( '../views/Clients.vue')
  },
  {
    path: '/trucks',
    name: 'trucks',
    component: () => import( '../views/Trucks.vue')
  },
  {
    path: '/drivers',
    name: 'drivers',
    component: () => import( '../views/Drivers.vue')
  },
  {
    path: '/staff',
    name: 'staff',
    component: () => import( '../views/Staff.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import( '../views/Login.vue')
  },
  {
    path: '/reset',
    name: 'reset',
    component: () => import( '../views/Reset.vue')
  },
  {
    path: '/reset/code',
    name: 'reset-code',
    component: () => import( '../views/ResetCode.vue')
  },
  {
    path: '/reset/password',
    name: 'reset-password',
    component: () => import( '../views/ResetPassword.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
