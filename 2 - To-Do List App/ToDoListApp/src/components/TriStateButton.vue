<script setup>
import { computed } from 'vue';

const props = defineProps({
  name: {
    type: String,
    required: true,
  },
});

const idTodo = computed(() => {
    return props.name + "-todo"
});

const idInProgress = computed(() => {
    return props.name + "-inProgress"
});

const idDone = computed(() => {
    return props.name + "-done"
});
</script>

<template>
    <div class="tri-state">
        <input :id="idTodo" :name="name" type="radio" checked/>
        <label :for="idTodo" onclick="">❌ To do</label>

        <input :id="idInProgress" :name="name" type="radio" />
        <label :for="idInProgress" onclick="">⏳ In Progress</label>

        <input :id="idDone" :name="name" type="radio" />
        <label :for="idDone" onclick="">✅ Done</label>
    </div>
</template>

<style>
.tri-state {
    display: flex;
    flex-direction: row;
    background-color: light-dark(#FFFFFF, #000000);
    border-radius: 5px;
    margin: 0 0 15px 0;
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
