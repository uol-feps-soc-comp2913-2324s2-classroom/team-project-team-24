<template>
    <div>
        <UserListItemComponent v-for="(user) in users" :key="user" v-bind:user="user" :button="button" />
    </div>
</template>

<script>
import UserListItemComponent from "@/components/lists/UserListItem.vue";

export default {
    name: "UserListComponent",
    props: {
        users: {
            type: Array
        },
        button: {
            default: {
                action: null,
                text: null,
            },
        }
    },
    data() {
        return {
            
        };
    },
    methods: {
        
    },
    components: {
        UserListItemComponent,
    }
};
</script>

