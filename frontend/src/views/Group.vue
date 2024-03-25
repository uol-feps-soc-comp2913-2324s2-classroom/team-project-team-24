<script>
import MapViewerComponent from "@/components/MapViewer.vue";
import PopupComponent from "@/components/Popup.vue";
import UserListComponent from "@/components/lists/UserList.vue";
import axiosAuth from "@/api/axios-auth.js";

export default {
    name: "MyGroup",
    data() {
        return {
            name: "",
            members: [],
            groupID: this.$route.query.groupID,
            buttonDict: {
                text: "Invite",
                action: this.inviteFriend,
            },
            friends: [],
            showFriends: false,
        };
    },
    methods: {
        getPageData() {
            axiosAuth.post('/groups/get-members', {
                groupID: this.groupID
            }).then(
                response => {
                    this.members = response.data.members;
                }
            );
            axiosAuth.post('/groups/get-name', {
                groupID: this.groupID
            }).then(
                response => {
                    this.name = response.data.name;
                }
            );
            axiosAuth.get('/friends/get-all').then(
                response => {
                    this.friends = response.data.friends;
                }
            );
        },
        addRoutes() {
            console.log("addRoutes");
        },
        inviteFriends() {
            // Need to make it so that you can't invite somebody twice
            this.showFriends = true;
        },
        async inviteFriend(friendID) {
            await axiosAuth.post('/groups/add-friend', {
                groupID: this.groupID,
                friendID: friendID,
            });
            this.getPageData();
        },
        leaveGroup() {
            axiosAuth.post('/groups/leave', {
                groupID: this.groupID
            }).then(
                this.$router.push({path: "/community"}),
            )
        },
        closePopup() {
            this.showFriends = false;
        }
    },
    components: {
        MapViewerComponent,
        UserListComponent,
        PopupComponent,
    },
    created() {
        this.getPageData();
    }
};
</script>

<template>
    <div class="myGroupPageContainer">
        <h1>{{ name }}</h1>
        <button @click="addRoutes" style="float:right;">Add routes</button>
        <MapViewerComponent />
        <div>
            <h3>Members</h3>
            <button @click="inviteFriends" style="float:right;">Invite</button>
            <div style="float:right;" v-if="showFriends">
                <PopupComponent>
                    <UserListComponent v-bind:users="friends" :button="buttonDict"/>
                </PopupComponent>
            </div>
            <UserListComponent v-bind:users="members"/>
        </div>
        <button @click="leaveGroup">Leave</button>
    </div>
</template>

<style scoped></style>
