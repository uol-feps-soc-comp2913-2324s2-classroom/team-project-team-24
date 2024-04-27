<script>
import UserListComponent from "@/components/lists/UserList.vue";
import GroupListComponent from "@/components/lists/GroupList.vue";
import NewFriendsComponent from "@/components/NewFriends.vue";
// import CreateGroupComponent from "@/components/forms/CreateGroup.vue";
import topNavRailed from '@/components/ui-components/topNavRailedCommunity.vue';

export default {
    name: "CommunityCenter",
    data() {
        return {
            friendsIsShowing: true,
            groupsIsShowing: false,
            createGroupIsShowing: false, // This is now handled by the groupIsShowing
            friendRequestsIsShowing: false,
            addFriendsIsShowing: false,
            friends: ["friend1", "friend2", "friend3", "friend4", "friend5", "friend6", "friend7", "friend7"],
            groups: ["group1", "group2"]
        };
    },
    methods: {
        navElementClicked(id) {
            console.log(id);
            id = parseInt(id);
            switch (id) {
                case 0:
                    console.log("Friends");
                    this.showFriends();
                    break;
                case 1:
                    console.log("Groups");
                    this.showGroups();
                    break;
                case 3:
                    console.log("Friend Requests");
                    this.showFriendRequests();
                    break;
                case 2:
                    console.log("Add Friends");
                    this.showAddFriends();
                    break;
                default:
                    console.log("Unknown");
                    break;
            }
            // console.log(event);
        },
        showFriends() {
            this.friendsIsShowing = true;
            this.groupsIsShowing = false;
            this.friendRequestsIsShowing = false;
            this.addFriendsIsShowing = false;
        },
        showGroups() {
            this.friendsIsShowing = false;
            this.groupsIsShowing = true;
            this.friendRequestsIsShowing = false;
            this.addFriendsIsShowing = false;
        },
        showFriendRequests() {
            this.friendsIsShowing = false;
            this.groupsIsShowing = false;
            this.friendRequestsIsShowing = true;
            this.addFriendsIsShowing = false;
        },
        showAddFriends() {
            this.friendsIsShowing = false;
            this.groupsIsShowing = false;
            this.friendRequestsIsShowing = false;
            this.addFriendsIsShowing = true;
        },
        createGroup() { // Deprecated
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
        // CreateGroupComponent,
        topNavRailed,
    },
};
</script>

<template>
    <div class="communityPageContainer p-4">
        <topNavRailed @NavElementClicked="navElementClicked"/>
        <div class="columns">
            <div>
                <!-- <div style="display:flex;">
                    <button @click="showFriends">Friends</button>
                    <button @click="showGroups">Groups</button>
                </div> -->
                <UserListComponent v-if="friendsIsShowing" v-bind:users="friends" />

                <!-- <button @click="createGroup" v-if="groupsIsShowing" style="float:right; margin-right: 30px;">+</button> -->
                <GroupListComponent v-if="groupsIsShowing" v-bind:groups="groups" />
                <!-- <CreateGroupComponent v-if="groupsIsShowing"/> -->

                <NewFriendsComponent v-if="addFriendsIsShowing"/>
                
                <!-- friend requests compnent should go here-->


            </div>
        </div>
        
        
    </div>
</template>

<style scoped>
.columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
}
</style>
