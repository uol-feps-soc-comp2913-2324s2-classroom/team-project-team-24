<script>
import AccountDetailsComponent from "@/components/AccountDetails.vue";

export default {
    name: "MyAccount",
    data() {
        return {

        };
    },
    methods: {
        accountLogout() {
            localStorage.removeItem('token');
            this.$router.push("/login");
        }
    },
    components: {
        AccountDetailsComponent,
    },
};
</script>

<template>
    <div class="myAccountPageContainer p-5 d-flex flex-column overflowScroll">
        <h1>My Account</h1>
        <span class="mt-2"><button class="btn-secondary" @click="accountLogout">Logout</button></span>
        <AccountDetailsComponent />
    </div>
</template>

<style scoped>
.myAccountPageContainer {
    width: 100%;
    height: 100%;
}
</style>
