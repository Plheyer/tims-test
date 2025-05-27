<script setup>
import { ref } from 'vue';
import Checklist from '@/model/Checklist';
import Card from './Card.vue';
import checklistsFromJson from '@/factory/ChecklistFactory';

let checklists;
if (localStorage.checklists) {
    checklists = ref(checklistsFromJson(localStorage.getItem("checklists")));
} else {
    checklists = ref([]);
}
const addChecklist = () => {
    checklists.value.push(new Checklist([]));
    localStorage.setItem("checklists", JSON.stringify(checklists.value));
}
</script>

<template>
    <button class="add-checklist" v-on:click="addChecklist">➕ Add a checklist</button>
    <div class="cards">
        <Card v-for="(checklist, checklistIndex) in checklists" :checklist="checklist" :checklists="checklists" :checklist-index="checklistIndex" />
    </div>
</template>

<style>
body {
    background-color: light-dark(#FFFFFF, #000000);
    width: 100%;
}

#app {
    padding: 15px !important;
}

.cards {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    gap: 15px;
    width: 100%;
}

.add-checklist {
    border: 3px solid #5dacda;
    border-radius: 5px;
    background-color: transparent;
    padding: 10px 0;
    width: 100%;
    margin-bottom: 10px;
    transition: all ease .4s;
}

.add-checklist:hover {
    background-color: #5dacda;
    transition: all ease .4s;
    cursor: pointer;
    transform: scale(1.05);
    font-size: 15px;
    color: white;
}
</style>
