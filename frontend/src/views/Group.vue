<script>
import MapViewerComponent from "@/components/MapViewer.vue";
import UserListComponent from "@/components/lists/UserList.vue";

export default {
    name: "MyGroup",
    data() {
        return {
            users: ["user1", "user2", "user3"],
            groupName: this.$route.query.groupName,
        };
    },
    methods: {
        addRoutes() {
            console.log("addRoutes");
        },
        inviteFriends() {
            console.log("Invite");
        },
    },
    components: {
        MapViewerComponent,
        UserListComponent,
    },
};
</script>

<template>
    <div class="myGroupPageContainer">
        <h1>{{ groupName }}</h1>
        <button @click="addRoutes" style="float:right;">Add routes</button>
        <MapViewerComponent />
        <div>
            <h3>Members</h3>
            <button @click="inviteFriends" style="float:right;">Invite</button>
            <UserListComponent v-bind:users="users"/>
        </div>
        <button>Leave</button>
    </div>
</template>

<style scoped></style>
