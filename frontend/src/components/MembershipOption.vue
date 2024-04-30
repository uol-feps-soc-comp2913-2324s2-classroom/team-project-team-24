<template>
    <div :class="'membership-option'" :style="{ backgroundColor: color }">
        <h3>{{ membership.name }}</h3>
        <ul>
            <li v-for="(point) in membership.points" :key="point">{{point}}</li>
        </ul>
        <div class="option-details">
            <h4>£{{ membership.price.toFixed(2) }}<br>{{ membership.regularity }}</h4>
        
            <template v-if="currentPlan.id===membership.id">
                <button class="btn-danger" @click="cancelMembership">Cancel Plan</button>
            </template>
            <template v-else>
                <button class="btn-primary" @click="buyMembership">Buy Now</button>
            </template>
    
            
        </div>
    </div>
</template>

<script>
import axiosAuth from '@/api/axios-auth.js';

export default {
    name: "MembershipOptionComponent",
    props: {
        membership: {},
        color: String, // Ensure the color prop is of type String,
        currentPlan: {},
    },
    data() {
        return {
            
        };
    },
    methods: {
        async buyMembership() {
            const confirmationMessage = `You are about to purchase the ${this.membership.regularity} membership for £${this.membership.price.toFixed(2)}. Are you sure?`;
            if (confirm(confirmationMessage)) {
                // Proceed with purchasing the membership
                // You can add your logic here, such as navigating to a checkout page or triggering a payment process
                await axiosAuth.post('/membership/purchase', {
                    membershipID: this.membership.id
                });
                this.$parent.getPageData();
            } else {
                console.log('Purchase cancelled.');
            }
        },
        async cancelMembership() {
            const confirmationMessage = `You are about to cancel your membership. Are you sure you want to do this?`;
            if (confirm(confirmationMessage)) {
                // Proceed with purchasing the membership
                // You can add your logic here, such as navigating to a checkout page or triggering a payment process
                await axiosAuth.get('/membership/cancel').catch(() => {});
                this.$parent.getPageData();
            } else {
                console.log('Purchase cancelled.');
            }
        }

    },
    components: {
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

.dummy-button {
    background-color: var(--tertiary-button-grey);
    border-style: solid;
    border-color: var(--tertiary-button-grey);
    border-width: 3px;
    font-weight: bold;
    color: var(--secondary-button-offBlack);
    padding-top: var(--button-padding-vertical);
    padding-bottom: var(--button-padding-vertical);
    padding-left: var(--button-padding-horizontal);
    padding-right: var(--button-padding-horizontal);
    text-align: center;
    text-decoration: none;
    display: inline-block;
    transition: background-color 0.2s, border-color 0.2s, color 0.2s;
    cursor: pointer;
    border-radius: 99999px;
}
</style>