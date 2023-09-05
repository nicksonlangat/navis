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
                            {{ client?.first_name }}  {{ client?.last_name }}
                        </DialogTitle>
                         </div>
                        <div class="mt-2">
                            <form class="flex text-xs font-base flex-col gap-3">
                                <div class="flex flex-col gap-1">
                                    <label for="first_name">First name</label>
                                    <input v-model="client.first_name" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="E.g James ">
                                   
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="last_name">Last name</label>
                                    <input v-model="client.last_name" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="E.g Brown">
                                    
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="email">Email</label>
                                    <input v-model="client.email" type="email" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="E.g jamesbrown@acme.com">
                                   
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="phone_number">Phone number</label>
                                    <input v-model="client.phone_number" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="E.g 0712345765">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="identity_number">Identity number</label>
                                    <input v-model="client.identity_number" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 placeholder:text-gray-500 font-base" placeholder="E.g 22886544">
                                </div>
                                <div class="flex flex-col gap-1">
                                    <label for="location">Location</label>
                                    <select v-model="client.location" type="text" class="bg-white border border-gray-200 focus:outline-none focus:right-0 py-2 rounded-md pl-3 font-base">
                                    <option v-for="location in locations" :value="location.id">{{ location.name }}</option>
                                    </select>
                                </div>
                                <div>
                                    <button @click.prevent="updateClientDetails" class="bg-violet-600 w-full text-center font-base text-white py-2 px-4 rounded-md">
                                        Update client
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
            client: {
                first_name: "",
                last_name: "",
                email: "",
                phone_number: "",
                identity_number: "",
                location: "",
            }
        }
    },
    computed: {
        ...mapGetters({
            storedLocations: 'getStoredLocations'
        }),
        locations() {
            return this.storedLocations
        }
    },
    methods: {
        ...mapActions({
            updateClient: 'updateClient',
            deleteClient: 'deleteClient',
            getAllLocations: 'getAllLocations',
        }),
        toggleModal() {
            this.isOpen = !this.isOpen
        },
        updateClientDetails() {
            this.updateClient({
                uuid: this.client.id,
                payload: this.client,
                cb: (() => {
                    this.toggleModal()
                    this.emitter.emit("reloadClients", "edit")
                })
            })
        }
    },
    mounted() {
        this.emitter.on("showClientModal", value => {
            this.client = value
            this.toggleModal()
        })
        this.getAllLocations({
            cb: () => {}
        })
    }
}
</script>
