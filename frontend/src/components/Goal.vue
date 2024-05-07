<template>
    <div>
        <h3>
            Mileage accumulated in <b>{{ month }}</b>
        </h3>
        <b-progress
            :value="value"
            :max="max"
            show-progress
            animated
        ></b-progress>
    </div>
</template>

<script>
export default {
    name: 'GoalComponent',
    data() {
        return {
            month: 'February',
            value: 50,
            max: 100,
        }
    },
    methods: {},
}
</script>
