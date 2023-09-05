<template>
<div class="">
    <button @click="openModal" class="bg-violet-600 flex gap-1 text-xs text-white py-1.5 px-4 rounded-md">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
        </svg>
        New truck
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
                                New truck
                            </DialogTitle>
                            <svg @click="closeModal" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 font-base cursor-pointer h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </div>

                        <p class="font-base text-gray-500 ml-2 mt-3">Enter truck's details below</p>
                        <div class="mt-8 ml-3">
                            <form class="flex text-xs font-base flex-col gap-6">
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
                                    <button @click.prevent="submitNewTruck" class="bg-violet-600 w-full text-center font-base text-white py-2 px-4 rounded-md">
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
    mapActions
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
            truck: {
                manufacturer: "",
                model: "",
                chasis_number: "",
                registration_number: "",
                engine_size: "",
                engine_power: "",
                yom: "",
                carry_weight: ""
            }
        }
    },
    methods: {
        ...mapActions({
            createTruck: 'createTruck',
        }),
        submitNewTruck() {
            this.createTruck({
                payload: this.truck,
                cb: (res => {
                    this.closeModal()
                    this.emitter.emit("reloadTrucks")
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
    mounted() {}
}
</script>
