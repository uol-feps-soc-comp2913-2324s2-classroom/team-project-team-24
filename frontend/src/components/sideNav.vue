<script>

export default {
    name: "SideNavComponent",
    data() {
        return {

        };
    },
    methods: {

    },
    components: {

    },
};
</script>

<template>
    <nav class="sideNav">
        <ul class="navList">
            <li class="navItem navItemLogo">
                <router-link :to="{ name: 'UploadTrail' }" class="navLink">
                    <img src="../assets/Logo.svg" alt="Logo" class="navLogo">
                    <span class="navText logoText">Walkley</span>
                </router-link>
            </li>
            <li class="navItem navItemLinkContainer navItemBoldOnSelect">
                <router-link :to="{ name: 'UploadTrail' }" class="navLink">
                    <img src="../assets/tracks_icon.svg" alt="Trail Icon" class="navIcons">
                    <span class="navText">Upload Trail</span>
                </router-link>
            </li>
            <li class="navItem navItemLinkContainer navItemBoldOnSelect">
                <router-link :to="{ name: 'Activity' }" class="navLink">
                    <img src="../assets/activity_icon.svg" alt="Activity Icon" class="navIcons">
                    <span class="navText">Activity</span>
                </router-link>
            </li>
            <li class="navItem navItemLinkContainer navItemBoldOnSelect">
                <router-link :to="{ name: 'Community' }" class="navLink">
                    <img src="../assets/community_icon.svg" alt="Community Icon" class="navIcons">
                    <span class="navText">Community</span>
                </router-link>
            </li>
            <li class="navItem navItemLinkContainer navItemBoldOnSelect">
                <router-link :to="{ name: 'Membership' }" class="navLink">
                    <img src="../assets/membership_icon.svg" alt="Membership Icon" class="navIcons">
                    <span class="navText">Membership</span>
                </router-link>
            </li>
            <li class="navItem navItemLinkContainer navItemBoldOnSelect">
                <router-link :to="{ name: 'Account' }" class="navLink">
                    <img src="../assets/community_icon.svg" alt="Account Icon" class="navIcons">
                    <span class="navText">My Account</span>
                </router-link>
            </li>
        </ul>
    </nav>
</template>

<style scoped></style>
