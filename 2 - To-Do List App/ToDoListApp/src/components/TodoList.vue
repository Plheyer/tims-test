<script setup>
    import TriStateButton from './TriStateButton.vue';
</script>

<template>
    <div class="cards">
        <div class="card">
            <div class="card-item">
                <div class="card-item-title">
                    <input type="text" value="Tâche 1" />
                    <button onclick="" class="edit-button">✏️</button>
                    <button class="delete-button">🗑️</button>
                </div>
                <TriStateButton name="1-task-1"/>
            </div>
            <div class="card-item">
                <div class="card-item-title">
                    <input type="text" value="Tâche 2" />
                    <button class="edit-button">✏️</button>
                    <button class="delete-button">🗑️</button>
                </div>
                <TriStateButton name="1-task-2"/>
            </div>
            <div class="card-item">
                <div class="card-item-title">
                    <input type="text" value="Tâche 3" />
                    <button class="edit-button">✏️</button>
                    <button class="delete-button">🗑️</button>
                </div>
                <TriStateButton name="1-task-3"/>
            </div>
            <div class="card-new-task">
                <input type="text" value="" placeholder="New task..." />
                <button>➕</button>
            </div>
        </div>
        <div class="card">
            <div class="card-item">
                <div class="card-item-title">
                    <input type="text" value="Tâche 1" />
                    <button onclick="" class="edit-button">✏️</button>
                    <button class="delete-button">🗑️</button>
                </div>
                <TriStateButton name="2-task-1"/>
            </div>
            <div class="card-new-task">
                <input type="text" value="" placeholder="New task..." />
                <button>➕</button>
            </div>
        </div>
        <div class="card">
            <div class="card-item">
                <div class="card-item-title">
                    <input type="text" value="Tâche 1" />
                    <button onclick="" class="edit-button">✏️</button>
                    <button class="delete-button">🗑️</button>
                </div>
                <TriStateButton name="3-task-1"/>
            </div>
            <div class="card-item">
                <div class="card-item-title">
                    <input type="text" value="Tâche 2" />
                    <button class="edit-button">✏️</button>
                    <button class="delete-button">🗑️</button>
                </div>
                <TriStateButton name="3-task-2"/>
            </div>
            <div class="card-item">
                <div class="card-item-title">
                    <input type="text" value="Tâche 3" />
                    <button class="edit-button">✏️</button>
                    <button class="delete-button">🗑️</button>
                </div>
                <TriStateButton name="3-task-3"/>
            </div>
            <div class="card-item">
                <div class="card-item-title">
                    <input type="text" value="Tâche 4" />
                    <button class="edit-button">✏️</button>
                    <button class="delete-button">🗑️</button>
                </div>
                <TriStateButton name="3-task-4"/>
            </div>
            <div class="card-item">
                <div class="card-item-title">
                    <input type="text" value="Tâche 5" />
                    <button class="edit-button">✏️</button>
                    <button class="delete-button">🗑️</button>
                </div>
                <TriStateButton name="3-task-5"/>
            </div>
            <div class="card-item">
                <div class="card-item-title">
                    <input type="text" value="Tâche 6" />
                    <button class="edit-button">✏️</button>
                    <button class="delete-button">🗑️</button>
                </div>
                <TriStateButton name="3-task-6"/>
            </div>
            <div class="card-item">
                <div class="card-item-title">
                    <input type="text" value="Tâche 7" />
                    <button class="edit-button">✏️</button>
                    <button class="delete-button">🗑️</button>
                </div>
                <TriStateButton name="3-task-7"/>
            </div>
            <div class="card-new-task">
                <input type="text" value="" placeholder="New task..." />
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

.card-item {
    display: flex;
    flex-direction: column;
    margin: 5px 0;
    padding: 5px;
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

.card-new-task {
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 27px;
    gap: 5px;
}

.card-new-task > input {
    flex: 1;
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

.delete-button {
    background-color: rgb(255, 96, 96);
    border-radius: 5px;
    transition: all ease-in-out .2s;
}

.delete-button:hover {
    background-color: rgb(255, 73, 73);
    transition: all ease-in-out .2s;
}

.edit-button {
    background-color: #5dacda;
    border-radius: 5px;
    transition: all ease-in-out .2s;
}

.edit-button:hover {
    background-color: #43a3db;
    transition: all ease-in-out .2s;
}
</style>
