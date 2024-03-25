<script>
import UserListComponent from "@/components/lists/UserList.vue";
import GroupListComponent from "@/components/lists/GroupList.vue";
import NewFriendsComponent from "@/components/NewFriends.vue";
import CreateGroupComponent from "@/components/forms/CreateGroup.vue";
import axiosAuth from "@/api/axios-auth.js";

export default {
    name: "CommunityCenter",
    data() {
        return {
            friendsIsShowing: true,
            groupsIsShowing: false,
            createGroupIsShowing: false,
            friends: [],
            groups: ["group1", "group2"],
            friendRequests: [],
            buttonDict: {
                text: "Remove",
                action: this.removeFriend
            },
        };
    },
    methods: {
        getPageData() {
            axiosAuth.get('/friends/get-all').then(
                response => {
                    this.friends = response.data.friends;
                    console.log("Friends:", this.friends);
                }
            )
        },
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
        async removeFriend(userID) {
            await axiosAuth.post("/friends/remove", {
                friendID: userID,
            }).catch(error => {
                console.log(error);
            })
            this.getPageData();
        }
    },
    created() {
        this.getPageData();
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
                <UserListComponent v-if="friendsIsShowing" v-bind:users="friends" :button="buttonDict"/>
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
