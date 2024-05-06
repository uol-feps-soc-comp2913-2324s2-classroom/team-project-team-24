<script>
import axiosAuth from "@/api/axios-auth.js";

export default {
    name: "TrailListItem",
    props: {
        trail: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            checked: false,
            buttonStyle: {
                width: "30px",
                height: "30px",
            }
        };
    },
    computed: {
        isSelected() {
            return this.checked;
        },
    },
    mounted() {
        // Get the size of the element
        const element = document.querySelector(".tableRow");
        let rowHeight = element.clientHeight;
        this.buttonStyle.height = rowHeight - 10 + "px";
        this.buttonStyle.width = rowHeight - 10 + "px";  
    },
    methods: {
        onCheckboxChange() {
            this.$emit('trail-selected', {
                trailId: this.trail.id,
                checked: this.checked,
            });
        },
        zoomToTrail() {
            this.$emit("zoom-to-trail", this.trail.id);
        },
        viewTrail() {
            this.$router.push({ path: "/mytrail", query: { trailID: this.trail.id } });
        },
        downloadTrail() {
            // Implement the logic to download the trail data
            axiosAuth
                .post("/trail/download", { trailID: this.trail.id })
                .then(
                    (response) => {
                        console.log(response.data.data);
                        const download_link = document.createElement("a");
                        download_link.href = URL.createObjectURL(new Blob([response.data.data], { type: "text/plain" }));
                        download_link.download = "route.gpx";
                        download_link.click();
                    }
                )
                .catch((error) => console.error("Error:", error));
        },
        deleteTrail() {
            axiosAuth
                .post("/trail/delete", { trailID: this.trail.id })
                .then(() => {
                    this.$emit("trail-deleted", this.trail.id);
                })
                .catch((error) => {
                    console.error("Error deleting trail:", error);
                });
        },
    },
};
</script>

<template>
    <tr class="tableRow p-1 my-5" @click="viewTrail">
        <td class="tdItem tdItemCheckbox"><input type="checkbox" :value="trail.id" v-model="checked" @click.stop @change="onCheckboxChange" /></td>
        <td class="tdItem"><p>{{ trail.name }}</p></td>
        <td class="tdItem"><p>{{ trail.exercise_type }}</p></td>
                <!-- <p>{{ trail.date }}</p> -->
        <td class="tdItem tdItemButtons">
            <div>
                <button class="imageButton zoom-button" :style="buttonStyle" v-if="isSelected" @click.stop="zoomToTrail"><span><img src="../../assets/Smock_Location_18_N.svg"></span></button>
                <button class="imageButton mx-3" :style="buttonStyle" @click.stop="downloadTrail"><span><img src="../../assets/Smock_Download_18_N.svg"></span></button>
                <button class="imageButton" :style="buttonStyle" @click.stop="deleteTrail"><img src="../../assets/Smock_Delete_18_N.svg"></button>
            </div>
        </td>
    </tr>
</template>

<style scoped>
.imageButton {
    background-color: transparent;
    border: none;
    cursor: pointer;
    border-radius: 9999999px;
}

.imageButton:hover {
    background-color: #efefef;
}

tr{
    background-color: var(--l1-color);
    cursor: pointer;
    margin-bottom: 1px;
}

tr:hover {
    /* box-shadow: 8px var(--selectionRailColor); */
    filter: drop-shadow(0px 0px 5px var(--selectionRailColor));
}

.tdItemCheckbox{
    
}

.tdItemButtons{
    display: flex;
    justify-content: flex-end;
}

.trail-list-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    border-bottom: 1px solid #ddd;
    cursor: pointer;
}

.tableRow{
    border-bottom: 1px solid #ddd;
    width: 100%;
}

.tdItem{
    padding: 10px 10px 10px 10px;
}

p{
    margin: 0;
}

.trail-info {
    flex-grow: 1;
}

.button-container {
    display: flex;
    gap: 10px;
}

.zoom-button {

}

.routes-checkbox {
}
</style>