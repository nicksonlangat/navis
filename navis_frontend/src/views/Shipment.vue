<template>
<div class="flex">
    <Aside />
    <div class="w-10/12">
        <div class="pl-6 pr-6 font-base">
            <div class="font-base mt-5">
                <h3 class="text-gray-400 text-sm">Shipments / <span class="text-violet-600">{{ shipmentId }}</span> </h3>
                <h1 class="text-2xl">{{ shipment?.route_from.name }} - {{ shipment?.route_to.name }} <span class="text-xs text-gray-500">{{ formatDate(shipment?.departure_date) }}</span></h1>
            </div>

            <div class="grid font-base mt-3 grid-cols-2 gap-y-4 gap-4">
                <div class="bg-white rounded-md pb-2">
                    <div class="flex font-base justify-between ml-5 mr-5 mt-3">
                        <h3 class="text-xl">Truck load</h3>
                        <h2 class="text-violet-600 text-2xl">{{percentageCalculator(shipment?.loaded_kg, shipment?.truck.carry_weight) }} %</h2>
                    </div>
                    <div class="flex justify-between ml-5 mr-5 mt-5 text-lg">
                        <ul class="text-gray-500 flex font-base flex-col gap-5">
                            <li>
                                <p>Available,kg</p>
                                <p class="text-gray-900">{{shipment?.loaded_kg}} / {{ shipment?.truck.carry_weight }}</p>
                            </li>

                        </ul>
                        <img class="w-3/4" src="../assets/van.svg" alt="">
                    </div>
                    <div class="relative mt-3 font-base overflow-x-auto">
                        <h3 class="ml-6 font-extrabold underline">Parcels in this shipment</h3>
                        <table class="w-full mt-3 text-xs text-left text-gray-500 font-base accent-violet-600">
                            <thead class="text-xs text-gray-700 uppercase bg-white border-b">
                                <tr>
                                    
                                    <th scope="col" class="px-6 py-3">
                                        Parcel number
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        Weight
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        destination
                                    </th>

                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="parcel in shipment?.parcels" class="bg-white border-b font-base">
                                    
                                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
                                        {{ parcel?.parcel_number }}
                                    </th>
                                    <td class="px-6 py-4">
                                        {{ parcel?.weight }}
                                    </td>
                                    <td class="px-6 py-4">
                                        {{ parcel.destination?.name }}
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="flex justify-between mr-5 mt-5 ml-5 text-sm font-base">
                        <button @click="printParcels" class="bg-violet-600 text-white py-1.5 px-4 rounded-md text-violet-600">Print parcels list</button>
                        <button @click="finishLoading" class="bg-violet-600 text-white py-1.5 px-4 rounded-md text-violet-600">Finish loading</button>
                    </div>
                </div>
                <div class="bg-white rounded-md pb-5">
                    <div class="flex items-center justify-between font-base ml-3 mt-2 mr-3">
                        <h3 class="font-bold">Available packages</h3>
                        <button @click.prevent="updateShipmentDetails" class="bg-violet-600 text-sm py-1 px-4 rounded-md text-white">Add selections to truck</button>
                    </div>
                    <div class="relative mt-2 font-base overflow-x-auto">
                        <table class="w-full text-xs text-left text-gray-500 font-base accent-violet-600">
                            <thead class="text-xs text-gray-700 uppercase bg-white border-b">
                                <tr>
                                    <th scope="col" class="p-4">
                                        <div class="flex items-center">
                                            <input id="checkbox-all-search" type="checkbox" class="w-4 h-4 text-violet-600 bg-gray-100 border-gray-300 rounded">
                                            <label for="checkbox-all-search" class="sr-only">checkbox</label>
                                        </div>
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        Parcel number
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        Weight
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        destination
                                    </th>

                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="parcel in parcels" class="bg-white border-b font-base">
                                    <td class="w-4 p-4">
                                        <div class="flex items-center">
                                            <input :checked="shipmentParcels.includes(parcel.id)" @click="addToParcelList(parcel)" type="checkbox" class="w-4 h-4 text-violet-600 bg-gray-100 border-gray-300 rounded">
                                            <label for="checkbox" class="sr-only">checkbox</label>
                                        </div>
                                    </td>
                                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
                                        {{ parcel.parcel_number }}
                                    </th>
                                    <td class="px-6 py-4">
                                        {{ parcel.weight }}
                                    </td>
                                    <td class="px-6 py-4">
                                        {{ parcel.destination.name }}
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import Aside from '@/components/Aside.vue';
import moment from 'moment';
import {
    mapActions,
    mapGetters
} from 'vuex';

export default {
    name: 'Shipment',
    components: {
        Aside
    },
    data() {
        return {
            shipmentId: null,
            selectedParcels: [],
            unselectedParcels: [],
            cc: ""
        }
    },
    computed: {
        ...mapGetters({
            storedShipments: 'getStoredShipments',
            storedParcels: 'getStoredParcels'
        }),
        shipment() {
            return this.storedShipments.find((shipment) => {
                return shipment.id == this.shipmentId
            })
        },
        parcels() {
            return this.storedParcels.filter((parcel) => {
                return parcel.destination.id == this.shipment?.route_to.id
            }) 
        },
        shipmentParcels() {
            return this.shipment.parcels.map(item => item.id)
        }
    },
    methods: {
        ...mapActions({
            getAllShipments: 'getAllShipments',
            getAllParcels: 'getAllParcels',
            updateShipment: 'updateShipment',
        }),
        init() {
            this.getAllShipments({
                cb: () => {}
            })
            this.getAllParcels({
                cb: () => {}
            })
        },
        formatDate(date) {
            return moment(date).format("MMM Do YY")
        },
        percentageCalculator(value, total) {
            return ((value / total) * 100).toFixed(2)
        },
        addToParcelList(parcel) {
            this.shipmentParcels.includes(parcel.id) ? this.unselectedParcels.push(parcel.id) : this.selectedParcels.push(parcel.id)
        },
        updateShipmentDetails() {
            this.shipment.truck = this.shipment.truck.id
            this.shipment.driver = this.shipment.driver.id
            this.shipment.route_from = this.shipment.route_from.id
            this.shipment.route_to = this.shipment.route_to.id
            
            if(this.unselectedParcels.length) {
                this.unselectedParcels.forEach((parcel)=>{
                    const index = this.shipmentParcels.indexOf(parcel)
                        if (index > -1) {
                            this.shipmentParcels.splice(index, 1)
                        }
                })
            }
            
            this.shipment.parcels = [...this.shipmentParcels, ...this.selectedParcels]
            
            this.updateShipment({
                uuid: this.shipment.id,
                payload: this.shipment,
                cb: (() => {
                    this.init()
                })
            })
        },
        printParcels() {

        },
        finishLoading() {
            this.shipment["status"] = "ON WAY"
            this.shipment.truck = this.shipment.truck.id
            this.shipment.driver = this.shipment.driver.id
            this.shipment.route_from = this.shipment.route_from.id
            this.shipment.route_to = this.shipment.route_to.id
            this.shipment.parcels = this.shipmentParcels
            this.updateShipment({
                uuid: this.shipment.id,
                payload: this.shipment,
                cb: (() => {
                    this.$router.push({"name": "shipments"})
                })
            })
        }
    },
    mounted() {
        this.shipmentId = this.$route.params['id']
        this.init()
    }
}
</script>

<style>
html {
    background-color: #F1F1FB;
}
</style>
