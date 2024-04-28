<script>
import MapViewerComponent from "@/components/MapViewer.vue";
import PopupComponent from "@/components/Popup.vue";
import ListComponent from "@/components/lists/List.vue";
import UserListItemComponent from "@/components/lists/UserListItem.vue";
import AddTrailListItemComponent from "@/components/lists/AddTrailListItem.vue";
import axiosAuth from "@/api/axios-auth.js";

export default {
    name: "MyGroup",
    data() {
        return {
            name: "",
            members: [],
            trails: [],
            groupID: this.$route.query.groupID,
            buttonDict: {
                text: "Invite",
                action: this.inviteFriend,
            },
            friends: [],
            showFriends: false,
            showTrails: false,
        };
    },
    methods: {
        async getPageData() {
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
            await axiosAuth.get('/trail/get-all').then(
                response => {
                    this.trails = response.data.trails;
                }
            );
        },
        toggle(bool) {
            if (bool) {
                return false;
            } else {
                return true;
            }
        },
        addRoutes() {
            this.showTrails = this.toggle(this.showTrails);
        },
        inviteFriends() {
            // Need to make it so that you can't invite somebody twice
            this.showFriends = this.toggle(this.showFriends);
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
        closeFriendsPopup() {
            this.showFriends = false;
        },
        closeTrailsPopup() {
            this.showTrails = false;
        }
    },
    components: {
        MapViewerComponent,
        UserListItemComponent,
        ListComponent,
        PopupComponent,
        AddTrailListItemComponent,
    },
    created() {
        this.getPageData();
    }
};
</script>

<template>
    <div class="myGroupPageContainer">
        <div class="groupViewHeading">
            <h1>{{ name }}</h1>
            <button @click="addRoutes" style="float:right;">Add routes</button>
        </div>
        <PopupComponent :closeWindow="closeTrailsPopup" style="float:right;" v-if="showTrails">
            <ListComponent v-bind:dataArray="trails" v-slot="slotProps">
                <AddTrailListItemComponent v-bind:trailID="slotProps.data" :groupID="groupID"/>
            </ListComponent>
        </PopupComponent>
        <div class="groupMapView">
            <MapViewerComponent />
        </div>
        <div>
            <h3>Members</h3>
            <button @click="inviteFriends" style="float:right;">Invite</button>
            <PopupComponent :closeWindow="closeFriendsPopup" style="float:right;" v-if="showFriends">
                <ListComponent v-bind:dataArray="friends" v-slot="slotProps">
                    <UserListItemComponent v-bind:user="slotProps.data" :button="buttonDict"/>
                </ListComponent>
            </PopupComponent>
            <ListComponent v-bind:dataArray="members" v-slot="slotProps">
                <UserListItemComponent v-bind:user="slotProps.data"/>
            </ListComponent>
        </div>
        <button @click="leaveGroup">Leave</button>
    </div>
</template>

<style scoped>
.groupViewHeading{
    background-color: var(--l1-color);
}

.groupMapView{
    background-color: var(--l1-color);
}
</style>
