<template>
<div class="flex">
    <Aside />
    <div class="w-10/12">
        <div class="pl-6 pr-6 font-base">
            <Search />
            <div class="flex font-base mt-5 justify-between">
                <div class="flex gap-4 items-center">
                    <h1 class="text-2xl font-extrabold">Shipments</h1>
                    <div>
                        <button @click="setShipmentFilter('arrival')" :class="currentShimentFilter === 'arrival' ? 'bg-violet-600 text-white' : 'text-gray-950 bg-white' " class="text-xs py-1.5 px-4 rounded-md">All(20)</button>
                    </div>
                    <div>
                        <button @click="setShipmentFilter('available')" :class="currentShimentFilter === 'available' ? 'bg-violet-600 text-white' : 'text-gray-950 bg-white' " class=" text-xs py-1.5 px-4 rounded-md">Available(20)</button>
                    </div>

                </div>
                <div class="flex gap-4 items-center">
                    <div>
                        <button class="bg-violet-600 text-xs text-white py-1.5 px-4 rounded-md">Sort by: Delayed</button>
                    </div>
                    <div>
                        <button class="bg-white text-xs text-gray-700 py-1.5 px-4 rounded-md">Arrival date: 15 Sept</button>
                    </div>

                </div>
            </div>

            <div v-if="currentShimentFilter === 'arrival'" class="font-base mt-5 rounded-md overflow-x-auto">
                <table class="w-full text-sm text-left text-gray-500">
                    <thead class="text-xs text-gray-950 uppercase bg-white border-b font-base">
                        <tr>
                            <th scope="col" class="px-6 py-3">
                                route
                            </th>
                            <th scope="col" class="px-6 py-3">
                                shipment number
                            </th>
                            <th scope="col" class="px-6 py-3">
                                truck
                            </th>
                            <th scope="col" class="px-6 py-3">
                                weight, kg
                            </th>
                            <th scope="col" class="px-6 py-3">
                                status
                            </th>
                            <th scope="col" class="px-6 py-3">
                                departure date
                            </th>
                            <th scope="col" class="px-6 py-3">
                                arrival date
                            </th>
                            <th scope="col" class="px-6 py-3">
                                time delay
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="shipment in shipments" class="bg-white text-xs font-base border-b">
                            <th scope="row" class="px-6 py-4 font-medium text-gray-950 whitespace-nowrap">
                                {{ shipment.route_from.name }} - {{ shipment.route_to.name }}
                            </th>
                            <td class="px-6 py-4">
                                {{ shipment.shipment_number }}
                            </td>
                            <td class="px-6 py-4">
                                {{ shipment.truck.manufacturer }} {{ shipment.truck.model }} - {{ shipment.truck.registration_number }}
                            </td>
                            <td class="px-6 py-4">
                                {{ shipment.truck.carry_weight }}
                            </td>
                            <td class="px-6 py-4">
                                <span v-if="shipment.status === 'DELAYED'" class="bg-pink-200 text-pink-700 px-2 text-xs py-0.5 rounded">{{ shipment.status }}</span>
                                <span v-if="shipment.status === 'ON WAY'" class="bg-amber-200 text-amber-700 px-2 text-xs py-0.5 rounded">{{ shipment.status }}</span>
                                <span v-if="shipment.status === 'ARRIVED'" class="bg-emerald-200 text-emerald-700 px-2 text-xs py-0.5 rounded">{{ shipment.status }}</span>

                            </td>
                            <td class="px-6 py-4">
                                {{ formatDate(shipment.departure_date) }}
                            </td>
                            <td class="px-6 py-4">
                                {{ formatDate(shipment.arrival_date) }}
                            </td>
                            <td class="px-6 py-4">
                                5:05 h
                            </td>
                        </tr>

                    </tbody>
                </table>
            </div>
            <div v-if="currentShimentFilter === 'available'" class="grid font-base mt-8 grid-cols-2 gap-y-4 gap-4">
                <div v-for="shipment in shipments" @click="goToShipmentPage(shipment.id)" class="bg-white rounded-md cursor-pointer hover:shadow-md transition-shadow duration-500 h-80">
                    <div class="flex font-base justify-between ml-5 mr-5 mt-3">
                        <h3 class="text-xl"> {{ shipment.route_from.name }} - {{ shipment.route_to.name }} <span class="text-xs text-gray-500"> {{ formatDate(shipment.departure_date) }}</span></h3>
                        <h2 class="text-red-600 text-2xl"> {{percentageCalculator(5000, shipment.truck.carry_weight) }}%</h2>
                    </div>
                    <div class="flex justify-between ml-5 mr-5 mt-5 text-sm">
                        <ul class="text-gray-500 flex font-base flex-col gap-5">
                            <li>
                                <p>Available,kg</p>
                                <p class="text-gray-900">20/{{ shipment.truck.carry_weight }}</p>
                            </li>
                            <li>
                                <p>Shipment number</p>
                                <p class="text-gray-900">
                                    {{ shipment.shipment_number }}
                                </p>
                            </li>
                            <li>
                                <p>Truck</p>
                                <p class="text-gray-900">
                                    {{ shipment.truck.manufacturer }} {{ shipment.truck.model }} - {{ shipment.truck.registration_number }}
                                </p>
                            </li>
                            <li>
                                <p>Driver</p>
                                <p class="text-gray-900">
                                    {{ shipment.driver.first_name }} {{ shipment.driver.last_name }}
                                </p>
                            </li>
                        </ul>
                        <img class="w-3/4 mt-10" src="../assets/van.svg" alt="">
                    </div>
                </div>

            </div>
        </div>
    </div>
</div>
</template>

<script>
import Aside from '@/components/Aside.vue';
import Search from '@/components/Search.vue';
import moment from 'moment';
import {
    mapActions,
    mapGetters
} from 'vuex';
export default {
    name: 'Shipments',
    components: {
        Aside,
        Search,
    },
    data() {
        return {
            currentShimentFilter: 'arrival',
            text: ''
        }
    },
    computed: {
        ...mapGetters({
            storedShipments: 'getStoredShipments'
        }),
        shipments() {
            return this.storedShipments.filter((shipment) => {
                return shipment.shipment_number.toLowerCase().includes(this.text.toLowerCase())
            })
        }
    },
    methods: {
        ...mapActions({
            getAllShipments: 'getAllShipments'
        }),
        init() {
            this.getAllShipments({
                cb: () => {}
            })
        },
        formatDate(date) {
            return moment(date).format("MMM Do YY")
        },
        setShipmentFilter(value) {
            this.currentShimentFilter = value
        },
        percentageCalculator(value, total) {
            return ((value / total) * 100).toFixed(2)
        },
        goToShipmentPage(uuid) {
          this.$router.push({"name": "shipment", "params": {"id": uuid}})
        }
    },
    mounted() {
        this.init()
        this.emitter.on("reloadShipments", value => {
            this.init()
        })
    }
}
</script>

<style>
html {
    background-color: #F1F1FB;
}
</style>
