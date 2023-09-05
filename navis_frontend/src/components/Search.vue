<template>
     <div class="bg-white h-12 flex items-center justify-between rounded-md mt-5">
                <div class="relative ml-5">
                    <input class=" pl-6 w-56 focus:outline-none font-base text-xs placeholder:text-xs" type="text" placeholder="Search by tracking number">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 text-gray-400 absolute top-0.5 h-5">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                    </svg>
                </div>
                
           
    <div class="flex gap-4 text-xs items-center mr-5 font-base">
                    <div class="ml-12 w-44">
                        <Listbox v-model="selectedStatus">
                            <div class="relative mt-1">
                                <ListboxButton class="relative w-full cursor-default rounded bg-[#f1f1fb] py-2 pl-3 pr-10 text-left focus:outline-none focus-visible:border-indigo-500 focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75 focus-visible:ring-offset-2 focus-visible:ring-offset-orange-300 sm:text-sm">
                                    <span class="block truncate text-xs">{{ selectedStatus?.name }}</span>
                                    <span class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-2">
                                        <ChevronUpDownIcon class="h-5 w-5 text-gray-400" aria-hidden="true" />
                                    </span>
                                </ListboxButton>

                                <transition leave-active-class="transition duration-100 ease-in" leave-from-class="opacity-100" leave-to-class="opacity-0">
                                    <ListboxOptions class="absolute mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm">
                                        <ListboxOption v-slot="{ active, selected }" v-for="person in people" :key="person.name" :value="person" as="template">
                                            <li :class="[
                  active ? 'bg-amber-100 text-amber-900' : 'text-gray-900',
                  'relative cursor-default select-none py-2 pl-10 pr-4',
                ]">
                                                <span :class="[
                    selected ? 'font-medium' : 'font-normal',
                    'block truncate',
                  ]">{{ person.name }}</span>
                                                <span v-if="selected" class="absolute inset-y-0 left-0 flex items-center pl-3 text-amber-600">
                                                    <CheckIcon class="h-5 w-5" aria-hidden="true" />
                                                </span>
                                            </li>
                                        </ListboxOption>
                                    </ListboxOptions>
                                </transition>
                            </div>
                        </Listbox>
                    </div>
                    
                    <h3 class="text-gray-600">Sunday, 20 August, 09:25</h3>
                </div>
                </div>
</template>
<script>
import {
    Listbox,
    ListboxLabel,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
} from '@headlessui/vue'
import {
    CheckIcon,
    ChevronUpDownIcon
} from '@heroicons/vue/20/solid'

export default {
    name: 'Search',
    components: {
        Listbox,
        ListboxLabel,
        ListboxButton,
        ListboxOptions,
        ListboxOption,
        CheckIcon,
        ChevronUpDownIcon
    },
    data() {
        return {
            selectedStatus: null,
            people: [
                {
                    name: 'Filter by status'
                },
                {
                    name: 'Ready'
                },
                {
                    name: 'On way'
                },
                {
                    name: 'Delayed'
                },
                {
                    name: 'Arrived'
                }
            ]
        }
    },
    mounted() {
        this.selectedStatus = this.people[0]
    }
}
</script>

<style>
html {
    background-color: #F1F1FB;
}
</style>
