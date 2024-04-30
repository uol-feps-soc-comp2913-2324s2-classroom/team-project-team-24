<script>
import MapViewerComponent from "@/components/MapViewer.vue";
import ModalComponent from "@/components/Modal.vue";
import ListComponent from "@/components/lists/List.vue";
import UserListItemComponent from "@/components/lists/UserListItem.vue";
import AddTrailListItemComponent from "@/components/lists/AddTrailListItem.vue";
import axiosAuth from "@/api/axios-auth.js";
import topNavRailedGroupMembers from "@/components/ui-components/topNavRailedGroupMembers.vue";

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
            friendsNonMembers: [],
            showFriends: false,
            showTrails: false,
            groupModalShowMembers: true,
            groupModalShowAddMembers: false,
            username: "",
            loadingTrailList: true,
            loadingMembersList: true,
            loadingFriendsList: true,
            loadingTrailName: true,

            trailItemFullyLoadedCount: 0,
            trailItemLoaded: false,
        };
    },
    methods: {
        clearArrays() {
            this.members = [];
            this.trails = [];
            this.friends = [];
            this.friendsNonMembers = [];
        },
        async getPageData() {
            console.log("GETTING PAGE DATA")
            this.loadingTrailList = true;
            this.loadingMembersList = true;
            this.loadingFriendsList = true;
            this.loadingTrailName = true;

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
                    this.loadingTrailName = false;
                }
            );

            const getAllFriendsPromise = axiosAuth.get('/friends/get-all').then(
                response => {
                    this.friends = response.data.friends;
                    // friendsRaw = response.data.friends;
                }
            );

            axiosAuth.get('/trail/get-all').then(
                response => {
                    this.trails = response.data.trails;
                    this.loadingTrailList = false;
                }
            );

            const getCurrentUsernamePromise = axiosAuth.get('/account/get-details').then(
                response => {
                    this.username = response.data.name;
                }
            );

            await Promise.all([getMembersPromise, getAllFriendsPromise, getCurrentUsernamePromise]);

            const membersSet = new Set(this.members.map(member => member.name));

            for(let i = 0; i < this.friends.length; i++) {
                if (!membersSet.has(this.friends[i].name)) {
                    this.friendsNonMembers.push(this.friends[i]);
                }
            }

            this.loadingMembersList = false;

            // Filter out the current user from the members list
            this.members = this.members.filter( member => {
                return member.name !== this.username;
            });
            this.loadingFriendsList = false;
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
                this.$router.push({path: "/community"}),
            )
        },
        closeFriendsPopup() {
            this.showFriends = false;
        },
        closeTrailsPopup() {
            this.showTrails = false;
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
            switch (id) {
                case 0:
                    this.groupModalShowMembersHandle();
                    console.log("Showing members")
                    break;
                case 1:
                    this.groupModalShowAddMembersHandle();
                    console.log("Showing add members")
                    break;
                default:
                    console.log("Unknown");
                    break;
            }
        },
        returnToCommunity() {
            this.$router.push({path: "/community"});
        },
        handleTrailItemDataUpdated() {
            this.trailItemFullyLoadedCount++;
            if (this.trailItemFullyLoadedCount === this.trails.length) {
                this.trailItemLoaded = true;
            }
        },
        resetTrailItemDataUpdated() {
            console.log("========================== RESETING TRAIL ITEM DATA ==========================")
            this.trailItemFullyLoadedCount = 0;
            this.trailItemLoaded = false;
        },
        updateFriendsAndMembers(){
            console.log("CLICKED CLICKED CLICKED CLICKED CLICKED CLICKED CLICKED CLICKED CLICKED CLICKED CLICKED CLICKED CLICKED CLICKED ")
            // this.loadingFriendsList = true;
            // this.loadingMembersList = true;
            // this.loadingTrailList = true;
            // this.loadingTrailName = true;
            
            // this.getPageData();
        }

    },
    components: {
        MapViewerComponent,
        UserListItemComponent,
        ListComponent,
        ModalComponent,
        AddTrailListItemComponent,
        topNavRailedGroupMembers,
    },
    created() {
        this.getPageData();
    }
};
</script>

<template>
    <div class="myGroupPageContainer">
        <div class="groupViewHeading d-flex flex-row justify-content-between align-items-center p-3">
            <div class="d-flex flex-row align-items-center">
                <img src="../assets/back_button.svg" class="backButton me-3" alt="back arrow icon" @click="returnToCommunity" >
                <h3 v-if="!loadingTrailName">{{ name }}</h3>
                <h3 v-if="loadingTrailName">Loading...</h3>
            </div>
            <div>
                <button @click="addRoutes" class="btn-primary me-3">
                    <div class="buttonText">
                        <img src="../assets/add.svg" class="addIcon" alt="plus icon">
                        <p>Add routes</p>
                    </div>
                </button>
                <button @click="inviteFriends" class="btn-secondary">Group members</button>
            </div>

            <ModalComponent :is-open="showTrails" @update:is-open="showTrails = $event">
                <div class="addTrailsModalWindow d-flex flex-column">
                    <h3>Add Trails</h3>
                    <div class="horizontalLine mb-3"></div>
                    <div class="scrollableList mb-4" v-show="!loadingTrailList && trailItemLoaded">
                        <ListComponent v-bind:dataArray="trails" v-slot="slotProps" v-if="trails.length > 0" @listComponentUnmounted="resetTrailItemDataUpdated">
                            <AddTrailListItemComponent class="slightlySmaller" v-bind:trailID="slotProps.data" :groupID="groupID" @trailItemDataUpdated="handleTrailItemDataUpdated"/>
                        </ListComponent>
                        <p v-if="trails.length == 0" class="greyText align-self-start">No trails available</p>
                    </div>
                    <p v-if="loadingTrailList || !trailItemLoaded" class="greyText mb-4">Loading trails...</p>
                    <button @click="closeTrailsPopup" class="btn-secondary align-self-end mt-2">Close</button>
                </div>
            </ModalComponent>

            <ModalComponent :is-open="showFriends" @update:is-open="showFriends = $event">
                <div class="groupMembersModalWindow d-flex flex-column">
                    <topNavRailedGroupMembers @NavElementClicked="handleNavElementClicked" class="mb-3"/>
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
                                <UserListItemComponent v-bind:user="slotProps.data" class="slightlySmaller"/>
                            </ListComponent>
                        </div>
                    </div>
                    <div v-if="groupModalShowAddMembers" class="mb-4">
                        <div class="scrollableList" v-if="!loadingFriendsList">
                            <ListComponent v-bind:dataArray="friendsNonMembers" v-slot="slotProps" v-if="friendsNonMembers.length > 0" class="width100">
                                <UserListItemComponent v-bind:user="slotProps.data" :button="buttonDict" class="slightlySmaller" @invitingFriendToGroup="updateFriendsAndMembers"/>
                            </ListComponent>
                        </div>
                        <p v-if="friendsNonMembers.length == 0 && !loadingFriendsList" class="greyText">You have added all your friends to this group</p>
                        <p v-if="loadingFriendsList" class="greyText">Loading friends... </p>
                    </div>
                    <button @click="closeFriendsPopup" class="btn-secondary align-self-end mt-2">Close</button>
                </div>
            </ModalComponent>

        </div>

        <div class="groupMapView">
            <MapViewerComponent />
        </div>
    </div>
</template>

<style scoped>
.backButton{
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


.width100{
    width: 100%;
}

.groupMembersModalWindow{
    width: 33vw;
}

h3{
    margin: 0;

}

.slightlySmaller{
    width: 99.5%;
    margin-left: 1px;
}

.scrollableList {
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
