<template>
    <div class="trailListItem">
        <div
            class="d-flex flex-row align-items-center justify-content-between my-2 px-2"
        >
            <div
                class="d-flex flex-row align-items-center justify-content-between nameAndDate me-5"
            >
                <p class="my-0">{{ trail.name }}</p>
                <p class="my-0">{{ trail.date }}</p>
            </div>
            <button
                v-if="!addingToGroup"
                @click.stop="addTrailToGroup"
                class="btn-tertiary"
            >
                Add
            </button>
            <button v-else class="btn-tertiary-disabled">Adding...</button>
        </div>
        <div class="horizontalLine"></div>
    </div>
</template>

<script>
import axiosAuth from '@/api/axios-auth.js'
export default {
    name: 'AddTrailListItemComponent',
    props: {
        trail: {},
        groupID: {
            type: Number,
        },
    },
    data() {
        return {
            addingToGroup: false,
        }
    },
    methods: {
        getPageData() {
            console.log('=================', this.trail)
        },
        addTrailToGroup() {
            this.addingToGroup = true
            axiosAuth
                .post('/groups/add-route', {
                    groupID: this.groupID,
                    routeID: this.trail.id,
                })
                .then(() => {
                    this.$emit('trailAddedToGroup')
                })
        },
    },
    created() {
        this.$emit('trailItemDataUpdated')
    },
}
</script>

<style>
.btn-tertiary-disabled {
    background-color: var(--tertiary-button-grey);
    border-style: solid;
    border-color: var(--tertiary-button-grey);
    border-width: 3px;
    font-weight: bold;
    color: var(--secondary-button-offBlack);
    padding-top: var(--button-padding-vertical);
    padding-bottom: var(--button-padding-vertical);
    padding-left: var(--button-padding-horizontal);
    padding-right: var(--button-padding-horizontal);
    text-align: center;
    text-decoration: none;
    display: inline-block;
    transition: background-color 0.2s, border-color 0.2s, color 0.2s;
    cursor: default;
    border-radius: 99999px;
}

.nameAndDate {
    width: 100%;
}
.trailListItem {
    width: 100%;
    display: flex;
    flex-direction: column;
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
