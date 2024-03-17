<script>
export default {
    name: 'textButton',
    props: {
        onClick: {
            type: Function,
            default: () => {},
        },
    },
    methods: {
        handleClick() {
            this.onClick();
        }
    }
}
</script>

<template>
    <button @click="handleClick"> 
        <slot></slot>
    </button>
</template>

<style scoped>
button {
    background: none;
    border-style: none;
    font-weight: bold;
    color: var(--action-blue);
    padding: 0;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    cursor: pointer;
}

button:hover {
    text-decoration: underline;
}
</style>
