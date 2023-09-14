<template>
<div class="lg:hidden flex mt-3 justify-between">
    <div class="flex items-center">
        <h1 class="text-violet-600 text-4xl font-bold">Navis</h1>
    </div>
    
    <Mobile/>
</div>
</template>
<script>
import Mobile from './Mobile.vue';
export default {
    components: {
        Mobile
    }
}
</script>
