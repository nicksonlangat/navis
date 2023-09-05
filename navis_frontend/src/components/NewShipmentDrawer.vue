<template>
<div class="">
    <button @click="openModal" class="text-white text-sm bg-violet-600 flex gap-2 px-6 py-2 items-center justify-center rounded-md"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
        </svg>
        Create shipment</button>
</div>
<TransitionRoot appear :show="isOpen" as="template">
    <Dialog as="div" @close="closeModal" class="relative z-10">
        <TransitionChild as="template" enter="duration-300 ease-out" enter-from="opacity-0" enter-to="opacity-100" leave="duration-200 ease-in" leave-from="opacity-100" leave-to="opacity-0">
            <div class="fixed inset-0 bg-black bg-opacity-25" />
        </TransitionChild>

        <div class="fixed inset-0 overflow-y-auto">
            <div class="flex font-base items-center justify-center p-4 text-center">
                <TransitionChild as="template" enter='transform transition ease-in-out duration-500 sm:duration-700' enterFrom='translate-x-full' enterTo='translate-x-0' leave='transform transition ease-in-out duration-500 sm:duration-700' leaveFrom='translate-x-0' leaveTo='translate-x-full'>
                    <DialogPanel class="fixed w-[550px] top-0 h-full right-0 z-40 transform overflow-hidden rounded-md bg-white p-6 text-left align-middle shadow-xl transition-all">
                        <DialogTitle as="h3" class="font-medium leading-6 ml-2 font-base text-xl">
                            New shipment
                        </DialogTitle>
                        <p class="font-base text-gray-500 ml-2 mt-3">Enter shipment's details below</p>
                        <div class="mt-12 ml-3">
                            <form class="flex text-xs font-base flex-col gap-6">
                                <div class="flex flex-col gap-1">
                                    <label for="truck">Truck</label>
                                    <select v-model="shipment.truck" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base">
                                        <option v-for="truck in trucks" :value="truck.id">{{ truck.registration_number }} - {{ truck.manufacturer }} {{ truck.model }}</option>
                                    </select>
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="driver">Driver</label>
                                    <select v-model="shipment.driver" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base">
                                        <option v-for="driver in drivers" :value="driver.id">{{ driver.first_name }} {{ driver.last_name }}</option>
                                    </select>
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="location">Route start</label>
                                    <select v-model="shipment.route_from" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 font-base">
                                    <option v-for="location in locations" :value="location.id">{{ location.name }}</option>
                                    </select>
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="location">Route end</label>
                                    <select v-model="shipment.route_to" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 font-base">
                                    <option v-for="location in locations" :value="location.id">{{ location.name }}</option>
                                    </select>
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="departure">Departure</label>
                                    <input v-model="shipment.departure_date" type="date" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="E.g Iveco ">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="arrival">Arrival</label>
                                    <input v-model="shipment.arrival_date" type="date" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="E.g Iveco ">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="status">Status</label>
                                    <select v-model="shipment.status" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="Brown">
                                        <option value="READY">Ready</option>
                                        <option value="ON WAY">On way</option>
                                        <option value="DELAYED">Delayed</option>
                                        <option value="ARRIVED">Arrived</option>
                                    </select>
                                </div>

                                <div>
                                    <button @click.prevent="submitNewShipment" class="bg-violet-600 w-full text-center font-base text-white py-2 px-4 rounded-md">
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
    mapActions,
    mapGetters
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
            shipment: {
                truck: "",
                driver: "",
                destination: "",
                departure_date: "",
                arrival_date: "",
                status: "READY",
                route_from: "",
                route_to: "",
                parcels: []
            }
        }
    },
    computed: {
        ...mapGetters({
            storedTrucks: 'getStoredTrucks',
            storedDrivers: 'getStoredDrivers',
            storedLocations: 'getStoredLocations'
        }),
        trucks() {
            return this.storedTrucks
        },
        drivers() {
            return this.storedDrivers
        },
        locations() {
            return this.storedLocations
        }
    },
    methods: {
        ...mapActions({
            createShipment: 'createShipment',
            getAllTrucks: 'getAllTrucks',
            getAllDrivers: 'getAllDrivers',
            getAllLocations: 'getAllLocations',
        }),
        resetForm() {
            this.shipment.truck = ""
            this.shipment.driver = ""
            this.shipment.destination = ""
            this.shipment.departure_date = ""
            this.shipment.arrival_date = ""
            this.shipment.status = "READY"
            this.shipment.route_from = ""
            this.shipment.route_to = ""
            this.shipment.parcels = []
        },
        submitNewShipment() {
            this.createShipment({
                payload: this.shipment,
                cb: (() => {
                    this.closeModal()
                    this.emitter.emit("reloadShipments", "add")
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
        this.getAllTrucks({
            cb: () => {}
        })
        this.getAllDrivers({
            cb: () => {}
        })
        this.getAllLocations({
            cb: () => {}
        })
    }
}
</script>
