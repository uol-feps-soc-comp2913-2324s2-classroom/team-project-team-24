<template>
    <div style="display: flex;">
        <img src="{{ testimg }}"/>
        <h4>{{ name }}</h4>
        <button v-if="addButtonShowing">Add</button>
    </div>
</template>

<script>
export default {
    name: "UserListItemComponent",
    props: {
        user: {
            type: String
        },
        addButtonShowing: {
            type: Boolean,
            default: false
        }
    },
    data() {
        return {
            testimg: "",
            name: this.user
        };
    },
    methods: {
        
    },
};
</script>

