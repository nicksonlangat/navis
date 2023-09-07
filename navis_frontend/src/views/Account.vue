<template>
    <div class="flex">
        <Aside />
        <div class="w-10/12">
            <div class="pl-6 pr-6 font-base">
                <div class="flex font-base mt-5 justify-between">
                    <div class="flex gap-4 items-center">
                        <h1 class="text-2xl font-extrabold">Staff</h1>
                        <div class="relative ml-5">
                            <input v-model="text" class="pl-8 w-72 bg-white py-2 rounded-md focus:outline-none font-base text-sm placeholder:text-xs" type="text" placeholder="Search staff by identity number">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 text-gray-400 absolute top-2 left-2 h-5">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                            </svg>
                        </div>
                    </div>
                    <div class="flex gap-4 items-center">
                        <div>
                            <NewStaffDrawer />
                            <EditStaffModal />
                            <DeleteModal/>
                            <Notification/>
                        </div>
                    </div>
                </div>
                <div class="font-base mt-5 rounded-md overflow-x-auto">
                    <table v-if="staff.length" class="w-full text-sm text-left text-gray-500">
                        <thead class="text-xs text-gray-950 uppercase bg-white border-b font-base">
                            <tr>
                                <th scope="col" class="px-6 py-3">
                                    full name
                                </th>
    
                                <th scope="col" class="px-6 py-3">
                                    email
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    phone number
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    id
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    role
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    kra pin
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    action
                                </th>
                            </tr>
                        </thead>
                        <tbody class="">
                            <tr v-for="user in staff" class="bg-white text-xs font-base border-b">
                                <th scope="row" class="px-6 py-4 font-medium text-gray-950 whitespace-nowrap">
                                    {{ user.first_name }} {{ user.last_name }}
                                </th>
    
                                <td class="px-6 py-4">
                                    {{ user.email }}
                                </td>
                                <td class="px-6 py-4">
                                    {{ user.phone_number }}
                                </td>
                                <td class="px-6 py-4">
                                    {{ user.id_number }}
                                </td>
                                <td class="px-6 py-4">
                                    {{ user.role }}
                                </td>
                               
                                <td class="px-6 py-4">
                                    {{ user.kra_pin }}
                                </td>
                                <td class="px-6 py-4 flex gap-4">
                                    <svg @click="editStaff(user)" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 text-gray-500 cursor-pointer hover:text-violet-500 transition-all duration-300 h-4">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L6.832 19.82a4.5 4.5 0 01-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 011.13-1.897L16.863 4.487zm0 0L19.5 7.125" />
                                    </svg>
                                    <svg @click="removeStaf(user)" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-4 text-gray-500 cursor-pointer hover:text-red-500 transition-all duration-300 h-4">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                                    </svg>
    
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <div v-else>
                        <EmptyIllustration data="staff" />
                    </div>
                </div>
            </div>
        </div>
    </div>
    </template>
    <script>
    import Aside from '@/components/Aside.vue';
    import NewStaffDrawer from '@/components/NewStaffDrawer.vue';
    import EditStaffModal from '@/components/EditStaffModal.vue';
    import EmptyIllustration from '@/components/EmptyIllustration.vue';
    import DeleteModal from '@/components/DeleteModal.vue';
    import {
        mapActions,
        mapGetters
    } from 'vuex';
    import moment from "moment"
    import Notification from '@/components/Notification.vue';
    export default {
        name: 'Staff',
        components: {
            Aside,
            NewStaffDrawer,
            EditStaffModal,
            EmptyIllustration,
            DeleteModal,
            Notification
        },
        data() {
            return {
                text: "",
                item: "Staff"
            }
        },
        computed: {
            ...mapGetters({
                storedStaff: 'getStoredStaff'
            }),
            staff() {
                return this.storedStaff
            }
        },
        methods: {
            ...mapActions({
                getAllStaff: 'getAllStaff',
                deleteStaff: 'deleteStaff',
            }),
            init() {
                this.getAllStaff({
                    cb: () => {}
                })
            },
            formatDate(date) {
                return moment(date).format("MMM Do YY")
            },
            editStaff(staff) {
                this.emitter.emit("showStaffModal", staff)
            },
            removeStaf(staff) {
                this.emitter.emit("showDeleteModal", {"type": "Staff", "value": staff.email, "id": staff.id} )
            },
            deleteConfirmedStaff(id) {
                this.deleteStaff({
                    uuid: id,
                    cb: (() => {
                        this.init()
                    })
                })
            }
        },
        mounted() {
            this.init()
            this.emitter.on("reloadStaff", value => {
                this.init()
                if(value === "edit"){
                    this.emitter.emit("showNotification", {
                    "action": "edit",
                    "item": this.item
                })
                }
                else if(value === "add") {
                    this.emitter.emit("showNotification", {
                    "action": "add",
                    "item": this.item
                })
                }
            })
            this.emitter.on("deleteStaff", id => {
                this.deleteConfirmedStaff(id)
                this.emitter.emit("showNotification", {
                    "action": "delete",
                    "item": this.item
                })
            })
        }
    }
    </script>
    
    <style>
    html {
        background-color: #F1F1FB;
    }
    </style>
    