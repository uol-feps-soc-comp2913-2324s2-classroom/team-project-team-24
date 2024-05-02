<template>
    <div>
        <h2>Find New Friends</h2>
        <form @submit.prevent="addFriend">
            <input id="friend-email" v-model="friend" type="text" placeholder="Enter their email" required />
            <h6 style="color:red" v-if="error">{{ error }}</h6>
            <h6 style="color:green" v-if="success">{{ success }}</h6>
            <br/>
            <button type="submit">Add</button>
        </form>
        <br/>
        <h2>Friend Requests</h2>
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
            })
        },
        async acceptRequest(userID) {
            await axiosAuth.post("/friends/accept-request",  {
                fromUserID: userID,
            }).catch(() => {});
            this.getPageData();
            this.$parent.getPageData();
        },
        async rejectRequest(userID) {
            await axiosAuth.post("/friends/reject-request",  {
                fromUserID: userID,
            }).catch(() => {});
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

