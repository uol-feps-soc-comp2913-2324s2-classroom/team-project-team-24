<template>
    <div>
        <p>{{ formLabel }}</p>
        <input :type="type" v-model="inputValue" @input="handleInput" :placeholder="placeHolder"/>
    </div>
</template>

<script>
export default {
    name: 'TextInputQuiet',
    props: {
        placeHolder: {
            type: String,
            default: ''
        },
        formLabel: {
            type: String,
            default: 'Form label'
        },
        type: {
            type: String,
            default: 'text'
        }
    },
    data() {
        return {
            inputValue: ''
        };
    },
    methods: {
        handleInput(event) {
            this.inputValue = event.target.value;
        }
    }
};
</script>

<style scoped>
p {
    margin: 0;
    font-size: 13px;
    color: #666666
}
input {
    margin: 0;
    border-width: 0 0 2px 0;
    border-style: solid;
    border-color: #c0c0c0;
}

input:focus {
    outline: none;
    border-color: #0e7eff;
    border-width: 0 0 3px 0;
}
</style>