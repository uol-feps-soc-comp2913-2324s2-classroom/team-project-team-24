<template>
    <div class="outer" @click="viewTrail">
        <div>
            <h3>{{ name }}</h3>
            <p>{{ date }}</p>
        </div>
        <button @click.stop="downloadTrail">Download</button>
        <button @click.stop="deleteTrail">Delete</button>
    </div>
</template>

<script>
import axiosAuth from "@/api/axios-auth.js";
export default {
    name: "TrailListItemComponent",
    props: {
        trail: {
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
                trailID: this.trail,
            }).then(
                response => {
                    this.name = response.data.name;
                    this.date = response.data.date;
                }
            )
        },
        viewTrail() {
            this.$router.push({path: "/mytrail", query: {trailId: this.trail}});
        },
        downloadTrail() {
            console.log("downloadTrail");
        },
        deleteTrail() {
            axiosAuth.post('/delete-trail', {
                trailID: this.trail,
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
    }
};
</script>

<style>
.outer {
    display: flex;
    cursor: pointer;
}
</style>