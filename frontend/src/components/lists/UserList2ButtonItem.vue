<template>
    <div style="display: flex;">
        <h4>{{ this.user.name }}</h4>
        <button v-if="this.button1.text !== null" @click.prevent="this.button1.action(this.user.id)">{{ this.button1.text }}</button>
        <button v-if="this.button2.text !== null" @click.prevent="this.button2.action(this.user.id)">{{ this.button2.text }}</button>
    </div>
</template>

<script>
export default {
    name: "UserList2ButtonItemComponent",
    props: {
        user: {
            
        },
        button1: {
            default: {
                action: {
                    type: Function 
                },
                text: null,
            },
        },
        button2: {
            default: {
                action: {
                    type: Function 
                },
                text: null,
            },
        }
    },
    data() {
        return {
            testimg: "",
            name: this.user
        };
    },
    methods: {
        blank() {},
    },
};
</script>

