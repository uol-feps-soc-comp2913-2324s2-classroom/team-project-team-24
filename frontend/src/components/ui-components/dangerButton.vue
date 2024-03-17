<script>
export default {
    name: 'dangerButton',
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
    background-color: var(--danger-color);
    border-style: solid;
    border-color: var(--danger-color);
    border-width: 3px;
    font-weight: bold;
    color: var(--l1-color);
    padding: 0.4rem 1.5rem;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    transition: background-color 0.2s, border-color 0.2s, color 0.2s;
    cursor: pointer;
    border-radius: 99999px;
}

button:hover {
    background-color: var(--danger-color-hover);
    border-color: var(--danger-color-hover);
}

button:active {
    background-color: var(--danger-color-active);
    border-color: var(--danger-color-active);
}
</style>
