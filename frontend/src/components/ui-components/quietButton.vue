<script>
export default {
    name: 'quietButton',
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
    background-color: rgba(0, 0, 0, 0);
    border-style: solid;
    border-color: rgba(0, 0, 0, 0);
    border-width: 3px;
    font-weight: bold;
    color: var(--secondary-button-offBlack);
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
    background-color: var(--tertiary-button-grey);
    border-color: var(--tertiary-button-grey);
}

button:active {
    background-color: var(--tertiary-button-grey-hover);
    border-color: var(--tertiary-button-grey-hover);
}
</style>
