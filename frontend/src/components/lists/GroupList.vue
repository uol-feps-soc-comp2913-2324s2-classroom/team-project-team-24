<template>
    <div>
        <h3 class="my-4">My Groups</h3>
        <GroupListItemComponent v-for="(group, x) in groups" :key="x" v-bind:group="group" />
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

