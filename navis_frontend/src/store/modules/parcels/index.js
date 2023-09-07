
import Api from '@/services/Api'
const state = {
  parcels: [],
  pageNumber: 1,
}

const mutations = {
  SET_PARCELS (state, payload) {
    state.parcels = payload
  },
  INCREASE_PAGE(state) {
    state.pageNumber++
  },
  DECREASE_PAGE(state) {
    state.pageNumber--
  }
}

const actions = {
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
          .get(`/parcels?page=${state.pageNumber}&destination=${destination}`)
          .then((response) => {
              if (setResult) {
                  commit('SET_PARCELS', response.data.results)
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
      }    
}

const getters = {
  getStoredParcels: (state) => {
    return state.parcels
},
}

const parcelModule = {
    state,
    mutations,
    actions,
    getters
  }
export default parcelModule
