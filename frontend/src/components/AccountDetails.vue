<script>
import dangerButton from './ui-components/dangerButton.vue';
import secondaryButton from './ui-components/secondaryButton.vue';

export default {
    name: "GoalComponent",
    data() {
        return {
            name: "Person",
            membershipTier: "Freemium",
            gender: "Male",
            age: 25,
            email: "test@gmail.com",
            membership: "Monthly"
        };
    },
    methods: {
        getAccountDetails() {
            
        },
        changePassword() {
            
        },
        deleteAccount() {
            
        }
    },
    components: {
        dangerButton,
        secondaryButton
    }
};
</script>

<template>
    <div>
        <table class="my-5">
            <tr>
                <td class="ps-5 floor-ceiling-padding">Profile picture</td>
                <td><img src="profile_photo"></td>
            </tr>
            <tr>
                <td class="ps-5 floor-ceiling-padding">Name</td>
                <td class="bold">{{ name }}</td>
            </tr>
            <tr>
                <td class="ps-5 floor-ceiling-padding">Email</td>
                <td class="bold">{{ email }}</td>
            </tr>
            <tr>
                <td class="ps-5 floor-ceiling-padding">Age</td>
                <td class="bold">{{ age }}</td>
            </tr>
            <tr>
                <td class="ps-5 floor-ceiling-padding">Gender</td>
                <td class="bold">{{ gender }}</td>
            </tr>
            <tr>
                <td class="ps-5 floor-ceiling-padding">Membership</td>
                <td class="bold">{{ membership }}</td>
            </tr>
            <tr>
                <td class="ps-5 floor-ceiling-padding">Password</td>
                <td>
                    <div class="d-flex flex-row justify-content-between align-items-center">
                        <span class="bold">********</span>
                        <span class="pe-5"><secondaryButton :on-click="this.changePassword">Change</secondaryButton></span>
                    </div>
                </td>
            </tr>
        </table>
        <div>
            <dangerButton :on-click="this.deleteAccount">Delete account</dangerButton>
        </div>
    </div>

</template>

<style scoped>
table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    /* border-radius: var(--border-radius) */
}

td {
    border-style: solid;
    border-top: var(--table-border-width) solid var(--table-border-color);
}

tr:first-child td:first-child {
    border-top-left-radius: var(--border-radius);
}

tr:first-child td:last-child {
    border-top-right-radius: var(--border-radius);
}

tr:last-child td:first-child {
    border-bottom-left-radius: var(--border-radius);
}

tr:last-child td:last-child {
    border-bottom-right-radius: var(--border-radius);
}

tr:last-child td {
    border-bottom: var(--table-border-width) solid var(--table-border-color);
}

td:first-child {
    border-left: var(--table-border-width) solid var(--table-border-color);
}

td:last-child {
    border-right: var(--table-border-width) solid var(--table-border-color);
}

.bold {
    font-weight: bold;
}

.floor-ceiling-padding{
    padding-top: 2rem;
    padding-bottom: 2rem;
}

</style>