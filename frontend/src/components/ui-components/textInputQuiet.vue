<script>
export default {
    name: 'TextInputQuiet',
    props: {
        placeHolder: {
            type: String,
            default: '',
        },
        formLabel: {
            type: String,
            // default: 'Form label'
        },
        type: {
            type: String,
            default: 'text',
        },
        width: {
            type: String,
            default: 'auto',
        },
        // customStyles: {
        //     type: Object,
        //     default: () => ({}),
        // },
        // //新加的，目的是想根据container改变线条长度
    },
    data() {
        return {
            inputValue: '',
        }
    },
    methods: {
        handleInput(event) {
            this.inputValue = event.target.value
        },
    },
}
</script>

<template>
    <p>{{ formLabel }}</p>
    <input
        :style="{ width: width }"
        :type="type"
        v-model="inputValue"
        @input="handleInput"
        :placeholder="placeHolder"
    />
</template>
<!-- :style="{ width: width }" -->

<style scoped>
p {
    margin: 0;
    font-size: 13px;
    color: #666666;
}

input {
    margin: 0;
    border-width: 0 0 2px 0;
    border-style: solid;
    border-color: #c0c0c0;
}

input:hover {
    border-color: #a2a2a2;
}

input:focus {
    outline: none;
    border-color: #0e7eff;
    border-width: 0 0 3px 0;
}
</style>
