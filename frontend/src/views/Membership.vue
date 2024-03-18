<script>
import MembershipOptionComponent from "@/components/MembershipOption.vue";
import '@/assets/css/style.css';
export default {
    name: "MembershipCenter" ,
    data() {
        return {
            membershipOptions: [
                {
                    regularity: "Weekly",
                    points: ["point1", "point2", "point3"],
                    price: "7/week"
                },
                {
                    regularity: "Monthly",
                    points: ["point1", "point2", "point3"],
                    price: "6.66/week"
                },
                {
                    regularity: "Yearly",
                    points: ["point1", "point2", "point4"],
                    price: "5/week"
                },
            ],
            // adjust the colours of each col
            membershipColors: [
                "#006992", // Red background
                "#27476E", // Blue background
                "#001D4A", // Green background
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
            <h1>Membership Page</h1>
        </div>
        <div class="membership-options-container">
            <MembershipOptionComponent v-for="(membership, x) in membershipOptions" 
            :key="x" v-bind:membership="membership" 
            :color="membershipColors[x]"
            />    
        </div>
        
    </div>
</template>

<style scoped>
.membershipPageContainer {
  display: flex;
  flex-direction: column;
  align-items: center; /* Center align horizontally */
  /* justify-content: center; Center align vertically */
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
}


</style>