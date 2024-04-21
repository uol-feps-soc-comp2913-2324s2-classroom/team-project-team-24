<script>
export default {
    name: 'primaryButton',
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
    <button @click.stop="handleClick"> 
        <slot></slot>
    </button>
</template>

<style scoped>
button {
    background-color: var(--app-green);
    border: 3px solid var(--app-green);
    font-weight: bold;
    color: white;
    padding-top: var(--button-padding-vertical);
    padding-bottom: var(--button-padding-vertical);
    padding-left: var(--button-padding-horizontal);
    padding-right: var(--button-padding-horizontal);
    /* padding: 0.4rem 1.5rem; */
    text-align: center;
    text-decoration: none;
    display: inline;
    transition: background-color 0.2s, border-color 0.2s;
    cursor: pointer;
    border-radius: 99999px;
}

button:hover {
    background-color: var(--app-green-hover);
    border-color: var(--app-green-hover);
}

button:active {
    background-color: var(--app-green-pressed);
    border-color: var(--app-green-pressed);
}
</style>
