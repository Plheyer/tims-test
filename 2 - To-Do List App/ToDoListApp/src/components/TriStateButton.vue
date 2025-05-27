<script setup>
import Task from '@/model/Task';
import { computed } from 'vue';

const props = defineProps({
    task: {
        type: Task,
        required: true
    },
    checklists: {
        type: Array,
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
});

const taskId = computed(() => {
    return props.checklistIndex + "-" + props.taskIndex;
})

const idTodo = computed(() => {
    return taskId.value + "-todo"
});

const idInProgress = computed(() => {
    return taskId.value + "-inProgress"
});

const idDone = computed(() => {
    return taskId.value + "-done"
});

const saveStates = (state) => {
    props.task.state = state;
    localStorage.setItem("checklists", JSON.stringify(props.checklists));
}
</script>

<template>
    <div class="tri-state">
        <input :id="idTodo" :name="taskId" type="radio" v-on:change="saveStates(0)" :checked="task.state == 0"/>
        <label :for="idTodo" onclick="">❌ To do</label>

        <input :id="idInProgress" :name="taskId" type="radio" v-on:change="saveStates(1)" :checked="task.state == 1"/>
        <label :for="idInProgress" onclick="">⏳ In Progress</label>

        <input :id="idDone" :name="taskId" type="radio" v-on:change="saveStates(2)" :checked="task.state == 2"/>
        <label :for="idDone" onclick="">✅ Done</label>
    </div>
</template>

<style>
.tri-state {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    background-color: light-dark(#FFFFFF, #000000);
    border-radius: 5px;
}

.tri-state > label {
    color: light-dark(#000000, #FFFFFF);
    padding: 0 5px;
    padding: 5px;
    transition: all .5s ease-out;
    cursor: pointer;
}

.tri-state input[type="radio"]:checked + label{
    background-color: #5dacda;
    transition: all .5s ease-out;
    border-radius: 5px;
}

.tri-state > label:not(:last-child) {
    border-right: solid #222222 1px;
}

.tri-state > input {
    position: fixed;
    opacity: 0;
    pointer-events: none;
}
</style>
