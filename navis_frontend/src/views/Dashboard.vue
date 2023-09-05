<template>
<div class="flex">
    <Aside />
    <div class="w-10/12">
        <div class="pl-6 pr-6 font-base">
            <Search />
            <h1 class="text-2xl mt-5 font-extrabold">Overview</h1>
            <div class="grid grid-cols-4 mt-5 gap-5">
                <div class="bg-white flex justify-between items-center h-24 rounded-md">
                    <div class="ml-5">
                        <p class="text-gray-400 text-sm">New packages</p>
                        <h3 class="text-2xl mt-1">222</h3>
                    </div>
                    <div class="mr-5">
                        <span class="bg-[#f1f1fb] px-3 py-2.5 rounded-full">
                            🤞🏿
                        </span>
                    </div>
                </div>

                <div class="bg-white flex justify-between items-center h-24 rounded-md">
                    <div class="ml-5">
                        <p class="text-gray-400 text-sm">Ready for shipping </p>
                        <h3 class="text-2xl mt-1">60</h3>
                    </div>
                    <div class="mr-5">
                        <span class="bg-[#f1f1fb] px-3 py-2.5 rounded-full">
                            📦
                        </span>
                    </div>
                </div>
                <div class="bg-white flex justify-between items-center h-24 rounded-md">
                    <div class="ml-5">
                        <p class="text-gray-400 text-sm">In transit</p>
                        <h3 class="text-2xl mt-1">2000</h3>
                    </div>
                    <div class="mr-5">
                        <span class="bg-[#f1f1fb] px-3 py-2.5 rounded-full">
                            🚛
                        </span>
                    </div>
                </div>
                <div class="bg-white flex justify-between items-center h-24 rounded-md">
                    <div class="ml-5">
                        <p class="text-gray-400 text-sm">Delivered</p>
                        <h3 class="text-2xl mt-1">3600</h3>
                    </div>
                    <div class="mr-5">
                        <span class="bg-[#f1f1fb] px-3 py-2.5 rounded-full">
                            🚀
                        </span>
                    </div>
                </div>
            </div>
            <div class="grid mt-8 font-base grid-cols-2 gap-y-4 gap-4">
                <div class="bg-white rounded-md h-64">
                    <div class="flex justify-between items-center mr-3 ml-3 mt-2">
                        <h3 class="text-xl font-base font-bold">Delayed delivery</h3>
                        <a href="" class="text-xs flex gap-1 text-violet-600">Show all <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                            </svg>
                        </a>
                    </div>
                    <div class="font-base mt-3 mr-3 ml-3 rounded-md overflow-x-auto">
                        <table class="w-full text-sm text-left text-gray-500">
                            <thead class="text-xs text-gray-950 uppercase bg-[#f1f1fb]  font-base">
                                <tr>
                                    <th scope="col" class="px-6 py-3">
                                        destination
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        truck
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        arrival time
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        time delay
                                    </th>

                                </tr>
                            </thead>
                            <tbody class="">
                                <tr class="bg-white text-xs font-base border-b">
                                    <th scope="row" class="px-6 py-4 font-medium text-gray-950 whitespace-nowrap">
                                        Kericho - Bomet
                                    </th>

                                    <td class="px-6 py-4">
                                        Iveco 80E18
                                    </td>
                                    <td class="px-6 py-4">
                                        07:05AM
                                    </td>
                                    <td class="px-6 py-4">
                                        <span class="bg-pink-200 text-pink-700 px-2 py-0.5 rounded">5:05 h</span>
                                    </td>

                                </tr>
                                <tr class="bg-white text-xs font-base border-b">
                                    <th scope="row" class="px-6 py-4 font-medium text-gray-950 whitespace-nowrap">
                                        Kericho - Bomet
                                    </th>

                                    <td class="px-6 py-4">
                                        Iveco 80E18
                                    </td>
                                    <td class="px-6 py-4">
                                        07:05AM
                                    </td>
                                    <td class="px-6 py-4">
                                        <span class="bg-pink-200 text-pink-700 px-2 py-0.5 rounded">5:05 h</span>
                                    </td>

                                </tr>
                                <tr class="bg-white text-xs font-base border-b">
                                    <th scope="row" class="px-6 py-4 font-medium text-gray-950 whitespace-nowrap">
                                        Kericho - Bomet
                                    </th>

                                    <td class="px-6 py-4">
                                        Iveco 80E18
                                    </td>
                                    <td class="px-6 py-4">
                                        07:05AM
                                    </td>
                                    <td class="px-6 py-4">
                                        <span class="bg-pink-200 text-pink-700 px-2 py-0.5 rounded">5:05 h</span>
                                    </td>

                                </tr>

                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="bg-white rounded-md h-64">
                    <div class="mt-2 font-base ml-3 mr-3 flex justify-between">
                        <h3 class="text-xl font-bold">Daily plan <span class="text-gray-500 text-xs">Wed 21 Aug</span></h3>
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 text-gray-500 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM12.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM18.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0z" />
                        </svg>

                    </div>
                    <div class="ml-3 mr-3 mt-6 text-sm flex justify-between">
                        <ul class="text-gray-500 flex font-base flex-col gap-5">
                            <li>
                                <p>Shipments processed</p>
                                <p class="text-gray-900">1010/2020</p>
                            </li>
                            <li>
                                <p>Orders processed</p>
                                <p class="text-gray-900">650/1300</p>
                            </li>
                            <li>
                                <p>Requests considered</p>
                                <p class="text-gray-900">10/20</p>
                            </li>

                        </ul>
                        <div class="w-64 mt-32 h-6 bg-gray-200 rounded-full">
                            <div class="h-6 bg-emerald-500 rounded-full" style="width: 50%"></div>
                        </div>
                    </div>
                </div>
                <div class="bg-white rounded-md">
                    <div class="flex justify-between items-center mr-3 ml-3 mt-1">
                        <h3 class="text-xl font-base font-bold">Available trucks</h3>
                        <a href="" class="text-xs flex gap-1 text-violet-600">Show all <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                            </svg>
                        </a>
                    </div>
                    <ul class="flex flex-col font-base gap-2 divide-y ml-3 mr-3 mt-2">
                        <li class="flex justify-between">
                            <div>
                                <h3 class=" text-sm">Iveco 80E18</h3>
                                <p class="text-gray-500 text-xs">Destination Kericho - Narok</p>
                            </div>
                            <div class="flex flex-col gap-2 items-center">
                                <p class="text-gray-500 text-sm"> <span class="text-red-600">90</span>/100%</p>
                                <div class="w-32 bg-gray-200 rounded-full h-1.5 mb-4">
                                    <div class="bg-red-600 h-1.5 rounded-full" style="width: 90%"></div>
                                </div>
                            </div>
                        </li>
                        <li class="flex justify-between pb-0.5">
                            <div>
                                <h3 class=" text-sm">Iveco 80E18</h3>
                                <p class="text-gray-500 text-xs">Destination Kericho - Narok</p>
                            </div>
                            <div class="flex flex-col gap-2 items-center">
                                <p class="text-gray-500 text-sm"> <span class="text-red-600">90</span>/100%</p>
                                <div class="w-32 bg-gray-200 rounded-full h-1.5 mb-4">
                                    <div class="bg-red-600 h-1.5 rounded-full" style="width: 90%"></div>
                                </div>
                            </div>
                        </li>
                        <li class="flex justify-between pb-0.5">
                            <div>
                                <h3 class=" text-sm">Iveco 80E18</h3>
                                <p class="text-gray-500 text-xs">Destination Kericho - Narok</p>
                            </div>
                            <div class="flex flex-col gap-2 items-center">
                                <p class="text-gray-500 text-sm"> <span class="text-red-600">90</span>/100%</p>
                                <div class="w-32 bg-gray-200 rounded-full h-1.5 mb-4">
                                    <div class="bg-red-600 h-1.5 rounded-full" style="width: 90%"></div>
                                </div>
                            </div>
                        </li>
                        <li class="flex justify-between">
                            <div>
                                <h3 class=" text-sm">Iveco 80E18</h3>
                                <p class="text-gray-500 text-xs">Destination Kericho - Narok</p>
                            </div>
                            <div class="flex flex-col gap-2 items-center">
                                <p class="text-gray-500 text-sm"> <span class="text-red-600">90</span>/100%</p>
                                <div class="w-32 bg-gray-200 rounded-full h-1.5 mb-4">
                                    <div class="bg-red-600 h-1.5 rounded-full" style="width: 90%"></div>
                                </div>
                            </div>
                        </li>
                    </ul>
                </div>
                <div class="bg-white rounded-md">
                    <div class="flex justify-between items-center mr-3 ml-3 mt-1">
                        <h3 class="text-xl font-base font-bold">Recent requests</h3>
                        <a href="" class="text-xs flex gap-1 text-violet-600">Show all <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 h-4">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                            </svg>
                        </a>
                    </div>
                    <ul class="flex flex-col font-base gap-2 divide-y ml-3 mr-3 mt-2">
                        <li class="flex justify-between pb-0.5">
                            <div class="flex gap-2">
                                <span class="bg-[#f1f1fb] px-3 py-2 rounded-full">
                                    📦
                                </span>
                                <div>
                                    <h3 class=" text-sm">Parcel redirection</h3>
                                    <p class="text-gray-500 text-xs">Destination Kericho - Narok</p>
                                </div>

                            </div>
                            <p class="text-gray-500 text-xs">1 min ago</p>
                        </li>
                        <li class="flex justify-between py-1">
                            <div class="flex gap-2">
                                <span class="bg-[#f1f1fb] px-3 py-2 rounded-full">
                                    📦
                                </span>
                                <div>
                                    <h3 class=" text-sm">Parcel redirection</h3>
                                    <p class="text-gray-500 text-xs">Destination Kericho - Narok</p>
                                </div>

                            </div>
                            <p class="text-gray-500 text-xs">1 min ago</p>
                        </li>
                        <li class="flex justify-between py-1">
                            <div class="flex gap-2">
                                <span class="bg-[#f1f1fb] px-3 py-2 rounded-full">
                                    📦
                                </span>
                                <div>
                                    <h3 class=" text-sm">Parcel redirection</h3>
                                    <p class="text-gray-500 text-xs">Destination Kericho - Narok</p>
                                </div>

                            </div>
                            <p class="text-gray-500 text-xs">1 min ago</p>
                        </li>
                        <li class="flex justify-between py-1">
                            <div class="flex gap-2">
                                <span class="bg-[#f1f1fb] px-3 py-2 rounded-full">
                                    📦
                                </span>
                                <div>
                                    <h3 class=" text-sm">Parcel redirection</h3>
                                    <p class="text-gray-500 text-xs">Destination Kericho - Narok</p>
                                </div>

                            </div>
                            <p class="text-gray-500 text-xs">1 min ago</p>
                        </li>
                    </ul>
                </div>

            </div>
        </div>

    </div>
</div>
</template>

<script>
import Aside from '@/components/Aside.vue';
import Search from '@/components/Search.vue';

export default {
    name: 'Dashboard',
    components: {
        Aside,
        Search,
    },
    data() {
        return {
            
        }
    },
    mounted() {}
}
</script>

<style>
html {
    background-color: #F1F1FB;
}
</style>
