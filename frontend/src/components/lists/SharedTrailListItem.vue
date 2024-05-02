<template>
    <div class="trailListItem">
        <div class="d-flex flex-row align-items-center justify-content-between my-2">
            <div class="d-flex flex-row align-items-center justify-content-between nameAndDate me-5">
                <p class="my-0">{{ trail.name }}</p> 
                <p class="my-0">{{ trail.date }}</p>
            </div>
        </div>
        <div class="horizontalLine"></div>
    </div>
</template>

<script>
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

        };
    },
    methods: {

    },
    created() {
        
        this.$emit('trailItemDataUpdated')
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