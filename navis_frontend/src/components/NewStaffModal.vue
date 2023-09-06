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
                        <div class="mt-2 font-base flex flex-col gap-5 justify-center items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-16 h-16 text-violet-600">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>

                            <h3 class="text-xl font-bold">Staff account created:</h3>
                           <div class="flex flex-col gap-1">
                            <p class="text-gray-500">
                                Email: {{ email }}                             
                            </p>
                            <p class="text-gray-500">      
                                Password: {{ password }}
                            </p>
                           </div>
                            <div class="flex text-sm gap-5">
                                <button @click="toggleModal" class="bg-[#F1F1FB] focus:outline-none focus:ring-0 px-12 py-1.5 text-gray-700 rounded-md">Cancel</button>
                                <button @click="copyPassword" class="bg-violet-600 text-white px-6 py-1.5 focus:outline-none focus:ring-0 rounded-md">Copy password</button>
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
            email: "",
            password: "",
        }
    },
    methods: {
        toggleModal() {
            this.isOpen = !this.isOpen
        },
        copyPassword() {
            this.copyStaffPassword()
            this.emitter.emit("reloadStaff", "add")
            this.emitter.emit("closeStaffDrawer")
            this.toggleModal()
        },
        unsecuredCopyToClipboard(text) {
            const textArea = document.createElement("textarea")
            textArea.value = text
            document.body.appendChild(textArea)
            textArea.focus()
            textArea.select()
            try {
                document.execCommand('copy')
            } catch (err) {
                console.error('Unable to copy to clipboard', err)
            }
            document.body.removeChild(textArea)
        },
        copyStaffPassword() {
            if (window.isSecureContext && navigator.clipboard) {
                navigator.clipboard.writeText(this.password)
            } else {
                this.unsecuredCopyToClipboard(this.password)
            }
        },
    },
    mounted() {
        this.emitter.on("showNewStaffModal", data => {
            this.email = data.email
            this.password = data.password
            this.toggleModal()
        })
    }
}
</script>
