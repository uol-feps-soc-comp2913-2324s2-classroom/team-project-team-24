<template>
    <div>
        <h3 class="my-4">Find new friends</h3>
        <!-- <h2>Friend Requests</h2> -->
        <!-- <UserListComponent v-bind:users="friendRequests" :addButtonShowing="true"/> -->
    </div>
</template>

<script>
// import UserListComponent from "@/components/lists/UserList.vue";
export default {
    name: "FindFriendsComponent",
    data() {
        return {
            month: "February",
            value: 50,
            max: 100,
            friendRequests: ["user1", "user2", "user3"]
        };
    },
    methods: {
        
    },
    components: {
        // UserListComponent,
    }
};
</script>

