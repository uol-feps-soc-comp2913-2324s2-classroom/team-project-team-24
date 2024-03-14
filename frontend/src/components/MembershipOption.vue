<template>
    <div>
        <h3>{{ membership.regularity }}</h3>
        <ul>
            <li v-for="(point, x) in membership.points" :key="x">{{point}}</li>
        </ul>
        <button @click="buyMembership">Buy Now</button>
        <h4>{{ membership.price }}</h4>
    </div>
</template>

<script>
export default {
    name: "MembershipOptionComponent",
    props: {
        membership: {}
    },
    data() {
        return {
            
        };
    },
    methods: {
        buyMembership() {
            
        }
    },
};
</script>

