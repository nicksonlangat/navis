<template>
<svg v-if="!isOpen" @click="openModal" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-8 h-8">
    <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
</svg>

<TransitionRoot appear :show="isOpen" as="template">
    <Dialog as="div" @close="closeModal" class="relative z-10">

        <div class="fixed inset-0 overflow-y-auto">
            <div class="flex min-h-full text-center">
                <TransitionChild as="template" enter='transform transition ease-in-out duration-500 sm:duration-700' enterFrom='translate-x-full' enterTo='translate-x-0' leave='transform transition ease-in-out duration-500 sm:duration-700' leaveFrom='translate-x-0' leaveTo='translate-x-full'>
                    <DialogPanel class="w-full max-w-lg transform overflow-hidden font-base bg-white text-gray-500 p-6 text-left align-middle shadow-xl transition-all">

                        <div class="mt-2 font-base">
                            <div class="flex justify-between items-center">
                                <h1 class="text-violet-600 text-4xl font-bold">Navis</h1>
                                <svg v-if="isOpen" size="32" @click="closeModal" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-8 h-8">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                                </svg>
                            </div>
                            <div class="mt-5 flex flex-col gap-3 text-xl">
                                <a href=""></a>
                                <a href="/shipments">Shipments</a>
                                <a href="/parcels">Parcels</a>
                                <a href="/clients">Clients</a>
                                <a href="/drivers">Drivers</a>
                                <a href="/trucks">Trucks</a>
                                <a href="/staff">Staff</a>
                                <a href="/account">My account</a>
                            </div>

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
export default {
    components: {
        TransitionRoot,
        TransitionChild,
        Dialog,
        DialogPanel,
        DialogTitle
    },
    data() {
        return {
            isOpen: false,
            currentPage: "",

        }
    },
    methods: {
        closeModal() {
            this.isOpen = false
        },
        openModal() {
            this.isOpen = true
        }
    },
    mounted() {
        this.currentPage = this.$route.name
    }
}
</script>

<style>
html {
    scroll-behavior: smooth;
}
</style>
