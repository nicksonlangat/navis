<template>
    <div class="flex w-full font-base flex-col justify-center items-center">
        <form class="mt-32 text-center font-base bg-white pb-20 w-1/2 max-w-lg rounded-xl">
            <div class="flex items-center justify-center">
                <img src="../assets//logo.png" class="h-32 w-32 rounded-full object-cover" alt="">
            </div>
            <h3 class="text-3xl font-bold">Reset your password</h3>
            <p class="text-sm text-center text-gray-600 mt-3">Enter the code that we sent to <span class="font-bold text-gray-900">nick.langat@navis.com</span> to proceed.</p>
            <div class="flex mt-5 text-start flex-col gap-2 mr-5 ml-5">
                <label for="code" class="text-gray-800 text-sm">Code</label>
                <input type="code" class="border border-gray-200 shadow-sm focus:ring-0 focus:outline-none bg-white py-2 rounded-md pl-4" placeholder="Enter code">
            </div>
            
            <div class="mr-5 ml-5 mt-5">
                <button class="bg-violet-600 w-full text-white py-2 px-12 rounded-md">Proceed</button>
            </div>
            
        </form>
    </div>
    </template>
    
    <style>
    html {
        background-color: #F1F1FB;
    }
    </style>
    