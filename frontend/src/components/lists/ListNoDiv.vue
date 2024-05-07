<template>
    <slot
        v-for="dataItem in dataArray"
        :key="dataItem"
        v-bind:data="dataItem"
    ></slot>
</template>

<script>
export default {
    name: 'ListComponentNoDiv',
    props: {
        dataArray: {
            type: Array,
        },
    },
    data() {
        return {}
    },
    methods: {},
    unmounted() {
        this.$emit('listComponentUnmounted')
    },
}
</script>
