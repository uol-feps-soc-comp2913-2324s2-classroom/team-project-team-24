<script>
import AccountDetailsComponent from "@/components/AccountDetails.vue";
import secondaryButton from "@/components/ui-components/secondaryButton.vue";
// import tertiaryButton from "@/components/ui-components/tertiaryButton.vue";
// import textButton from "@/components/ui-components/textButton.vue";

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
        secondaryButton,
    },
};
</script>

<template>
    <div class="myAccountPageContainer p-5 d-flex flex-column overflowScroll">
        <h1>My Account</h1>
        <span class="mt-2"><secondaryButton :on-click="this.accountLogout">Logout</secondaryButton></span>
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
