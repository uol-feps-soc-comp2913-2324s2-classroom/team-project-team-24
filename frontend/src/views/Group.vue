<script>
import MapViewerComponent from "@/components/MapViewer.vue";
// import PopupComponent from "@/components/Popup.vue";
import ModalComponent from "@/components/Modal.vue";
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
        ModalComponent,
        // PopupComponent,
        AddTrailListItemComponent,
    },
    created() {
        this.getPageData();
    }
};
</script>

<template>
    <div class="myGroupPageContainer">
        <div class="groupViewHeading d-flex flex-row justify-content-between align-items-center p-3">
            <h2>{{ name }}</h2>
            <div>
                <button @click="addRoutes" class="btn-primary me-3">
                    <div class="buttonText">
                        <img src="../assets/add.svg" class="addIcon" alt="plus icon">
                        <p>Add routes</p>
                    </div>
                </button>
                <button @click="inviteFriends" class="btn-secondary">Group members</button>
            </div>
            <!-- <PopupComponent :closeWindow="closeTrailsPopup" style="float:right;" v-if="showTrails"> -->
            <ModalComponent :is-open="showTrails" @update:is-open="showTrails = $event">
                <h3>Add Trails</h3>
                <div class="horizontalLine mb-3"></div>
                <div class="scrollableTrailsList mb-4">
                    <ListComponent v-bind:dataArray="trails" v-slot="slotProps" class="addTrailsModalWindow">
                        <AddTrailListItemComponent class="slightlySmaller" v-bind:trailID="slotProps.data" :groupID="groupID"/>
                    </ListComponent>
                </div>
                <button @click="closeTrailsPopup" class="btn-secondary align-self-end mt-2">Close</button>
            </ModalComponent>
            <!-- </PopupComponent> -->

            <!-- <PopupComponent :closeWindow="closeFriendsPopup" style="float:right;" v-if="showFriends"> -->
            <ModalComponent :is-open="showFriends" @update:is-open="showFriends = $event">
                <div>
                    <h3>Members</h3>
                    <button @click="leaveGroup" class="btn-quiet-danger">Leave group</button>
                    <ListComponent v-bind:dataArray="members" v-slot="slotProps">
                        <UserListItemComponent v-bind:user="slotProps.data"/>
                    </ListComponent>
                </div>
                <ListComponent v-bind:dataArray="friends" v-slot="slotProps">
                    <UserListItemComponent v-bind:user="slotProps.data" :button="buttonDict"/>
                </ListComponent>
            </ModalComponent>
            <!-- </PopupComponent> -->
        </div>

        <div class="groupMapView">
            <MapViewerComponent />
        </div>
    </div>
</template>

<style scoped>
h2{
    margin: 0;

}

.slightlySmaller{
    width: 99.5%;
    margin-left: 1px;
}

.scrollableTrailsList {
    max-height: 35vh;
    overflow-y: auto;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.addIcon {
    width: 12px;
    height: 12px;
    margin-right: 5px;
}

.buttonText {
    display: flex;
    flex-direction: row;
    align-items: center;
}

.buttonText p {
    margin: 0;
}

.groupViewHeading{
    background-color: var(--l1-color);
    border-radius: var(--border-radius);
    margin-bottom: 0.5rem;
}

.groupMapView{
    background-color: var(--l1-color);
}

.addTrailsModalWindow{
    width: 33vw;
}
</style>
