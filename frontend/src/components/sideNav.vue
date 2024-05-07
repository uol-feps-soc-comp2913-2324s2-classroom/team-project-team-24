<script>
/* 
    Attribution:
    Credit to the original author of the code FireShip
    
    This code was adapted from the following source:
    github.com/fireship-io/222-responsive-icon-nav-css
    Watch the [Responsive CSS Navbar](https://youtu.be/biOMz4puGt8) episode on on youtube
*/

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
    <nav class="navbar">
        <ul class="navbarNav">
            <li class="logo">
                <router-link :to="{ name: 'Welcome' }" class="navLink">
                    <img src="../assets/Logo.svg" alt="Logo" class="navLogo">
                    <span class="navText logoText">Walkley</span>
                </router-link>
            </li>

            <li class="nav-item">
                <router-link :to="{ name: 'UploadTrail' }" class="navLink">
                    <img src="../assets/upload_icon.svg" alt="Trail Icon" class="navIcons">
                    <span class="navText">Upload&nbsp;Trail</span>
                    <span class="navTextMobile">Upload</span>
                </router-link>
            </li>

            <li class="nav-item">
                <router-link :to="{ name: 'Activity' }" class="navLink">
                    <img src="../assets/activity_icon.svg" alt="Activity Icon" class="navIcons">
                    <span class="navText">Activity</span>
                    <span class="navTextMobile">Activity</span>
                </router-link>
            </li>

            <li class="nav-item">
                <router-link :to="{ name: 'Community' }" class="navLink">
                    <img src="../assets/community_icon.svg" alt="Community Icon" class="navIcons">
                    <span class="navText">Community</span>
                    <span class="navTextMobile">Community</span>
                </router-link>
            </li>

            <li class="nav-item">
                <router-link :to="{ name: 'Membership' }" class="navLink">
                    <img src="../assets/membership_icon.svg" alt="Membership Icon" class="navIcons">
                    <span class="navText">Membership</span>
                    <span class="navTextMobile">Membership</span>
                </router-link>
            </li>

            <li class="nav-item">
                <router-link :to="{ name: 'Account' }" class="navLink">
                    <img src="../assets/user_icon.svg" alt="Account Icon" class="navIcons">
                    <span class="navText">My&nbsp;Account</span>
                    <span class="navTextMobile">Account</span>
                </router-link>
            </li>
        </ul>
    </nav>
</template>

<style scoped></style>
