<template>
    <div>
        <TrailListItemComponent v-for="(trail, x) in trails" :key="x" v-bind:trail="trail"/>
    </div>
</template>

<script>
import TrailListItemComponent from "@/components/lists/TrailListItem.vue";

export default {
    name: "TrailListComponent",
    props: {
        trails: {
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
        TrailListItemComponent,
        
    }
};
</script>

<style scoped>

.outer:hover {
  background-color: lightgray; /* Change background color on hover */
  border-radius: var(--border-radius);
}
</style>