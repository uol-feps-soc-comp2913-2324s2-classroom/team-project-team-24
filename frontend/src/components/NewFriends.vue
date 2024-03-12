<template>
    <div>
        <h2>Find New Friends</h2>
        <form @submit.prevent="addFriend">
            <input id="friend-email" v-model="text" type="text" placeholder="Enter their email" required />
            <br/>
            <button type="submit">Add</button>
        </form>
        <br/>
        <h2>Friend Requests</h2>
        <UserListComponent v-bind:users="friendRequests" :addButtonShowing="true"/>
    </div>
</template>

<script>
import UserListComponent from "@/components/lists/UserList.vue";
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
        UserListComponent,
    }
};
</script>

