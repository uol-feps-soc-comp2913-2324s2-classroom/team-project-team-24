<template>
  <div class="trail-list-item" @click="viewTrail">
    <div class="trail-info">
      <h3>{{ trail.name }}</h3>
      <p>{{ trail.date }}</p>
      <p>{{ trail.type }}</p>
    </div>
    <div class="button-container">
      <button class="btn-primary" @click.stop="downloadTrail">Download</button>
      <button class="btn-danger" @click.stop="deleteTrail">Delete</button>
    </div>
  </div>
</template>

<script>
import axiosAuth from "@/api/axios-auth.js";

export default {
  name: "TrailListItem",
  props: {
    trail: {
      type: Object,
      required: true,
    },
  },
  methods: {
    viewTrail() {
      this.$router.push({ path: "/mytrail", query: { trailID: this.trail.id } });
    },
    downloadTrail() {
      // Implement the logic to download the trail data
      console.log("Download trail:", this.trail.id);
    },
    deleteTrail() {
      axiosAuth
        .post("/trail/delete", { trailID: this.trail.id })
        .then((response) => {
          console.log("Trail deleted:", response.data);
          this.$emit("trail-deleted", this.trail.id);
        })
        .catch((error) => {
          console.error("Error deleting trail:", error);
        });
    },
  },
};
</script>

<style scoped>
.trail-list-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #ddd;
  cursor: pointer;
}

.trail-info {
  flex-grow: 1;
}

.button-container {
  display: flex;
  gap: 10px;
}


</style>