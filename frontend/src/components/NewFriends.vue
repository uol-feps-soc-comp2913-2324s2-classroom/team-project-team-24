<template>
    <div>
        <form @submit.prevent="addFriend" class="my-3 d-flex flex-row align-items-center">
            <input id="friend-email" v-model="friend" type="text" class="text-input-loud me-3" placeholder="Enter a Walkeley username to send a friend request" required />
            <button type="submit" class="btn-primary sendRequestButton">Send request</button>
            <h6 style="color:red" v-if="error">{{ error }}</h6>
            <h6 style="color:green" v-if="success">{{ success }}</h6>
            <br/>
            
        </form>
        <!-- <br/> -->
        <!-- <h2>Friend Requests</h2> -->
        <!-- <UserListComponent v-bind:users="friendRequests" :addButtonShowing="true"/> -->
        
        <h4 class="mt-4 mb-3">Friend requests</h4>
        <ListComponent v-bind:dataArray="friendRequests" v-slot="slotProps">
            <UserList2ButtonItemComponent v-bind:user="slotProps.data" :button1="acceptButtonDict" :button2="rejectButtonDict"/>
        </ListComponent>
    </div>
</template>

<script>
import UserList2ButtonItemComponent from "@/components/lists/UserList2ButtonItem.vue";
import ListComponent from "@/components/lists/List.vue";
import axiosAuth from "@/api/axios-auth.js";

export default {
    name: "FindFriendsComponent",
    data() {
        return {
            friendRequests: [],
            error: null,
            success: null,
            acceptButtonDict: {
                action: this.acceptRequest,
                text: "Accept",
            },
            rejectButtonDict: {
                action: this.rejectRequest,
                text: "Reject",
            }
        };
    },
    methods: {
        getPageData() {
            axiosAuth.get('/friends/get-requests').then(
                response => {
                    this.friendRequests = response.data.requests;
                    console.log("FriendRequests: " + this.friendRequests);
                }
            )
        },
        addFriend() {
            axiosAuth.post("/friends/send-request",  {
                receiveUserID: this.friend,
            }).then(() => {
                this.success = "Friend request sent";
                this.error = null;
                this.$parent.getPageData();
            }).catch(error => {
                this.error = error.response.data.error;
                this.success = null;
                console.log(error.response.data.error);
            })
        },
        async acceptRequest(userID) {
            console.log("ID: " + userID);
            await axiosAuth.post("/friends/accept-request",  {
                fromUserID: userID,
            }).catch(error => {
                console.log(error.response.data.error);
            })
            this.getPageData();
            this.$parent.getPageData();
        },
        async rejectRequest(userID) {
            console.log("ID: " + userID);
            await axiosAuth.post("/friends/reject-request",  {
                fromUserID: userID,
            }).catch(error => {
                console.log(error.response.data.error);
            })
            this.getPageData();
            this.$parent.getPageData();
        },
    },
    created() {
        this.getPageData();
    },
    components: {
        ListComponent,
        UserList2ButtonItemComponent,
    }
};
</script>

<style scoped>
.sendRequestButton{
    white-space: nowrap;
    width: auto;
}
</style>

