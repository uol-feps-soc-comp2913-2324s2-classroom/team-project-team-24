<template>
    <ModalComponent :is-Open="modalState" @update:isOpen="closePopup">
        <div class="createGroupContent">
            <form class="d-flex flex-column">
                <h4>Create group</h4>
                <div class="horizontalLine"></div>
                <p class="mt-4 mb-3">Enter a name for your new group</p>
                <div class="form-field mb-4">
                    <label for="name" class="input-label-loud">Group name</label>
                    <input class="text-input-loud" id="name" v-model="name" placeholder="e.g. Vulpes vulpes running group" />
                </div>
                <div class="align-self-end mt-2">
                    <button class="btn-secondary me-3" type="button" @click.prevent="closePopup">Cancel</button>
                    <button class="btn-primary" type="submit" @click.prevent="createGroup">Create group</button>
                </div>
            </form>
        </div>
    </ModalComponent>
</template>

<script>
// import PopupComponent from "@/components/Popup.vue";
import ModalComponent from "@/components/Modal.vue";
import '@/assets/css/form.css';
import axiosAuth from "@/api/axios-auth.js";

export default {
    name: "CreateGroupComponent",
    data() {
        return {
            name: ""
        };
    },
    props: {
        modalState: {
            type: Boolean,
            default: false,
        },
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
        },
    },
    components: {
        ModalComponent,
    },
    mounted() {
        console.log("CreateGroupComponent mounted. Modal state: " + this.modalState);
    }
};
</script>

<style scoped>

/* Small screens */
@media screen and (max-width: 600px){
    .createGroupContent{
        width: 80vw;
    }

    .btn-mobile {
        display: inline;
    }

    .btn-desktop {
        display: none;
    } 
}

/* Medium screens */
@media screen and (min-width: 600px) and (max-width: 900px){
    .createGroupContent {
    width: 50vw;
    }

    .btn-mobile {
        display: none;
    }

    .btn-desktop {
        display: inline;
    }
}

/* Large screens */
@media screen and (min-width: 900px){
    .createGroupContent{
        width: 33vw;
    }

    .btn-mobile {
        display: none;
    }

    .btn-desktop {
        display: inline;
    }
}



p{
    margin: 0;
}
</style>

