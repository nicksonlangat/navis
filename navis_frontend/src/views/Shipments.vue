<template>
<div class="flex">
    <Aside class="hidden lg:block" />
    <div class="lg:w-10/12 w-full">
        <div class="pl-6 pr-6 font-base">
            <DeleteModal />
            <Notification />
            <div class="hidden lg:flex font-base mt-5 justify-between">
                <div class="flex gap-4 items-center">
                    <h1 class="text-2xl font-extrabold">Shipments</h1>
                    <div class="relative ml-5 ">
                        <input v-model="text" class="pl-8 w-96 bg-white py-2.5 rounded-md focus:outline-none font-base text-sm placeholder:text-xs" type="text" placeholder="Search shipments by shipment number">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 text-gray-400 absolute top-2.5 left-2 h-5">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                        </svg>
                    </div>
                    <div>
                        <button @click="setShipmentFilter('arrival')" :class="currentShimentFilter === 'arrival' ? 'bg-violet-600 text-white' : 'text-gray-950 bg-white' " class="text-sm py-2.5 px-4 rounded-md">All({{ shipments.length }})</button>
                    </div>
                    <div>
                        <button @click="setShipmentFilter('available')" :class="currentShimentFilter === 'available' ? 'bg-violet-600 text-white' : 'text-gray-950 bg-white' " class=" text-sm py-2.5 px-4 rounded-md">Available({{ shipments.length }})</button>
                    </div>

                </div>
                <div>
                    <NewShipmentDrawer />
                </div>

            </div>

            <div class="lg:hidden mt-10 flex flex-col gap-4">
                <h1 class="text-2xl font-extrabold">Shipments</h1>
                <div class="relative">
                    <input v-model="text" class="pl-8 w-[365px] bg-white py-2.5 rounded-md focus:outline-none font-base text-sm placeholder:text-xs" type="text" placeholder="Search shipments by shipment number">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 text-gray-400 absolute top-2.5 left-2 h-5">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                    </svg>
                </div>

            </div>
            <div v-if="currentShimentFilter === 'arrival'" class="lg:hidden bg-white pb-2 font-base mt-5 rounded-md overflow-x-auto">

                <div v-for="shipment in shipments" class="lg:hidden border-b first:py-2 pb-2 last:border-0 last:pb-0">
                    <div class="flex justify-between ml-3 mr-5 text-xs mt-5">
                        <h3 class="uppercase text-gray-500">route <br>
                            <span class="text-gray-900"> {{ shipment.route_from.name }} - {{ shipment.route_to.name }}</span></h3>
                        <h3 class="uppercase text-gray-500">shipment number <br>
                            <span class="text-gray-900"> {{ shipment.shipment_number }}</span></h3>
                        <h3 class="uppercase text-gray-500">truck <br>
                            <span class="text-gray-900"> {{ shipment.truck.registration_number }}</span></h3>
                    </div>
                    <div class="flex justify-between ml-3 mr-5 text-xs mt-5">
                        <h3 class="uppercase text-gray-500">departure <br>
                            <span class="text-gray-900"> {{ formatDate(shipment.departure_date) }}</span></h3>
                        <h3 class="uppercase text-gray-500">arrival <br>
                            <span class="text-gray-900"> {{ formatDate(shipment.arrival_date) }}</span></h3>
                            <h3 class="uppercase text-gray-500">status <br>
                                <span v-if="shipment.status === 'READY'" class="bg-violet-200 text-violet-700 px-2 text-xs py-0.5 rounded">{{ shipment.status }}</span>
                                <span v-if="shipment.status === 'DELAYED'" class="bg-pink-200 text-pink-700 px-2 text-xs py-0.5 rounded">{{ shipment.status }}</span>
                                <span v-if="shipment.status === 'ON WAY'" class="bg-amber-200 text-amber-700 px-2 text-xs py-0.5 rounded">{{ shipment.status }}</span>
                                <span v-if="shipment.status === 'ARRIVED'" class="bg-emerald-200 text-emerald-700 px-2 text-xs py-0.5 rounded">{{ shipment.status }}</span>
                         
                            </h3>
                    </div>
                </div>
                <ul v-if="shipments.length" class="mt-2 text-sm font-base inline-flex -space-x-px items-center divide-x">
                    <li @click="goToLastPage" :class="previousPage === '' || previousPage == null ? 'text-gray-300' : 'text-gray-600'" class="flex cursor-pointer items-center justify-center px-4 h-5 ml-0 leading-tight bg-white rounded-l-md">
                        Previous
                    </li>
                    <li v-for="i in totalPages" :class="currentPage == i ? 'text-violet-600' : 'text-gray-600'" class="flex items-center justify-center px-4 h-5 leading-tight bg-white">
                        {{ i }}
                    </li>

                    <li @click="goToNextPage" :class="nextPage === '' || nextPage == null ? 'text-gray-300' : 'text-gray-600'" class="flex cursor-pointer items-center justify-center px-4 h-5 ml-0 leading-tight bg-white rounded-r-md">
                        Next
                    </li>
                </ul>
            </div>

            <div v-if="currentShimentFilter === 'arrival'" class="hidden lg:block font-base mt-5 rounded-md overflow-x-auto">
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
                                action
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
                                <span v-if="shipment.status === 'READY'" class="bg-violet-200 text-violet-700 px-2 text-xs py-0.5 rounded">{{ shipment.status }}</span>
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

                            <td class="px-6 py-4 flex gap-4">
                                <svg @click="goToShipmentPage(shipment.id)" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 text-gray-500 cursor-pointer hover:text-violet-500 transition-all duration-300 h-4">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L6.832 19.82a4.5 4.5 0 01-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 011.13-1.897L16.863 4.487zm0 0L19.5 7.125" />
                                </svg>
                                <svg @click="removeShipment(shipment)" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 text-gray-500 cursor-pointer hover:text-red-500 transition-all duration-300 h-4">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                                </svg>
                            </td>
                        </tr>

                    </tbody>
                </table>
                <ul v-if="shipments.length" class="mt-2 text-sm font-base inline-flex -space-x-px items-center divide-x">
                    <li @click="goToLastPage" :class="previousPage === '' || previousPage == null ? 'text-gray-300' : 'text-gray-600'" class="flex cursor-pointer items-center justify-center px-4 h-10 ml-0 leading-tight bg-white rounded-l-md">
                        Previous
                    </li>
                    <li v-for="i in totalPages" :class="currentPage == i ? 'text-violet-600' : 'text-gray-600'" class="flex items-center justify-center px-4 h-10 leading-tight bg-white">
                        {{ i }}
                    </li>

                    <li @click="goToNextPage" :class="nextPage === '' || nextPage == null ? 'text-gray-300' : 'text-gray-600'" class="flex cursor-pointer items-center justify-center px-4 h-10 ml-0 leading-tight bg-white rounded-r-md">
                        Next
                    </li>
                </ul>
            </div>
            <div v-if="currentShimentFilter === 'available'" class="grid font-base mt-8 grid-cols-2 gap-y-4 gap-4">
                <div v-for="shipment in shipments.slice(-4)" @click="goToShipmentPage(shipment.id)" class="bg-white rounded-md cursor-pointer hover:shadow-md transition-shadow duration-500 h-80">
                    <div class="flex font-base justify-between ml-5 mr-5 mt-3">
                        <h3 class="text-xl"> {{ shipment.route_from.name }} - {{ shipment.route_to.name }} <span class="text-xs text-gray-500"> {{ formatDate(shipment.departure_date) }}</span></h3>
                        <h2 class="text-violet-600 text-2xl"> {{percentageCalculator(0, shipment.truck.carry_weight) }}%</h2>
                    </div>
                    <div class="flex justify-between ml-5 mr-5 mt-5 text-sm">
                        <ul class="text-gray-500 flex font-base flex-col gap-5">
                            <li>
                                <p>Available,kg</p>
                                <p class="text-gray-900">0/{{ shipment.truck.carry_weight }}</p>
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
            <ul v-if="currentShimentFilter === 'available'" class="mt-2 text-sm font-base inline-flex -space-x-px items-center divide-x">
                <li @click="goToLastPage" :class="previousPage === '' || previousPage == null ? 'text-gray-300' : 'text-gray-600'" class="flex cursor-pointer items-center justify-center px-4 h-10 ml-0 leading-tight bg-white rounded-l-md">
                    Previous
                </li>
                <li v-for="i in totalPages" :class="currentPage == i ? 'text-violet-600' : 'text-gray-600'" class="flex items-center justify-center px-4 h-10 leading-tight bg-white">
                    {{ i }}
                </li>

                <li @click="goToNextPage" :class="nextPage === '' || nextPage == null ? 'text-gray-300' : 'text-gray-600'" class="flex cursor-pointer items-center justify-center px-4 h-10 ml-0 leading-tight bg-white rounded-r-md">
                    Next
                </li>
            </ul>
        </div>
    </div>
</div>
</template>

<script>
import Aside from '@/components/Aside.vue';
import moment from 'moment';
import DeleteModal from '@/components/DeleteModal.vue';
import Notification from '@/components/Notification.vue';
import {
    mapActions,
    mapGetters,
    mapMutations
} from 'vuex';
import NewShipmentDrawer from '@/components/NewShipmentDrawer.vue';
export default {
    name: 'Shipments',
    components: {
        Aside,
        DeleteModal,
        Notification,
        NewShipmentDrawer
    },
    data() {
        return {
            currentShimentFilter: 'arrival',
            text: '',
            item: "Shipment",
            totalPages: 0,
            previousPage: "",
            nextPage: "",
            currentPage: ""
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
            getAllShipments: 'getAllShipments',
            deleteShipment: 'deleteShipment'
        }),
        ...mapMutations({
            INCREASE_PAGE: 'INCREASE_PAGE',
            DECREASE_PAGE: 'DECREASE_PAGE',
        }),
        goToNextPage() {
            if (this.nextPage != null) {
                this.INCREASE_PAGE()
                this.init()
            }
        },
        goToLastPage() {
            if (this.previousPage != null) {
                this.DECREASE_PAGE()
                this.init()
            }
        },
        init() {
            this.getAllShipments({
                cb: (res) => {
                    this.previousPage = res.previous
                    this.nextPage = res.next
                    this.totalPages = res.total_pages
                    this.currentPage = res.current_page_number
                }
            })
        },
        formatDate(date) {
            return moment(date).format("DD-MM-YY")
        },
        setShipmentFilter(value) {
            this.currentShimentFilter = value
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
        removeShipment(shipment) {
            this.emitter.emit("showDeleteModal", {
                "type": "Shipment",
                "value": shipment.shipment_number,
                "id": shipment.id
            })
        },
        deleteConfirmedShipment(id) {
            this.deleteShipment({
                uuid: id,
                cb: (() => {
                    this.init()
                })
            })
        }
    },
    mounted() {
        this.init()
        this.emitter.on("reloadShipments", value => {
            this.init()
            if (value === "edit") {
                this.emitter.emit("showNotification", {
                    "action": "edit",
                    "item": this.item
                })
            } else if (value === "add") {
                this.emitter.emit("showNotification", {
                    "action": "add",
                    "item": this.item
                })
            }
        })
        this.emitter.on("deleteShipment", id => {
            this.deleteConfirmedShipment(id)
            this.emitter.emit("showNotification", {
                "action": "delete",
                "item": this.item
            })
        })
    }
}
</script>

<style>
html {
    background-color: #F1F1FB;
}
</style>
