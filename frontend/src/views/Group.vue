<script>
import MapViewerComponent from "@/components/MapViewer.vue";
import ModalComponent from "@/components/Modal.vue";
import ListComponent from "@/components/lists/List.vue";
import UserListItemComponent from "@/components/lists/UserListItem.vue";
import AddTrailListItemComponent from "@/components/lists/AddTrailListItem.vue";
import SharedTrailListItemComponent from "@/components/lists/SharedTrailListItem.vue";
import axiosAuth from "@/api/axios-auth.js";
import topNavRailedGroupMembers from "@/components/ui-components/topNavRailedGroupMembers.vue";
import topNavRailedGroupTrails from "@/components/ui-components/topNavRailedGroupTrails.vue";

export default {
    name: "MyGroup",
    data() {
        return {
            name: "",
            members: [],
            trails: [],
            groupTrails: [],
            shareableTrails: [],
            groupID: this.$route.query.groupID,
            buttonDict: {
                text: "Invite",
                action: this.inviteFriend,
            },
            friends: [],
            friendsNonMembers: [],
            showFriends: false,
            showTrails: false,
            groupModalShowMembers: true,
            groupModalShowAddMembers: false,
            username: "",
            loadingTrailList: true,
            loadingMembersList: true,
            loadingFriendsList: true,
            loadingGroupName: true,
            loadingGroupTrails: true,

            // Used to show the loading message when the user's trails are still being rendered
            trailItemFullyLoadedCount: 0,
            trailItemLoaded: false,

            trailsModalShowSharedTrails: true,
            trailsModalShowAddTrails: false,
            lastTrailsModalView: 0,
            lastGroupMembersModalView: 0,

            mapWidth: null,
            mapHeight: null,
        };
    },
    methods: {
        clearArrays() {
            this.members = [];
            this.trails = [];
            this.friends = [];
            this.friendsNonMembers = [];
            this.shareableTrails = [];
            this.groupTrails = [];

        },
        async getPageData() {
            this.loadingTrailList = true;
            this.loadingMembersList = true;
            this.loadingFriendsList = true;
            this.loadingGroupName = true;
            this.loadingGroupTrails = true;

            const getMembersPromise = axiosAuth.post('/groups/get-members', {
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
                    this.loadingGroupName = false;
                }
            );

            const getAllFriendsPromise = axiosAuth.get('/friends/get-all').then(
                response => {
                    this.friends = response.data.friends;
                    // friendsRaw = response.data.friends;
                }
            );

            const getAllTrailsPromise = axiosAuth.get('/trail/get-all').then(
                response => {
                    this.trails = response.data.trails;
                    // this.loadingTrailList = false;
                }
            );

            const getCurrentUsernamePromise = axiosAuth.get('/account/get-details').then(
                response => {
                    this.username = response.data.name;
                }
            );
            
            // Get all of the user's trails
            axiosAuth.post('/groups/get-trails', {
                groupID: this.groupID
            }).then(
                response => {
                    this.groupTrailsIDOnly = response.data.trails;
                }
            );

            // Get all of the group's trails
            const getGroupTrailsPromise = axiosAuth.post('groups/get-trails-complete', {
                groupID: this.groupID
            }).then(
                response => {
                    this.groupTrails = response.data.trails;

                    // Get map width and height
                    this.getMapDimensions();

                    // this.groupTrailsIDOnly = response.data.trails.map(trail => trail.id);
                    // console.log("Group trail IDs: ", this.groupTrailsIDOnly);
                    this.loadingGroupTrails = false;
                }
            );

            await Promise.all([getMembersPromise, getAllFriendsPromise, getCurrentUsernamePromise]).then(() => {
                const membersSet = new Set(this.members.map(member => member.name));

                for (let i = 0; i < this.friends.length; i++) {
                    if (!membersSet.has(this.friends[i].name)) {
                        this.friendsNonMembers.push(this.friends[i]);
                    }
                }

                this.loadingMembersList = false;

                // Filter out the current user from the members list
                this.members = this.members.filter(member => {
                    return member.name !== this.username;
                });
                this.loadingFriendsList = false;
            });

            await Promise.all([getAllTrailsPromise, getGroupTrailsPromise]).then(() => {
                const groupTrailsSet = new Set(this.groupTrails.map(trail => trail.id));
                this.shareableTrails = this.trails.filter(trail => !groupTrailsSet.has(trail.id));
                this.loadingTrailList = false;
                if (this.shareableTrails.length === 0) {
                    this.trailItemLoaded = true;
                }

            });

        },
        getMapDimensions() {
            const element = document.getElementById("mapViewComponent");
            this.mapWidth = element.clientWidth;
            this.mapHeight = element.clientHeight;
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

            // Not the most efficient nor the nicest user experience, but it works
            this.clearArrays();
            this.getPageData();
        },
        leaveGroup() {
            axiosAuth.post('/groups/leave', {
                groupID: this.groupID
            }).then(
                this.$router.push({ path: "/community" }),
            )
        },
        closeFriendsPopup() {
            this.showFriends = false;
        },
        closeTrailsPopup() {
            this.showTrails = false;
            console.log("Closing trails popup")
        },
        groupModalShowAddMembersHandle() {
            this.groupModalShowMembers = false;
            this.groupModalShowAddMembers = true;
        },
        groupModalShowMembersHandle() {
            this.groupModalShowMembers = true;
            this.groupModalShowAddMembers = false;
        },
        handleNavElementClicked(id) {
            id = parseInt(id);
            // Commented out because turns out user experience is better without it
            // this.lastGroupMembersModalView = id;
            switch (id) {
                case 0:
                    this.groupModalShowMembersHandle();
                    break;
                case 1:
                    this.groupModalShowAddMembersHandle();
                    break;
                default:
                    console.log("Unknown");
                    break;
            }
        },
        returnToCommunity() {
            this.$router.push({ path: "/community" });
        },
        handleTrailItemDataUpdated() {
            this.trailItemFullyLoadedCount++;
            console.log("xxxxxxxxxxxxxxxxx Trail item fully loaded count: ", this.trailItemFullyLoadedCount);
            console.log("xxxxxxxxxxxxxxxxx Expected count: ", this.shareableTrails.length);
            if (this.trailItemFullyLoadedCount === this.shareableTrails.length) {
                this.trailItemLoaded = true;
                console.log("All trail items fully loaded");
            }
        },
        handleNavElementClickedTrails(id) {
            id = parseInt(id);
            // Commented out because turns out user experience is better without it
            // this.lastTrailsModalView = id;
            switch (id) {
                case 0:
                    this.trailsModalShowSharedTrails = true;
                    this.trailsModalShowAddTrails = false;
                    break;
                case 1:
                    this.trailsModalShowSharedTrails = false;
                    this.trailsModalShowAddTrails = true;
                    break;
                default:
                    console.log("Unknown");
                    break;
            }
        },
        resetTrailItemDataUpdated() {
            this.trailItemFullyLoadedCount = 0;
            this.trailItemLoaded = false;
        },
        updateFriendsAndMembers() { // Deprecated
            // this.loadingFriendsList = true;
            // this.loadingMembersList = true;
            // this.loadingTrailList = true;
            // this.loadingTrailName = true;

            // this.getPageData();
        },
        updateTrailsList() {
            this.loadingTrailList = true;
            this.loadingGroupTrails = true;
            this.trailItemLoaded = false;
            this.trailItemFullyLoadedCount = 0;

            this.groupTrails = [];
            this.shareableTrails = [];
            this.trails = [];

            const getGroupTrailsPromise = axiosAuth.post('/groups/get-trails-complete', {
                groupID: this.groupID
            }).then(
                response => {
                    this.groupTrails = response.data.trails;
                    this.loadingGroupTrails = false;
                }
            );

            const getAllTrailsPromise = axiosAuth.get('/trail/get-all').then(
                response => {
                    this.trails = response.data.trails;
                }
            );

            Promise.all([getGroupTrailsPromise, getAllTrailsPromise]).then(() => {
                const groupTrailsSet = new Set(this.groupTrails.map(trail => trail.id));
                this.shareableTrails = this.trails.filter(trail => !groupTrailsSet.has(trail.id));
                this.loadingTrailList = false;
                if (this.shareableTrails.length === 0) {
                    this.trailItemLoaded = true;
                }
            });

        },
    },
    components: {
        MapViewerComponent,
        UserListItemComponent,
        ListComponent,
        ModalComponent,
        AddTrailListItemComponent,
        topNavRailedGroupMembers,
        topNavRailedGroupTrails,
        SharedTrailListItemComponent,
    },
    created() {
        this.getPageData();
    }
};
</script>

<template>
    <div class="myGroupPageContainer d-flex flex-column">
        <div class="groupViewHeading d-flex flex-row justify-content-between align-items-center p-3">
            <div class="d-flex flex-row align-items-center">
                <img src="../assets/back_button.svg" class="backButton me-3" alt="back arrow icon"
                    @click="returnToCommunity">
                <h3 v-if="!loadingGroupName">{{ name }}</h3>
                <h3 v-if="loadingGroupName">Loading...</h3>
            </div>
            <div>
                <button @click="addRoutes" class="btn-primary me-3">
                    <div class="buttonText">
                        <p>Manage routes</p>
                    </div>
                </button>
                <button @click="inviteFriends" class="btn-secondary">Group members</button>
            </div>

            <ModalComponent :is-open="showTrails" @update:is-open="showTrails = $event; closeTrailsPopup">
                <div class="addTrailsModalWindow d-flex flex-column">
                    <topNavRailedGroupTrails @NavElementClicked="handleNavElementClickedTrails" class="mb-3" :lastSelectedElement="lastTrailsModalView"/>
                    <div v-if="trailsModalShowSharedTrails" class="mb-4">
                        <div class="scrollable mb-4">
                            <ListComponent v-bind:dataArray="groupTrails" v-slot="slotProps"
                                v-if="groupTrails.length > 0" class="width100">
                                <SharedTrailListItemComponent v-bind:trail="slotProps.data" class="slightlySmaller" />
                            </ListComponent>
                            <p v-if="groupTrails.length == 0 && !loadingGroupTrails" class="greyText">You haven't shared
                                any trails yet...</p>
                            <p v-if="loadingGroupTrails" class="greyText">Loading shared trails...</p>
                        </div>
                    </div>
                    <div v-if="trailsModalShowAddTrails">
                        <div class="scrollableList mb-4" v-show="!loadingTrailList && trailItemLoaded">
                            <ListComponent v-bind:dataArray="shareableTrails" v-slot="slotProps"
                                v-if="shareableTrails.length > 0" @listComponentUnmounted="resetTrailItemDataUpdated"
                                class="width100">
                                <AddTrailListItemComponent class="slightlySmaller" v-bind:trail="slotProps.data"
                                    :groupID="parseInt(groupID)" @trailItemDataUpdated="handleTrailItemDataUpdated" @trailAddedToGroup="updateTrailsList" />
                            </ListComponent>
                            <p v-if="shareableTrails.length == 0" class="greyText align-self-start">No trails available</p>
                        </div>
                        <p v-if="loadingTrailList || !trailItemLoaded" class="greyText mb-4">Loading trails...</p>
                    </div>
                    <button @click="closeTrailsPopup" class="btn-secondary align-self-end mt-2">Close</button>
                </div>
            </ModalComponent>

            <ModalComponent :is-open="showFriends" @update:is-open="showFriends = $event" :lastSelectedElement="lastGroupMembersModalView">
                <div class="groupMembersModalWindow d-flex flex-column">
                    <topNavRailedGroupMembers @NavElementClicked="handleNavElementClicked" class="mb-3" />
                    <div v-if="groupModalShowMembers">
                        <div class="scrollableList mb-4">
                            <div style="display: flex;" class="friendItem slightlySmaller">
                                <div class="friendNameandAction my-2 px-4">
                                    <p>{{ this.username }} (Me)</p>
                                    <button @click="leaveGroup" class="btn-quiet-danger">Leave group</button>
                                </div>
                                <div class="horizontalLine"></div>
                            </div>
                            <ListComponent v-bind:dataArray="members" v-slot="slotProps" class="width100">
                                <UserListItemComponent v-bind:user="slotProps.data" class="slightlySmaller" />
                            </ListComponent>
                        </div>
                    </div>
                    <div v-if="groupModalShowAddMembers" class="mb-4">
                        <div class="scrollableList" v-if="!loadingFriendsList">
                            <ListComponent v-bind:dataArray="friendsNonMembers" v-slot="slotProps"
                                v-if="friendsNonMembers.length > 0" class="width100">
                                <UserListItemComponent v-bind:user="slotProps.data" :button="buttonDict"
                                    class="slightlySmaller" />
                            </ListComponent>
                        </div>
                        <p v-if="friendsNonMembers.length == 0 && !loadingFriendsList" class="greyText">You have added
                            all your friends to this group</p>
                        <p v-if="loadingFriendsList" class="greyText">Loading friends... </p>
                    </div>
                    <button @click="closeFriendsPopup" class="btn-secondary align-self-end mt-2">Close</button>
                </div>
            </ModalComponent>

        </div>

        <div class="groupMapView" id="mapViewComponent">
            <MapViewerComponent :selected-trails="groupTrails.map( trail => trail.id )" :width="mapWidth" :height="mapHeight"/>
        </div>
    </div>
</template>

<style scoped>
.slightlySmaller {
    width: 99.5%;
    margin-left: 1px;
}

.backButton {
    width: 23px;
    height: 23px;
    cursor: pointer;
}

p {
    margin: 0;
}

.friendItem {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    transition: box-shadow 0.2s;
    transition: background-color 0.2s;
}

.friendItem:hover {
    box-shadow: 0 0 2px var(--selectionRailColor);
}

.friendNameandAction {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    width: 100%;
}

.width100 {
    width: 100%;
}

.groupMembersModalWindow {
    width: 33vw;
}

h3 {
    margin: 0;

}

.scrollableList {
    padding-top: 1px;
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

.groupViewHeading {
    background-color: var(--l1-color);
    border-radius: var(--border-radius);
    margin-bottom: 0.5rem;
}

.groupMapView {
    background-color: var(--l1-color);
    width: 100%;
    height: 100%;
    overflow: hidden;
    border-radius: var(--border-radius);
}

.addTrailsModalWindow {
    width: 33vw;
}
</style>
