<script>
import sideNav from './components/sideNav.vue';

export default {
    name: "App",
    created() {
        this.$store.dispatch('auth/autoLogin');
    },
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
        <div class="navPanel">
            <sideNav />
        </div>
        <div class="content">
            <router-view />
        </div>
    </div>
</template>

<style scoped></style>