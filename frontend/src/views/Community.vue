<script>
import UserListItemComponent from "@/components/lists/UserListItem.vue";
import ListComponent from "@/components/lists/List.vue";
import GroupListItemComponent from "@/components/lists/GroupListItem.vue";
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
            groups: [],
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
                }
            );
            axiosAuth.get('/groups/get-all').then(
                response => {
                    this.groups = response.data.groups;
                }
            );
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
            await axiosAuth.post('/friends/remove', {
                friendID: userID,
            }).catch(() => {});
            this.getPageData();
        }
    },
    created() {
        this.getPageData();
    },
    components: {
        UserListItemComponent,
        ListComponent,
        NewFriendsComponent,
        CreateGroupComponent,
        GroupListItemComponent,
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
                <ListComponent v-if="friendsIsShowing" v-bind:dataArray="friends" v-slot="slotProps">
                    <UserListItemComponent v-bind:user="slotProps.data" :button="buttonDict"/>
                </ListComponent>
                <button @click="createGroup" v-if="groupsIsShowing" style="float:right; margin-right: 30px;">+</button>
                <ListComponent v-if="groupsIsShowing" v-bind:dataArray="groups" v-slot="slotProps">
                    <GroupListItemComponent v-bind:group="slotProps.data"/>
                </ListComponent>
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
