<template>
    <div>
        <h3 class="my-4">Find new friends</h3>
        <form @submit.prevent="addFriend">
            <input id="friend-email" v-model="friend" type="text" placeholder="Enter their email" required />
            <h6 style="color:red" v-if="error">{{ error }}</h6>
            <h6 style="color:green" v-if="success">{{ success }}</h6>
            <br/>
            <!-- <button type="submit">Add</button>
             -->
        </form>
        <br/>
        <!-- <h2>Friend Requests</h2> -->
        <!-- <UserListComponent v-bind:users="friendRequests" :addButtonShowing="true"/> -->
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

