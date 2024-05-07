<template>
    <div>
        <form
            @submit.prevent="addFriend"
            class="my-3 d-flex flex-row align-items-center"
        >
            <div class="sendRequestField d-flex flex-column me-3">
                <input
                    id="friend-email"
                    v-model="friend"
                    type="text"
                    class="text-input-loud me-3"
                    placeholder="Enter a Walkley username to send a friend request"
                    required
                    @input="removeErrorText"
                />
                <h6 style="color: red" class="mt-1" v-if="error">
                  {{ error }}
                </h6>
                <h6 style="color: green" class="mt-1" v-if="success">
                  {{ success }}
                </h6>
        
            </div>
            <button
                type="submit"
                class="btn-primary sendRequestButton align-self-start"
            >
                Send request
            </button>
            <br />
        </form>

        <h4 class="mt-4 mb-3">Friend requests</h4>
        <ListComponent
            v-bind:dataArray="friendRequests"
            v-slot="slotProps"
            v-if="friendRequests.length > 0"
        >
            <UserList2ButtonItemComponent
                v-bind:user="slotProps.data"
                :button1="acceptButtonDict"
                :button2="rejectButtonDict"
            />
        </ListComponent>
        <p
            v-if="friendRequests.length == 0 && !loadingFriendRequests"
            class="greyText"
        >
            You have no incoming friend requests
        </p>
        <p v-if="loadingFriendRequests" class="greyText">
            Loading friend requests...
        </p>
    </div>
</template>

<script>
import UserList2ButtonItemComponent from '@/components/lists/UserList2ButtonItem.vue'
import ListComponent from '@/components/lists/List.vue'
import axiosAuth from '@/api/axios-auth.js'

export default {
    name: 'FindFriendsComponent',
    data() {
        return {
            friendRequests: [],
            error: null,
            success: null,
            acceptButtonDict: {
                action: this.acceptRequest,
                text: 'Accept',
            },
            rejectButtonDict: {
                action: this.rejectRequest,
                text: 'Reject',
            },
            loadingFriendRequests: true,
        }
    },
    methods: {
        getPageData() {
            axiosAuth.get('/friends/get-requests').then((response) => {
                this.friendRequests = response.data.requests
                this.loadingFriendRequests = false
            })
        },
        addFriend() {
            axiosAuth
                .post('/friends/send-request', {
                    receiveUserID: this.friend,
                })
                .then(() => {
                    this.success = 'Friend request sent'
                    this.error = null
                    this.$parent.getPageData()
                })
                .catch((error) => {
                    this.error = error.response.data.error
                    this.success = null
                })
        },
        async acceptRequest(userID) {
            await axiosAuth
                .post('/friends/accept-request', {
                    fromUserID: userID,
                })
                .catch(() => {})
            this.getPageData()
            this.$parent.getPageData()
        },
        async rejectRequest(userID) {
            await axiosAuth
                .post('/friends/reject-request', {
                    fromUserID: userID,
                })
                .catch(() => {})
            this.getPageData()
            this.$parent.getPageData()
        },
        removeErrorText() {
            this.error = null;
            this.success = null;
        }
    },
    created() {
        this.getPageData()
    },
    components: {
        ListComponent,
        UserList2ButtonItemComponent,
    },
}
</script>

<style scoped>
.sendRequestField {
    width: 100%;
}

.sendRequestButton {
    white-space: nowrap;
    width: auto;
}
</style>
