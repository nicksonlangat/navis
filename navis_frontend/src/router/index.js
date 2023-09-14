import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  {
    path: '/',
    name: 'dashboard',
    component: () => import( '../views/Dashboard.vue'),
    async beforeEnter(to, from, next) {
      try {
        var hasPermission = localStorage.getItem("hasPermission");
        if (hasPermission) {
          next()
        }
        else {
          next({
            name: "login"
          })
        }
      } catch (e) {
        next({
          name: "login"
        })
      }
    } 
  },
  {
    path: '/shipments',
    name: 'shipments',
    component: () => import( '../views/Shipments.vue'),
    async beforeEnter(to, from, next) {
      try {
        var hasPermission = localStorage.getItem("hasPermission");
        if (hasPermission) {
          next()
        }
        else {
          next({
            name: "login"
          })
        }
      } catch (e) {
        next({
          name: "login"
        })
      }
    } 
  },
  {
    path: '/shipment/:id',
    name: 'shipment',
    component: () => import( '../views/Shipment.vue'),
    async beforeEnter(to, from, next) {
      try {
        var hasPermission = localStorage.getItem("hasPermission");
        if (hasPermission) {
          next()
        }
        else {
          next({
            name: "login"
          })
        }
      } catch (e) {
        next({
          name: "login"
        })
      }
    } 
  },
  {
    path: '/parcels',
    name: 'parcels',
    component: () => import( '../views/Parcels.vue'),
    async beforeEnter(to, from, next) {
      try {
        var hasPermission = localStorage.getItem("hasPermission");
        if (hasPermission) {
          next()
        }
        else {
          next({
            name: "login"
          })
        }
      } catch (e) {
        next({
          name: "login"
        })
      }
    } 
  },
  {
    path: '/clients',
    name: 'clients',
    component: () => import( '../views/Clients.vue'),
    async beforeEnter(to, from, next) {
      try {
        var hasPermission = localStorage.getItem("hasPermission");
        if (hasPermission) {
          next()
        }
        else {
          next({
            name: "login"
          })
        }
      } catch (e) {
        next({
          name: "login"
        })
      }
    } 
  },
  {
    path: '/trucks',
    name: 'trucks',
    component: () => import( '../views/Trucks.vue'),
    async beforeEnter(to, from, next) {
      try {
        var hasPermission = localStorage.getItem("hasPermission");
        if (hasPermission) {
          next()
        }
        else {
          next({
            name: "login"
          })
        }
      } catch (e) {
        next({
          name: "login"
        })
      }
    } 
  },
  {
    path: '/drivers',
    name: 'drivers',
    component: () => import( '../views/Drivers.vue'),
    async beforeEnter(to, from, next) {
      try {
        var hasPermission = localStorage.getItem("hasPermission");
        if (hasPermission) {
          next()
        }
        else {
          next({
            name: "login"
          })
        }
      } catch (e) {
        next({
          name: "login"
        })
      }
    } 
  },
  {
    path: '/staff',
    name: 'staff',
    component: () => import( '../views/Staff.vue'),
    async beforeEnter(to, from, next) {
      try {
        var hasPermission = localStorage.getItem("hasPermission");
        if (hasPermission) {
          next()
        }
        else {
          next({
            name: "login"
          })
        }
      } catch (e) {
        next({
          name: "login"
        })
      }
    } 
  },
  {
    path: '/login',
    name: 'login',
    component: () => import( '../views/Login.vue'),
    
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
  },
  {
    path: '/account',
    name: 'account',
    component: () => import( '../views/Account.vue'),
    async beforeEnter(to, from, next) {
      try {
        var hasPermission = localStorage.getItem("hasPermission");
        if (hasPermission) {
          next()
        }
        else {
          next({
            name: "login"
          })
        }
      } catch (e) {
        next({
          name: "login"
        })
      }
    } 
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
