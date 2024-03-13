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
    <div class="myAccountPageContainer">
        <h1>My Account Page</h1>
        <AccountDetailsComponent />
        <button type="submit" @click.prevent="accountLogout">Logout</button>
    </div>
</template>

<style scoped></style>
