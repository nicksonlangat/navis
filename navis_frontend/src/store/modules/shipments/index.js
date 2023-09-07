
import Api from '@/services/Api'
const state = {
    shipments: [],
    pageNumber: 1
}

const mutations = {
  SET_SHIPMENTS (state, payload) {
    state.shipments = payload
  },
  INCREASE_PAGE(state) {
    state.pageNumber++
  },
  DECREASE_PAGE(state) {
    state.pageNumber--
  }
}

const actions = {
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
          .get(`/shipments?page=${state.pageNumber}`)
          .then((response) => {
              if (setResult) {
                  commit('SET_SHIPMENTS', response.data.results)
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
      }
}

const getters = {
  getStoredShipments: (state) => {
    return state.shipments
},
}

const shipmentModule = {
    state,
    mutations,
    actions,
    getters
  }
export default shipmentModule
