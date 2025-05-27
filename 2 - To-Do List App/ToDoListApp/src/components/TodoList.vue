<script setup>
import { ref } from 'vue';
import Task from '@/model/Task';
import Checklist from '@/model/Checklist';
import Card from './Card.vue';
import checklistsFromJson from '@/factory/ChecklistFactory';
const tasks = ref([
    new Task("My first task", 0),
    new Task("My second task", 2),
    new Task("My third task", 1),
]);
const tasks2 = ref([
    new Task("My first task", 0),
]);
const tasks3 = ref([
    new Task("My first task", 0),
    new Task("My second task", 2),
    new Task("My third task", 1),
    new Task("My fourth task", 2),
    new Task("My fifth task", 1),
    new Task("My sixth task", 2),
    new Task("My seventh task", 1),
]);
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
