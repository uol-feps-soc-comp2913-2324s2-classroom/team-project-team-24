<template>
    <div class="communityPageContainer p-4" id="communityPageContainer">
        <topNavRailed @NavElementClicked="navElementClicked" id="topNav" />
        <div class="columns" id="columnsContainer">
            <h4 class="mt-4 mb-3" v-if="friendsIsShowing">My friends</h4>
            <div
                class="groupNavigations mt-4 mb-3"
                v-if="groupsIsShowing"
                id="groupNav"
            >
                <h4 class="">My groups</h4>
                <button
                    @click="createGroup"
                    class="btn-primary createGroupButton"
                >
                    <div class="buttonText">
                        <img
                            src="../assets/add.svg"
                            class="addIcon"
                            alt="plus icon"
                        />
                        <p>Create group</p>
                    </div>
                </button>
            </div>

            <ListComponent
                v-if="friendsIsShowing && friends.length > 0"
                v-bind:dataArray="friends"
                v-slot="slotProps"
            >
                <UserListItemComponent
                    v-bind:user="slotProps.data"
                    :button="buttonDict"
                />
            </ListComponent>
            <p
                v-if="
                    friendsIsShowing &&
                    friends.length == 0 &&
                    !loadingFriendsList
                "
                class="greyText"
            >
                You haven't add anyone as friends yet...
            </p>
            <p v-if="friendsIsShowing && loadingFriendsList" class="greyText">
                Loading friends...
            </p>

            <ListComponent
                v-if="groupsIsShowing"
                v-bind:dataArray="groups"
                v-slot="slotProps"
            >
                <GroupListItemComponent v-bind:group="slotProps.data" />
            </ListComponent>

            <p
                v-if="
                    groupsIsShowing && groups.length == 0 && !loadingGroupsList
                "
                class="greyText"
            >
                You haven't joined any groups yet. Create a group and start
                sharing your trails!
            </p>
            <CreateGroupComponent :modal-state="createGroupIsShowing" />

            <NewFriendsComponent v-if="addFriendsIsShowing" />
        </div>
    </div>
</template>
<script>
import UserListItemComponent from '@/components/lists/UserListItem.vue'
import ListComponent from '@/components/lists/List.vue'
import GroupListItemComponent from '@/components/lists/GroupListItem.vue'
import NewFriendsComponent from '@/components/NewFriends.vue'
import topNavRailed from '@/components/ui-components/topNavRailedCommunity.vue'
import CreateGroupComponent from '@/components/forms/CreateGroup.vue'
import axiosAuth from '@/api/axios-auth.js'

export default {
    name: 'CommunityCenter',
    data() {
        return {
            friendsIsShowing: true,
            groupsIsShowing: false,
            createGroupIsShowing: false, // For the modal
            friendRequestsIsShowing: false,
            friends: [],
            groups: [],
            friendRequests: [],
            buttonDict: {
                text: 'Remove',
                action: this.removeFriend,
            },
            loadingFriendsList: true,
            loadingGroupsList: true,
        }
    },
    methods: {
        navElementClicked(id) {
            id = parseInt(id)
            switch (id) {
                case 0:
                    console.log('Friends')
                    this.showFriends()
                    break
                case 1:
                    console.log('Groups')
                    this.showGroups()
                    break
                case 3:
                    console.log('Friend Requests')
                    this.showFriendRequests()
                    break
                case 2:
                    console.log('Add Friends')
                    this.showAddFriends()
                    break
                default:
                    console.log('Unknown')
                    break
            }
        },
        getPageData() {
            this.loadingFriendsList = true
            this.loadingGroupsList = true

            axiosAuth.get('/friends/get-all').then((response) => {
                this.friends = response.data.friends
                this.loadingFriendsList = false
            })
            axiosAuth.get('/groups/get-all').then((response) => {
                this.groups = response.data.groups
                this.loadingGroupsList = false
            })
        },
        showFriends() {
            this.friendsIsShowing = true
            this.groupsIsShowing = false
            this.friendRequestsIsShowing = false
            this.addFriendsIsShowing = false
        },
        showGroups() {
            this.friendsIsShowing = false
            this.groupsIsShowing = true
            this.friendRequestsIsShowing = false
            this.addFriendsIsShowing = false
        },
        showFriendRequests() {
            this.friendsIsShowing = false
            this.groupsIsShowing = false
            this.friendRequestsIsShowing = true
            this.addFriendsIsShowing = false
        },
        showAddFriends() {
            this.friendsIsShowing = false
            this.groupsIsShowing = false
            this.friendRequestsIsShowing = false
            this.addFriendsIsShowing = true
        },
        createGroup() {
            this.createGroupIsShowing = true
        },
        closeCreateGroup() {
            this.createGroupIsShowing = false
        },
        async removeFriend(userID) {
            await axiosAuth
                .post('/friends/remove', {
                    friendID: userID,
                })
                .catch(() => {})
            this.getPageData()
        },
    },
    created() {
        this.getPageData()
    },
    components: {
        UserListItemComponent,
        ListComponent,
        NewFriendsComponent,
        topNavRailed,
        CreateGroupComponent,
        GroupListItemComponent,
    },
}
</script>

<style scoped>
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

.groupNavigations {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}

h4 {
    margin: 0;
    padding: 0;
}
</style>
