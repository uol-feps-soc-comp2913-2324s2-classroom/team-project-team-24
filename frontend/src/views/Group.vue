<script>
import MapViewerComponent from "@/components/MapViewer.vue";
// import PopupComponent from "@/components/Popup.vue";
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
            loading: true,
        };
    },
    methods: {
        async getPageData() {
            const getMembersPromise = axiosAuth.post('/groups/get-members', {
                groupID: this.groupID
            }).then(
                response => {
                    this.members = response.data.members;
                }
            );

            const getNamePromise = axiosAuth.post('/groups/get-name', {
                groupID: this.groupID
            }).then(
                response => {
                    this.name = response.data.name;
                }
            );

            const getAllFriendsPromise = axiosAuth.get('/friends/get-all').then(
                response => {
                    this.friends = response.data.friends;
                }
            );

            const getTrailsPromise = axiosAuth.get('/trail/get-all').then(
                response => {
                    this.trails = response.data.trails;
                }
            );

            const getCurrentUsernamePromise = axiosAuth.get('/account/get-details').then(
                response => {
                    this.username = response.data.name;
                }
            );

            await Promise.all([getMembersPromise, getNamePromise, getAllFriendsPromise, getTrailsPromise, getCurrentUsernamePromise]);

            // Filter out friends that are already in the group
            this.friendsNonMembers = this.friends.filter(friend => {
                return !this.members.some(member => member.userID === friend.userID);
            });

            // Filter out the current user from the members list
            this.members = this.members.filter( member => {
                return member.name !== this.username;
            });

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
        }

    },
    components: {
        MapViewerComponent,
        UserListItemComponent,
        ListComponent,
        ModalComponent,
        // PopupComponent,
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
                <h3>{{ name }}</h3>
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
            <!-- <PopupComponent :closeWindow="closeTrailsPopup" style="float:right;" v-if="showTrails"> -->
            <ModalComponent :is-open="showTrails" @update:is-open="showTrails = $event">
                <div class="addTrailsModalWindow d-flex flex-column">
                    <h3>Add Trails</h3>
                    <div class="horizontalLine mb-3"></div>
                    <div class="scrollableList mb-4">
                        <ListComponent v-bind:dataArray="trails" v-slot="slotProps" v-if="trails.length > 0">
                            <AddTrailListItemComponent class="slightlySmaller" v-bind:trailID="slotProps.data" :groupID="groupID"/>
                        </ListComponent>
                        <p v-if="trails.length == 0" class="greyText align-self-start">No trails available</p>
                    </div>
                    <button @click="closeTrailsPopup" class="btn-secondary align-self-end mt-2">Close</button>
                </div>
            </ModalComponent>
            <!-- </PopupComponent> -->

            <!-- <PopupComponent :closeWindow="closeFriendsPopup" style="float:right;" v-if="showFriends"> -->
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
                    <div v-if="groupModalShowAddMembers">
                        <ListComponent v-bind:dataArray="friendsNonMembers" v-slot="slotProps" v-if="friendsNonMembers.length > 0">
                            <UserListItemComponent v-bind:user="slotProps.data" :button="buttonDict"/>
                        </ListComponent>
                        <p v-if="friendsNonMembers.length == 0" class="greyText">You have added all your friends to this group</p>
                    </div>
                    <button @click="closeFriendsPopup" class="btn-secondary align-self-end mt-2">Close</button>
                </div>
            </ModalComponent>
            <!-- </PopupComponent> -->
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
