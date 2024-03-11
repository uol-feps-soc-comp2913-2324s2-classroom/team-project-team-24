<script>

export default {
  name: "MembershipCenter",
  data() {
    return {

    };
  },
  methods: {
    onSubmit() {
      this.$store.dispatch('auth/logout').then(() => {
        this.$router.push('/login');
      });
    }
  },
  components: {

  },
};
</script>

<template>
  <div class="membershipPageContainer">
    <h1>Membership Page</h1>
    <button type="submit" @click.prevent="onSubmit">Logout</button>
  </div>
</template>

<style scoped></style>
