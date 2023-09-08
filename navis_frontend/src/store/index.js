import { createStore } from 'vuex'
import clientModule from './modules/clients'
import driverModule from './modules/drivers'
import parcelModule from './modules/parcels'
import shipmentModule from './modules/shipments'
import staffModule from './modules/staff'
import truckModule from './modules/trucks'
import authModule from './modules/auth'

export default createStore({
  modules: {
    clientModule,
    driverModule,
    parcelModule,
    shipmentModule,
    staffModule,
    truckModule,
    authModule
  }
})
