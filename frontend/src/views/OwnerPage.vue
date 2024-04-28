<template>
    <div>
        <!-- 页面上方的黑色容器 -->
        <div class="header">
            <h4>Admin</h4>
        </div>
        <!-- <div>
            <button @click="setCurrentView('UserInfo')">User Info</button>
            <button @click="setCurrentView('Revenue')">Revenue</button>
        </div> -->
        <div style="display: flex">
            <button @click="showUsers">Users Info</button>
            <button @click="showRevenue">Revenue</button>
        </div>
        <!-- 动态显示组件 -->
        <!-- <div v-if="userInfoIsShowing === 'UserInfo'">
            <UserInfo :numberOfUsers="numberOfUsers" />
        </div>
        <div v-if="revenueIsShowing === 'Revenue'">
            <RevenueComponent />
        </div> -->
        <div v-if="userInfoIsShowing">
            <UserInfo :numberOfUsers="numberOfUsers" />
        </div>
        <div v-if="revenueIsShowing">
            <RevenueComponent />
        </div>
        <p>worked</p>
    </div>
</template>

<script>
import UserInfo from '@/components/UserInfo.vue'
import RevenueComponent from '@/components/RevenueComponent.vue'
// import axiosAuth from '@/api/axios-auth.js'

export default {
    data() {
        return {
            userInfoIsShowing: true,
            revenueIsShowing: false,
        }
    },

    methods: {
        // getPageData() {
        //     axiosAuth.get('/UserInfo/get-all').then((response) => {
        //         this.numberOfUsers = response.data.count
        //         console.log('Number of registered users:', this.numberOfUsers)
        //     })
        //     axiosAuth.get('/Revenue/get-all').then((response) => {
        //         this.groups = response.data.groups
        //     })
        // },
        showUsers() {
            this.userInfoIsShowing = true
            this.revenueIsShowing = false
        },
        showRevenue() {
            this.revenueIsShowing = true
            this.userInfoIsShowing = false
        },
    },
    // mounted() {
    //     this.getPageData()
    // },
    components: {
        UserInfo,
        RevenueComponent,
    },
}
</script>

<style>
/* Your existing styles */
.header {
    background-color: black; /* Set the background color to black */
    color: white; /* Set text color to white for better contrast */
    padding: 5px 20px; /* Add some padding */
    width: 100%; /* Make sure it spans the full width */
    box-sizing: border-box; /* Include padding in the width calculation */
}
.numOfUsers {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
}
</style>
