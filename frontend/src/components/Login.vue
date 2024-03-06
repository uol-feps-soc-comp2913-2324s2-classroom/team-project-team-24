<template>
    <form @submit="login">
      <input v-model="username" placeholder="Username">
      <input v-model="password" type="password">
      <input type="submit" value="Submit">
    </form>
  </template>
  
  <script>
  import { mapActions, mapGetters } from 'vuex'
  export default {
    data: () => ({
      user: {
        username: null,
        password: null
      }
    }),
    computed: {
      ...mapGetters({
        authUser: 'auth/user'
      })
    },
    methods: {
      ...mapActions({
        loginUser: 'auth/loginUser'
      }),
      async login() {
        await this.loginUser(this.user)
          .then(() => {
            if (this.authUser.authenticated) {
              this.$router.push('/secure')
            } else {
              // Handle error
              this.user = {
                username: null,
                password: null
              }
            }
          })
        
      }
    }
  }
  </script>