<script>
// Only use within a topNavRailed component
export default {
    name: 'topNavElement',
    props: {
        to: {
            type: String,
            required: true,
        },
    },
    data() {
        return {}
    },
    methods: {
        emitClicked(event) {
            this.$emit('NavElementClicked',  event )
        },
    },
}
</script>

<template>
    <router-link :to="`${to}`" @click="emitClicked($event)" class="topNavElement">
        <slot></slot>
    </router-link>
</template>

<style scoped>
.topNavElement{
    text-decoration: none;
    color: var(--topNavElementUnselectedTextColor);
}
</style>
