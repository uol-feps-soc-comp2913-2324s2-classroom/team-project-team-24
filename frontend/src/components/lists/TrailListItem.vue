<template>
    <div class="outer" @click="viewTrail">
      <!-- <div class="content"> -->
        <h3>{{ trailName }}</h3>
        <p>{{ trailDate }}</p>
      <!-- </div> -->
      <div class="buttons">
        <primaryButton @click.stop="downloadTrail">Download</primaryButton>
        <dangerButton @click.stop="deleteTrail">Delete</dangerButton>
      </div>
    </div>
  </template>
  
  <script>
  import primaryButton from '../ui-components/primaryButton.vue';
  import dangerButton from '../ui-components/dangerButton.vue';

  export default {
    name: "TrailListItemComponent",
    props: {
      trail: {
        type: String
      }
    },
    data() {
      return {
        trailName: this.trail,
        trailDate: "25/07/03",
      };
    },
    methods: {
      viewTrail() {
        this.$router.push({ path: "/mytrail", query: { trailName: this.trail } });
      },
      downloadTrail() {
        console.log("downloadTrail");
      },
      deleteTrail() {
        console.log("deleteTrail");
      }
    },
    components: {
        primaryButton,
        dangerButton
    }
  };
  </script>
  
  <style scoped>
  
  .outer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px;
    border-bottom: 1px solid #ddd; /* Add a border bottom for separation */
    cursor: pointer;
  }
  
  .buttons button {
    margin-left: 10px;
    padding: 5px 10px;
    border: none;
    background-color: #007bff;
    color: #fff;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .buttons button:hover {
    background-color: #0056b3;
  }
  </style>
  