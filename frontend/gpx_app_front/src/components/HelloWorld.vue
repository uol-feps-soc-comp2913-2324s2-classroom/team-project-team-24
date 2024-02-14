<script>

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      count: 0
    }
  }
}

</script>

<template>
  <h1>{{ msg }}</h1>
</template>

<style scoped>

</style>
