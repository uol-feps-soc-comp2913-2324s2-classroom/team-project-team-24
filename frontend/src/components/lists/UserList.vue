<template>
    <div>
        <UserListItemComponent v-for="(user) in users" :key="user" v-bind:user="user" :addButtonShowing="addButtonShowing" />
    </div>
</template>

<script>
import UserListItemComponent from "@/components/lists/UserListItem.vue";

export default {
    name: "UserListComponent",
    props: {
        users: {
            type: Array
        },
        addButtonShowing: {
            type: Boolean,
            default: false
        },
    },
    data() {
        return {
            
        };
    },
    methods: {
        
    },
    components: {
        UserListItemComponent,
    }
};
</script>

