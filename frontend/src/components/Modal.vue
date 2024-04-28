<template>
    <!--This modal's visibility is controlled by the isOpen prop.-->
    <!--which should be controlled by the parent component.-->
    <Transition name="modal">
        <div class="modal" v-if="isOpen">
            <div class="modal-overlay" @click="closeModal"></div>
            <div class="modal-content p-5">
                <slot></slot>
            </div>
        </div>
    </Transition>
</template>

<script>
export default {
    name: 'ModalComponent',
    props: {
        isOpen: {
            type: Boolean,
            default: false
        }
    },
    methods: {
        closeModal() {
            this.$emit('update:isOpen', false);
        },
        closeModalOnEsc(event) {
            if (event.key === 'Escape') {
                this.closeModal();
            }
        }
    },
    mounted() {
        document.addEventListener('keydown', this.closeModalOnEsc);
        console.log('Modal mounted. Is open: ' + this.isOpen);
    },
}
</script>

<style scoped>
.modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
}

.modal-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(var(--backdrop-filter-blur));
    transition: backdrop-filter 0.5s;
}

.modal-content {
    width: auto;
    height: auto;
}

.modal-enter-active, .modal-leave-active {
    transition: opacity 0.2s, backdrop-filter 0.5s;
}

.modal-enter-from{
    opacity: 0;
    backdrop-filter: blur(0);
}

.modal-enter-to{
    opacity: 1;
    backdrop-filter: blur(var(--backdrop-filter-blur));
}

.modal-leave-from {
    opacity: 1;
    backdrop-filter: blur(var(--backdrop-filter-blur));
}

.modal-leave-to {
    opacity: 0;
    backdrop-filter: blur(0);
}

</style>