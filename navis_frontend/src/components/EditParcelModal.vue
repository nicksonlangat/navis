<template>
<TransitionRoot appear :show="isOpen" as="template">
    <Dialog as="div" @close="toggleModal" class="relative z-10">
        <TransitionChild as="template" enter="duration-300 ease-out" enter-from="opacity-0" enter-to="opacity-100" leave="duration-200 ease-in" leave-from="opacity-100" leave-to="opacity-0">
            <div class="fixed inset-0 bg-black bg-opacity-25" />
        </TransitionChild>
        <div class="fixed inset-0 overflow-y-auto">
            <div class="flex min-h-full items-center justify-center p-4 text-center">
                <TransitionChild as="template" enter="duration-300 ease-out" enter-from="opacity-0 scale-95" enter-to="opacity-100 scale-100" leave="duration-200 ease-in" leave-from="opacity-100 scale-100" leave-to="opacity-0 scale-95">
                    <DialogPanel class="w-full max-w-xl transform overflow-hidden rounded-md bg-white p-6 text-left align-middle shadow-xl transition-all">
                        <div class=" flex justify-between">
                            <DialogTitle as="h3" class="text-lg font-medium leading-6 text-gray-900">
                            Parcel {{parcel?.parcel_number}}
                        </DialogTitle>
                        <button @click="deleteParcelDetails" class="text-xs bg-red-500 text-white rounded-md py-1.5 px-6">Delete</button>
                        </div>
                        <div class="mt-2">
                            <form class="flex text-xs font-base flex-col gap-3">
                                <div class="flex flex-col gap-1">
                                    <label for="client">Client</label>
                                    <select v-model="parcel.client" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 font-base">
                                        <option v-for="client in clients" :value="client.id">{{ client.first_name }} {{ client.last_name }}</option>
                                    </select>
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="item">Item</label>
                                    <input v-model="parcel.item" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="E.g Macbook Air">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="weight">Weight</label>
                                    <input v-model="parcel.weight" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="E.g 50">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="location">Destination</label>
                                    <select v-model="parcel.destination" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 font-base">
                                    <option v-for="location in locations" :value="location.id">{{ location.name }}</option>
                                    </select>
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="recipient_contact">Recipient contact</label>
                                    <input v-model="parcel.recipient_contact" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="E.g 0712345676">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="status">Status</label>
                                    <select v-model="parcel.status" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="Brown">
                                        <option value="DELAYED">Delayed</option>
                                        <option value="ON WAY">On way</option>
                                        <option value="ARRIVED">Arrived</option>
                                    </select>
                                </div>
                                <div>
                                    <button @click.prevent="updateParcelDetails" class="bg-violet-600 w-full text-center font-base text-white py-2 px-4 rounded-md">
                                        Update parcel
                                    </button>
                                </div>
                            </form>
                        </div>
                    </DialogPanel>
                </TransitionChild>
            </div>
        </div>
    </Dialog>
</TransitionRoot>
</template>

<script>
import {
    TransitionRoot,
    TransitionChild,
    Dialog,
    DialogPanel,
    DialogTitle,
} from '@headlessui/vue'
import { mapActions, mapGetters } from 'vuex'

export default {
    components: {
        TransitionRoot,
        TransitionChild,
        Dialog,
        DialogPanel,
        DialogTitle,
    },
    data() {
        return {
            isOpen: false,
            parcel: {
                client: "",
                item: "",
                weight: "",
                destination: "",
                recipient_contact: "",
                status: ""
            }
            
        }
    },
    computed: {
        ...mapGetters({
            storedClients: 'getStoredClients',
            storedLocations: 'getStoredLocations'
        }),
        clients() {
            return this.storedClients
        },
        locations() {
            return this.storedLocations
        }
    },
    methods: {
        ...mapActions({
            updateParcel: 'updateParcel',
            deleteParcel: 'deleteParcel',
            getAllClients: 'getAllClients',
            getAllLocations: 'getAllLocations',
        }),
        toggleModal() {
            this.isOpen = !this.isOpen
        },
        updateParcelDetails() {
            this.updateParcel({
                uuid: this.parcel.id,
                payload: this.parcel,
                cb: (() => {
                    this.toggleModal()
                    this.emitter.emit("reloadParcels", "edit")
                })
            })
        }
    },
    mounted() {
        this.emitter.on("showParcelModal", value => {
            this.parcel = value
            this.toggleModal()
        })
        this.getAllClients({
            cb: () => {}
        })
        this.getAllLocations({
            cb: () => {}
        })
    }
}
</script>
