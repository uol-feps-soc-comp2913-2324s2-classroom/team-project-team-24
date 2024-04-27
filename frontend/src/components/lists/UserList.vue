<template>
    <div>
        <h3 class="my-4">My friends list</h3>
        <UserListItemComponent v-for="(user, x) in users" :key="x" v-bind:user="user" :addButtonShowing="addButtonShowing" />
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

