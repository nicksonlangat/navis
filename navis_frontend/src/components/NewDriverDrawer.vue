<template>
<div class="">
    <button @click="openModal" class="bg-violet-600 flex gap-1 text-sm text-white py-2 px-12 rounded-md">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
        </svg>
        New driver
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
                                New driver
                            </DialogTitle>
                            <svg @click="closeModal" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 font-base cursor-pointer h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </div>

                        <p class="font-base text-gray-500 ml-2 mt-3">Enter driver's details below</p>
                        <div class="mt-5 ml-3">
                            <form class="flex text-sm font-base flex-col gap-6">
                                <div class="flex flex-col gap-1">
                                    <label for="first_name">First name</label>
                                    <input v-model="driver.first_name" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-400 shadow-sm font-base" placeholder="E.g Daniel ">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="last_name">Last name</label>
                                    <input v-model="driver.last_name" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-400 shadow-sm font-base" placeholder="E.g Smith ">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="email">Email</label>
                                    <input v-model="driver.email" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-400 shadow-sm font-base" placeholder="E.g danielsmith@acme.com ">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="phone_number">Phone number</label>
                                    <input v-model="driver.phone_number" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-400 shadow-sm font-base" placeholder="E.g 0712345675 ">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="id_number">Id number</label>
                                    <input v-model="driver.identity_number" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-400 shadow-sm font-base" placeholder="E.g 22776544 ">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="licence_number">Licence number</label>
                                    <input v-model="driver.licence_number" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-400 shadow-sm font-base" placeholder="E.g 14564312 ">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="kra_pin">KRA pin</label>
                                    <input v-model="driver.kra_pin" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-400 shadow-sm font-base" placeholder="E.g A02567975U ">
                                </div>
                                <div>
                                    <button @click.prevent="submitNewDriver" class="bg-violet-600 w-full text-center font-base text-white py-2 px-4 rounded-md">
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
            driver: {
                first_name: "",
                last_name: "",
                email: "",
                phone_number: "",
                identity_number: "",
                licence_number: "",
                kra_pin: ""
            }
        }
    },
    methods: {
        ...mapActions({
            createDriver: 'createDriver',
        }),
        resetForm() {
            this.driver.first_name = ""
            this.driver.last_name = ""
            this.driver.email = ""
            this.driver.phone_number = ""
            this.driver.identity_number = ""
            this.driver.licence_number = ""
            this.driver.kra_pin = ""
        },
        submitNewDriver() {
            this.createDriver({
                payload: this.driver,
                cb: (() => {
                    this.closeModal()
                    this.emitter.emit("reloadDrivers", "add")
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
    mounted() {}
}
</script>
