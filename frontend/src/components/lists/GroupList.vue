<template>
    <div>
        <GroupListItemComponent v-for="(group) in groups" :key="group" v-bind:group="group" />
    </div>
</template>

<script>
import GroupListItemComponent from "@/components/lists/GroupListItem.vue";

export default {
    name: "GroupListComponent",
    props: {
        groups: {
            type: Array
        }
    },
    data() {
        return {
            
        };
    },
    methods: {
        
    },
    components: {
        GroupListItemComponent,
    }
};
</script>

