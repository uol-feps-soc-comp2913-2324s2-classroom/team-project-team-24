<template>
    <div class="top-nav-railed">
        <div class="navElements mb-2">
            <div
                @click="handleClicked"
                id="0"
                class="topNavElement"
                :style="navStyles[0]"
            >
                Friends
            </div>
            <div
                @click="handleClicked"
                id="1"
                class="topNavElement"
                :style="navStyles[1]"
            >
                Groups
            </div>
            <div
                @click="handleClicked"
                id="2"
                class="topNavElement"
                :style="navStyles[2]"
            >
                Add&nbsp;Friends
            </div>
        </div>
        <div id="selection-rail" class="selectionRail" :style="railStyle"></div>
        <div
            id="selection-train"
            class="selectorTrain"
            :style="selectionTrainStyle"
        ></div>
    </div>
</template>
<script>
// Adobe Spectrum Inspired Top Nav
// Unfortunately, the current implementation is not very flexible and is not very reusable

// import topNavElement from './topNavElement.vue';

export default {
    name: 'topNavRailed',
    props: {},
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
            ],
        }
    },
    methods: {
        handleClicked(event) {
            const clickedElement = event.target.getBoundingClientRect()
            const parentElement =
                event.target.parentNode.getBoundingClientRect()
            this.selectionTrainStyle.width = `${clickedElement.width}px`
            this.selectionTrainStyle.transform = `translateX(${
                clickedElement.left - parentElement.left
            }px) translateY(-4px)`

            // Set the color of the selected element to the selected color
            const navElements = document.querySelectorAll('.navElements')
            navElements.forEach((element) => {
                element.style.color = 'var(--topNavElementUnselectedTextColor)'
            })

            for (let i = 0; i < this.navStyles.length; i++) {
                if (i == event.target.getAttribute('id')) {
                    this.navStyles[i].color = 'var(--text-color)'
                    continue
                } else {
                    this.navStyles[i].color =
                        'var(--topNavElementUnselectedTextColor)'
                }
            }

            for (let i = 0; i < this.navStyles.length; i++) {
                console.log(this.navStyles[i].color)
            }

            this.$emit('NavElementClicked', event.target.getAttribute('id'))
        },
    },
    components: {},
    mounted() {
        this.$nextTick(() => {
            const navElements = document.querySelectorAll('.navElements')

            // Set the current selection to the nav first element
            console.log(this.$refs)

            // Set the width of the rail to the size of all the nav elements
            let width = 0
            navElements.forEach((element) => {
                width += element.getBoundingClientRect().width
            })
            this.railStyle.width = `${width - 30}px`

            // Set the width of the train to the size of the first nav element
            this.selectionTrainStyle.width = `${
                navElements[0].children[0].getBoundingClientRect().width
            }px`
        })
    },
}
</script>

<style scoped>
.router-link-active {
    color: var(--text-color);
}

.top-nav-railed {
    font-size: 20px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.navElements {
    display: flex;
    flex-direction: row;
}

.navElements > * {
    margin-right: 30px;
}

.topNavElement {
    text-decoration: none;
    cursor: pointer;
}
</style>
