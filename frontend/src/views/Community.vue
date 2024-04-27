<script>
import UserListItemComponent from "@/components/lists/UserListItem.vue";
import ListComponent from "@/components/lists/List.vue";
import GroupListItemComponent from "@/components/lists/GroupListItem.vue";
import NewFriendsComponent from "@/components/NewFriends.vue";
import topNavRailed from '@/components/ui-components/topNavRailedCommunity.vue';
// import CreateGroupComponent from "@/components/forms/CreateGroup.vue";
import axiosAuth from "@/api/axios-auth.js";


export default {
    name: "CommunityCenter",
    data() {
        return {
            friendsIsShowing: true,
            groupsIsShowing: false,
            createGroupIsShowing: false, // This is now handled by the groupIsShowing
            friendRequestsIsShowing: false,
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
        getPageData() {
            axiosAuth.get('/friends/get-all').then(
                response => {
                    this.friends = response.data.friends;
                    console.log("Friends:", this.friends);
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
        async removeFriend(userID) {
            await axiosAuth.post('/friends/remove', {
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
        UserListItemComponent,
        ListComponent,
        NewFriendsComponent,
        topNavRailed,
        // CreateGroupComponent,
        GroupListItemComponent,
    },
};
</script>

<template>
    <div class="communityPageContainer p-4">
        <topNavRailed @NavElementClicked="navElementClicked"/>
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
