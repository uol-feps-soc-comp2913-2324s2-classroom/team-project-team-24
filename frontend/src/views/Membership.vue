<script>
import MembershipOptionComponent from "@/components/MembershipOption.vue";
export default {
    name: "MembershipCenter",
    data() {
        return {
            membershipOptions: [
                {
                    regularity: "Weekly",
                    points: ["point1", "point2"],
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
            ]
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
    <div class="membershipPageContainer">
        <h1>Membership Page</h1>
        <div style="display:flex;">
            <MembershipOptionComponent v-for="(membership, x) in membershipOptions" :key="x" v-bind:membership="membership" />    
        </div>
        
    </div>
</template>

<style scoped></style>
