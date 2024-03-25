<template>
    <div style="display: flex;">
        <img src="{{ this.user.profilePhoto }}"/>
        <h4>{{ this.user.name }}</h4>
        <button v-if="this.button.text !== null" @click.prevent="this.button.action(this.user.id)">{{ this.button.text }}</button>
    </div>
</template>

<script>
export default {
    name: "UserListItemComponent",
    props: {
        user: {
            
        },
        button: {
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

