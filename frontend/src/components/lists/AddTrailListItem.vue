<template>
    <div class="outer">
        <div>
            <h3>{{ name }}</h3>
            <p>{{ date }}</p>
        </div>
        <button @click.stop="addTrailToGroup">Add</button>
    </div>
</template>

<script>
import axiosAuth from "@/api/axios-auth.js";
export default {
    name: "AddTrailListItemComponent",
    props: {
        trailID: {
            type: Number
        },
        groupID: {
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
        addTrailToGroup() {
            axiosAuth.post('/groups/add-route', {
                groupID: this.groupID,
                trailID: this.trailID,
            })
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