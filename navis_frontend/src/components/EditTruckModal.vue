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
                                Truck {{truck?.registration_number}}
                            </DialogTitle>
                                 </div>
                        <div class="mt-2">
                            <form class="flex text-xs font-base flex-col gap-3">
                                <div class="flex flex-col gap-1">
                                    <label for="manufacturer">Manufacturer</label>
                                    <input v-model="truck.manufacturer" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="E.g Iveco ">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="model">Model</label>
                                    <input v-model="truck.model" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="E.g 80E18 ">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="yom">Year of manufacture</label>
                                    <input v-model="truck.yom" type="date" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="E.g Iveco ">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="chasis_number">Chasis number</label>
                                    <input v-model="truck.chasis_number" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="E.g KYEG566543 ">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="registration_number">Registration number</label>
                                    <input v-model="truck.registration_number" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="E.g KDL 654R ">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="engine_size">Engine size</label>
                                    <input v-model="truck.engine_size" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="E.g 3000 CC ">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="engine_power">Engine power</label>
                                    <input v-model="truck.engine_power" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="E.g 530 HP ">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="weight">Carry weight</label>
                                    <input v-model="truck.carry_weight" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="E.g 120000 KGS ">   
                                </div>
                                <div>
                                    <button @click.prevent="updateTruckDetails" class="bg-violet-600 w-full text-center font-base text-white py-2 px-4 rounded-md">
                                        Update truck
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
    mapActions
} from 'vuex'

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
            truck: {
                manufacturer: "",
                model: "",
                chasis_number: "",
                registration_number: "",
                engine_size: "",
                engine_power: "",
                yom: "",
                carry_weight: "",
            }

        }
    },
    methods: {
        ...mapActions({
            updateTruck: 'updateTruck',
            deleteTruck: 'deleteTruck',
        }),
        toggleModal() {
            this.isOpen = !this.isOpen
        },
        updateTruckDetails() {
            this.updateTruck({
                uuid: this.truck.id,
                payload: this.truck,
                cb: (res => {
                    this.toggleModal()
                    this.emitter.emit("reloadTrucks", "edit")
                })
            })
        }
    },
    mounted() {
        this.emitter.on("showTruckModal", value => {
            this.truck = value
            this.toggleModal()
        })
    }
}
</script>
