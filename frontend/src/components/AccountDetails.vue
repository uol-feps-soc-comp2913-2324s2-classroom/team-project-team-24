<template>
    <div style="display:flex;">
        <img src="proflie_photo">
        <div>
            <h2>{{ name }}</h2>
            <i>{{ membershipTier }}</i>
        </div>
    </div>
    <h4><b>Gender: </b>{{ gender }}</h4>
    <h4><b>Age: </b>{{ age }}</h4>
    <h4><b>Email: </b>{{ email }}</h4>
    <h4><b>Membership: </b>{{ membership }}</h4>
    <button @click="changePassword">Change password</button>
    <button @click="deleteAccount">Delete account</button>
</template>

<script>
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
};
</script>

