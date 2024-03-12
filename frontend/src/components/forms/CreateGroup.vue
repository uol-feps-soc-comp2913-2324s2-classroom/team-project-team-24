<template>
    <form>
        <div class="inner-container">
            <button @click="closeWindow" style="float:right;">X</button>
            <h2>Create your group</h2>
            <div class="form-field">
                <label for="name">Group: </label>
                <input class="text-input" id="name" v-model="text" placeholder="Group name" />
            </div>
            <button class="submit-button" type="submit" @click.prevent="createGroup">Create</button>
        </div>
    </form>
</template>

<script>
import '@/assets/css/form.css'

export default {
    name: "CreateGroupComponent",
    data() {
        return {
            name: ""
        };
    },
    methods: {
        createGroup() {

        },
        closeWindow() {
            this.$parent.closeCreateGroup();
        }
    },
};
</script>

