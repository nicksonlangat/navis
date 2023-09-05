import { createStore } from 'vuex'
import Api from '@/services/Api'

export default createStore({
  state: {
    clients: [],
    parcels: [],
    trucks: [],
    drivers: [],
    shipments: [],
    locations: [],
  },
  getters: {
    getStoredClients: (state) => {
      return state.clients
  },
    getStoredParcels: (state) => {
      return state.parcels
  },
    getStoredTrucks: (state) => {
      return state.trucks
  },
    getStoredDrivers: (state) => {
      return state.drivers
  },
    getStoredShipments: (state) => {
      return state.shipments
  },
    getStoredLocations: (state) => {
      return state.locations
  },
  },
  mutations: {
    SET_CLIENTS(state, clients) {
      state.clients = clients
  },
    SET_PARCELS(state, parcels) {
      state.parcels = parcels
  },
    SET_TRUCKS(state, trucks) {
      state.trucks = trucks
  },
    SET_DRIVERS(state, drivers) {
      state.drivers = drivers
  },
    SET_SHIPMENTS(state, shipments) {
      state.shipments = shipments
  },
    SET_LOCATIONS(state, locations) {
      state.locations = locations
  },
  },
  actions: {
    async createClient({ commit }, { payload, cb }) {
      return await Api()
          .post('clients', payload)
          .then((response) => {
              if (cb) {
                  cb(response.data)
              }
              return response.data
          })
          .catch((error) => {
              return Promise.reject(error)
          })
  },
    async getAllClients({ commit, state }, { setResult=true, cb }) {
      return await Api()
          .get('/clients')
          .then((response) => {
              if (setResult) {
                  commit('SET_CLIENTS', response.data.results)
              }
              if (cb) {
                  cb(response.data.results)
              }
              return response.data.results
          })
          .catch((error) => {
              return Promise.reject(error)
          })
  },
  async updateClient({ commit }, { uuid, payload, cb }) {
    return await Api()
        .put(`clients/${uuid}/`, payload)
        .then((response) => {
            if (cb) {
                cb(response.data)
            }
            return response.data
        })
        .catch((error) => {
            return Promise.reject(error)
        })
  },
  async deleteClient({ commit }, { uuid, cb }) {
    return await Api()
        .delete(`clients/${uuid}/`)
        .then((response) => {
            if (cb) {
                cb(response.data)
            }
            return response.data
        })
        .catch((error) => {
            return Promise.reject(error)
        })
  },

  async createParcel({ commit }, { payload, cb }) {
    return await Api()
        .post('parcels', payload)
        .then((response) => {
            if (cb) {
                cb(response.data)
            }
            return response.data
        })
        .catch((error) => {
            return Promise.reject(error)
        })
  },
  async getAllParcels({ commit, state }, { setResult=true, cb, destination }) {
  return await Api()
      .get(`/parcels?destination=${destination}`)
      .then((response) => {
          if (setResult) {
              commit('SET_PARCELS', response.data.results)
          }
          if (cb) {
              cb(response.data.results)
          }
          return response.data.results
      })
      .catch((error) => {
          return Promise.reject(error)
      })
  },
  async updateParcel({ commit }, { uuid, payload, cb }) {
  return await Api()
    .put(`parcels/${uuid}/`, payload)
    .then((response) => {
        if (cb) {
            cb(response.data)
        }
        return response.data
    })
    .catch((error) => {
        return Promise.reject(error)
    })
  },
  async deleteParcel({ commit }, { uuid, cb }) {
  return await Api()
    .delete(`parcels/${uuid}/`)
    .then((response) => {
        if (cb) {
            cb(response.data)
        }
        return response.data
    })
    .catch((error) => {
        return Promise.reject(error)
    })
  },

  async createTruck({ commit }, { payload, cb }) {
    return await Api()
        .post('trucks', payload)
        .then((response) => {
            if (cb) {
                cb(response.data)
            }
            return response.data
        })
        .catch((error) => {
            return Promise.reject(error)
        })
  },
  async getAllTrucks({ commit, state }, { setResult=true, cb }) {
  return await Api()
      .get('/trucks')
      .then((response) => {
          if (setResult) {
              commit('SET_TRUCKS', response.data.results)
          }
          if (cb) {
              cb(response.data.results)
          }
          return response.data.results
      })
      .catch((error) => {
          return Promise.reject(error)
      })
  },
  async updateTruck({ commit }, { uuid, payload, cb }) {
  return await Api()
    .put(`trucks/${uuid}/`, payload)
    .then((response) => {
        if (cb) {
            cb(response.data)
        }
        return response.data
    })
    .catch((error) => {
        return Promise.reject(error)
    })
  },
  async deleteTruck({ commit }, { uuid, cb }) {
  return await Api()
    .delete(`trucks/${uuid}/`)
    .then((response) => {
        if (cb) {
            cb(response.data)
        }
        return response.data
    })
    .catch((error) => {
        return Promise.reject(error)
    })
  },

  async createDriver({ commit }, { payload, cb }) {
    return await Api()
        .post('drivers', payload)
        .then((response) => {
            if (cb) {
                cb(response.data)
            }
            return response.data
        })
        .catch((error) => {
            return Promise.reject(error)
        })
  },
  async getAllDrivers({ commit, state }, { setResult=true, cb }) {
  return await Api()
      .get('/drivers')
      .then((response) => {
          if (setResult) {
              commit('SET_DRIVERS', response.data.results)
          }
          if (cb) {
              cb(response.data.results)
          }
          return response.data.results
      })
      .catch((error) => {
          return Promise.reject(error)
      })
  },
  async updateDriver({ commit }, { uuid, payload, cb }) {
  return await Api()
    .put(`drivers/${uuid}/`, payload)
    .then((response) => {
        if (cb) {
            cb(response.data)
        }
        return response.data
    })
    .catch((error) => {
        return Promise.reject(error)
    })
  },
  async deleteDriver({ commit }, { uuid, cb }) {
  return await Api()
    .delete(`drivers/${uuid}/`)
    .then((response) => {
        if (cb) {
            cb(response.data)
        }
        return response.data
    })
    .catch((error) => {
        return Promise.reject(error)
    })
  },

  async createShipment({ commit }, { payload, cb }) {
    return await Api()
        .post('shipments', payload)
        .then((response) => {
            if (cb) {
                cb(response.data)
            }
            return response.data
        })
        .catch((error) => {
            return Promise.reject(error)
        })
  },
  async getAllShipments({ commit, state }, { setResult=true, cb }) {
  return await Api()
      .get('/shipments')
      .then((response) => {
          if (setResult) {
              commit('SET_SHIPMENTS', response.data.results)
          }
          if (cb) {
              cb(response.data.results)
          }
          return response.data.results
      })
      .catch((error) => {
          return Promise.reject(error)
      })
  },
  async updateShipment({ commit }, { uuid, payload, cb }) {
  return await Api()
    .put(`shipments/${uuid}/`, payload)
    .then((response) => {
        if (cb) {
            cb(response.data)
        }
        return response.data
    })
    .catch((error) => {
        return Promise.reject(error)
    })
  },
  async deleteShipment({ commit }, { uuid, cb }) {
  return await Api()
    .delete(`shipments/${uuid}/`)
    .then((response) => {
        if (cb) {
            cb(response.data)
        }
        return response.data
    })
    .catch((error) => {
        return Promise.reject(error)
    })
  },
  async getAllLocations({ commit, state }, { setResult=true, cb }) {
    return await Api()
        .get('/locations')
        .then((response) => {
            if (setResult) {
                commit('SET_LOCATIONS', response.data.results)
            }
            if (cb) {
                cb(response.data.results)
            }
            return response.data.results
        })
        .catch((error) => {
            return Promise.reject(error)
        })
},

  

  },


  modules: {
  }
})
