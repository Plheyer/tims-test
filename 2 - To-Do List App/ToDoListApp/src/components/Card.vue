<script setup>
import { ref } from 'vue';
import CardItem from './CardItem.vue';
import Checklist from '@/model/Checklist';
import Task from '@/model/Task';
const props = defineProps({
    checklists: {
        type: Array,
        required: true
    },
    checklist: {
        type: Checklist,
        required: true
    },
    checklistIndex: {
        type: Number,
        required: true
    }
});
const newTaskText = ref("");
const addTask = () => {
    if (!newTaskText.value) return;
    props.checklist.addTask(new Task(newTaskText.value, 0));
    localStorage.setItem("checklists", JSON.stringify(props.checklists));
    newTaskText.value = "";
};
const deleteChecklist = (index) => {
    props.checklists.splice(index, 1);
    localStorage.setItem("checklists", JSON.stringify(props.checklists));
}
</script>

<template>
    <div class="card">
        <button class="delete-checklist" v-on:click="deleteChecklist(checklistIndex)">🗑️ Delete checklist</button>
        <div class="tasks" v-for="(task, index) in props.checklist.tasks">
            <CardItem :task="task" :checklist-index="props.checklistIndex" :checklists="props.checklists" :checklist="props.checklist" :task-index="index" />
        </div>
        <div class="card-new-task">
            <input type="text" v-model="newTaskText" placeholder="New task..." class="test" />
            <button v-on:click="addTask">➕</button>
        </div>
    </div>
</template>

<style>
input {
    min-width: 0px !important;
}

.card {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    background-color: light-dark(#DDDDDD, #222222);
    border-radius: 5px;
    padding: 15px;
    height: 100%;
}

.card-new-task {
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 27px;
    gap: 5px;
}

.card-new-task > button {
    border: none;
    background-color: #62d174;
    border-radius: 5px;
    cursor: pointer;
    transition: all ease-in-out .2s;
}

.card-new-task > button:hover {
    background-color: #49c05c;
    transition: all ease-in-out .2s;
}

.tasks:not(:nth-last-child(2)) {
    border-bottom: solid 1px black;
}

.delete-checklist {
    border: 3px solid rgb(255, 73, 73);
    border-radius: 5px;
    background-color: transparent;
    padding: 10px 0;
    width: 100%;
    margin-bottom: 10px;
    transition: all ease .4s;
}

.delete-checklist:hover {
    background-color: rgb(255, 73, 73);
    transition: all ease .4s;
    cursor: pointer;
    transform: scale(1.05);
    font-size: 15px;
    color: white;
}
</style>
