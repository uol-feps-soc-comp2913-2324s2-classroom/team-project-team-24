<script>
import MembershipOptionComponent from "@/components/MembershipOption.vue";
export default {
    name: "MembershipCenter" ,
    data() {
        return {
            membershipOptions: [
                {
                    regularity: "Weekly",

                    price: "£1/week"
                },
                {
                    regularity: "Monthly",

                    price: "£3/month"
                },
                {
                    regularity: "Yearly",

                    price: "£10/year"
                },
            ],
            // adjust the colours of each col
            membershipColors: [
                "#073617",
                "#14903F",
                "#0A481F",
                // Add more colors as needed
            ],
        };
    },
    methods: {
        getMembershipOptions() {
            
        }
    },
    components: {
        MembershipOptionComponent,
    },
};
</script>

<template>
    <div class="membershipPageContainer" >
        <div class="page-heading-container">
            <h1>Membership</h1>
        </div>
        <p> To get access to Walkley, please choose your payment subscription option</p>
        <div class="membership-options-container">
            <MembershipOptionComponent v-for="(membership, x) in membershipOptions" 
            :key="x" v-bind:membership="membership" 
            :color="membershipColors[x]"
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