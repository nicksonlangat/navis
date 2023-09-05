<template>
<div class="bg-white h-screen w-2/12">
    <div class="pl-4 mt-5 flex gap-3">
        <img src="../assets//logo.jpg" class="h-16 w-16 rounded-full object-cover" alt="">
        <div class="mt-2 text-gray-500 font-base">
            <h1 class="text-violet-600 text-xl font-bold">Navis</h1>
            <p class="text-xs mt-1"> Workspace</p>
        </div>
    </div>
    <ul class="pl-3 mt-10 flex text-sm flex-col gap-3 mr-5 text-gray-500 font-base">
        <li :class="currentRoute === 'requests' ? 'bg-[#F1F1FB] text-gray-900' : ''" class="flex w-full rounded-md px-4 gap-2 hover:bg-[#F1F1FB] group hover:text-gray-900 cursor-pointer transition-all duration-500 py-2">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 group-hover:text-violet-500 ">
                <path stroke-linecap="round" stroke-linejoin="round" d="M11.25 11.25l.041-.02a.75.75 0 011.063.852l-.708 2.836a.75.75 0 001.063.853l.041-.021M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9-3.75h.008v.008H12V8.25z" />
            </svg>

            Requests
            <span class="bg-[#f1f1fb] text-gray-500 h-5 w-6 text-center ml-5 rounded">10</span>
        </li>
        <li :class="currentRoute === 'notifications' ? 'bg-[#F1F1FB] text-gray-900' : ''" class="flex w-full rounded-md px-4 gap-2 hover:bg-[#F1F1FB] group hover:text-gray-900 cursor-pointer transition-all duration-500 py-2">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 group-hover:text-violet-500 ">
                <path stroke-linecap="round" stroke-linejoin="round" d="M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0" />
            </svg>

            Notifications
            <span class="bg-[#f1f1fb] text-gray-500 h-5 w-6 text-center ml-5 rounded">1</span>
        </li>
    </ul>
    <hr class="mt-10">

    <ul class="pl-3 mt-10 flex text-sm flex-col gap-3 text-gray-500 font-base mr-5">
        <li :class="currentRoute === 'dashboard' ? 'bg-[#F1F1FB] text-gray-900' : ''" @click="navigateToPage('dashboard')" class="flex w-full rounded-md px-4 gap-2 hover:bg-[#F1F1FB] group hover:text-gray-900 cursor-pointer transition-all duration-500 py-2">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" :class="currentRoute === 'dashboard' ? 'text-violet-500' : ''" class="w-5 group-hover:text-violet-500 h-5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
            </svg>

            Dashboard</li>
        <li :class="currentRoute === 'shipments' ? 'bg-[#F1F1FB] text-gray-900' : ''" @click="navigateToPage('shipments')" class="flex w-full rounded-md px-4 gap-2 hover:bg-[#F1F1FB] group hover:text-gray-900 cursor-pointer transition-all duration-500 py-2">
            <svg :class="currentRoute === 'shipments' ? 'text-violet-500' : ''" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 group-hover:text-violet-500 ">
                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 18.75a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m3 0h6m-9 0H3.375a1.125 1.125 0 01-1.125-1.125V14.25m17.25 4.5a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m3 0h1.125c.621 0 1.129-.504 1.09-1.124a17.902 17.902 0 00-3.213-9.193 2.056 2.056 0 00-1.58-.86H14.25M16.5 18.75h-2.25m0-11.177v-.958c0-.568-.422-1.048-.987-1.106a48.554 48.554 0 00-10.026 0 1.106 1.106 0 00-.987 1.106v7.635m12-6.677v6.677m0 4.5v-4.5m0 0h-12" />
            </svg>

            Shipments</li>
        <li :class="currentRoute === 'parcels' ? 'bg-[#F1F1FB] text-gray-900' : ''" @click="navigateToPage('parcels')" class="flex w-full rounded-md px-4 gap-2 hover:bg-[#F1F1FB] group hover:text-gray-900 cursor-pointer transition-all duration-500 py-2">
            <svg :class="currentRoute === 'parcels' ? 'text-violet-500' : ''" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 group-hover:text-violet-500 ">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6.429 9.75L2.25 12l4.179 2.25m0-4.5l5.571 3 5.571-3m-11.142 0L2.25 7.5 12 2.25l9.75 5.25-4.179 2.25m0 0L21.75 12l-4.179 2.25m0 0l4.179 2.25L12 21.75 2.25 16.5l4.179-2.25m11.142 0l-5.571 3-5.571-3" />
            </svg>

            Parcels
            <span class="bg-red-500 text-white h-5 w-5 text-center ml-5 rounded">2</span>
        </li>
        <li :class="currentRoute === 'drivers' ? 'bg-[#F1F1FB] text-gray-900' : ''" @click="navigateToPage('drivers')" class="flex w-full rounded-md px-4 gap-2 hover:bg-[#F1F1FB] group hover:text-gray-900 cursor-pointer transition-all duration-500 py-2">
            <svg :class="currentRoute === 'drivers' ? 'text-violet-500' : ''" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 group-hover:text-violet-500 ">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
            </svg>

            Drivers</li>
        <li :class="currentRoute === 'trucks' ? 'bg-[#F1F1FB] text-gray-900' : ''" @click="navigateToPage('trucks')" class="flex w-full rounded-md px-4 gap-2 hover:bg-[#F1F1FB] group hover:text-gray-900 cursor-pointer transition-all duration-500 py-2">

            <svg :class="currentRoute === 'trucks' ? 'text-violet-500' : ''" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 group-hover:text-violet-500 ">
                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 18.75a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m3 0h6m-9 0H3.375a1.125 1.125 0 01-1.125-1.125V14.25m17.25 4.5a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m3 0h1.125c.621 0 1.129-.504 1.09-1.124a17.902 17.902 0 00-3.213-9.193 2.056 2.056 0 00-1.58-.86H14.25M16.5 18.75h-2.25m0-11.177v-.958c0-.568-.422-1.048-.987-1.106a48.554 48.554 0 00-10.026 0 1.106 1.106 0 00-.987 1.106v7.635m12-6.677v6.677m0 4.5v-4.5m0 0h-12" />
            </svg>

            Trucks</li>
        <li :class="currentRoute === 'clients' ? 'bg-[#F1F1FB] text-gray-900' : ''" @click="navigateToPage('clients')" class="flex w-full rounded-md px-4 gap-2 hover:bg-[#F1F1FB] group hover:text-gray-900 cursor-pointer transition-all duration-500 py-2">
            <svg :class="currentRoute === 'clients' ? 'text-violet-500' : ''" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 group-hover:text-violet-500 ">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
            </svg>

            Clients</li>
    </ul>
    <div class="pl-5 font-base w-full mt-20">

        <NewShipmentDrawer />
    </div>
    <hr class="mt-8">
    <div class="pl-4 mt-4 font-base flex justify-between mr-5">
        <img src="../assets//user.jpeg" class="h-10 w-10 rounded-full object-cover" alt="">
        <div class="text-gray-500 font-base">
            <h1 class="text-gray-700">Nick Adams</h1>
            <p class="text-xs"> Manager</p>
        </div>
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 mt-1 cursor-pointer">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z" />
        </svg>

    </div>

</div>
</template>

<script>
import NewShipmentDrawer from './NewShipmentDrawer.vue'
export default {
    components: {
        NewShipmentDrawer
    },
    data() {
        return {
            currentRoute: null,
        }
    },
    methods: {
        navigateToPage(page) {
            this.$router.push({
                "name": page
            })
        }
    },
    mounted() {
        this.currentRoute = this.$route.name
    }
}
</script>
