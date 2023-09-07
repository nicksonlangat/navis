<template>
<TransitionRoot appear :show="isOpen" as="template">
    <Dialog as="div" @close="toggleModal" class="relative z-10">
        <TransitionChild as="template" enter="duration-300 ease-out" enter-from="opacity-0" enter-to="opacity-100" leave="duration-200 ease-in" leave-from="opacity-100" leave-to="opacity-0">
            <div class="fixed inset-0 bg-black bg-opacity-25" />
        </TransitionChild>
        <div class="fixed inset-0 overflow-y-auto">
            <div class="flex min-h-full items-center justify-center p-4 text-center">
                <TransitionChild as="template" enter="duration-300 ease-out" enter-from="opacity-0 scale-95" enter-to="opacity-100 scale-100" leave="duration-200 ease-in" leave-from="opacity-100 scale-100" leave-to="opacity-0 scale-95">
                    <DialogPanel class="w-full max-w-lg transform overflow-hidden rounded-md bg-white p-6 text-left align-middle shadow-xl transition-all">
                        <div class="flex justify-end">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" @click="toggleModal" class="w-8 hover:bg-[#F1F1FB] transition-all duration-300 rounded-full h-8 text-gray-500 cursor-pointer">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                            </svg>

                        </div>
                        <div class=" font-base flex flex-col gap-5 justify-center items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-16 text-red-500 h-16">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M9.879 7.519c1.171-1.025 3.071-1.025 4.242 0 1.172 1.025 1.172 2.687 0 3.712-.203.179-.43.326-.67.442-.745.361-1.45.999-1.45 1.827v.75M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9 5.25h.008v.008H12v-.008z" />
                            </svg>
                            <h3 class="text-2xl font-bold">Remove {{ type }} ?</h3>
                            <p class="text-gray-500 text-center">Are you sure you want to remove <span class="text-violet-600 underline">{{ data }}</span> from the system?</p>
                          <div class="flex text-sm gap-5">
                            <button @click="toggleModal" class="bg-[#F1F1FB] focus:outline-none focus:ring-0 px-12 py-1.5 text-gray-700 rounded-md">Cancel</button>
                            <button @click="confirmDeletion" class="bg-red-500 text-white px-6 py-1.5 focus:outline-none focus:ring-0 rounded-md">Yes, remove</button>
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
        DialogTitle,
    },
    data() {
        return {
            isOpen: false,
            type: "",
            data: "",
            id: null
        }
    },
    methods: {
        toggleModal() {
            this.isOpen = !this.isOpen
        },
        confirmDeletion() {
            if(this.type === "Driver") {
                this.deleteDriver()
            }
            else if(this.type === "Truck") {
                this.deleteTruck()
            }
            else if(this.type === "Client") {
                this.deleteClient()
            }
            else if(this.type === "Parcel") {
                this.deleteParcel()
            }
            else if(this.type === "Shipment") {
                this.deleteShipment()
            }
            else if(this.type === "Staff") {
                this.deleteStaff()
            }
            this.toggleModal()
        },
        deleteClient() {
            this.emitter.emit("deleteClient", this.id)
        },
        deleteDriver() {
            this.emitter.emit("deleteDriver", this.id)
        },
        deleteTruck() {
            this.emitter.emit("deleteTruck", this.id)
        },
        deleteParcel() {
            this.emitter.emit("deleteParcel", this.id)
        },
        deleteShipment() {
            this.emitter.emit("deleteShipment", this.id)
        },
        deleteStaff() {
            this.emitter.emit("deleteStaff", this.id)
        }
    },
    mounted() {
        this.emitter.on("showDeleteModal", data => {
            this.type = data.type
            this.data = data.value
            this.id = data.id
            this.toggleModal()
        })
    }
}
</script>
