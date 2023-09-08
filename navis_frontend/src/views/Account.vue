<template>
<div class="flex">
    <Aside />
    <div class="w-10/12">
        <div class="pl-6 pr-6 font-base">
            <div class="flex font-base mt-5 justify-between">
                <div class="flex gap-4 items-center">
                    <h1 class="text-2xl font-extrabold">Account</h1>

                </div>
                <div class="flex gap-4 items-center">
                    <div>
                        <button @click="logoutUser" class="bg-violet-600 text-white px-12 py-2 rounded-md">Logout</button>
                    </div>
                </div>
            </div>
            <Notification />
            <div class="font-base bg-white pb-5 mt-2 rounded-md overflow-x-auto">
                <div class="grid grid grid-cols-3 gap-4 gap-y-1">
                    <div class="ml-5 mt-3 flex flex-col gap-2">
                        <h3 class="uppercase text-gray-500">profile image</h3>
                        <img src="../assets/user.jpeg" class="rounded-md h-64 w-64 object-cover" alt="">
                        <a href="" class="text-violet-600">Change profile picture</a>
                    </div>
                    <div class="col-span-2 ml-5 mr-5 mt-5 flex flex-col gap-3">
                        <h3 class="uppercase text-gray-500">information</h3>
                        <ul class="grid grid-cols-2 gap-4 gap-y-5">
                            <li class="bg-[#f1f1fb]/40 rounded-md text-gray-900 pl-4 flex flex-col gap-2">
                                <p class="text-gray-400 uppercase font-bold text-xs mt-1">Name</p>
                                <p>{{ user?.first_name }} {{ user?.last_name }}</p>
                            </li>
                            <li class="bg-[#f1f1fb]/40 rounded-md pb-2 text-gray-900 pl-4 flex flex-col gap-2">
                                <p class="text-gray-400 uppercase font-bold text-xs mt-1">Email</p>
                                <p>{{ user?.email }}</p>
                            </li>
                            <li class="bg-[#f1f1fb]/40 rounded-md text-gray-900 pl-4 flex flex-col gap-2">
                                <p class="text-gray-400 uppercase font-bold text-xs mt-1">Phone number</p>
                                <p>{{ user?.phone_number }}</p>
                            </li>
                            <li class="bg-[#f1f1fb]/40 pb-2 rounded-md text-gray-900 pl-4 flex flex-col gap-2">
                                <p class="text-gray-400 uppercase font-bold text-xs mt-1">Identity number</p>
                                <p>{{ user?.id_number }}</p>
                            </li>
                            <li class="bg-[#f1f1fb]/40 rounded-md text-gray-900 pl-4 flex flex-col gap-2">
                                <p class="text-gray-400 uppercase font-bold text-xs mt-1">Kra pin</p>
                                <p>{{ user?.kra_pin }}</p>
                            </li>
                            <li class="bg-[#f1f1fb]/40 rounded-md text-gray-900 pb-2 pl-4 flex flex-col gap-2">
                                <p class="text-gray-400 uppercase font-bold text-xs mt-1">role</p>
                                <p>{{ user?.role }}</p>
                            </li>

                        </ul>
                    </div>

                    <div class="ml-5 mt-5 flex flex-col gap-3">
                        <h3 class="uppercase text-gray-500">change password</h3>
                        <form class="text-center text-gray-500 flex flex-col gap-4 font-base bg-white rounded-xl">
                            <div class="flex text-start flex-col gap-2">
                                <label for="password" class="text-gray-800 text-sm">Old Password</label>
                                <input v-model="old_password" type="password" class="border focus:ring-0 focus:outline-none border-gray-200 bg-white py-2 rounded-md pl-4 shadow-sm">
                            </div>
                            <div class="flex text-start flex-col gap-2">
                                <label for="password" class="text-gray-800 text-sm">New Password</label>
                                <input v-model="new_password" type="password" class="border focus:ring-0 focus:outline-none border-gray-200 bg-white py-2 rounded-md pl-4 shadow-sm">
                            </div>
                            <div class="flex text-start flex-col gap-2">
                                <label for="password" class="text-gray-800 text-sm">Confirm Password</label>
                                <input v-model="confirm_password" type="password" class="border focus:ring-0 focus:outline-none border-gray-200 bg-white py-2 rounded-md pl-4 shadow-sm">
                                <small v-if="passwordMistMatch" class="text-red-500">{{ errorMessage }}</small>
                            </div>
                            <div class="mt-5">
                                <button @click.prevent="changeUserPassword" class="bg-violet-600 w-full text-white py-2 px-12 rounded-md">Change password</button>
                            </div>

                        </form>
                    </div>
                    <div class=" col-span-2 ml-5 mr-5 mt-5 flex flex-col gap-3">
                        <h3 class="uppercase text-gray-500">update information</h3>
                        <form class="text-center text-gray-500 font-base grid grid-cols-2 gap-4 bg-white rounded-xl">
                            <div class="flex text-start flex-col gap-2">
                                <label for="first_name" class="text-gray-800 text-sm">First name</label>
                                <input v-model="userInfo.first_name" type="text" class="border focus:ring-0 focus:outline-none border-gray-200 bg-white py-2 rounded-md pl-4 shadow-sm">
                            </div>
                            <div class="flex text-start flex-col gap-2">
                                <label for="last_name" class="text-gray-800 text-sm">Last name</label>
                                <input v-model="userInfo.last_name" type="text" class="border focus:ring-0 focus:outline-none border-gray-200 bg-white py-2 rounded-md pl-4 shadow-sm">
                            </div>
                            <div class="flex text-start flex-col gap-2">
                                <label for="email" class="text-gray-800 text-sm">Email</label>
                                <input v-model="userInfo.email" type="email" class="border focus:ring-0 focus:outline-none border-gray-200 bg-white py-2 rounded-md pl-4 shadow-sm">
                            </div>
                            <div class="flex text-start flex-col gap-2">
                                <label for="phone_number" class="text-gray-800 text-sm">Phone number</label>
                                <input v-model="userInfo.phone_number" type="text" class="border focus:ring-0 focus:outline-none border-gray-200 bg-white py-2 rounded-md pl-4 shadow-sm">
                            </div>
                            <div class="flex text-start flex-col gap-2">
                                <label for="id_number" class="text-gray-800 text-sm">ID number</label>
                                <input v-model="userInfo.id_number" type="text" class="border focus:ring-0 focus:outline-none border-gray-200 bg-white py-2 rounded-md pl-4 shadow-sm">
                            </div>
                            <div class="flex text-start flex-col gap-2">
                                <label for="kra_pin" class="text-gray-800 text-sm">KRA pin</label>
                                <input v-model="userInfo.kra_pin" type="text" class="border focus:ring-0 focus:outline-none border-gray-200 bg-white py-2 rounded-md pl-4 shadow-sm">
                            </div>
                            <div>

                            </div>
                            <div class="mt-5 ">
                                <button @click.prevent="updateStaffDetails" class="bg-violet-600 w-full text-white py-2 px-12 rounded-md">Update information</button>
                            </div>

                        </form>
                    </div>

                </div>

            </div>
        </div>
    </div>
</div>
</template>

<script>
import Aside from '@/components/Aside.vue';
import {
    mapActions,
    mapGetters
} from 'vuex';
import Notification from '@/components/Notification.vue';
export default {
    name: 'Account',
    components: {
        Aside,
        Notification
    },
    data() {
        return {
            old_password: "",
            new_password: "",
            confirm_password: "",
            userInfo: {
                first_name: "",
                last_name: "",
                email: "",
                phone_number: "",
                id_number: "",
                kra_pin: ""
            },
            item: "Staff",
            passwordMistMatch: false,
            errorMessage: ""
        }
    },
    computed: {
        ...mapGetters({
            storedUser: 'getStoredUser'
        }),
        user() {
            return this.storedUser
        }
    },
    methods: {
        ...mapActions({
            changePassword: "changePassword",
            getUsersMe: "getUsersMe",
            updateStaff: "updateStaff"
        }),
        changeUserPassword() {
            if (this.new_password != this.confirm_password) {
                this.passwordMistMatch = true
                this.errorMessage = "Passwords do not match"
                setTimeout(() => this.passwordMistMatch = false, 2000)
            } else {
                this.changePassword({
                    payload: {
                        "old_password": this.old_password,
                        "new_password": this.new_password
                    },
                    cb: (() => {
                        this.emitter.emit("showNotification", {
                            "action": "edit",
                            "item": this.item
                        })
                        this.logoutUser()
                    })
                })
            }
        },
        updateStaffDetails() {
            this.updateStaff({
                uuid: this.user.id,
                payload: this.userInfo,
                cb: (() => {
                    this.emitter.emit("showNotification", {
                        "action": "edit",
                        "item": this.item
                    })
                })
            })
        },
        logoutUser() {
            localStorage.removeItem("navis_token")
            this.$router.push({"name": "login"})
        },
        init() {
            this.getUsersMe({
                cb: (res) => {
                    this.userInfo = res
                }
            })
        },
    },
    mounted() {
        this.init()
    }
}
</script>

<style>
html {
    background-color: #F1F1FB;
}
</style>
