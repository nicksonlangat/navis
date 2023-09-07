
import Api from '@/services/Api'
const state = {
    trucks: [],
    pageNumber: 1
}

const mutations = {
  SET_TRUCKS(state, payload) {
    state.trucks = payload
  },
  INCREASE_PAGE(state) {
    state.pageNumber++
  },
  DECREASE_PAGE(state) {
    state.pageNumber--
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
          .get(`/trucks?page=${state.pageNumber}`)
          .then((response) => {
              if (setResult) {
                  commit('SET_TRUCKS', response.data.results)
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
