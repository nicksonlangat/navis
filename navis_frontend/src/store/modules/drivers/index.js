
import Api from '@/services/Api'
const state = {
  drivers: [],
}

const mutations = {
  SET_DRIVERS (state, payload) {
    state.drivers = payload
  }
}

const actions = {
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
      }
}

const getters = {
  getStoredDrivers: (state) => {
    return state.drivers
},
}

const driverModule = {
    state,
    mutations,
    actions,
    getters
  }
export default driverModule
