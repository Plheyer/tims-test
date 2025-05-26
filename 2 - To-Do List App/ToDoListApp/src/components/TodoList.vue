<script setup>
    import { ref } from 'vue';
    import CardItem from './CardItem.vue';
import Task from '@/model/Task';
import Checklist from '@/model/Checklist';
    const newTask = ref({ text: "", status: 0 });
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
    const checklists = ref([
        new Checklist(tasks),
        new Checklist(tasks2),
        new Checklist(tasks3),
    ]);
</script>

<template>
    <div class="cards">
        <div class="card" v-for="(checklist, checklistIndex) in checklists">
            <div class="tasks" v-for="(task, index) in checklist.tasks">
                <CardItem :task="task" :checklist-index="checklistIndex" :task-index="index" />
            </div>
            <div class="card-new-task">
                <input type="text" :value="newTask.text" placeholder="New task..." />
                <button>➕</button>
            </div>
        </div>
    </div>
</template>

<style>
body {
    background-color: light-dark(#FFFFFF, #000000);
}

.cards {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    gap: 15px;
    width: 100%;
}

.card {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    background-color: light-dark(#DDDDDD, #222222);
    border-radius: 5px;
    padding: 15px;
    min-width: 200px;
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
</style>
