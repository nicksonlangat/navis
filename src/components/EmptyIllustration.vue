<template>
<div class="text-gray-400 font-base flex flex-col gap-3 mt-5 justify-center items-center">
    <img class="w-48" src="../assets/empty.svg" alt="">
    <p class="font-base">There are currently no {{ data }} to display</p>
</div>
</template>

<script>
export default {
    props: {
        data: String
    }
}
</script>
