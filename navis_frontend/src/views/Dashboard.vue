<template>
<div class="flex">
    <Aside class="hidden lg:block" />
    <div class="lg:w-10/12 w-full pb-10 lg:pb-0">
        <div class="pl-6 pr-6 font-base">
            <div class="hidden lg:flex mx-5 flex-col lg:flex-row justify-between items-center">
                <h1 class="text-2xl mt-5 font-extrabold">Overview</h1>
                <div class="relative mx-10 lg:ml-5 mt-5">
                    <input v-model="text" class="pl-8 w-96 bg-white py-2.5 rounded-md focus:outline-none font-base text-sm placeholder:text-xs" type="text" placeholder="Search shipments by shipment number">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 text-gray-400 absolute top-2.5 left-2 h-5">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                    </svg>
                </div>
                <div class="mt-5">
                    <NewShipmentDrawer />
                </div>
            </div>
            <div class="lg:hidden relative mt-5">
                <input v-model="text" class="pl-8 w-full bg-white py-2.5 rounded-md focus:outline-none font-base text-sm placeholder:text-xs" type="text" placeholder="Search shipments by shipment number">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 text-gray-400 absolute top-2.5 left-2 h-5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                </svg>
            </div>
            <div class="grid lg:grid-cols-4 grid-cols-2 mt-5 gap-5">

                <div class="bg-white flex justify-between items-center h-24 rounded-md">
                    <div class="ml-5">
                        <p class="text-gray-400 text-sm">New parcels</p>
                        <h3 class="text-2xl mt-1">{{ new_parcels }}</h3>
                    </div>
                    <div class="mr-5">
                        <span class="bg-[#f1f1fb] px-3 py-2.5 rounded-full">
                            🤞🏿
                        </span>
                    </div>
                </div>

                <div class="bg-white flex justify-between items-center h-24 rounded-md">
                    <div class="ml-5">
                        <p class="text-gray-400 hidden lg:block text-sm">Ready for shipping </p>
                        <p class="text-gray-400 lg:hidden text-sm">Ready </p>
                        <h3 class="text-2xl mt-1">{{ new_parcels }}</h3>
                    </div>
                    <div class="mr-5">
                        <span class="bg-[#f1f1fb] px-3 py-2.5 rounded-full">
                            📦
                        </span>
                    </div>
                </div>
                <div class="bg-white flex justify-between items-center h-24 rounded-md">
                    <div class="ml-5">
                        <p class="text-gray-400 text-sm">In transit</p>
                        <h3 class="text-2xl mt-1">{{ on_way_parcels }}</h3>
                    </div>
                    <div class="mr-5">
                        <span class="bg-[#f1f1fb] px-3 py-2.5 rounded-full">
                            🚛
                        </span>
                    </div>
                </div>
                <div class="bg-white flex justify-between items-center h-24 rounded-md">
                    <div class="ml-5">
                        <p class="text-gray-400 text-sm">Delivered</p>
                        <h3 class="text-2xl mt-1">{{ delivered_parcels }}</h3>
                    </div>
                    <div class="mr-5">
                        <span class="bg-[#f1f1fb] px-3 py-2.5 rounded-full">
                            🚀
                        </span>
                    </div>
                </div>
            </div>
            <div class="lg:hidden">
                <div class="bg-white rounded-md pb-5">
                    <div class="flex justify-between items-center mr-3 ml-3 mt-5">
                        <h3 class="text-xl font-base mt-4 font-bold">Active shipments</h3>
                        <a href="/shipments" class="text-xs mt-4 flex gap-1 text-violet-600">Show all <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                            </svg>
                        </a>
                    </div>
                    <div v-for="shipment in shipments.slice(-4)" class="border-b first:py-2 pb-2 last:border-0 last:pb-0">
                        <div class="flex justify-between ml-3 mr-5 text-xs mt-5">
                            <h3 class="uppercase text-gray-500">shipment number <br>
                                <span class="text-gray-900"> {{ shipment.shipment_number }}</span></h3>
                            <h3 class="uppercase text-gray-500">truck <br>
                                <span class="text-gray-900"> {{ shipment.truck.registration_number }}</span></h3>
                        </div>
                        <div class="flex justify-between ml-3 mr-5 text-xs mt-5">
                            <h3 class="uppercase text-gray-500">destination <br>
                                <span class="text-gray-900"> {{ shipment.route_to.name }}</span></h3>
                            <h3 class="uppercase text-gray-500">arrival <br>
                                <span class="text-gray-900"> {{ formatDate(shipment.arrival_date) }}</span></h3>
                        </div>
                    </div>
                </div>

                <div class="bg-white rounded-md pb-5">
                    <div class="flex justify-between items-center mr-3 ml-3 mt-5">
                        <h3 class="text-xl font-base mt-4 font-bold">Latest clients</h3>
                        <a href="/clients" class="text-xs mt-4 flex gap-1 text-violet-600">Show all <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                            </svg>
                        </a>
                    </div>
                    <div v-for="client in clients.slice(-4)" class="border-b first:py-2 pb-2 last:border-0 last:pb-0">
                        <div class="flex justify-between ml-3 mr-5 text-xs mt-5">
                            <h3 class="uppercase text-gray-500">name <br>
                                <span class="text-gray-900"> {{ client.first_name }} {{ client.last_name }}</span></h3>
                            <h3 class="uppercase text-gray-500">phone <br>
                                <span class="text-gray-900"> {{ client.phone_number }}</span></h3>
                        </div>
                        <div class="flex justify-between ml-3 mr-5 text-xs mt-5">
                            <h3 class="uppercase text-gray-500">email <br>
                                <span class="text-gray-900"> {{ client.email }}</span></h3>
                            <h3 class="uppercase text-gray-500">location <br>
                                <span class="text-gray-900"> {{ client.location.name }}</span></h3>
                        </div>
                    </div>
                </div>
                <div class="bg-white rounded-md pb-5">
                    <div class="flex justify-between items-center mr-3 ml-3 mt-5">
                        <h3 class="text-xl font-base mt-4 font-bold">Available trucks</h3>
                        <a href="/trucks" class="text-xs mt-4 flex gap-1 text-violet-600">Show all <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                            </svg>
                        </a>
                    </div>
                    <div v-for="truck in trucks.slice(-4)" class="border-b first:py-2 pb-2 last:border-0 last:pb-0">
                        <div class="flex justify-between ml-3 mr-5 text-xs mt-5">
                            <h3 class="uppercase text-gray-500">registration <br>
                                <span class="text-gray-900"> {{ truck.registration_number }}</span></h3>
                            <h3 class="uppercase text-gray-500">name <br>
                                <span class="text-gray-900"> {{ truck.manufacturer }}</span></h3>
                        </div>
                        <div class="flex justify-between ml-3 mr-5 text-xs mt-5">
                            <h3 class="uppercase text-gray-500">model <br>
                                <span class="text-gray-900"> {{ truck.model }}</span></h3>
                            <h3 class="uppercase text-gray-500">weight <br>
                                <span class="text-gray-900"> {{ truck.carry_weight }}</span></h3>
                        </div>
                    </div>
                </div>
                <div class="bg-white rounded-md pb-5">
                    <div class="flex justify-between items-center mr-3 ml-3 mt-5">
                        <h3 class="text-xl font-base mt-4 font-bold">Recent parcels</h3>
                        <a href="/parcels" class="text-xs mt-4 flex gap-1 text-violet-600">Show all <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                            </svg>
                        </a>
                    </div>
                    <div v-for="parcel in recent_parcels.slice(-4)" class="border-b first:py-2 pb-2 last:border-0 last:pb-0">
                        <div class="flex justify-between ml-3 mr-5 text-xs mt-5">
                            <h3 class="uppercase text-gray-500">parcel number <br>
                                <span class="text-gray-900"> {{ parcel.parcel_number }}</span></h3>
                            <h3 class="uppercase text-gray-500">destination <br>
                                <span class="text-gray-900"> {{ parcel.destination.name }}</span></h3>
                        </div>
                        <div class="flex justify-between ml-3 mr-5 text-xs mt-5">
                            <h3 class="uppercase text-gray-500">client <br>
                                <span class="text-gray-900"> {{ parcel.client.first_name }}</span></h3>
                            <h3 class="uppercase text-gray-500">item <br>
                                <span class="text-gray-900"> {{ parcel.item }}</span></h3>
                        </div>
                    </div>
                </div>

            </div>
            <div class="hidden lg:grid mt-8 font-base lg:grid-cols-2 gap-y-4 gap-4">
                <div class="bg-white rounded-md h-72">
                    <div class="flex justify-between items-center mr-3 ml-3 mt-2">
                        <h3 class="text-xl font-base font-bold">Active shipments</h3>
                        <a href="/shipments" class="text-xs flex gap-1 text-violet-600">Show all <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                            </svg>
                        </a>
                    </div>
                    <div class="font-base mt-3 mr-3 ml-3 rounded-md overflow-x-auto">
                        <table class="w-full text-sm text-left text-gray-500">
                            <thead class="text-xs text-gray-950 uppercase bg-[#f1f1fb]  font-base">
                                <tr>
                                    <th scope="col" class="px-6 py-3">
                                        shipment number
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        truck
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        destination
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        arrival
                                    </th>
                                </tr>
                            </thead>
                            <tbody class="">
                                <tr v-for="shipment in shipments.slice(-4)" class="bg-white text-xs font-base border-b last:border-0">
                                    <th scope="row" class="px-6 py-4 font-medium text-gray-950 whitespace-nowrap">
                                        {{ shipment.shipment_number }}
                                    </th>

                                    <td class="px-6 py-4">
                                        {{ shipment.truck.registration_number }}
                                    </td>
                                    <td class="px-6 py-4">
                                        {{ shipment.route_to.name }}
                                    </td>
                                    <td class="px-6 py-4">
                                        {{ formatDate(shipment.arrival_date) }}
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="bg-white rounded-md h-72">
                    <div class="flex justify-between items-center mr-3 ml-3 mt-2">
                        <h3 class="text-xl font-base font-bold">Latest clients</h3>
                        <a href="/clients" class="text-xs flex gap-1 text-violet-600">Show all <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                            </svg>
                        </a>
                    </div>
                    <div class="font-base mt-3 mr-3 ml-3 rounded-md overflow-x-auto">
                        <table class="w-full text-sm text-left text-gray-500">
                            <thead class="text-xs text-gray-950 uppercase bg-[#f1f1fb]  font-base">
                                <tr>
                                    <th scope="col" class="px-6 py-3">
                                        name
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        phone
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        email
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        location
                                    </th>
                                </tr>
                            </thead>
                            <tbody class="">
                                <tr v-for="client in clients.slice(-4)" class="bg-white text-xs font-base border-b last:border-0">
                                    <th scope="row" class="px-6 py-4 font-medium text-gray-950 whitespace-nowrap">
                                        {{ client.first_name}} {{ client.last_name}}
                                    </th>

                                    <td class="px-6 py-4">
                                        {{ client.phone_number }}
                                    </td>
                                    <td class="px-6 py-4">
                                        {{ client.email }}
                                    </td>
                                    <td class="px-6 py-4">
                                        {{ client.location.name }}
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="bg-white rounded-md h-72">
                    <div class="flex justify-between items-center mr-3 ml-3 mt-1">
                        <h3 class="text-xl font-base font-bold">Available trucks</h3>
                        <a href="/trucks" class="text-xs flex gap-1 text-violet-600">Show all <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                            </svg>
                        </a>
                    </div>
                    <ul class="flex flex-col font-base gap-2 divide-y ml-3 mr-3 mt-2">
                        <li v-for="truck in trucks.slice(-4)" class="flex justify-between">
                            <div>
                                <h3 class=" text-sm">{{ truck.registration_number }}</h3>
                                <p class="text-gray-500 text-xs">{{ truck.manufacturer }} {{ truck.model }}</p>
                            </div>
                            <div class="flex flex-col gap-2 items-center">
                                <p class="text-gray-500 text-sm"> <span class="text-violet-600">0</span>/100%</p>
                                <div class="w-32 bg-gray-200 rounded-full h-1.5 mb-4">
                                    <div class="bg-red-600 h-1.5 rounded-full" style="width: 0%"></div>
                                </div>
                            </div>
                        </li>

                    </ul>
                </div>
                <div class="bg-white rounded-md h-72">
                    <div class="flex justify-between items-center mr-3 ml-3 mt-1">
                        <h3 class="text-xl font-base font-bold">Recent parcels</h3>
                        <a href="/parcels" class="text-xs flex gap-1 text-violet-600">Show all <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                            </svg>
                        </a>
                    </div>
                    <ul class="flex flex-col font-base gap-2 divide-y ml-3 mr-3 mt-2">
                        <li v-for="parcel in recent_parcels.slice(-4)" class="flex justify-between pb-0.5 py-1">
                            <div class="flex gap-2">
                                <span class="bg-[#f1f1fb] px-3 py-2 rounded-full">
                                    📦
                                </span>
                                <div>
                                    <h3 class=" text-sm">{{ parcel.parcel_number }}</h3>
                                    <p class="text-gray-500 text-xs">{{ parcel.destination.name }}</p>
                                </div>

                            </div>
                            <div>
                                <h3 class=" text-sm">{{ parcel.client.first_name }} {{ parcel.client.last_name }}</h3>
                                <p class="text-gray-500 text-xs">{{ parcel.recipient_contact }}</p>
                            </div>
                            <p class="text-gray-500 text-xs">{{ parcel.item }}</p>
                        </li>

                    </ul>
                </div>

            </div>
        </div>

    </div>
</div>
</template>

<script>
import Aside from '@/components/Aside.vue';
import NewShipmentDrawer from '@/components/NewShipmentDrawer.vue';
import moment from 'moment';

import {
    mapActions,
    mapGetters
} from 'vuex';
export default {
    name: 'Dashboard',
    components: {
        Aside,
        NewShipmentDrawer
    },
    data() {
        return {
            text: "",
            status: "",
            active_shipments: [],
            available_trucks: [],
            recent_parcels: [],
            clients: [],
            on_way_parcels: 0,
            delivered_parcels: 0,
            new_parcels: 0,
        }
    },
    computed: {
        ...mapGetters({
            storedShipments: 'getStoredShipments',
            storedAnalytics: 'getStoredAnalytics'
        }),
        trucks() {
            return this.available_trucks.filter((truck) => {
                return truck.is_available

            })
        },
        shipments() {
            return this.active_shipments.filter((shipment) => {
                return shipment.shipment_number.toLowerCase().includes(this.text.toLowerCase())
            })
        }
    },
    methods: {
        ...mapActions({
            getAllShipments: 'getAllShipments',
            getAllAnalytics: 'getAllAnalytics'
        }),
        init() {
            this.getAllShipments({
                cb: () => {}
            })
            this.getAllAnalytics({
                cb: (res) => {
                    this.active_shipments = res.active_shipments
                    this.new_parcels = res.new_parcels
                    this.on_way_parcels = res.on_way_parcels
                    this.delivered_parcels = res.delivered_parcels
                    this.available_trucks = res.available_trucks
                    this.recent_parcels = res.recent_parcels
                    this.clients = res.clients
                }
            })
        },
        formatDate(date) {
            return moment(date).format("DD-MM-YY")
        },
        percentageCalculator(value, total) {
            return ((value / total) * 100).toFixed(2)
        },
        goToShipmentPage(uuid) {
            this.$router.push({
                "name": "shipment",
                "params": {
                    "id": uuid
                }
            })
        },
    },
    mounted() {
        this.init()
    }
}
</script>

<style>
html {
    background-color: #F1F1FB;
}
</style>
