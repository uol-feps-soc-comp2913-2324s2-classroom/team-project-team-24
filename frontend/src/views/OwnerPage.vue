<template>
    <div>
        <div class="header" style="display: flex">
            <h4>Admin</h4>
            <button class="btn-secondary logout-btn" @click="accountLogout">
                logout
            </button>
        </div>
        <topNavRailedAdmin
            @NavElementClicked="handleNavChange"
            class="mt-2 ms-4"
        />
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
import topNavRailedAdmin from '@/components/ui-components/topNavRailedAdmin.vue'

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
            axiosAuth
                .get('/owner/get-owner-membership-data')
                .then((response) => {
                    this.numberOfUsers = response.data.numUsers
                })
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
            localStorage.removeItem('token')
            this.$router.push('/login')
        },
        handleNavChange(id) {
            const id_val = parseInt(id)
            switch (id_val) {
                case 0:
                    this.showUsers()
                    break
                case 1:
                    this.showRevenue()
                    break
            }
        },
    },
    mounted() {
        this.getPageData()
    },
    components: {
        UserInfo,
        RevenueComponent,
        topNavRailedAdmin,
    },
}
</script>

<style>
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
    margin-left: auto;
}
</style>
