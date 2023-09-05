<template>
    <div class="flex">
        <Aside />
        <div class="w-10/12">
            <div class="pl-6 pr-6 font-base">
                <div class="flex font-base mt-5 justify-between">
                    <div class="flex gap-4 items-center">
                        <h1 class="text-2xl font-extrabold">Trucks</h1>
                        <div class="relative ml-5">
                            <input v-model="text" class="pl-8 w-72 bg-white py-1.5 rounded-md focus:outline-none font-base text-xs placeholder:text-xs" type="text" placeholder="Search trucks by chasis or reg no">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 text-gray-400 absolute top-1 left-1 h-5">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                            </svg>
                        </div>
                    </div>
                    <div class="flex gap-4 items-center">
                        <div>
                            <NewTruckDrawer />
                            <EditTruckModal/>
                        </div>
                    </div>
                </div>
                <div class="font-base mt-5 rounded-md overflow-x-auto">
                    <table v-if="trucks.length" class="w-full text-sm text-left text-gray-500">
                        <thead class="text-xs text-gray-950 uppercase bg-white border-b font-base">
                            <tr>
                                <th scope="col" class="px-6 py-3">
                                    manufacturer
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    model
                                </th>
    
                                <th scope="col" class="px-6 py-3">
                                    year of mfg
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    chasis number
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    regn number
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    engine size
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    engine power
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    carry weight
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    action
                                </th>
                            </tr>
                        </thead>
                        <tbody class="">
                            <tr v-for="truck in trucks" class="bg-white text-xs font-base border-b">
                                <th scope="row" class="px-6 py-4 font-medium text-gray-950 whitespace-nowrap">
                                    {{ truck.manufacturer }}
                                </th>
                                <td class="px-6 py-4">
                                    {{ truck.model }}
                                </td>
                                <td class="px-6 py-4">
                                    {{ truck.yom }}
                                </td>
                                <td class="px-6 py-4">
                                    {{ truck.chasis_number }}
                                </td>
                                <td class="px-6 py-4">
                                    {{ truck.registration_number }}
                                </td>
                                <td class="px-6 py-4">
                                    {{ truck.engine_size }}
                                </td>
                                <td class="px-6 py-4">
                                    {{ truck.engine_power }}
                                </td>
                                <td class="px-6 py-4">
                                    {{ truck.carry_weight }}
                                </td>
                                <td class="px-6 py-4">
                                    <svg @click="editTruck(truck)" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 text-gray-500 cursor-pointer h-4">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L6.832 19.82a4.5 4.5 0 01-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 011.13-1.897L16.863 4.487zm0 0L19.5 7.125" />
                                    </svg>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <div v-else>
                <EmptyIllustration data="trucks"/>
               </div>
                </div>
            </div>
        </div>
    </div>
    </template>
    
    <script>
    import Aside from '@/components/Aside.vue';
    import Search from '@/components/Search.vue';
    import NewTruckDrawer from '@/components/NewTruckDrawer.vue';
    import EditTruckModal from '@/components/EditTruckModal.vue';
    import EmptyIllustration from '@/components/EmptyIllustration.vue';
    import {
        mapActions,
        mapGetters
    } from 'vuex';
    import moment from "moment"
    export default {
        name: 'Trucks',
        components: {
            Aside,
            Search,
            NewTruckDrawer,
            EditTruckModal,
            EmptyIllustration
        },
        data() {
            return {
                text: ""
            }
        },
        computed: {
            ...mapGetters({
                storedTrucks: 'getStoredTrucks'
            }),
            trucks() {
                return this.storedTrucks.filter((truck) => {
                    return truck.chasis_number.toLowerCase().includes(this.text.toLowerCase()) || truck.registration_number.toLowerCase().includes(this.text.toLowerCase())
                }) 
            }
        },
        methods: {
            ...mapActions({
                getAllTrucks: 'getAllTrucks',
            }),
            init() {
                this.getAllTrucks({
                    cb: (res) => {}
                })
            },
            formatDate(date) {
                return moment(date).format("MMM Do YY")
            },
            editTruck(truck) {
                this.emitter.emit("showTruckModal", truck)
            }
        },
        mounted() {
            this.init()
            this.emitter.on("reloadTrucks", value => {
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
    