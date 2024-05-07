<template>
    <router-link
        :to="`${to}`"
        @click="emitClicked($event)"
        class="topNavElement"
    >
        <slot></slot>
    </router-link>
</template>

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
            this.$emit('NavElementClicked', event)
        },
    },
}
</script>

<style scoped>
.topNavElement {
    text-decoration: none;
    color: var(--topNavElementUnselectedTextColor);
}
</style>
