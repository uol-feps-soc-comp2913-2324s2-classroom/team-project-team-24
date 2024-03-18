<template>
    <div :class="'membership-option'" :style="{ backgroundColor: color }">
        <h3>{{ membership.regularity }}</h3>
        <ul>
            <li v-for="(point, x) in membership.points" :key="x">{{point}}</li>
        </ul>
        <div class="option-details">
            <h4>{{ membership.price }}</h4>
            <button class="btn btn-primary" @click="buyMembership">Buy Now</button>
        </div>
    </div>
</template>

<script>
import '@/assets/css/style.css';
export default {
    name: "MembershipOptionComponent",
    props: {
        membership: {},
        color: String // Ensure the color prop is of type String
    },
    data() {
        return {
            
        };
    },
    methods: {
        buyMembership() {
            const confirmationMessage = `You are about to purchase the ${this.membership.regularity} membership for ${this.membership.price}. Are you sure?`;
            if (confirm(confirmationMessage)) {
                // Proceed with purchasing the membership
                // You can add your logic here, such as navigating to a checkout page or triggering a payment process
                console.log('Membership purchased!');
            } else {
                console.log('Purchase cancelled.');
            }
        }

    },
};
</script>

<style scoped>
.membership-option {
    text-align: center; /* Center align all the content */
    padding: 20px; /* Add padding to the container */
}

.membership-option h3,
.membership-option h4,
.membership-option ul {
    margin: 10px 0; /* Add margin between elements */
    color: white; /* Set text color to white */
}

.membership-option button {
    margin: 10px 0; /* Add margin between elements */
}

.option-details {
  display: flex;
  flex-direction: column; /* Stack items vertically */
  align-items: center; /* Center align horizontally */
  margin-top: 4rem; /* Adjust as needed */
}

.option-details h4 {
  margin: 0; /* Remove default margin */
}


</style>