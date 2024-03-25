<template>
    <div class="inner-container">
        <button @click="closeWindow" style="float:right;">X</button>
        <slot></slot>
    </div>
</template>

<script>
import '@/assets/css/form.css';

export default {
    name: "PopupComponent",
    props: {
        inner: {

        }
    },
    data() {
        return {
            
        };
    },
    methods: {
        closeWindow() {
            this.$parent.closePopup();
        }
    },
};
</script>

