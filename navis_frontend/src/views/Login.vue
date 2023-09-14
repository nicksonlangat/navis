<template>
<div class="flex w-full font-base flex-col justify-center items-center">
    <form class="mt-32 text-center font-base bg-white pb-20 w-1/2 max-w-lg rounded-xl">
        <div class="flex items-center justify-center">
            <img src="../assets//logo.png" class="h-32 w-32 rounded-full object-cover" alt="">
        </div>
        <h3 class="text-3xl font-bold">Welcome back</h3>
        <p class="text-sm text-gray-600 mt-3">Please enter your details to log in</p>
        <div class="flex mt-5 text-start flex-col gap-2 mr-5 ml-5">
            <label for="email" class="text-gray-800 text-sm">Email address</label>
            <input v-model="user.email" type="email" class="border border-gray-200 shadow-sm focus:ring-0 focus:outline-none bg-white py-2 rounded-md pl-4" placeholder="Enter your email">
            <small v-if="emailError" class="text-red-500">{{ errorMessage }}</small>
        </div>
        <div class="flex mt-5 text-start flex-col gap-2 mr-5 ml-5">
            <label for="password" class="text-gray-800 text-sm">Password</label>
            <input v-model="user.password" type="password" class="border focus:ring-0 focus:outline-none border-gray-200 bg-white py-2 rounded-md pl-4 shadow-sm" placeholder="********">
            <small v-if="passwordError" class="text-red-500">{{ errorMessage }}</small>
            <div class="flex justify-end text-violet-600 underline text-sm mt-2">
                <a href="/reset">Forgot password?</a>
            </div>
        </div>
        <div class="mr-5 ml-5 mt-5 flex gap-5">
            <button @click.prevent="submitLoginRequest" class="bg-violet-600 w-full text-white py-2 px-12 rounded-md">Log in</button>
            <button @click.prevent="submitGuestLoginRequest" class="bg-violet-600 w-full text-white py-2 px-12 rounded-md">Guest log in</button>
        </div>
        <div class="flex justify-center text-violet-600 gap-2 mt-5 text-sm">
            <p class="text-gray-800">Don't have an account?</p> <a href="#">Request one</a>
        </div>
    </form>
</div>
</template>

<script>
import {
    mapActions,
    mapMutations
} from 'vuex';
export default {
    name: 'Login',
    data() {
        return {
            user: {
                email: "",
                password: "",

            },
            emailError: false,
            passwordError: false,
            errorMessage: ""
        }
    },
    methods: {
        ...mapActions({
            loginUser: 'loginUser'
        }),
        ...mapMutations({

        }),
        submitLoginRequest() {
            this.loginUser({
                payload: this.user,
                cb: (res => {
                    this.$router.push({
                        "name": "dashboard"
                    })
                }),
                errorCb: (error => {
                    if (error.response.data.detail.includes("password")) {
                        this.passwordError = true
                        this.errorMessage = error.response.data.detail
                        setTimeout(() => this.passwordError = false, 2000)
                    }
                    if (error.response.data.detail.includes("user")) {
                        this.emailError = true
                        this.errorMessage = error.response.data.detail
                        setTimeout(() => this.emailError = false, 2000)
                    }

                })
            })
        },
        submitGuestLoginRequest() {
            this.user = {
                email: "nick@gmail.com",
                password: "33992433nkl",
            }
            this.submitLoginRequest()
        }
    }
}
</script>

<style>
html {
    background-color: #F1F1FB;
}
</style>
