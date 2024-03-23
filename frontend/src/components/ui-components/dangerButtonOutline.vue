<script>
export default {
    name: 'dangerButtonOutline',
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
    background-color: var(--l1-color);
    border-style: solid;
    border-color: var(--danger-color);
    border-width: 3px;
    font-weight: bold;
    color: var(--danger-color);
    padding-top: var(--button-padding-vertical);
    padding-bottom: var(--button-padding-vertical);
    padding-left: var(--button-padding-horizontal);
    padding-right: var(--button-padding-horizontal);
    /* padding: 0.4rem 1.5rem; */
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
    color: white;
}

button:active {
    background-color: var(--danger-color-active);
    border-color: var(--danger-color-active);
}
</style>
