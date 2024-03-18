<template>
    <div :class="'membership-option'" :style="{ backgroundColor: color }">
        <h3>{{ membership.regularity }}</h3>
        <ul>
            <li v-for="(point, x) in membership.points" :key="x">{{point}}</li>
        </ul>
        <div class="option-details">
            <h4>{{ membership.price }}</h4>
            <primaryButton  :on-click="this.increment" @click="buyMembership">Buy Now</primaryButton>
        </div>
    </div>
</template>

<script>
import primaryButton from './ui-components/primaryButton.vue';

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
    components: {
        primaryButton,
    }
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
    margin: 10px 0;
    color: white;
}

.membership-option button {
    margin: 10px 0; /* Add margin between elements */
}

.option-details {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 4rem; 
}

.option-details h4 {
  margin: 0;
}


</style>