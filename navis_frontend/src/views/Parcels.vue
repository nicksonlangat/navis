<template>
<div class="flex">
    <Aside />
    <div class="w-10/12">
        <div class="pl-6 pr-6 font-base">
            <div class="flex font-base mt-5 justify-between">
                <div class="flex gap-4 items-center">
                    <h1 class="text-2xl font-extrabold">Parcels</h1>
                    <div class="relative ml-5">
                        <input v-model="text" class="pl-8 w-56 bg-white py-1.5 rounded-md focus:outline-none font-base text-xs placeholder:text-xs" type="text" placeholder="Search by parcel number">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 text-gray-400 absolute top-1 left-1 h-5">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                        </svg>
                    </div>
                </div>
                <div class="flex gap-4 items-center">
                    <div>
                        <NewParcelDrawer/>
                        <EditParcelModal/>
                    </div>
                </div>
            </div>
            <div class="font-base mt-5 rounded-md overflow-x-auto">
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
                                <span v-if="parcel.status === 'DELAYED'" class="bg-pink-200 text-pink-700 px-2 text-xs py-0.5 rounded">{{ parcel.status }}</span>
                                <span v-if="parcel.status === 'ON WAY'" class="bg-amber-200 text-amber-700 px-2 text-xs py-0.5 rounded">{{ parcel.status }}</span>
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
                            <td class="px-6 py-4">
                                <svg @click="editParcel(parcel)" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 text-gray-500 cursor-pointer h-4">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L6.832 19.82a4.5 4.5 0 01-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 011.13-1.897L16.863 4.487zm0 0L19.5 7.125" />
                                </svg>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <div v-else>
                <EmptyIllustration data="parcels"/>
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
import {
    mapActions,
    mapGetters
} from 'vuex';
import moment from "moment"
export default {
    name: 'Parcels',
    components: {
        Aside,
        NewParcelDrawer,
        EditParcelModal,
        EmptyIllustration
    },
    data() {
        return {
            text: ""
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
        }),
        init() {
            this.getAllParcels({
                cb: () => {}
            })
        },
        formatDate(date) {
            return moment(date).format("MMM Do YY")
        },
        editParcel(parcel) {
            this.emitter.emit("showParcelModal", parcel)
        }
    },
    mounted() {
        this.init()
        this.emitter.on("reloadParcels", value => {
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
