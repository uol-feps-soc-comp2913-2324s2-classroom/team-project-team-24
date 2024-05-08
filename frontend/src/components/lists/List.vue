<template>
    <div>
        <slot
            v-for="dataItem in dataArray"
            :key="dataItem"
            v-bind:data="dataItem"
        ></slot>
    </div>
</template>

<script>
export default {
    name: 'ListComponent',
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
