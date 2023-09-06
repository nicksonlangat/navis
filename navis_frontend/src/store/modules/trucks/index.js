
import Api from '@/services/Api'
const state = {
    trucks: [],
}

const mutations = {
  SET_TRUCKS(state, payload) {
    state.trucks = payload
  }
}

const actions = {
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
      }    
}

const getters = {
  getStoredTrucks: (state) => {
    return state.trucks
},
}

const truckModule = {
    state,
    mutations,
    actions,
    getters
  }
export default truckModule
