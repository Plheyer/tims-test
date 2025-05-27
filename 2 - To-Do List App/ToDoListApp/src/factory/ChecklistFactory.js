import Checklist from "@/model/Checklist";
import Task from "@/model/Task";

export default function checklistsFromJson(json) {
    let checklists = [];

    const checklistsParsed = JSON.parse(json);
    for (let checklist of checklistsParsed) {
        let tasks = [];
        for (let task of checklist.tasks) {
            tasks.push(new Task(task.text, task.state));
        }
        checklists.push(new Checklist(tasks));
    }

    return checklists;
}