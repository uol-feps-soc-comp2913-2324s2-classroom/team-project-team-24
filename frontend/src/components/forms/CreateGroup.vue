<template>
    <PopupComponent>
        <form>
            <h2>Create your group</h2>
            <div class="form-field">
                <label for="name">Group: </label>
                <input class="text-input" id="name" v-model="name" placeholder="Group name" />
            </div>
            <button class="submit-button" type="submit" @click.prevent="createGroup">Create</button>
        </form>
    </PopupComponent>
</template>

<script>
import PopupComponent from "@/components/Popup.vue";
import '@/assets/css/form.css';
import axiosAuth from "@/api/axios-auth.js";

export default {
    name: "CreateGroupComponent",
    data() {
        return {
            name: ""
        };
    },
    methods: {
        async createGroup() {
            await axiosAuth.post("/groups/create", {
                groupName: this.name,
            }).then(
                this.closePopup(),
            )
            this.$parent.getPageData();
        },
        closePopup() {
            this.$parent.closeCreateGroup();
        }
    },
    components: {
        PopupComponent,
    },
};
</script>

