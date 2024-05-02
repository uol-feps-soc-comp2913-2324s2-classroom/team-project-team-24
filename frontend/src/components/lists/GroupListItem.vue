<template>
    <div @click="showGroup" class="outer">
        <p class="my-3 px-4">{{ group.name }}</p>
        <div class="horizontalLine"></div>
    </div>
</template>

<script>
export default {
    name: "GroupListItemComponent",
    props: {
        group: {
            
        }
    },
    data() {
        return {
            
        };
    },
    methods: {
        showGroup() {
            this.$router.push({path: "/group", query: {groupID: this.group.id}});
        }
    },
};
</script>

<style scoped>
.outer {
    cursor: pointer;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    /* justify-items: flex-start; */
    box-shadow: 0 0 0 var(--selectionRailColor);
    transition: box-shadow 5s;
    transition: background-color 0.2s;
}

.outer:hover {
    box-shadow: 0 0 2px var(--selectionRailColor);
}

p {
    margin: 0;
    padding: 0;
}
</style>
