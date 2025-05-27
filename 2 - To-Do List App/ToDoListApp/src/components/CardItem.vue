<script setup>
import Task from '@/model/Task';
import TriStateButton from './TriStateButton.vue';
import Checklist from '@/model/Checklist';
const props = defineProps({
    task: {
        type: Task,
        required: true
    },
    checklistIndex: {
        type: Number,
        required: true
    },
    taskIndex: {
        type: Number,
        required: true
    },
    checklists: {
        type: Array,
        required: true
    },
    checklist: {
        type: Checklist,
        required: true
    },
});
const removeTask = () => {
    props.checklist.removeTask(props.task);
    localStorage.setItem("checklists", JSON.stringify(props.checklists));
}
</script>

<template>
    <div class="card-item">
        <div class="card-item-title">
            <input type="text" :value="task.text" />
            <button class="delete-button" v-on:click="removeTask">🗑️</button>
        </div>
        <TriStateButton :checklistIndex="checklistIndex" :checklists="props.checklists" :taskIndex="taskIndex" :task="task" />
    </div>
</template>

<style>
.card-item {
    display: flex;
    flex-direction: column;
    margin: 15px 0;
}

.card-item:not(:last-child)::after {
    content: '';
    height: 1px;
    width: 100%;
    background-color: #000000;
}

.card-item-title {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 100%;
    margin-bottom: 5px;
    gap: 5px;
}

.card-item-title > input, .card-new-task > input {
    border-radius: 5px;
    border: solid #5dacda 2px;
}

.card-item-title button {
    border: none;
    padding: 5px;
    cursor: pointer;
}

.card-item-title > input, .card-new-task > input {
    flex-grow: 1;
    width: 100%;
}

.delete-button {
    background-color: rgb(255, 96, 96);
    border-radius: 5px;
    transition: all ease-in-out .2s;
}

.delete-button:hover {
    background-color: rgb(255, 73, 73);
    transition: all ease-in-out .2s;
}
</style>
