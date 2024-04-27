<script>
// Adobe Spectrum Inspired Top Nav
// Unfortunately, the current implementation is not very flexible and is not very reusable

// import topNavElement from './topNavElement.vue';

export default {
    name: 'topNavRailed',
    props: {

    },
    data() {
        return {
            railStyle: {
                width: '0px',
                backgroundColor: 'var(--selectionRailColor)',
                height: '4px',
                borderRadius: '9999px',
            },
            selectionTrainStyle: {
                width: '100px',
                backgroundColor: 'var(--selectionTrainColor)',
                height: '4px',
                transform: 'translateX(0px) translateY(-4px)',
                transition: 'transform 0.2s, width 0.1s',
                borderRadius: '9999px',
            },

            navStyles: [
                {
                    color: 'var(--text-color)',
                    transition: 'color 0.2s',
                },
                {
                    color: 'var(--topNavElementUnselectedTextColor)',
                    transition: 'color 0.2s',
                },
                {
                    color: 'var(--topNavElementUnselectedTextColor)',
                    transition: 'color 0.2s',
                },
                {
                    color: 'var(--topNavElementUnselectedTextColor)',
                    transition: 'color 0.2s',
                },
            ]
            // navElstyle1: {
            //     color: 'var(--text-color)',
            // },
            // navElstyle2: {
            //     color: 'var(--topNavElementUnselectedTextColor)',
            // },
            // navElstyle3: {
            //     color: 'var(--topNavElementUnselectedTextColor)',
            // },
            // navElstyle4: {
            //     color: 'var(--topNavElementUnselectedTextColor)',
            // },
        };
    },
    methods: {
        handleClicked(event) {

            const clickedElement = event.target.getBoundingClientRect();
            const parentElement = event.target.parentNode.getBoundingClientRect();
            this.selectionTrainStyle.width = `${clickedElement.width}px`
            this.selectionTrainStyle.transform = `translateX(${clickedElement.left - parentElement.left}px) translateY(-4px)`

            // Set the color of the selected element to the selected color
            const navElements = document.querySelectorAll('.navElements');
            navElements.forEach((element) => {
                element.style.color = 'var(--topNavElementUnselectedTextColor)';
            });

            // navStyles[event.target.getAttribute('id') - 1].color = 'var(--text-color)';

            for (let i = 0; i < this.navStyles.length; i++) {
                if (i == event.target.getAttribute('id')) {
                    this.navStyles[i].color = 'var(--text-color)';
                    continue;
                } else {
                    this.navStyles[i].color = 'var(--topNavElementUnselectedTextColor)';
                }
            }

            for (let i = 0; i < this.navStyles.length; i++) {
                console.log(this.navStyles[i].color);
                // navElements[i].style.color = this.navStyles[i].color;
            }

            this.$emit('NavElementClicked', event.target.getAttribute('id'));
        }
    },
    components: {
        // topNavElement,
    },
    mounted() {

        this.$nextTick(() => {
            const navElements = document.querySelectorAll('.navElements');

            // // Set the current selection to the nav first element
            console.log(this.$refs);

            // Set the width of the rail to the size of all the nav elements
            let width = 0;
            navElements.forEach((element) => {
                width += element.getBoundingClientRect().width;
            });
            this.railStyle.width = `${width - 30}px`;

            // Set the width of the train to the size of the first nav element
            this.selectionTrainStyle.width = `${navElements[0].children[0].getBoundingClientRect().width}px`;
        });
    },
};
</script>

<template>
    <div class="top-nav-railed">
        <div class="navElements mb-2">
            <router-link @click="handleClicked" to="#" id="0" class="topNavElement" :style="navStyles[0]">Friends</router-link>
            <router-link @click="handleClicked" to="#" id="1" class="topNavElement" :style="navStyles[1]">Groups</router-link>
            <router-link @click="handleClicked" to="#" id="2" class="topNavElement" :style="navStyles[2]">Add Friends</router-link>
            <router-link @click="handleClicked" to="#" id="3" class="topNavElement" :style="navStyles[3]">Friend Requests</router-link>

            <!-- <topNavElement ref="navElement" @NavElementClicked="handleClicked" to="#" id="1">Friends</topNavElement>
            <topNavElement ref="navElement" @NavElementClicked="handleClicked" to="#" id="2">Groups</topNavElement>
            <topNavElement ref="navElement" @NavElementClicked="handleClicked" to="#" id="3">Add Friends</topNavElement>
            <topNavElement ref="navElement" @NavElementClicked="handleClicked" to="#" id="3">Friend Requests</topNavElement> -->
        </div>
        <div id="selection-rail" class="selectionRail" :style="railStyle"></div>
        <div id="selection-train" class="selectorTrain" :style="selectionTrainStyle"></div>
    </div>
</template>

<style scoped>
.router-link-active {
    color: var(--text-color);
}

.top-nav-railed {
    font-size: 20px;
    display: flex;
    flex-direction: column;
    align-items: start;
}

.navElements {
    display: flex;
    flex-direction: row;
}

.navElements>* {
    margin-right: 30px;
}

.topNavElement{
    text-decoration: none;
    /* color: var(--topNavElementUnselectedTextColor); */
}
</style>
