<script>
import MembershipOptionComponent from "@/components/MembershipOption.vue";
import axiosAuth from "@/api/axios-auth.js";
export default {
    name: "MembershipCenter" ,
    data() {
        return {
            membershipOptions: [],
            // adjust the colours of each col
            membershipColors: [
                "#073617",
                "#14903F",
                "#0A481F",
                // Add more colors as needed
            ],
            currentPlan: {"id": -1, "name": "", "regularity": "", "price": 0}, // Simulate currentPlan state
        };
    },
    computed: {
        
        // Computed property to determine the viewer's current membership tier
        viewerMembershipOption() {
            // Find the membership option that matches the viewer's tier
            return this.membershipOptions.find(option => option.regularity === this.viewerMembershipTier);
        }
    },
    methods: {
        getPageData() {
            axiosAuth.get('/membership/get-options').then(
                response => {
                    this.membershipOptions = response.data.membershipOptions;
                }
            ),
            axiosAuth.get('/membership/get-current').then(
                response => {
                    if (response.data.membership !== null) {
                        this.currentPlan = response.data.membership;
                    } else {
                        this.currentPlan.id = -1;
                    }
                }
            )
        }
    },
    components: {
        MembershipOptionComponent,
    },
    created() {
        this.getPageData();
    }
};
</script>

<template>
    <div class="membershipPageContainer" >
        <div class="page-heading-container">
            <h1>Membership</h1>
        </div>
        <p v-if="currentPlan.id===-1">
            We've detected you haven't subscribed to Walkley. To get access to Walkley, please choose your payment subscription option
        </p>
        <p v-else>
            Hello Member! You are subscribed to the <b>{{ currentPlan.regularity }}</b> plan.
        </p>
        <div class="membership-options-container">
            <MembershipOptionComponent v-for="(membership, x) in membershipOptions" 
            :key="membership" v-bind:membership="membership" 
            :color="membershipColors[x]"
            v-bind:currentPlan="currentPlan"
            />    
        </div>
        
    </div>
</template>

<style scoped>
@import "@/assets/css/style.css";
.membershipPageContainer {
  display: flex;
  flex-direction: column;
  align-items: center; /* Center align horizontally */
  padding: 20px; /* Add padding around the container */
}


.membership-options-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between; /* Distribute items evenly */
    align-items: flex-end; /* Align items to the bottom */
    width: 100%;
    max-width: 600px; /* Limit the width of the options container */
    margin-top: 20px; /* Add some space at the top */
}

.membership-option {
  flex: 0 0 calc(33.33% - 20px); /* Adjust width to accommodate margin */
  margin-bottom: 20px; /* Add bottom margin */
  display: flex; /* Enable flexbox layout for option content */
  flex-direction: column; /* Stack regularity and details vertically */
  border-radius: 0.8rem;
}


</style>