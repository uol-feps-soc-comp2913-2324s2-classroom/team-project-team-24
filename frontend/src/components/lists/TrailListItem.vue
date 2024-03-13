<template>
    <div class="outer" @click="viewTrail">
        <div>
            <h3>{{ trailName }}</h3>
            <p>{{ trailDate }}</p>
        </div>
        <button @click.stop="downloadTrail">Download</button>
        <button @click.stop="deleteTrail">Delete</button>
    </div>
</template>

<script>
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
            this.$router.push({path: "/mytrail", query: {trailName: this.trail}});
        },
        downloadTrail() {
            console.log("downloadTrail");
        },
        deleteTrail() {
            console.log("deleteTrail");
        }
    },
};
</script>

<style>
.outer {
    display: flex;
    cursor: pointer;
}
</style>