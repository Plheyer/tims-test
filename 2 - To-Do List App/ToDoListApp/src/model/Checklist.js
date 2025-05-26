export default class Checklist {
  constructor(tasks) {
    this.tasks = tasks;
  }

  addTask(task) {
    this.tasks.push(task);
  }

  removeTask(task) {
    this.tasks = this.tasks.filter(function (item) {
      return item.text !== task.text;
    });
  }
}
