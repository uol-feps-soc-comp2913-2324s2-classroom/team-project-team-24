<script>

export default {
  name: "SideNav",
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
<div class="sideNav">
    <ul class="navList">
        <li class="navItem">
            <router-link :to="{ name: 'MyTrail'}">My Trail</router-link>
            <img src="../assets/Smock_ImageMapPolygon_18_N.svg" alt="Trails Icon" class="navIcons">
        </li>
        <li class="navItem">
            <router-link :to="{ name: 'Activity'}">Activity</router-link>
            <img src="../assets/Run.svg" >
        </li>
        <li class="navItem">
            <router-link :to="{ name: 'Community'}">Community</router-link>
            <img src="../assets/Smock_PeopleGroup_18_N.svg" alt="Community Icon" class="navIcons">
        </li>
        <li class="navItem">
            <router-link :to="{ name: 'Membership'}">Membership</router-link>
            <img src="../assets/Membership.svg" alt="Membership Icon" class="navIcons">
        </li>
        <li class="navItem">
            <router-link :to="{ name: 'Account'}">My Account</router-link>
        </li>
    </ul>

</div>
</template>

<style scoped></style>
