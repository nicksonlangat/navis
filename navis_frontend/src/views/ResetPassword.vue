<template>
<div class="flex w-full font-base flex-col justify-center items-center">
    <form class="lg:mt-32 mt-20 text-center font-base bg-white pb-20 mx-4 lg:mx-0 lg:w-1/2 max-w-lg rounded-xl">
        <div class="flex items-center justify-center">
            <img src="../assets//logo.png" class="h-32 w-32 rounded-full object-cover" alt="">
        </div>
        <h3 class="text-3xl text-start ml-5 mr-5 font-bold">Reset your password</h3>
        <p class="text-sm text-start ml-5 mr-5 text-gray-600 mt-3">Your new password must be different from previously used passwords.</p>
        <div class="flex mt-5 text-start flex-col gap-2 mr-5 ml-5">
            <label for="password" class="text-gray-800 text-sm">Password</label>
            <input type="password" class="border focus:ring-0 focus:outline-none border-gray-200 bg-white py-2 rounded-md pl-4 shadow-sm" placeholder="********">
            <p class="text-xs text-gray-500">Must be at least 8 alphanumeric characters.</p>
        </div>
        <div class="flex mt-5 text-start flex-col gap-2 mr-5 ml-5">
            <label for="password" class="text-gray-800 text-sm">Confirm Password</label>
            <input type="password" class="border focus:ring-0 focus:outline-none border-gray-200 bg-white py-2 rounded-md pl-4 shadow-sm" placeholder="********">
            <p class="text-xs text-gray-500">Both passwords must match.</p>
        </div>
        <div class="mr-5 ml-5 mt-5">
            <button class="bg-violet-600 w-full text-white py-2 px-12 rounded-md">Reset password</button>
        </div>
    </form>
</div>
</template>
<style>
html {
    background-color: #F1F1FB;
}
</style>
