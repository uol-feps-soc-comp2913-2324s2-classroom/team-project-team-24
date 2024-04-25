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
            this.$store.dispatch('auth/logout').then(() => {
                this.$router.push('/login');
            });
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
        <!-- <button type="submit" @click.prevent="accountLogout">Logout</button> -->
    </div>
</template>

<style scoped>
.myAccountPageContainer {
    width: 100%;
    height: 100%;
}
</style>
