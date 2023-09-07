
import Api from '@/services/Api'
const state = {
  clients: [],
  locations: [],
  pageNumber: 1
}

const mutations = {
  SET_CLIENTS (state, payload) {
    state.clients = payload
  },
  SET_LOCATIONS(state, payload) {
    state.locations = payload
},
INCREASE_PAGE(state) {
    state.pageNumber++
  },
  DECREASE_PAGE(state) {
    state.pageNumber--
  }
}

const actions = {
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
        .get(`/clients?page=${state.pageNumber}`)
        .then((response) => {
            if (setResult) {
                commit('SET_CLIENTS', response.data.results)
            }
            if (cb) {
                cb(response.data)
            }
            return response.data
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
async getAllAnalytics({ commit, state }, { setResult=true, cb }) {
  return await Api()
      .get('/analytics')
      .then((response) => {
          if (cb) {
              cb(response.data.data)
          }
          return response.data.data
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
}

}

const getters = {
  getStoredClients: (state) => {
    return state.clients
},
getStoredLocations: (state) => {
  return state.locations
},
}

const clientModule = {
    state,
    mutations,
    actions,
    getters
  }
export default clientModule
