<template>
    <div style="display: flex" class="friendItem">
        <div class="friendNameandAction my-2 px-4">
            <p>{{ this.user.name }}</p>
            <button
                class="btn-tertiary"
                v-if="this.button.text !== null"
                @click.prevent="this.button.action(this.user.id)"
            >
                {{ this.button.text }}
            </button>
        </div>
        <div class="horizontalLine"></div>
    </div>
</template>

<script>
export default {
    name: 'UserListItemComponent',
    props: {
        user: {},
        button: {
            default: {
                action: {
                    type: Function,
                },
                text: null,
            },
        },
    },
    data() {
        return {
            testimg: '',
            name: this.user,
        }
    },
    methods: {
        blank() {},
        invitingFriendToGroup() {
            this.$emit('invitingFriendToGroup')
        },
    },
}
</script>

<style scoped>
.friendItem {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    transition: box-shadow 0.2s;
    transition: background-color 0.2s;
}

.friendItem:hover {
    box-shadow: 0 0 2px var(--selectionRailColor);
}

.friendNameandAction {
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
