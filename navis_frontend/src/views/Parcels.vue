<template>
<div class="flex">
    <Aside class="hidden lg:block" />
    <div class="lg:w-10/12 w-full">
        <div class="pl-6 pr-6 font-base">
            <div class="hidden lg:flex font-base mt-5 justify-between">
                <div class="flex gap-4 items-center">
                    <h1 class="text-2xl font-extrabold">Parcels</h1>
                    <div class="relative ml-5">
                        <input v-model="text" class="pl-8 w-56 bg-white py-2 rounded-md focus:outline-none font-base text-sm placeholder:text-xs" type="text" placeholder="Search by parcel number">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 text-gray-400 absolute top-2 left-2 h-5">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                        </svg>
                    </div>
                </div>
                <div class="flex gap-4 items-center">
                    <div>
                        <NewParcelDrawer />
                        <EditParcelModal />
                        <DeleteModal />
                        <Notification />
                    </div>
                </div>
            </div>
            <div class="lg:hidden mt-10 flex flex-col gap-4">
                <h1 class="text-2xl font-extrabold">Parcels</h1>
                <div class="relative">
                    <input v-model="text" class="pl-8 w-[365px] bg-white py-2.5 rounded-md focus:outline-none font-base text-sm placeholder:text-xs" type="text" placeholder="Search by parcel number">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 text-gray-400 absolute top-2.5 left-2 h-5">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                    </svg>
                </div>

            </div>
            <div class="lg:hidden bg-white pb-2 font-base mt-5 rounded-md">
                <div v-for="parcel in parcels" class="border-b first:py-2 pb-2 last:border-0 last:pb-0">
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
                <ul v-if="parcels.length" class="mt-2 text-sm font-base inline-flex -space-x-px items-center divide-x">
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
            <div class="hidden lg:block font-base mt-5 rounded-md overflow-x-auto">
                <table v-if="parcels.length" class="w-full text-sm text-left text-gray-500">
                    <thead class="text-xs text-gray-950 uppercase bg-white border-b font-base">
                        <tr>
                            <th scope="col" class="px-6 py-3">
                                parcel number
                            </th>
                            <th scope="col" class="px-6 py-3">
                                client
                            </th>
                            <th scope="col" class="px-6 py-3">
                                weight
                            </th>

                            <th scope="col" class="px-6 py-3">
                                item
                            </th>
                            <th scope="col" class="px-6 py-3">
                                status
                            </th>

                            <th scope="col" class="px-6 py-3">
                                date
                            </th>
                            <th scope="col" class="px-6 py-3">
                                contact
                            </th>
                            <th scope="col" class="px-6 py-3">
                                destination
                            </th>
                            <th scope="col" class="px-6 py-3">
                                action
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="parcel in parcels" class="bg-white text-xs font-base border-b">
                            <td class="px-6 py-4 font-medium text-gray-950 whitespace-nowrap">
                                {{ parcel.parcel_number }}
                            </td>
                            <th scope="row" class="px-6 py-4">
                                {{ parcel.client.first_name }} {{ parcel.client.last_name }}
                            </th>
                            <td class="px-6 py-4">
                                {{ parcel.weight }}
                            </td>
                            <td class="px-6 py-4">
                                {{ parcel.item }}
                            </td>
                            <td class="px-6 text-xs py-4">
                                <span v-if="parcel.status === 'READY'" class="bg-violet-200 text-violet-700 px-2 text-xs py-0.5 rounded">{{ parcel.status }}</span>

                                <span v-if="parcel.status === 'DELAYED'" class="bg-pink-200 text-pink-700 px-2 text-xs py-0.5 rounded">{{ parcel.status }}</span>
                                <span v-if="parcel.status === 'ON WAY'" class="bg-yellow-200 text-yellow-700 px-2 text-xs py-0.5 rounded">{{ parcel.status }}</span>
                                <span v-if="parcel.status === 'ARRIVED'" class="bg-emerald-200 text-emerald-700 px-2 text-xs py-0.5 rounded">{{ parcel.status }}</span>
                            </td>
                            <td class="px-6 py-4">
                                {{ formatDate(parcel.created_at) }}
                            </td>
                            <td class="px-6 py-4">
                                {{ parcel.recipient_contact }}
                            </td>
                            <td class="px-6 py-4">
                                {{ parcel.destination.name }}
                            </td>
                            <td class="px-6 py-4 flex gap-4">
                                <svg @click="editParcel(parcel)" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 text-gray-500 cursor-pointer hover:text-violet-500 transition-all duration-300 h-4">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L6.832 19.82a4.5 4.5 0 01-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 011.13-1.897L16.863 4.487zm0 0L19.5 7.125" />
                                </svg>
                                <svg @click="removeParcel(parcel)" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 text-gray-500 cursor-pointer hover:text-red-500 transition-all duration-300 h-4">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                                </svg>
                            </td>
                        </tr>

                    </tbody>
                </table>
                <ul v-if="parcels.length" class="mt-2 text-sm font-base inline-flex -space-x-px items-center divide-x">
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
                <div v-else>
                    <EmptyIllustration data="parcels" />
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import Aside from '@/components/Aside.vue';
import NewParcelDrawer from '@/components/NewParcelDrawer.vue';
import EditParcelModal from '@/components/EditParcelModal.vue';
import EmptyIllustration from '@/components/EmptyIllustration.vue';
import DeleteModal from '@/components/DeleteModal.vue';

import {
    mapActions,
    mapGetters,
    mapMutations
} from 'vuex';
import moment from "moment"
import Notification from '@/components/Notification.vue';
export default {
    name: 'Parcels',
    components: {
        Aside,
        NewParcelDrawer,
        EditParcelModal,
        EmptyIllustration,
        DeleteModal,
        Notification
    },
    data() {
        return {
            text: "",
            item: "Parcel",
            totalPages: 0,
            previousPage: "",
            nextPage: "",
            currentPage: ""
        }
    },
    computed: {
        ...mapGetters({
            storedParcels: 'getStoredParcels'
        }),
        parcels() {
            return this.storedParcels.filter((parcel) => {
                return parcel.parcel_number.toLowerCase().includes(this.text.toLowerCase())
            })
        }
    },
    methods: {
        ...mapActions({
            getAllParcels: 'getAllParcels',
            deleteParcel: 'deleteParcel'
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
            this.getAllParcels({
                cb: (res) => {
                    this.previousPage = res.previous
                    this.nextPage = res.next
                    this.totalPages = res.total_pages
                    this.currentPage = res.current_page_number
                }
            })
        },
        formatDate(date) {
            return moment(date).format("MMM Do YY")
        },
        editParcel(parcel) {
            this.emitter.emit("showParcelModal", parcel)
        },
        removeParcel(parcel) {
            this.emitter.emit("showDeleteModal", {
                "type": "Parcel",
                "value": parcel.parcel_number,
                "id": parcel.id
            })
        },
        deleteConfirmedParcel(id) {
            this.deleteParcel({
                uuid: id,
                cb: (() => {
                    this.init()
                })
            })
        }
    },
    mounted() {
        this.init()
        this.emitter.on("reloadParcels", value => {
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
        this.emitter.on("deleteParcel", id => {
            this.deleteConfirmedParcel(id)
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
