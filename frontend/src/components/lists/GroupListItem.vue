<template>
    <div @click="showGroup" class="outer">
        <h4>{{ group }}</h4>
    </div>
</template>

<script>
export default {
    name: "GroupListItemComponent",
    props: {
        group: {
            type: String
        }
    },
    data() {
        return {
            
        };
    },
    methods: {
        showGroup() {
            this.$router.push({path: "/group", query: {groupName: this.group}});
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
