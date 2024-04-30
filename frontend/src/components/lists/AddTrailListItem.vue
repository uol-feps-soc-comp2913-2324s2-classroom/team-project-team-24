<template>
    <div class="trailListItem">
        <div class="d-flex flex-row align-items-center justify-content-between my-2">
            <div class="d-flex flex-row align-items-center justify-content-between nameAndDate me-5">
                <p class="my-0">{{ name }}</p> 
                <p class="my-0">{{ date }}</p>
            </div>
            <button @click.stop="addTrailToGroup" class="btn-quiet">Add</button>
        </div>
        <div class="horizontalLine"></div>
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
                    console.log("trailItemDataUpdated")
                    this.$emit('trailItemDataUpdated')
                }
            )
        },
        addTrailToGroup() {
            axiosAuth.post('/groups/add-route', {
                groupID: this.groupID,
                routeID: this.trailID,
            })
        }
        
    },
    created() {
        this.getPageData();
    },
};
</script>

<style>
.nameAndDate{
    width: 100%;
}
.trailListItem {
    width: 100%;
    display: flex;
    flex-direction: column;
    /* justify-items: flex-start; */
    box-shadow: 0 0 0 var(--selectionRailColor);
    transition: box-shadow 5s;
    transition: background-color 0.2s;
}

.trailListItem:hover {
    box-shadow: 0 0 2px var(--selectionRailColor);
}

p {
    margin: 0;
}
</style>