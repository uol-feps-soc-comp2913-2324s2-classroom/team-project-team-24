<script>
import axiosAuth from "@/api/axios-auth.js";

export default {
    name: "GoalComponent",
    data() {
        return {
            name: "",
            membershipTier: "",
            gender: "",
            age: null,
            email: "",
            membership: ""
        };
    },
    methods: {
        getPageData() {
            axiosAuth.get('/account/get-details').then(
                response => {
                    this.name = response.data.name;
                    this.gender = response.data.gender;
                    this.age = response.data.age;
                    this.email = response.data.email;
                    this.membershipTier = response.data.membershipTier;
                    this.membership = response.data.paymentRegularity;
                }
            )
        },
        deleteAccount() {
            axiosAuth.get('/account/delete').then(
                response => {
                    console.log(response.data);
                    localStorage.removeItem('token');
                    this.$router.push("/login");
                }
            )
            
        }
    },
    components: {
    },
    created() {
        this.getPageData();
    }
};
</script>

<template>
    <div>
        <table class="my-5">
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
                        
                        
                    </div>
                </td>
            </tr>
        </table>
        <div>
            <button class="btn-danger" @click="deleteAccount">Delete account</button>
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