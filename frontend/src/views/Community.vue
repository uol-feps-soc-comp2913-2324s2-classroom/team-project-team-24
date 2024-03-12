<script>
import UserListComponent from "@/components/lists/UserList.vue";
import GroupListComponent from "@/components/lists/GroupList.vue";
import NewFriendsComponent from "@/components/NewFriends.vue";
import CreateGroupComponent from "@/components/forms/CreateGroup.vue";

export default {
    name: "CommunityCenter",
    data() {
        return {
            friendsIsShowing: true,
            groupsIsShowing: false,
            createGroupIsShowing: false,
            friends: ["friend1", "friend2", "friend3", "friend4", "friend5", "friend6", "friend7", "friend7"],
            groups: ["group1", "group2"]
        };
    },
    methods: {
        showFriends() {
            this.friendsIsShowing = true;
            this.groupsIsShowing = false;
        },
        showGroups() {
            this.groupsIsShowing = true;
            this.friendsIsShowing = false;
        },
        createGroup() {
            /* For now, i hide groups and friends coz its easier,
             * but in future, we should have this overlay */
            this.groupsIsShowing = false;
            this.friendsIsShowing = false;
            this.createGroupIsShowing = true;
        },
        closeCreateGroup() {
            this.groupsIsShowing = true;
            this.friendsIsShowing = false;
            this.createGroupIsShowing = false;
        },
    },
    components: {
        UserListComponent,
        GroupListComponent,
        NewFriendsComponent,
        CreateGroupComponent,
    },
};
</script>

<template>
    <div class="communityPageContainer">
        <h1>Community Page</h1>
        <div class="columns">
            <div>
                <div style="display:flex;">
                    <button @click="showFriends">Friends</button>
                    <button @click="showGroups">Groups</button>
                </div>
                <UserListComponent v-if="friendsIsShowing" v-bind:users="friends" />
                <button @click="createGroup" v-if="groupsIsShowing" style="float:right; margin-right: 30px;">+</button>
                <GroupListComponent v-if="groupsIsShowing" v-bind:groups="groups" />
                <CreateGroupComponent v-if="createGroupIsShowing"/>
            </div>
            <NewFriendsComponent />
        </div>
        
        
    </div>
</template>

<style scoped>
.columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
}
</style>
