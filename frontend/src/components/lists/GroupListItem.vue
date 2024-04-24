<template>
    <div @click="showGroup" class="outer">
        <h4>{{ group.name }}</h4>
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

<style>
.outer {
    display: flex;
    cursor: pointer;
}
</style>
