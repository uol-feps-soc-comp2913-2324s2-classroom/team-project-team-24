<template>
    <div class="inner-container">
        <button @click="closeWindow" style="float: right">X</button>
        <slot></slot>
    </div>
</template>

<script>
import '@/assets/css/form.css'

export default {
    name: 'PopupComponent',
    props: {
        closeWindow: {
            type: Function,
        },
    },
    data() {
        return {}
    },
    methods: {},
}
</script>
