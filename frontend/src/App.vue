<script>
import sideNavComponent from './components/sideNav.vue';

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
        sideNavComponent,
    },
};
</script>

<template>
    <div class="main" id="mainElement">
        <div class="navPanel">
            <sideNavComponent />
        </div>
        <div class="content">
            <router-view />
        </div>
    </div>
</template>

<style scoped></style>