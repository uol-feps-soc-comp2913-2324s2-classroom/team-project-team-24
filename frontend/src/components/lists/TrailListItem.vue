<script>
import primaryButton from '../ui-components/primaryButton.vue';
import dangerButton from '../ui-components/dangerButton.vue';

import axiosAuth from "@/api/axios-auth.js";
export default {
    name: "TrailListItemComponent",
    props: {
        trailID: {
            type: Number
        }
    },
    data() {
        return {
            name: "",
            date: "",
        };
    },
    methods: {
        getPageData() {
            axiosAuth.post('/trail/get-data', {
                trailID: this.trailID,
            }).then(
                response => {
                    this.name = response.data.name;
                    this.date = response.data.date;
                }
            )
        },
        viewTrail() {
            this.$router.push({path: "/mytrail", query: {trailID: this.trailID}});
        },
        downloadTrail() {
            console.log("downloadTrail");
        },
        deleteTrail() {
            axiosAuth.post('/delete-trail', {
                trailID: this.trailID,
            }).then(
                response => {
                    console.log(response.status);
                    this.$parent.$parent.getPageData();
                }
            )
            
        }
    },
    created() {
        this.getPageData();
    },
    components: {
      primaryButton,
      dangerButton,
    }
};
</script>

<template>
  <div class="outer" @click="viewTrail">
      <div class="name-type">
        <h3>{{ trailName }}</h3>
        <h5>{{ trailType }}</h5>
      </div>
      <div class="trail-date">
        <h5>{{ trailDate }}</h5>
      </div>
      <div class="button-container">
        <primaryButton @click.stop="downloadTrail">Download</primaryButton>
        <dangerButton @click.stop="deleteTrail">Delete</dangerButton>
      </div>
  </div>
</template>
  
<style scoped>
.outer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px;
  border-bottom: 1px solid #ddd; /* Add a border bottom for separation */
  cursor: pointer;
}

.name-type {
  display: flex;
  align-items: flex-start; /* Align items vertically at the start */
  align-items: center; /* Align buttons vertically */
}

.name-type h3 {
  margin-right: 20px; /* Add space between trailName and trailType */
  align-items: center; /* Align buttons vertically */
}

.trail-date {
  align-items: center; /* Align buttons vertically */
}
.button-container {
  display: flex;
  align-items: center; /* Align items vertically */
}
.primaryButton {
  margin-right: 15px; /* Add margin to the right of the primary button */
}
.dangerButton {
  margin-left: 7px; /* Add margin to the left of the danger button */
}

</style>
