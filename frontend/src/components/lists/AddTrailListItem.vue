<template>
    <div class="trailListItem">
        <div class="d-flex flex-row align-items-center justify-content-between my-2">
            <div class="d-flex flex-row align-items-center justify-content-between nameAndDate me-5">
                <p class="my-0">{{ trail.name }}</p> 
                <p class="my-0">{{ trail.date }}</p>
            </div>
            <button v-if="!addedToGroup" @click.stop="addTrailToGroup" class="btn-quiet">Add</button>
            <button v-if="addedToGroup" @click.stop="" class="btn-quiet disabled">Added</button>
        </div>
        <div class="horizontalLine"></div>
    </div>
</template>

<script>
import axiosAuth from "@/api/axios-auth.js";
export default {
    name: "AddTrailListItemComponent",
    props: {
        trail: {},
        groupID: {
            type: Number
        }
    },
    data() {
        return {
            addedToGroup : false
        };
    },
    methods: {
        getPageData() {
            console.log("=================", this.trail);
        },
        addTrailToGroup() {
            // this.addedToGroup = true
            axiosAuth.post('/groups/add-route', {
                groupID: this.groupID,
                routeID: this.trail.id,
            })
            this.$emit('trailAddedToGroup')
        }
        
    },
    created() {
        this.$emit('trailItemDataUpdated')
    },
};
</script>

<style>
.disabled {
    cursor: pointer;
    background-color: var(--disabledButtonColor);
    color: var(--disabledButtonTextColor);
}

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