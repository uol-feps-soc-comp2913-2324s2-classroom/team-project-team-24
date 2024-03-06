<script>

import sideNav from './components/sideNav.vue';

export default {
    name: "App",
    data() {
        return {

        };
    },
    methods: {

    },
    components: {
        sideNav,
    },
};
</script>

<template>

<div class="main" id="mainElement">
    <sideNav />
    <div class="content">
        <router-view />
    </div>
</div>
</template>

<style scoped></style>
