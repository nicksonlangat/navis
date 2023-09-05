<template>
<div class="">
    <button @click="openModal" class="bg-violet-600 flex gap-1 text-sm text-white py-2 px-12 rounded-md">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
        </svg>
        New parcel
    </button>
</div>
<TransitionRoot appear :show="isOpen" as="template">
    <Dialog as="div" @close="closeModal" class="relative z-10">
        <TransitionChild as="template" enter="duration-300 ease-out" enter-from="opacity-0" enter-to="opacity-100" leave="duration-200 ease-in" leave-from="opacity-100" leave-to="opacity-0">
            <div class="fixed inset-0 bg-black bg-opacity-25" />
        </TransitionChild>

        <div class="fixed inset-0 overflow-y-auto">
            <div class="flex font-base items-center justify-center p-4 text-center">
                <TransitionChild as="template" enter='transform transition ease-in-out duration-500 sm:duration-700' enterFrom='translate-x-full' enterTo='translate-x-0' leave='transform transition ease-in-out duration-500 sm:duration-700' leaveFrom='translate-x-0' leaveTo='translate-x-full'>
                    <DialogPanel class="fixed w-[500px] top-0 h-full right-0 z-40 transform overflow-hidden rounded-md bg-white p-6 text-left align-middle shadow-xl transition-all">
                        <div class="ml-2 flex justify-between mr-2">
                            <DialogTitle as="h3" class="font-medium leading-6  font-base text-xl">
                                New parcel
                            </DialogTitle>
                            <svg @click="closeModal" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 font-base cursor-pointer h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </div>

                        <p class="font-base text-gray-500 ml-2 mt-3">Enter package details below</p>
                        <div class="mt-12 ml-3">
                            <form class="flex text-xs font-base flex-col gap-6">
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
                                        <option value="READY">Ready</option>
                                        <option value="ON WAY">On way</option>
                                        <option value="DELAYED">Delayed</option>
                                        <option value="ARRIVED">Arrived</option>
                                    </select>
                                </div>
                                <div>
                                    <button @click.prevent="submitNewParcel" class="bg-violet-600 w-full text-center font-base text-white py-2 px-4 rounded-md">
                                        Submit
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
import {
    mapActions, mapGetters
} from 'vuex';
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
                status: "READY"
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
            createParcel: 'createParcel',
            getAllClients: 'getAllClients',
            getAllLocations: 'getAllLocations',
        }),
        resetForm() {
            this.parcel.client = "",
            this.parcel.item = "",
            this.parcel.weight = "",
            this.parcel.destination = "",
            this.parcel.recipient_contact = "",
            this.parcel.status = "READY"
        },
        submitNewParcel() {
            this.createParcel({
                payload: this.parcel,
                cb: (() => {
                    this.closeModal()
                    this.emitter.emit("reloadParcels", "add")
                    this.resetForm()
                })
            })
        },
        closeModal() {
            this.isOpen = false
        },
        openModal() {
            this.isOpen = true
        }
    },
    mounted() {
        this.getAllClients({
            cb: () => {}
        })
        this.getAllLocations({
            cb: () => {}
        })
    }
}
</script>
