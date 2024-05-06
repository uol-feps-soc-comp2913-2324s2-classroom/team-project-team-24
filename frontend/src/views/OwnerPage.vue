<template>
    <div>
        <div class="header" style="display: flex">
            <h4>Admin</h4>
            <button class="btn-secondary logout-btn"  @click="accountLogout">logout</button>
        </div>
        <div class="button" style="display: flex">
            <button @click="showUsers">Users Info</button>
            <button @click="showRevenue">Revenue</button>
        </div>
        <div v-if="userInfoIsShowing">
            <UserInfo :numberOfUsers="numberOfUsers" />
        </div>
        <div v-if="revenueIsShowing">
            <RevenueComponent />
        </div>
    </div>
</template>

<script>
import UserInfo from '@/components/UserInfo.vue'
import RevenueComponent from '@/components/RevenueComponent.vue'
import axiosAuth from '@/api/axios-auth.js'

export default {
    data() {
        return {
            userInfoIsShowing: true,
            revenueIsShowing: false,
            numberOfUsers: 0,
        }
    },

    methods: {
        getPageData() {
            axiosAuth.get('/owner/get-owner-membership-data').then(
                response => {
                    this.numberOfUsers = response.data.numUsers;
                }
            )
        },
        showUsers() {
            this.userInfoIsShowing = true
            this.revenueIsShowing = false
        },
        showRevenue() {
            this.revenueIsShowing = true
            this.userInfoIsShowing = false
        },
        accountLogout() {
            localStorage.removeItem('token');
            this.$router.push("/login");
        },
    },
    mounted() {
        this.getPageData()
    },
    components: {
        UserInfo,
        RevenueComponent,
    },
}
</script>

<style>
/* Your existing styles */
.header {
    background-color: black;
    color: white;
    padding: 5px 20px;
    width: 100%;
    box-sizing: border-box;
}
.button {
    margin-right: 10px;
    padding: 10px;
    color: white;
    border: none;
    cursor: pointer;
    border-bottom: 1px solid black;
    border: none;
}
.numOfUsers {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
}

.logout-btn {
    /* float: right; */
    margin-left: auto;
}
</style>
