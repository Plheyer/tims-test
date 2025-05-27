<script setup>
import TodoList from './components/TodoList.vue'
const toggleLightDarkMode = () => {
  let appClassList = document.body.classList;
  if (appClassList.contains("light")) {
    appClassList.add("dark");
    appClassList.remove("light");
    localStorage.setItem("mode", "dark");
  } else {
    appClassList.add("light");
    appClassList.remove("dark");
    localStorage.setItem("mode", "light");
  }
}

if (localStorage.mode) {
  const mode = localStorage.getItem("mode");
  if (mode == "light") {
    document.body.classList.add("light");
  } else {
    document.body.classList.add("dark");
  }
}
</script>

<template>
  <main>
    <div class="switch-dark-mode">
      <button v-on:click="toggleLightDarkMode">☀️/🌙</button>
    </div>
    <TodoList />
  </main>
</template>

<style>
:root {
  color-scheme: light dark;
}

.light {
  color-scheme: light;
}
.dark {
  color-scheme: dark;
}
.switch-dark-mode {
  display: flex;
  justify-content: end;
  margin-bottom: 5px;
}

.switch-dark-mode > button {
  border: none;
  background-color: light-dark(#DDDDDD, #222222);
  padding: 15px;
  border-radius: 5px;
  cursor: pointer;
}

main {
  width: 100%;
}
</style>
