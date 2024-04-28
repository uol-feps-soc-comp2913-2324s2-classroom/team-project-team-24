<template>
    <div style="display: flex;" class="userListItem2Buttons">
        <!-- <div class="horizontalLine"></div> -->
        <div class="userListUNameandButton my-2 px-4">
            <p>{{ this.user.name }}</p>
            <div class="2buttons">
                <button v-if="this.button1.text !== null" class="btn-quiet-action-blue me-5" @click.prevent="this.button1.action(this.user.id)">{{ this.button1.text }}</button>
                <button v-if="this.button2.text !== null" class="btn-quiet-danger" @click.prevent="this.button2.action(this.user.id)">{{ this.button2.text }}</button>
            </div>
        </div>
        <div class="horizontalLine"></div>
    </div>
</template>

<script>
export default {
    name: "UserList2ButtonItemComponent",
    props: {
        user: {
            
        },
        button1: {
            default: {
                action: {
                    type: Function 
                },
                text: null,
            },
        },
        button2: {
            default: {
                action: {
                    type: Function 
                },
                text: null,
            },
        }
    },
    data() {
        return {
            testimg: "",
            name: this.user
        };
    },
    methods: {
        blank() {},
    },
};
</script>

<style scoped>
.userListItem2Buttons{
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    box-shadow: 0 0 0 var(--selectionRailColor);
    transition: box-shadow 5s;
    transition: background-color 0.2s;
}

.userListItem2Buttons:hover {
    box-shadow: 0 0 2px var(--selectionRailColor);
}

.userListUNameandButton {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    width: 100%;
}

p {
    margin: 0;
    padding: 0;
}
</style>

