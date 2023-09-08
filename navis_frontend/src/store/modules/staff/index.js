
import Api from '@/services/Api'
const state = {
    staff: [],
    pageNumber: 1
}

const mutations = {
  SET_STAFF(state, payload) {
    state.staff = payload
  },
  INCREASE_PAGE(state) {
    state.pageNumber++
  },
  DECREASE_PAGE(state) {
    state.pageNumber--
  }
}

const actions = {
    async createStaff({ commit }, { payload, cb }) {
        return await Api()
            .post('/accounts/register/', payload)
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
    async getAllStaff({ commit, state }, { setResult=true, cb }) {
        return await Api()
            .get(`/accounts/users?page=${state.pageNumber}`)
            .then((response) => {
                if (setResult) {
                    commit('SET_STAFF', response.data.results)
                }
                if (cb) {
                    cb(response.data)
                }
                return response.data.results
            })
            .catch((error) => {
                return Promise.reject(error)
            })
    },
    async updateStaff({ commit }, { uuid, payload, cb }) {
        return await Api()
            .put(`accounts/users/${uuid}/`, payload)
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
      async deleteStaff({ commit }, { uuid, cb }) {
        return await Api()
            .delete(`accounts/users/${uuid}/`)
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
      async changeProfileImage ({ commit }, { payload, cb }) {
        return await Api('multipart/formdata')
            .patch('/accounts/users/profile', payload)
            .then((response) => {
                if (cb) {
                    cb(response.data)
                }
            })
            .catch((error) => console.log(error))
          
          },
}

const getters = {
  getStoredStaff: (state) => {
    return state.staff
},
}

const staffModule = {
    state,
    mutations,
    actions,
    getters
  }
export default staffModule
